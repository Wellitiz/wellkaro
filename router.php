<?php
$uri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

if ($uri === '/artisan') {
    chdir(__DIR__ . '/Projetos/Veiculos');
    include __DIR__ . '/Projetos/Veiculos/artisan';
    exit;
}

$publicPath = __DIR__ . '/Projetos/Veiculos/public';

if ($uri === '/' || $uri === '') {
    $uri = '/index.php';
}

$file = $publicPath . $uri;

if (!is_dir($file) && file_exists($file)) {
    return false;
}

if (!file_exists($publicPath . '/index.php')) {
    http_response_code(500);
    echo "index.php não encontrado";
    exit;
}

chdir($publicPath);
$_SERVER['SCRIPT_NAME'] = '/index.php';
$_SERVER['SCRIPT_FILENAME'] = $publicPath . '/index.php';

require $publicPath . '/index.php';