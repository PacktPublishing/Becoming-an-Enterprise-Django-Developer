/**** FUNCTION - AJAX Related Switch To Navigate To Related Page ****/
function $gotoSPA_Page() {
  const container = document.getElementById('details');
  const input = document.getElementById('seller-id');
  const id = input.value;

  console.log('id = ' + id);

  // Exercise 1
  // Renders as JSON Example - URL Created by the seller API through the router that we created.
  var url = `/chapter-8/sellers/${id}/`;

  // Exercise 2
  // Renders as HTML Example
  /*var url = `/chapter-8/seller/${id}/`;*/

  // Exercise 3
  // Fetch With Token URL
  /*var url = `/chapter-8/sellertoken/${id}/`;*/
  
  // Exercise 1
  // Renders as the JSON Example
  fetch(url, {
    method: 'GET',
    headers: {
    'Content-Type': 'application/json',
  }})
    .then(async(response) => {
    /*.then(response => {*/
      /*const html = await response.text();*/
      //const html = response.text();
    
      //console.log(response);
      //console.log(html);

      /*container.innerHTML = html;*/
      /*container.innerHTML = JSON.stringify(html);*/
      /*return res.json();*/
      return await response.json();
    })
    .then(async(data) => {
      const thisData = await data;
      console.log('Success:', thisData);
      /*container.innerHTML = thisData;*/
      container.innerHTML = JSON.stringify(thisData);
    });

  // Exercise 2
  // Renders as HTML Snippet Example
  //fetch(url, {
  //  method: 'GET',
  //  headers: {
  //  'Content-Type': 'application/json',
  //}})
  //  .then(async(response) => {
  //    return await response.text();
  //  })
  //  .then(async(data) => {
  //    container.innerHTML = await data;
  //  });

  // Exercise 3
  // Renders as HTML Snippet using an authorization Token Example
  //fetch(url, {
  //  method: 'GET',
  //  headers: {
  //  'Content-Type': 'application/json',
  //  'Authorization': 'Token fd9191f7d80770014d9e2824693bfbcf9225a020',
  //  'User': 'test'
  //}})
  //  .then(async(response) => {
  //    return await response.text();
  //  })
  //  .then(async(data) => {
  //    container.innerHTML = await data;
  //  });
}

//const btn = document.getElementById('get-sellers');

//btn.addEventListener('click', function (e) {
//  e.preventDefault();
//  e.stopPropagation();
//  e.stopImmediatePropagation();
//  $gotoSPA_Page();
//});