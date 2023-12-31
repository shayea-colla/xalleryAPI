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
  return await res.json();
}


function setLinksEventHandlers(setDisplay) {
  console.log("executin setLinksEventHnalders")
  /* Add event listener to all links */
  // Default display is "orders"
 
}

function setNavLink(navLink) {
  console.log("executin setNavLink")
  // Set the nav link to be active based on the SelectedNav global variable
  let navLinks = $("#navigation .nav-link");

  for (let nav of navLinks) {
    $(nav).removeClass("active");
  }

  $(`[data-display='${navLink}']`).addClass("active");
}


export {
  fetchOrders,
  setLinksEventHandlers,
  setNavLink,
  getCookie,
};
