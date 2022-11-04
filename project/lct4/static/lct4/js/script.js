

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

window.onload = function () {
    getRegions().then(
        values => {
            let regionPanel = document.getElementById('regions')
            for (let v of values) {
                let li = document.createElement('li')
                li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['name']}</a></li>`
                li.addEventListener('click', function (e) {
                    let region = e.target.id
                    getProductsByRegion(region).then(
                        values => {
                            getRegionById(region).then(
                                val => {
                                    let div = document.getElementById('products')
                                    div.innerHTML = ''
                                    div.innerHTML += `<h4 id="scrollspyHeading1">${val['name']}</h4><p>${values.length}</p>`
                                }
                            )
                        }
                    )
                })
                regionPanel.appendChild(li)
            }
        }
    )

    getCodes().then (
        values => {
            let codePanel = document.getElementById('codes')
            for (let v of values) {
                let li = document.createElement('li')
                li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['description']}</a></li>`
                li.addEventListener('click', function (e) {
                    let code = e.target.id
                    getProductsByCode(code).then(
                        values => {
                            getNameByCode(code).then(
                                val => {
                                    let div = document.getElementById('products')
                                    div.innerHTML = ''
                                    div.innerHTML += `<h4 id="scrollspyHeading1">${val['description']}</h4><p>${values.length}</p>`
                                }
                            )
                        }
                    )
                })
                codePanel.appendChild(li)
            }
        }
    )

    getDistricts().then (
        values => {
            let districtPanel = document.getElementById('districts')
            for (let v of values) {
                let li = document.createElement('li')
                li.innerHTML = `<li><a class="dropdown-item" href="#" id="${v['id']}">${v['name']}</a></li>`
                li.addEventListener('click', function (e) {
                    let district = e.target.id
                    getProductsByDistrict(district).then(
                        values => {
                            getDistrictById(district).then(
                                val => {
                                    let div = document.getElementById('products')
                                    div.innerHTML = ''
                                    div.innerHTML += `<h4 id="scrollspyHeading1">${val['name']}</h4><p>${values.length}</p>`
                                }
                            )
                        }
                    )
                })
                districtPanel.appendChild(li)
            }
        }
    )
}