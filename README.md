# 🔍 ELK Stack Project Suite

Welcome to the **Elastic Stack (ELK) Integration & Search School** project repository. This comprehensive collection combines real-world ELK implementations with structured learning materials for mastering the Elastic Stack ecosystem.

---

## 📋 Project Overview

This repository is organized into two main sections:
- **🔧 ELK-Integration**: Production-ready implementations of various ELK pipelines
- **🎓 SearchSchool**: Structured learning course for Elasticsearch fundamentals

---

## 📁 Repository Structure

### 📦 **ELK-Integration/**
Complete end-to-end ELK pipeline implementations with Docker support.

#### 🌐 **django-integration/**
- **Purpose**: Logstash integration with Django web framework
- **Contents**: Django project configured to send logs to Logstash
- **Key Files**:
  - `dj_logstash/`: Django application with custom logging configuration
  - `logstash.conf`: Logstash pipeline configuration for Django logs
  - `docker-compose.yml`: Complete ELK stack deployment
- **Use Case**: Send Django application logs directly to Elasticsearch via Logstash

#### 📄 **filebeat-pipeline/**
- **Purpose**: Lightweight log shipping with Filebeat
- **Contents**: Filebeat configuration for monitoring files and Java applications
- **Key Files**:
  - `filebeat.yml`: Main Filebeat configuration
  - `filebeat.java_app.yml`: Specialized config for Java application logs
  - `logstash.conf`: Pipeline processing for incoming file data
  - `main.py`: Utility script for pipeline management
- **Use Case**: Monitor log files in real-time and forward to Elasticsearch

#### 🚀 **kafka-pipeline/**
- **Purpose**: High-throughput log processing with Apache Kafka
- **Contents**: Kafka producer integration with Logstash consumer
- **Key Files**:
  - `kafka-producer.py`: Producer script to send logs to Kafka topics
  - `logstash.conf`: Consumer pipeline reading from Kafka
  - `docker-compose.yml`: Kafka, Zookeeper, and ELK stack setup
- **Use Case**: Decouple log producers from Elasticsearch for scalability

#### 📊 **metricbeat-integration/**
- **Purpose**: Metrics collection from various data sources
- **Contents**: Two specialized metric collection pipelines

##### 🔴 **Redis/**
- **Purpose**: Monitor Redis database metrics
- **Key Files**:
  - `metricbeat.yml`: Metricbeat configuration with Redis module
  - `redis.yml`: Redis module-specific settings
  - `main.py`: Redis metrics collection script
  - `Dockerfile`: Container image for Redis with metrics export
- **Use Case**: Real-time monitoring of Redis performance and memory usage

##### 💾 **SQL/**
- **Purpose**: Monitor SQL database (MySQL) metrics
- **Key Files**:
  - `metricbeat.yml`: Metricbeat configuration with MySQL module
  - `mysql.yml`: MySQL-specific metric collection settings
  - `main.py`: Database metrics collection script
  - `Dockerfile`: Container image for monitored MySQL instance
- **Use Case**: Track database performance, query rates, and system resources

#### 🔄 **redis-pipeline/**
- **Purpose**: Event streaming through Redis queues
- **Contents**: Redis-based message queue architecture
- **Key Files**:
  - `redis_cli.py`: Redis client utilities for queue management
  - `logstash.conf`: Pipeline consuming from Redis queues
  - `docker-compose.yml`: Redis and ELK stack deployment
- **Use Case**: Use Redis as a message broker between data sources and Elasticsearch

#### ⚙️ **logstash_generator/**
- **Purpose**: Standalone Logstash configuration for testing
- **Contents**: Minimal Logstash setup for development and testing
- **Key Files**:
  - `logstash.conf`: Sample data generation pipeline
  - `logstash.yml`: Logstash runtime configuration
  - `docker-compose.yml`: Quick deployment setup
- **Use Case**: Test Logstash configurations without external dependencies

---

### 🎓 **SearchSchool/**
Comprehensive educational program on Elasticsearch and Elastic Stack

#### 📚 **Course Modules** (Sequential Learning Path)

| Module | Title | Focus Area |
|--------|-------|-----------|
| **0** | 📖 Introduction | Course overview and prerequisites |
| **1** | 🔑 Key Concepts | Fundamental Elasticsearch terminology |
| **2** | 🛠️ Installation ELK | Setup and configuration of ELK Stack |
| **3** | 📝 Indexing | Creating and managing indices |
| **4** | 🔍 Search DSL | Query syntax and search techniques |
| **5** | 📋 Indexing p.2 | Advanced indexing strategies |
| **6** | 📖 Text Analysis | Analyzers and text processing |
| **7** | 🔎 Search API | Practical search implementation |
| **8** | 📊 Aggregations | Data aggregation and analytics |
| **9** | 🎯 Types of Searches | Various search patterns |
| **10** | 🏗️ Hierarchical Documents | Nested and parent-child relationships |
| **11** | ⭐ Relevancy | Search ranking and scoring |
| **12** | 📤 Logstash and Beats | Data pipeline integration |

#### 📂 **Course Resources**
- `README.md`: Course overview and learning objectives
- `Practice.md`: Hands-on exercises for applicable modules
- `Readme.md`: Module-specific documentation
- `docker-compose.yml`: Quick-start ELK environment (Module 12)
- `src/`: Source code, sample data, and scripts for each module

#### 📊 **Practical Datasets**
- `movies.csv`, `ratings.csv`, `tags.csv`: Movie rating dataset (Module 10)
- `access-code-password-recovery-code.csv`: Authentication data (Module 5)
- `common.py`: Shared utilities for course exercises

---

## ⚙️ **Core Dependencies**

The project uses the following key technologies:

🐍 Python ecosystem:
- Django (4.1.4) - Web framework
- Flask (2.2.2) - Lightweight web framework
- Elasticsearch (7.11.0) - Search engine
- Pandas (1.5.2) - Data analysis
- NumPy (1.23.5) - Numerical computing
- Pydantic (1.10.2) - Data validation

🔄 Message & Cache:
- Redis (4.4.0) - Data caching and messaging
- aioredis (2.0.1) - Async Redis client

🛠️ Utilities & Testing:
- Faker (15.3.4) - Fake data generation
- Requests (2.28.1) - HTTP client
- python-dotenv (0.21.0) - Environment configuration

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.8+
- pip package manager

### Running a Pipeline

**Option 1: Django Integration**
```bash
cd ELK-Integration/django-integration
docker-compose up -d
# Access at http://localhost:8000
```

Option 2: Kafka Pipeline
```bash
cd ELK-Integration/kafka-pipeline
docker-compose up -d
python kafka-producer.py  # Start sending events
# Access Kibana at http://localhost:5601
```

Option 3: Learning Track
```bash
cd SearchSchool/2.\ Installation\ ELK
docker-compose up -d
# Follow practice exercises in Practice.md
```

---

📖 Learning Path Recommendations
- Beginner: 0 → 1 → 2 → 3 → 4
- Intermediate: 5 → 6 → 7 → 8 → 9
- Advanced: 10 → 11 → 12

---

🏗️ Architecture Highlights

Pipeline Architecture

Data Source → Beat/Agent → Logstash → Elasticsearch → Kibana


Supported Data Sources

- ✅ Django application logs
- ✅ File-based logs
- ✅ Kafka event streams
- ✅ Redis queues
- ✅ Database metrics (MySQL, Redis)


Processing Features

- 🔄 Real-time data transformation
- 📊 Metrics aggregation
- 🔍 Full-text search indexing
- 📈 Time-series analytics
- 🎯 Custom filtering and enrichment

---

📝 Contributing
- Each subfolder is self-contained and can be developed independently:
- Follow the docker-compose.yml structure for consistency
- Include proper documentation in module READMEs
- Test configurations locally before committing

 ---

🔗 External Resources
- 📌 Elasticsearch Official Docs
- 📌 Logstash Documentation
- 📌 Kibana Visualization Guide

 ---

📄 License & Notes

This project combines educational materials with production implementations.
Use responsibly and refer to individual module documentation for specific setup instructions.
Last Updated: May 2026

  ---

Happy Learning! 🎉 Dive into the Elastic Stack and master modern data indexing and search!