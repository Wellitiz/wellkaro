<?php

$uri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

if ($uri === '/artisan') {
    chdir(__DIR__ . '/../Veiculos');
    passthru('php ' . __DIR__ . '/Veiculos/artisan serve --port=3004');
    exit;
}

if ($uri === '/' || $uri === '') {
    $uri = '/index.php';
}

$file = __DIR__ . '/Veiculos/public' . $uri;

if (!file_exists($file)) {
    $file = __DIR__ . '/Veiculos/public/index.php';
    $_SERVER['SCRIPT_NAME'] = '/index.php';
    $_SERVER['SCRIPT_FILENAME'] = $file;
}

if (!file_exists($file)) {
    http_response_code(404);
    echo "404 Not Found";
    exit;
}

require $file;