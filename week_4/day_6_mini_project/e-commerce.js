// Product Data
const products = [
  { id: 1, name: "Smartphone", price: 15000, category: "Electronics", image: "https://images.unsplash.com/photo-1597740985671-2a8a3b80502e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHNtYXJ0cGhvbmV8ZW58MHwxfDB8fHww&auto=format&fit=crop&q=60&w=500" },
  { id: 2, name: "Headphones", price: 2000, category: "Electronics", image: "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=388" },
  { id: 3, name: "T-Shirt", price: 799, category: "Clothing", image: "https://images.unsplash.com/photo-1759572095329-1dcf9522762b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1374" },
  { id: 4, name: "Jeans", price: 1200, category: "Clothing", image: "https://images.unsplash.com/photo-1602293589930-45aad59ba3ab?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=387" },
  { id: 5, name: "Novel - The Alchemist", price: 499, category: "Books", image: "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=387" },
  { id: 6, name: "Bike Helmet", price: 900, category: "Automobile", image: "https://images.unsplash.com/photo-1601971360277-7b4c8aa60894?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1374" },
  { id: 7, name: "Car Perfume", price: 350, category: "Automobile", image: "https://images.unsplash.com/photo-1693960794591-fc7c72a15e9f?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=387" },
];

// Cart Array
let cart = [];

// Function to display products
function displayProducts(filter = "all") {
  const productList = document.getElementById("product-list");
  productList.innerHTML = "";

  const filteredProducts = filter === "all" ? products : products.filter(p => p.category === filter);

  filteredProducts.forEach(p => {
    const card = `
      <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm">
          <img src="${p.image}" class="card-img-top" alt="${p.name}">
          <div class="card-body">
            <h5 class="card-title">${p.name}</h5>
            <p class="card-text">₹${p.price}</p>
            <button class="btn btn-add w-100" onclick="addToCart(${p.id})">Add to Cart</button>
          </div>
        </div>
      </div>`;
    productList.innerHTML += card;
  });
}

// Function to add to cart
function addToCart(id) {
  const product = products.find(p => p.id === id);
  cart.push(product);
  updateCart();
}

// Function to remove from cart
function removeFromCart(index) {
  cart.splice(index, 1);
  updateCart();
}

// Function to update cart modal
function updateCart() {
  const cartItems = document.getElementById("cart-items");
  const cartCount = document.getElementById("cart-count");
  const cartTotal = document.getElementById("cart-total");

  cartCount.textContent = cart.length;

  if (cart.length === 0) {
    cartItems.innerHTML = `<p class="text-center text-muted">Cart is empty.</p>`;
    cartTotal.textContent = "0";
    return;
  }

  let total = 0;
  cartItems.innerHTML = "";

  cart.forEach((item, index) => {
    total += item.price;
    cartItems.innerHTML += `
      <div class="d-flex justify-content-between align-items-center border-bottom py-2">
        <div>
          <h6 class="mb-0">${item.name}</h6>
          <small>₹${item.price}</small>
        </div>
        <button class="btn btn-sm btn-danger" onclick="removeFromCart(${index})">Remove</button>
      </div>`;
  });

  cartTotal.textContent = total;
}

// Filter Products
document.getElementById("categoryFilter").addEventListener("change", (e) => {
  displayProducts(e.target.value);
});

// Initialize
displayProducts();

// Optional: Initialize Select2
if (window.jQuery) {
  $('#categoryFilter').select2();
}
