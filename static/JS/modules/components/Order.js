export default function Order (order) {

  let color = "info";
  if (order.state === true) {
    color = "success";
  } else if (order.state === false) {
    color = "danger";
  }

  // if order is not accepted  or rejected,  it should have both buttons
  const acceptButton = `<button  data-order-id="${order.id}"  class="btn accept-order-btn btn-info">accept</button>`;
  const rejectButton = `<button  data-order-id="${order.id}"  class="btn reject-order-btn btn-danger">reject</button>`;
  const deleteButton = `<button  data-order-id="${order.id}" class="btn delete-order btn-danger">delete<span class="visually-hidden">order</span></button>`;

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
            <a class="text-secondary fs-6 fw-light" href="/accounts/${order.orderer.id}/">
              ${order.orderer.username}
            </a>
          </div>
          <div class="data fs-6 text-secondary fw-light">
            ${order.date}
          </div>
        </div>
        <div class="body mb-4 text-light">
          ${order.message}
        </div>
      <div class="footer d-flex justify-content-between"> 
      ${footer}
      </div>
    </div> 
   `);
};
