<?php
$host = '0.0.0.0';
$port = 3004;

$docroot = __DIR__ . '/../Veiculos/public';

$router = <<<'ROUTE'
<?php
$uri = $_SERVER['REQUEST_URI'];
$file = __DIR__ . $_SERVER['SCRIPT_NAME'];

if ($uri === '/artisan' || strpos($uri, '/artisan') === 0) {
    chdir(__DIR__ . '/../Veiculos');
    passthru('php artisan serve');
    exit;
}

if (is_dir($file)) {
    $file = rtrim($file, '/') . '/index.php';
}

if (!file_exists($file)) {
    http_response_code(404);
    echo "404 Not Found";
    exit;
}

require $file;
ROUTE;

$pidFile = __DIR__ . '/server.pid';

if (file_exists($pidFile)) {
    $pid = (int)file_get_contents($pidFile);
    if ($pid && posix_kill($pid, 0)) {
        echo "Servidor já está rodando na porta $port (PID: $pid)\n";
        exit;
    }
    unlink($pidFile);
}

echo "Iniciando servidor em http://localhost:$port\n";
echo "Pressione Ctrl+C para parar\n";

$cmd = "php -S $host:$port -t \"$docroot\"";
system($cmd);