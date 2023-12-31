function Success(action) {
  return (`
    <h3 class="text-success">Successful ${action}<h3>
  `)
}

function Error(action) {
  return (`
    <h3 class="text-danger">Some ERROR Acurred While ${action}<h3>
  `)
}


export { Success, Error }
