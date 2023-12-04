// Declare the ORDERS array an set it to empty for now
let ORDERS = []

// Decalre the type of data to display to the user and set it to DEFAULT value
let type = 'orders'

function Main() {
    addEventListeners()
    handleDefault()
    console.log($("#navigation .nav-link"))
}

Main()




const Order = (order) => (
  $(`
    <div id=${order.id} class="order-item border border-secondary m-2 p-3 rounded-3">
        <div class="header mb-4 d-flex justify-content-between">
          <div class="orderer">
            <a class="text-muted" href="">
              ${order.orderer}
            </a>
          </div>
          <div class="data text-muted">
            ${order.date}
          </div>
        </div>
        <div class="body mb-4 text-light">
          ${order.message}
        </div>
        <div class="footer d-flex justify-content-between">
          <button class="btn accept btn-outline-success">accept</button>
          <button class="btn refuse btn-outline-secondary">refuse</button>
        </div>
    </div> `
  )
)



async function fetchOrders(type='') {
  let url = `/api/order/orders/?type=${type}`
  let res = await fetch(url)
  return await res.json()
}

function render() {
  orderList = $('#order-list')

  // delete all existing orders
  orderList.empty()

  ORDERS.map((order) => {
    orderList.append(Order(order))
  })

}

function addEventListeners() {
    // Add event listener to all links 
    
    // Default display ( orderer is another user)
    $('#orders').click(() => handleDefault())

    // orderer is the user
    $('#my-orders').click(() => handleMyOrders())

    // accepted orders by the current user
    $('#accepted').click(() => handleAccepted())

    // rejected orders by the current user
    $('#rejected').click(() => handleRejected())

}

function handleDefault() {
    clear('orders')
    newOrders = []
    fetchOrders().then((orders) => {
        // Add new objects
        orders.map(order => newOrders.push(order))
    }).then(()=> {
        ORDERS = newOrders
        render()
    })

}

function handleMyOrders() {
    clear('my-orders')
    newOrders = []
    fetchOrders(type='my_orders').then((orders) => {
        // Add new objects
        orders.map(order => newOrders.push(order))
    }).then(()=> {
        ORDERS = newOrders
        render()
    })
}

function handleAccepted() {
    clear('accepted')
    newOrders = []
    fetchOrders().then((orders) => {
        // Add new objects
        orders.map((order) => {
            if (order.state === true) {
                newOrders.push(order)
            }
        })

    }).then(()=> {
        ORDERS = newOrders
        render()
    })
}

function handleRejected() {
    clear('rejected')
    newOrders = []
    fetchOrders().then((orders) => {
        // Add new objects
        orders.map((order) => {
            if (order.state === false) {
                newOrders.push(order)
            }
        })

    }).then(()=> {
        ORDERS = newOrders
        render()
    })
}

function clear(active='') {
    ORDERS = []
    navChildren = $('#navigation').children()
    for (let child of navChildren) {
       // child.children[0].removeClass('active')
       $(child.children[0]).removeClass('active')
    }
    // set new active link
    $('#' + active).addClass('active')
    render()
}
