# zap-scan

The ZAP Baseline Scan with seed urls

```sh
docker build -t zap .
docker run --rm -v $(pwd):/zap/wrk/:rw -t zap zap-baseline.py -t https://example.com -r report.html --url-file=url.txt
open report.html
```

```sh
docker run --rm -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t https://example.com -r report.html --hook=hooks.py
```
