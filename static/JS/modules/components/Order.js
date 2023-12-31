function Order (order) {
  let color = "info";
  if (order.state === true) {
    color = "success";
  } else if (order.state === false) {
    color = "danger";
  }

  // if order is not accepted  or rejected,  it should have both buttons
  const acceptButton = `<button data-orderid="${order.id}" data-state="true"  class="btn setState btn-info">accept</button>`;
  const rejectButton = `<button data-orderid="${order.id}" data-state="false"  class="btn setState btn-danger">reject</button>`;
  const deleteButton = `<button data-orderid="${order.id}" class="btn delete-order btn-danger">delete<span class="visually-hidden">order</span></button>`;

  // if order is belong to the user, accept and reject button shouldn't appear
  let footer = "";
  if (order.my_order) {
    // Only delete button should appear
    footer = deleteButton;
  } else if (order.state === null) {
    footer = acceptButton + rejectButton;
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

export {Order}
