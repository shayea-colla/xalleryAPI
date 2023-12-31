import { Order } from "./modules/components/Order.js";
import { setEventListenersHandlers } from "./modules/utils/handleAjax.js";

import {
  fetchOrders,
  setLinksEventHandlers,
  setNavLink,
} from "./modules/utils/utils.js";

// Declare the ORDERS array an set it to empty for now
let MY_ORDERS = [];
let ORDERS = [];
let DISPLAY = [];
let navLink = "orders"; // Default display is orders
const bURL = "/api/order/orders/";

function Main() {
  setMyOrders();
  setOrders();

  // DEFAULT VALUE FOR SELECTED NAV
  setLinksEventHandlers(setDisplay);
}

Main();

function setDisplay(display) {
  // function to change  the DISPLAY array values  based on the type provided by navigation link

  navLink = display

  switch (display) {
    case "orders":
      DISPLAY = ORDERS;
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


async function setMyOrders(display='my_orders') {
  // fetch MY_ORDERS
  MY_ORDERS = await fetchOrders(bURL, "my_orders");

  // add my_order attr to each order that belong to the user, so you can differ between orders in term of UI design
  MY_ORDERS.map((order) => {
    order.my_order = true;
  });

  // set the Display to reflect new changes
  return setDisplay(display);
}


async function setOrders() {
  // fetch ORDERS
  ORDERS = await fetchOrders(bURL);

  // set the Display to reflect new changes
  return setDisplay('orders');
}


function render() {

  let orderList = $("#order-list");

  // delete all existing orders
  orderList.empty();

  DISPLAY.map((order) => {
    orderList.append(Order(order));
  });

  // Reset selected nav link
  setNavLink(navLink);
  setLinksEventHandlers()

  // set click listeners for accept , reject and delete buttons
  // and make ajax request based on the event, (accept clicked; accept request, etc)
  setEventListenersHandlers(bURL, setOrders, setMyOrders, navLink);

}

