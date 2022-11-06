async function getProductsByRegion(region) {
    const request = await fetch(`api/products/regions/${region}`)
    const json = request.json()
    return json
}

async function getProductsByCode(code) {
    const request = await fetch(`api/products/codes/${code}`)
    const json = request.json()
    return json
}

async function getProductsByDistrict(district) {
    const request = await fetch(`api/products/districts/${district}`)
    const json = request.json()
    return json
}

async function getRegions() {
    const request = await fetch(`api/regions/`)
    const json = request.json()
    return json
}

async function getCodes() {
    const request = await fetch(`api/codes/`)
    const json = request.json()
    return json
}

async function getDistricts() {
    const request = await fetch(`api/districts/`)
    const json = request.json()
    return json
}

async function getNameByCode(code) {
    const request = await fetch(`api/codes/${code}`)
    const json = request.json()
    return json
}

async function getRegionById(id) {
    const request = await fetch(`api/regions/${id}`)
    const json = request.json()
    return json
}

async function getDistrictById(id) {
    const request = await fetch(`api/districts/${id}`)
    const json = request.json()
    return json
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function add_nisha(product_id, region_id) {
    const request = await fetch(`api/nishas/`, {
        method: 'POST',
        body: JSON.stringify({
            product_id: product_id,
            region_id: region_id,
            user_id: JSON.parse(document.getElementById('user_id').textContent)
        }),
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json',
        },
    })
}

async function getName(code4) {
    const request = await fetch(`api/names/${code4}/`)
    const json = await request.json()
    return json
}


function getCountCodes(code, products) {
    let count = 0
    for (let p of products) {
        if (Math.floor(p['product'] / 1000000) == code) {
            count++
        }
    }
    return count
}

function getCountRegions(region, products) {
    let count = 0
    for (let p of products) {
        if (Math.floor(p['region']) == region) {
            count++
        }
    }
    return count
}

async function addRow(row, codes, values) {
    for (let c of codes) {
        getName(c).then(
            n => {
                row[n['description']] = getCountCodes(c, values)
            })
    }
    return row
}

async function getNames(res, codes) {
    return Array.from(codes).map(c => getName(c))
}

async function getlocalRegions(regions) {
    return Array.from(regions).map(r => getRegionById(r))
}

function changeRegions() {
    getRegions().then(
        values => {
            let regionPanel = document.getElementById('regions')
            regionPanel.innerHTML = ''
            let search = document.getElementById('search-regions')
            console.log(search.value)
            for (let v of values) {
                let li = document.createElement('li')
                li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['name']}</a></li>`
                li.addEventListener('click', function (e) {
                    let region = e.target.id
                    getProductsByRegion(region).then(val => val).then(
                        values => {
                            let codes = new Set()
                            for (let v of values) {
                                codes.add(Math.floor(v['product'] / 1000000))
                            }
                            let div = document.getElementById('products')
                            // div.innerHTML = `<h4 id="scrollspyHeading1">${val['name']}</h4>`
                            getRegionById(region).then(
                                val => {
                                    div.innerHTML = ` <h4 id="scrollspyHeading1">Импорт по: ${val['name']}</h4> <canvas id="myChart" width="100" height="100"></canvas>`
                                    let counts = Array.from(codes).map(c => getCountCodes(c, values))
                                    let res = []
                                    getNames(res, codes).then(
                                        val => {
                                            Promise.all(val).then(
                                                v => {
                                                    const ctx = document.getElementById('myChart');
                                                    const myChart = new Chart(ctx, {
                                                        type: 'doughnut',
                                                        data: {
                                                            labels: Array.from(v).map(x => x['description']).map(x => String(x).substring(0, 128)),
                                                            datasets: [{
                                                                label: 'imports',
                                                                data: Array.from(counts),
                                                                backgroundColor: [
                                                                    'rgba(255, 99, 132, 0.2)',
                                                                    'rgba(54, 162, 235, 0.2)',
                                                                    'rgba(255, 206, 86, 0.2)',
                                                                    'rgba(75, 192, 192, 0.2)',
                                                                    'rgba(153, 102, 255, 0.2)',
                                                                    'rgba(255, 159, 64, 0.2)'
                                                                ],
                                                                borderColor: [
                                                                    'rgba(255, 99, 132, 1)',
                                                                    'rgba(54, 162, 235, 1)',
                                                                    'rgba(255, 206, 86, 1)',
                                                                    'rgba(75, 192, 192, 1)',
                                                                    'rgba(153, 102, 255, 1)',
                                                                    'rgba(255, 159, 64, 1)'
                                                                ],
                                                                borderWidth: 1
                                                            }]
                                                        },
                                                        options: {
                                                            scales: {
                                                                y: {
                                                                    beginAtZero: true
                                                                }
                                                            }
                                                        }
                                                    });
                                                }
                                            )
                                        })
                                }
                            )


                        })


                })
                if (search.value === '') {
                    console.log(v['name'])
                    regionPanel.appendChild(li)
                } else if (v['name'].includes(search.value.toUpperCase())) {
                    console.log(v['name'])
                    regionPanel.appendChild(li)
                }
            }
        })
}

function changeCodes() {
    getCodes().then(
        values => {
            let codePanel = document.getElementById('codes')
            codePanel.innerHTML = ''
            let search = document.getElementById('search-products')
            for (let v of values) {
                let li = document.createElement('li')
                li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['description']}</a></li>`
                li.addEventListener('click', function (e) {
                    let code = e.target.id
                    getProductsByCode(code).then(
                        values => {
                            getNameByCode(code).then(
                                val => {
                                    let regions = new Set()
                                    for (let v of values) {
                                        regions.add(v['region'])
                                    }

                                    let div = document.getElementById('products')
                                    div.innerHTML = `<h4 id="scrollspyHeading1">Импорт по: ${val['description']}</h4> <canvas id="myChart" width="100" height="100"></canvas>`
                                    let counts = Array.from(regions).map(r => getCountRegions(r, values))
                                    getlocalRegions(regions).then(
                                        val => {
                                            Promise.all(val).then(
                                                v => {
                                                    console.log(v)
                                                    const ctx = document.getElementById('myChart');
                                                    const myChart = new Chart(ctx, {
                                                        type: 'doughnut',
                                                        data: {
                                                            labels: Array.from(v).map(x => x['name']),
                                                            datasets: [{
                                                                label: 'imports',
                                                                data: Array.from(counts),
                                                                backgroundColor: [
                                                                    'rgba(255, 99, 132, 0.2)',
                                                                    'rgba(54, 162, 235, 0.2)',
                                                                    'rgba(255, 206, 86, 0.2)',
                                                                    'rgba(75, 192, 192, 0.2)',
                                                                    'rgba(153, 102, 255, 0.2)',
                                                                    'rgba(255, 159, 64, 0.2)'
                                                                ],
                                                                borderColor: [
                                                                    'rgba(255, 99, 132, 1)',
                                                                    'rgba(54, 162, 235, 1)',
                                                                    'rgba(255, 206, 86, 1)',
                                                                    'rgba(75, 192, 192, 1)',
                                                                    'rgba(153, 102, 255, 1)',
                                                                    'rgba(255, 159, 64, 1)'
                                                                ],
                                                                borderWidth: 1
                                                            }]
                                                        },
                                                        options: {
                                                            scales: {
                                                                y: {
                                                                    beginAtZero: true
                                                                }
                                                            }
                                                        }
                                                    });
                                                }
                                            )
                                        })

                                    // for (let r of regions) {
                                    //     getRegionById(r).then(
                                    //         reg => {
                                    //             div.innerHTML += `<button id="add" class="btn btn-light"> <h5> + ${reg['name']} </h5> </button> <p>${getCountRegions(r, values)}</p>`
                                    //             let btn = document.getElementById('add')
                                    //             btn.addEventListener('click', function (e) {
                                    //                 add_nisha(3, 32000).then(
                                    //                     v => {
                                    //                         console.log(v)
                                    //                     }
                                    //                 )
                                    //             })
                                    //         }
                                    //     )
                                    // }

                                }
                            )
                        }
                    )
                })
                if (search.value === '') {
                    codePanel.appendChild(li)
                } else if (v['description'].toLowerCase().includes(search.value.toLowerCase())) {
                    console.log(v['name'])
                    codePanel.appendChild(li)
                }
            }
        }
    )
}

window.onload = function () {
    // getRegions().then(
    //     values => {
    //         let regionPanel = document.getElementById('regions')
    //         let search = document.getElementById('search-regions')
    //         for (let v of values) {
    //             let li = document.createElement('li')
    //             li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['name']}</a></li>`
    //             li.addEventListener('click', function (e) {
    //                 let region = e.target.id
    //                 getProductsByRegion(region).then(val => val).then(
    //                     values => {
    //                         let codes = new Set()
    //                         for (let v of values) {
    //                             codes.add(Math.floor(v['product'] / 1000000))
    //                         }
    //                         let div = document.getElementById('products')
    //                         // div.innerHTML = `<h4 id="scrollspyHeading1">${val['name']}</h4>`
    //                         getRegionById(region).then(
    //                             val => {
    //                                 div.innerHTML = ` <h4 id="scrollspyHeading1">Импорт по: ${val['name']}</h4> <canvas id="myChart" width="100" height="100"></canvas>`
    //                         let counts = Array.from(codes).map(c => getCountCodes(c, values))
    //                         console.log(counts)
    //                         let res = []
    //                         getNames(res, codes).then(
    //                             val => {
    //                                 Promise.all(val).then(
    //                                     v => {
    //                                         console.log(v)
    //                                         const ctx = document.getElementById('myChart');
    //                                         const myChart = new Chart(ctx, {
    //                                             type: 'doughnut',
    //                                             data: {
    //                                                 labels: Array.from(v).map(x => x['description']).map(x => String(x).substring(0,32)),
    //                                                 datasets: [{
    //                                                     label: 'imports',
    //                                                     data: Array.from(counts),
    //                                                     backgroundColor: [
    //                                                         'rgba(255, 99, 132, 0.2)',
    //                                                         'rgba(54, 162, 235, 0.2)',
    //                                                         'rgba(255, 206, 86, 0.2)',
    //                                                         'rgba(75, 192, 192, 0.2)',
    //                                                         'rgba(153, 102, 255, 0.2)',
    //                                                         'rgba(255, 159, 64, 0.2)'
    //                                                     ],
    //                                                     borderColor: [
    //                                                         'rgba(255, 99, 132, 1)',
    //                                                         'rgba(54, 162, 235, 1)',
    //                                                         'rgba(255, 206, 86, 1)',
    //                                                         'rgba(75, 192, 192, 1)',
    //                                                         'rgba(153, 102, 255, 1)',
    //                                                         'rgba(255, 159, 64, 1)'
    //                                                     ],
    //                                                     borderWidth: 1
    //                                                 }]
    //                                             },
    //                                             options: {
    //                                                 scales: {
    //                                                     y: {
    //                                                         beginAtZero: true
    //                                                     }
    //                                                 }
    //                                             }
    //                                         });
    //                                     }
    //                                 )
    //                             })
    //                             }
    //                         )
    //
    //
    //                     })
    //
    //
    //             })
    //             if (search.textContent == '') {
    //                 regionPanel.appendChild(li)
    //             }
    //             else if (search.textContent in v['name']) {
    //                 regionPanel.appendChild(li)
    //             }
    //         }
    //     })

    // getCodes().then(
    //     values => {
    //         let codePanel = document.getElementById('codes')
    //         for (let v of values) {
    //             let li = document.createElement('li')
    //             li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['description']}</a></li>`
    //             li.addEventListener('click', function (e) {
    //                 let code = e.target.id
    //                 getProductsByCode(code).then(
    //                     values => {
    //                         getNameByCode(code).then(
    //                             val => {
    //                                 let regions = new Set()
    //                                 for (let v of values) {
    //                                     regions.add(v['region'])
    //                                 }
    //
    //                                 let div = document.getElementById('products')
    //                                 div.innerHTML = `<h4 id="scrollspyHeading1">Импорт по: ${val['description']}</h4> <canvas id="myChart" width="100" height="100"></canvas>`
    //                                 let counts = Array.from(regions).map(r => getCountRegions(r, values))
    //                                 getlocalRegions(regions).then(
    //                                     val => {
    //                                         Promise.all(val).then(
    //                                             v => {
    //                                                 console.log(v)
    //                                                 const ctx = document.getElementById('myChart');
    //                                                 const myChart = new Chart(ctx, {
    //                                                     type: 'doughnut',
    //                                                     data: {
    //                                                         labels: Array.from(v).map(x => x['name']),
    //                                                         datasets: [{
    //                                                             label: 'imports',
    //                                                             data: Array.from(counts),
    //                                                             backgroundColor: [
    //                                                                 'rgba(255, 99, 132, 0.2)',
    //                                                                 'rgba(54, 162, 235, 0.2)',
    //                                                                 'rgba(255, 206, 86, 0.2)',
    //                                                                 'rgba(75, 192, 192, 0.2)',
    //                                                                 'rgba(153, 102, 255, 0.2)',
    //                                                                 'rgba(255, 159, 64, 0.2)'
    //                                                             ],
    //                                                             borderColor: [
    //                                                                 'rgba(255, 99, 132, 1)',
    //                                                                 'rgba(54, 162, 235, 1)',
    //                                                                 'rgba(255, 206, 86, 1)',
    //                                                                 'rgba(75, 192, 192, 1)',
    //                                                                 'rgba(153, 102, 255, 1)',
    //                                                                 'rgba(255, 159, 64, 1)'
    //                                                             ],
    //                                                             borderWidth: 1
    //                                                         }]
    //                                                     },
    //                                                     options: {
    //                                                         scales: {
    //                                                             y: {
    //                                                                 beginAtZero: true
    //                                                             }
    //                                                         }
    //                                                     }
    //                                                 });
    //                                             }
    //                                         )
    //                                     })
    //
    //                                 // for (let r of regions) {
    //                                 //     getRegionById(r).then(
    //                                 //         reg => {
    //                                 //             div.innerHTML += `<button id="add" class="btn btn-light"> <h5> + ${reg['name']} </h5> </button> <p>${getCountRegions(r, values)}</p>`
    //                                 //             let btn = document.getElementById('add')
    //                                 //             btn.addEventListener('click', function (e) {
    //                                 //                 add_nisha(3, 32000).then(
    //                                 //                     v => {
    //                                 //                         console.log(v)
    //                                 //                     }
    //                                 //                 )
    //                                 //             })
    //                                 //         }
    //                                 //     )
    //                                 // }
    //
    //                             }
    //                         )
    //                     }
    //                 )
    //             })
    //             codePanel.appendChild(li)
    //         }
    //     }
    // )

    changeRegions()
    changeCodes()
    let regionSearch = document.getElementById('search-regions')
    regionSearch.onchange = function () {
        console.log(regionSearch.value)
        setTimeout(changeRegions(), 1000)
    }
    let codeSearch = document.getElementById('search-products')
    codeSearch.onchange = function () {
        setTimeout(changeCodes(), 1000)
    }
}
