//import { util } from './modules/utils.js'

// Declare the ORDERS array an set it to empty for now
let MY_ORDERS = [];
let ORDERS = [];
let DISPLAY = [];
let SelectedNav = "orders"; // Default display is orders
const BaseURL = "/api/order/orders/";

function Main() {
  setDefaultValues();
  setLinksEventHandlers();
}

Main();


function setDisplay(type = null) {
  // function to change  the DISPLAY array values  based on the type provided by navigation link
  SelectedNav = type;
  switch (type) {
    case "orders":
      DISPLAY = ORDERS
      break;

    case "my_orders":
      DISPLAY = MY_ORDERS.filter((order) => {
        return order.state === null;
      });
      break;

    case "accepted":
      DISPLAY = MY_ORDERS.filter((order) => {
        return order.state === true;
      });

      break;

    case "rejected":
      DISPLAY = MY_ORDERS.filter((order) => {
        return order.state === false;
      });

      break;
  }

  return render();
}

const Order = (order) => {
  let color = "info";
  if (order.state === true) {
    color = 'success'
  } else if (order.state === false) {
    color = 'danger'
  }

  // if order is not accepted  or rejected,  it should have both buttons
  const acceptButton = `<button data-orderid="${order.id}" data-state="true"  class="btn setState btn-info">accept</button>` 
  const rejectButton = `<button data-orderid="${order.id}" data-state="false"  class="btn setState btn-danger">reject</button>` 
  const deleteButton = `<button data-orderid="${order.id}"  class="btn delete-order btn-danger">Del</button>` 

  // if order is belong to the user, accept and reject button shouldn't appear
  let  footer = '';
    if (order.my_order) {
        // Only delete button should appear
        footer = deleteButton

    } else if (order.state === null) {
        footer = acceptButton + rejectButton
    } 



  return $(`
    <div id=${order.id} class="order-item border border-${color}-subtle bg-${color}-subtle m-2 p-3 rounded-3">
        <div class="header text-light mb-4 d-flex justify-content-between">
          <div class="orderer">
            <a class="text-light" href="/accounts/${order.orderer.id}/">
              ${order.orderer.username}
            </a>
          </div>
          <div class="data ">
            ${order.date}
          </div>
        </div>
        <div class="body mb-4 text-muted">
          ${order.message}
        </div>
      <div class="footer d-flex justify-content-between"> 
      ${footer}
      </div>
    </div> 
   `);
};

async function fetchOrders(type ="") {
  let url = BaseURL + `?type=${type}`;
  let res = await fetch(url);
  return await res.json();
}

async function setDefaultValues() {
  // fetch ORDERS
  ORDERS = await fetchOrders();

  // fetch MY_ORDERS
  MY_ORDERS = await fetchOrders("my_orders");

  // add my_order attr to each order that belong to the user, so you can differ between orders in term of UI design
  MY_ORDERS.map((order) => {
    order.my_order = true;
  });

  // set DISPLAY to default value ( ORDERS )
  DISPLAY = ORDERS

  // Setas default values;
  return render();
}

function render() {
  let orderList = $("#order-list");

  // delete all existing orders
  orderList.empty();

  DISPLAY.map((order) => {
    orderList.append(Order(order));
  });

  // Reset selected nav link
  setNavLink();
  // set event handler for accept buttons after rendering them
  setAcceptRejectDeleteEventHandlers();
}

function setAcceptRejectDeleteEventHandlers() {
  /* Add event listener to all accept and reject buttons */

  $(".setState").click((e) => {
    // Get the order Id attatch to the button via data-orderId attribute, (don't forget to wrapt e.target to the jquery object or you won't have access to the data method)
    const orderId = $(e.target).data("orderid");
    const state = $(e.target).data("state");
    $.ajax({
      url: BaseURL + `${orderId}/`,
      method: "PATCH",
      data: { state: state },
      headers: {
        "X-CSRFTOKEN": getCookie("csrftoken"),
      },
      success: (data, statusCode) => {
        setDefaultValues();
      },
      error: (data, statusCode) => {
        console.log(statusCode);
      },
    });
  });
    $('.delete-order').click((e)=> {
        const orderId = $(e.target).data("orderid");
        $.ajax({
          url: BaseURL + `${orderId}/`,
          method: "DELETE",
          headers: {
            "X-CSRFTOKEN": getCookie("csrftoken"),
          },
          success: (data, statusCode) => {
            setDefaultValues();
          },
          error: (data, statusCode) => {
            console.log(statusCode);
          },
        });

    })
}

function setLinksEventHandlers() {
  /* Add event listener to all links */

  // Default display ( orderer is another user)
  $("#navigation .nav-link").click((e) => {
    let type = $(e.target).data("type");
    setDisplay(type);
  });
}

function setNavLink() {
  // Set the nav link to be active based on the SelectedNav global variable
  let navLinks = $("#navigation .nav-link");
  for (let nav of navLinks) {
    $(nav).removeClass("active");
  }
  $(`[data-type='${SelectedNav}']`).addClass("active");
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

