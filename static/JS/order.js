import { 
  fetchOrders, 
  display, 
  setNavLink, 
  getCookie,
  updateOrder,
} from './modules/utils/utils.js'

const baseUrl = '/api/order/orders/'



// Set the Default display when the page load
$(document).ready( async () => {
 
  handleDisplayingOrders('orders')

})


// Attache event listeners to the nav links and display orders depending on that 
$(".nav-link").click( async (e) => {
  const displayType = $(e.target).data('display-type')

  // handle the Displaying of orders 
  handleDisplayingOrders(displayType)
})



async function handleDisplayingOrders(displayType) {
  // Set the navigation link to be active
  setNavLink(displayType)

  // Fetch orders from the server
  const res = await fetchOrders(baseUrl, displayType)

  // Display orders
  display(res)

  // Set Listeners to buttons ( accept , reject, delete )
  setButtonsListeners()

}


function setButtonsListeners() {
  // Set click Listeners and handle function for each buttons ( accept , reject, delete )

  $(".accept-order-btn").click(handleOrderAcception)
  $(".reject-order-btn").click(handleOrderRejection)

}

$("#add-order").click(handleAddingNewOrder)

async function getDesigners() {
  const response = await fetch('http://127.0.0.1:8000/api/order/designers/')
  return await response.json()
}

function validateOrder() {
  // get order inputs values
  getDesigners().then((designers) => {

    const receiver = $("#order-receiver").val()
    const message = $("#order-message").val()

    // Check that receiver exist among designers
    const designer = designers.filter((designer) => {
      designer.username === receiver
    })[0]
    if (message.trim().length > 0 && designer?.id !== undefined) {
      // if valid data submitted 
      return { is_valid: true, data: { designer, message } }
    }
    return { is_valid:false, data:null }
  })
}

function showErrorMessage(element) {
  // show error message by removing the dsiplay class 
  $(element).removeClass('d-none')

}

function sendOrder(data) {
  // Ajax request to add new order
  $.ajax({
    url: baseUrl,
    method: "POST",
    data: {
      message: data.message,
      receiver: data.receiver.id
    },
    headers: {
      "X-CSRFTOKEN": getCookie("csrftoken"),
    },

    success: (data, statusCode) => {
      console.log('added new order')

    },
    error: (data, statusCode) => {
      console.error(data.responseJSON.detail);
    },
  });

}
function handleAddingNewOrder(e) {
  const addOrderModal = new bootstrap.Modal('#addOrderModal')

  // show adding new order modal form
  addOrderModal.show()

  // Listen for the user to submit the order
  $("#confirmOrderSend").click( async () =>{
    const order = await validateOrder()

    if (order.is_valid == true) {
      // sned order
      sendOrder(order.data)

    } else {
      showErrorMessage("#add-order-alert")
    }

  })

  // Steps to add new order
  //
  // - Show adding new order modal form
  // - validate data when submitted
  // - if valid ( send order ) else show error message
  // - if request rejected due to invalid user: show the message that indicate that 
}

function handleOrderAcception(e) {
  const orderId = $(e.target).data('order-id')

  // disable button 
  $(e.target).addClass("disabled")

  // show spinner 
  $(e.target).prepend(`
    <div class="spinner-border-sm spinner-border text-secondary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  `)

  $.ajax({
    url: baseUrl + `${orderId}/`,
    method: "PATCH",
    data: { state: true },
    headers: {
      "X-CSRFTOKEN": getCookie("csrftoken"),
    },

    success: (data, statusCode) => {
      // Rerender the whole list of orders ( it will not be an effecint approache )
      console.log('success acception')
      updateOrder(orderId, 'success')

    },
    error: (data, statusCode) => {
      console.error(data.responseJSON.detail);
    },
  });

}



function handleOrderRejection(e) {

  const orderId = $(e.target).data('order-id')

  // disable button 
  $(e.target).addClass("disabled")

  // show spinner 
  $(e.target).prepend(`
    <div class="spinner-border-sm spinner-border text-secondary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
`)

  // Send ajax request to update the state of an order to ( flase )
  $.ajax({
    url: baseUrl + `${orderId}/`,
    method: "PATCH",
    data: { state: false },
    headers: {
      "X-CSRFTOKEN": getCookie("csrftoken"),
    },

    success: (data, statusCode) => {
      // Rerender the whole list of orders ( it will not be an effecint approache )
      console.log('success rejection')
      updateOrder(orderId, 'danger')

    },
    error: (data, statusCode) => {
      console.error(data.responseJSON.detail);
    },
  });
}

// Expermenting 

