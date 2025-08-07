<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Punto de Venta - Tienda de Abarrotes</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Punto de Venta</h1>
        </header>

        <main class="main-layout">
            <!-- Sección de Productos -->
            <section class="products-section">
                <h2>Productos</h2>
                <div class="product-search">
                    <input type="text" id="search" placeholder="Buscar producto por nombre o código...">
                </div>
                <?php
                    require_once 'database.php';

                    try {
                        $stmt = $pdo->query('SELECT name, price FROM products ORDER BY name');
                        $products = $stmt->fetchAll();
                    } catch (PDOException $e) {
                        $products = [];
                        // En un entorno de producción, sería bueno registrar este error.
                        // error_log('Error al consultar productos: ' . $e->getMessage());
                    }
                ?>
                <ul class="product-list">
                    <?php if (empty($products)): ?>
                        <li>No hay productos para mostrar.</li>
                    <?php else: ?>
                        <?php foreach ($products as $product): ?>
                            <li>
                                <span><?= htmlspecialchars($product['name']) ?> - $<?= htmlspecialchars(number_format($product['price'], 2)) ?></span>
                                <button>Agregar</button>
                            </li>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </ul>
            </section>

            <!-- Sección del Ticket/Venta -->
            <aside class="ticket-section">
                <h2>Ticket de Venta</h2>
                <ul class="ticket-items">
                    <!-- Productos agregados aparecerán aquí -->
                    <li class="ticket-item">
                        <span>Leche Entera (1L)</span>
                        <span>$20.00</span>
                    </li>
                </ul>
                <div class="ticket-total">
                    <p>Total: <span id="total-amount">$20.00</span></p>
                </div>
                <div class="ticket-actions">
                    <button class="btn-pagar">Pagar</button>
                    <button class="btn-cancelar">Cancelar</button>
                </div>
            </aside>
        </main>

        <footer>
            <p>Sistema de Punto de Venta - Mi Tiendita</p>
        </footer>
    </div>
</body>
</html>
