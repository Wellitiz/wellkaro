$phpIni = "C:\Users\welli\Downloads\Antigravity\Projetos\Veiculos\php.ini"
$publicDir = "C:\Users\welli\Downloads\Antigravity\Projetos\Veiculos\public"
$port = 3004

$proc = Start-Process php -ArgumentList "-S", "localhost:$port", "-c", $phpIni, "-t", $publicDir, "-d", "auto_prepend_file=C:\Users\welli\Downloads\Antigravity\router.php" -PassThru -WindowStyle Hidden

Start-Sleep 3

if ($proc.HasExited) {
    Write-Host "Erro ao iniciar servidor"
    exit 1
}

Write-Host "Servidor rodando em http://localhost:$port (PID: $($proc.Id))"
Write-Host "Pressione Ctrl+C para parar"

try {
    while (-not $proc.HasExited) {
        Start-Sleep -Seconds 1
    }
} finally {
    Stop-Process $proc.Id -Force -ErrorAction SilentlyContinue
}