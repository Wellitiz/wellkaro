<?php

require __DIR__ . '/Veiculos/vendor/autoload.php';

$app = require_once __DIR__ . '/Veiculos/bootstrap/app.php';

$kernel = $app->make(Illuminate\Contracts\Http\Kernel::class);

$request = Illuminate\Http\Request::capture();

$response = $kernel->handle($request);

$response->send();

$kernel->terminate($request, $response);