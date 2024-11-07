$("#slider1, #slider2, #slider3, #slider4").owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
      nav: false,
      autoplay: true,
    },
    600: {
      items: 3,
      nav: true,
      autoplay: true,
    },
    1000: {
      items: 5,
      nav: true,
      loop: true,
      autoplay: true,
    },
  },
});

$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];

  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // Update the quantity text on the page
      eml.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];

  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // Update the quantity text on the page
      eml.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];

  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // Update the quantity text on the page
      eml.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

$(".minus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];

  $.ajax({
    type: "GET",
    url: "/minuscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // Update the quantity text on the page
      eml.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

$(".remove-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var $button = $(this); // Cache the jQuery object for better performance and readability

  $.ajax({
    type: "GET",
    url: "/removecart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      console.log("Item removed successfully");
      // Update the quantity text on the page
      $("#amount").text(data.amount);
      $("#totalamount").text(data.totalamount);
      $button.closest(".cart-item").remove(); // Assuming each cart item is wrapped within a parent with class "cart-item"
    },
    error: function (xhr, status, error) {
      console.error("Error removing item from cart:", error);
      // Handle error condition appropriately, e.g., show an error message to the user
    },
  });
});

// $(".remove-cart").click(function () {
//   var id = $(this).attr("pid").toString();
//   var eml = this;

//   $.ajax({
//     type: "GET",
//     url: "/removecart",
//     data: {
//       prod_id: id,
//     },
//     success: function (data) {
//       console.log("Delete");
//       // Update the quantity text on the page
//       document.getElementById("amount").innerText = data.amount;
//       document.getElementById("totalamount").innerText = data.totalamount;
//       eml.parentNode.parentNode.parentNode.parentNode.remove();
//     },
//   });
// });
