export function isValidOrder(order) {
  // Validate Recipient and message 
  //
  if (order.recipient === "" || order.message === "") {
    return false

  } else {
    return true

  }
}

//  const modalAlert = $(".modal-body .modal-alert .alert")
//  modalAlert.removeClass('d-none')
//  modalAlert.addClass('d-none')
