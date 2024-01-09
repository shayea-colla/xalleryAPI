import  Order from '../components/Order.js'
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


async function fetchOrders(bURL, type = "") {
  /* This function takes two arguments: 
   __bURL : base url to fetch resource from
   __type : query_params arguemnt to specifiy the type of orders to fetch 
   */
  let url = bURL + `?type=${type}`;
  let res = await fetch(url);
  return transform(await res.json());
}


function display(orders) {
  /* display orders to the screen
   __orders : array of orders objects
  */
  const orderListContainer = $("#order-list-container")

  // empty the order list
  orderListContainer.empty()

  // Create an array containing Order objects orderList 
  const orderList = orders.map((order) => Order(order))

  // Appned Order List to the container
  orderListContainer.append(orderList)

}


function setNavLink(displayType) {
  /* set active link to whatever passed as displayType */

  $("#navigation .nav-link").removeClass('active');

  $(`[data-display-type=${displayType}]`).addClass("active");
}


function transform(orders) {
  // Transform Response
  return orders

}

function updateOrder(orderId, state) {
  /* what are the changes required after accepting or rejecting any order? 
   - change the background color
   - change the border color
   - remove the footer buttons */

 // change the background color
 $(`#${orderId}`).removeClass(`bg-info-subtle`)
 $(`#${orderId}`).addClass(`bg-${state}-subtle`)

 // change the border collor
 $(`#${orderId}`).removeClass(`border-info-subtle`)
 $(`#${orderId}`).addClass(`border-${state}-subtle`)

 // remove the footer buttons
 $(`#${orderId}`).children('.footer').empty()

}


export {
  fetchOrders,
  setNavLink,
  getCookie,
  display,
  updateOrder,
};
