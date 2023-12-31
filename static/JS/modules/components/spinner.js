function Loading(color='danger') {
  return(
    `<div class="spinner-border text-${color}" style="width: 3rem; height: 3rem;" role="status">
        <span class="visually-hidden">Loading...</span>
    </div>`

  )
  
} 


export { Loading }
