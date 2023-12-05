// Declare the ORDERS array an set it to empty for now
let ORDERS = [];
let MY_ORDERS = [];
let DISPLAY = []

// Decalre the type of data to display to the user and set it to DEFAULT value
let type = "orders";

function Main() {
  setEventHandlers();
  setDefaultValues()
}

Main();

function setDisplay(type=null) {
  console.log('no way hoem')
  // function to change  the DISPLAY array values  based on the type provided by navigation link
  switch (type) {
    case 'orders':
      DISPLAY = ORDERS.filter((order) => {
        return order.state === 'null'
      })
      break;

    case 'my-orders':
      DISPLAY = MY_ORDERS
      break;

    case 'accepted':
      DISPLAY = ORDERS.filter((order) => {
        return order.state === 'true'
       })
      
      break;

    case 'rejected':
      DISPLAY = ORDERS.filter((order) => {
        return order.state === 'false'
      })
      
      break;
  }

  return render()
  

}
const Order = (order) =>
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
    </div> `);

async function fetchOrders(type='') {
  let url  =  `/api/order/orders/?type=${type}`;
  let res  =  await fetch(url);
  return await res.json();
}

function setDefaultValues() {
  fetchOrders().then(
    
  )
  
  
}

function render() {
  orderList = $("#order-list");

  // delete all existing orders
  orderList.empty();

  DISPLAY.map((order) => {
    orderList.append(Order(order));
  });
}

function setEventHandlers() {
  // Add event listener to all links

  // Default display ( orderer is another user)
  let links = $("#navigation .nav-link");
  for (let link of links) {
    link = $(link)
    link.click((e) => {
      let type = $(e.target).data('type')
      setDisplay(type)
    })
  }
  //    $('#orders').click(() => handleDefault())
  //
  //    // orderer is the user
  //    $('#my-orders').click(() => handleMyOrders())
  //
  //    // accepted orders by the current user
  //    $('#accepted').click(() => handleAccepted())
  //
  //    // rejected orders by the current user
  //    $('#rejected').click(() => handleRejected())
  //
}


function handleMyOrders() {
  clear("my-orders");
  newOrders = [];
  fetchOrders((type = "my_orders"))
    .then((orders) => {
      // Add new objects
      orders.map((order) => newOrders.push(order));
    })
    .then(() => {
      ORDERS = newOrders;
      render();
    });
}

function handleAccepted() {
  clear("accepted");
  newOrders = [];
  fetchOrders()
    .then((orders) => {
      // Add new objects
      orders.map((order) => {
        if (order.state === true) {
          newOrders.push(order);
        }
      });
    })
    .then(() => {
      ORDERS = newOrders;
      render();
    });
}

function handleRejected() {
  clear("rejected");
  newOrders = [];
  fetchOrders()
    .then((orders) => {
      // Add new objects
      orders.map((order) => {
        if (order.state === false) {
          newOrders.push(order);
        }
      });
    })
    .then(() => {
      ORDERS = newOrders;
      render();
    });
}

function clear(active = "") {
  ORDERS = [];
  navChildren = $("#navigation").children();
  for (let child of navChildren) {
    // child.children[0].removeClass('active')
    $(child.children[0]).removeClass("active");
  }
  // set new active link
  $("#" + active).addClass("active");
  render();
}
