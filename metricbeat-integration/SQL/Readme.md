docker run -it --rm --network sql docker.elastic.co/beats/metricbeat:8.5.3 /bin/bash

docker cp  .\metricbeat.yml quirky_ride:/usr/share/metricbeat/
docker cp  .\mysql.yml quirky_ride:/usr/share/metricbeat/modules.d/

metricbeat modules enable sql

metricbeat test config
metricbeat test output

metricbeat -e -c metricbeat.yml


````yaml
- module: redis                                                                          
  metricsets:                                                                           
    - info                                                                              
    - keyspace   

  period: 10s                                                                            
  hosts: ["127.0.0.1:6379"]                                                                                                                                                       
  network: tcp                                                                          
  maxconn: 5                                                                           

````

docker cp  .\metricbeat.yml gracious_rubin:/usr/share/metricbeat/