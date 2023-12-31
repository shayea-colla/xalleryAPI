import { Loading } from "./../components/spinner.js";
import { Success, Error } from "./../components/Complete.js";
import { getCookie } from "./utils.js";
import { isValidOrder } from './validation.js'

function handleDeleteOrder(e, bURL, setMyOrders, navLink) {
  // Get ID of the order you want to delete
  const orderId = $(e.target).data("orderid");


  const ModalBody = $("#ConfirmOrderDeletion .modal-body")
  const ModalConfirm = new bootstrap.Modal('#ConfirmOrderDeletion')


  // show the confirmation modal
  ModalConfirm.show()

  // set click listener to the actuall button that will run the deletion
  $("#confirmDelete").click((e)=> {

    // Replace the warning content with a loading spinner 
    replaceBody(Loading())


    // Hide action buttons
    $(e.target).addClass('disabled')


    // Make DELETE request to delete order
    $.ajax({
      url: bURL + `${orderId}/`,
      method: "DELETE",
      headers: {
        "X-CSRFTOKEN": getCookie("csrftoken"),
      },
      success: (data, statusCode) => {
        // handle Sucesss after deletion
        handleSuccess()
      },
      error: (data, statusCode) => {
        // handle Errors 
        handleError()
      },
    });
  })

  function handleSuccess() {
    // Replace Body with success indication
    replaceBody(Success("Deletion"))

    // close the modal after a peariod of time, no right away
    setTimeout(() => {
      ModalConfirm.hide()
    }, 1300);
    
    // Reset myOrders to reflect new changes, ( order should be removed )
    setMyOrders(navLink)
  }

  function handleError() {
    replaceBody(Error("Deletion"))

  }

  function replaceBody(element) {
    ModalBody.empty()
    ModalBody.append(element)

  }

}


function setEventListenersHandlers(bURL, setOrders, setMyOrders, navLink) {
  /* Set Event listeners to everythign that needs to*/

  console.log("Executin setAjaxEventHandlers")

  // Set listeners to navigation links
  $("#navigation .nav-link").click((e) => {
    // Get display data from the html data attribute named 'display'
    let display = $(e.target).data("display");
    // set the display to the selected
    setDisplay(display);
  });




  // handle order deletion
  $(".delete-order").click((e)=> handleDeleteOrder(e, bURL, setMyOrders, navLink));
  // handle order sending
  $(".confirmSend").click((e) => console.log(e))

  $(".setState").click((e) => {
    /* Make patch request to change the state of an order ( accepted, rejected ) */

    // Get the order Id attatch to the button via data-orderId attribute,
    // (don't forget to wrapt e.target to the jquery object or you won't have access to the data method)
    const orderId = $(e.target).data("orderid");
    const state = $(e.target).data("state");
    $.ajax({
      url: bURL + `${orderId}/`,
      method: "PATCH",
      data: { state: state },
      headers: {
        "X-CSRFTOKEN": getCookie("csrftoken"),
      },
      success: (data, statusCode) => {
        // Reset the orders  to reflect new changes
        setOrders().then(() => setDisplay());
      },
      error: (data, statusCode) => {
        console.log(statusCode);
      },
    });
  });
}

function handleSendingOrder() {

  const order = {
      recipient: $("#recipient-name").val().trim(),
      message: $("#message-text").val().trim(),
  }

  if (isValidOrder(order)) {
    sendOrder(order)
  } else {
    alert("not sending")
  }
}



function sendOrder(order) {
    // Send ajax request to server 
    console.log(`sending order to: ${order.recipient} with message: ${order.message}`)

}



export {
  setEventListenersHandlers,
};
