#ARG ELASTIC_STACK_VERSION
FROM docker.elastic.co/beats/metricbeat:8.5.3
COPY metricbeat.yml /usr/share/metricbeat/metricbeat.yml
USER root
RUN chown root:metricbeat /usr/share/metricbeat/metricbeat.yml
RUN chmod go-w /usr/share/metricbeat/metricbeat.yml
USER metricbeat
CMD ["-environment", "container"]