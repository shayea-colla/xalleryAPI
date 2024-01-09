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


// What should I do when I am waiting for server response ?
// display spinner 
// disable button


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

