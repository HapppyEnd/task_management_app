FROM prom/prometheus:v2.47.0

COPY prometheus.yml /etc/prometheus/prometheus.yml
COPY alert.rules.yml /etc/prometheus/alert.rules.yml

HEALTHCHECK --interval=30s --timeout=10s \
  CMD wget -q -O - http://localhost:9090/-/healthy || exit 1