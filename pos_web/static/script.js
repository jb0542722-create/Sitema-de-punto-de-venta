document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list');
    const cartList = document.getElementById('cart-list');
    const cartTotal = document.getElementById('cart-total');

    // Función para renderizar el carrito
    function renderCart(cart) {
        cartList.innerHTML = '';
        let total = 0;
        cart.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.nombre} - $${item.precio.toFixed(2)}`;
            cartList.appendChild(li);
            total += item.precio;
        });
        cartTotal.textContent = total.toFixed(2);
    }

    // Cargar productos al iniciar
    fetch('/api/products')
        .then(response => response.json())
        .then(products => {
            products.forEach(product => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <span>${product.nombre} - $${product.precio.toFixed(2)}</span>
                    <button class="add-to-cart-btn" data-id="${product.id}">Añadir al Carrito</button>
                `;
                productList.appendChild(li);
            });
        });

    // Cargar carrito inicial
    fetch('/api/cart')
        .then(response => response.json())
        .then(cart => renderCart(cart));

    // Manejar clicks para añadir al carrito (usando delegación de eventos)
    productList.addEventListener('click', (event) => {
        if (event.target.classList.contains('add-to-cart-btn')) {
            const productId = event.target.dataset.id;

            fetch('/api/cart/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id: parseInt(productId) }),
            })
            .then(response => response.json())
            .then(cart => {
                renderCart(cart);
            });
        }
    });
});
