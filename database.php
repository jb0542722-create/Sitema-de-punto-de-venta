<?php
// database.php

$db_path = __DIR__ . '/pos.db';

try {
    // Crear una nueva conexión PDO a la base de datos SQLite
    $pdo = new PDO('sqlite:' . $db_path);

    // Configurar PDO para que lance excepciones en caso de error
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Opcional: Configurar el modo de obtención por defecto a asociativo
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    // Si la conexión falla, se muestra un mensaje de error y se termina el script
    die("Error de conexión a la base de datos: " . $e->getMessage());
}
?>
