export function isValidOrder(order) {
  // Validate Recipient and message 

  const modalAlert = $(".modal-body .modal-alert .alert")

  if (order.recipient === "" || order.message === "") {
    modalAlert.removeClass('d-none')
    return false

  } else {
    modalAlert.addClass('d-none')
    return true
  }
}
