docker run -it --rm --network  docker.elastic.co/beats/metricbeat:7.10.0 /bin/bash

docker cp  .\metricbeat.yml objective_albattani:/usr/share/metricbeat/
docker cp  .\redis.yml objective_albattani:/usr/share/metricbeat/modules.d/

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