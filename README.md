# Sentinel

> ML-powered incident detection and root-cause analysis for distributed software systems.

Sentinel is a machine learning engineering project designed to detect abnormal behavior in distributed software systems, characterize incidents, and rank likely root causes.

The project uses a controlled, simulated e-commerce platform called **ShopStream** to create realistic operational scenarios, generate telemetry, deliberately inject failures, and investigate how machine learning can assist engineers during software incidents.

The system is being built progressively, from the underlying distributed application and observability layer to ML models, model serving, monitoring, and eventual retraining.

## Problem

Modern technology systems are distributed across multiple services and infrastructure components. When one component begins to fail, the resulting effects can propagate through the system.

For example:

```text
Database degradation
        ↓
Payment latency increases
        ↓
Order requests become slower
        ↓
API errors increase
        ↓
Users experience failures
```

The component showing the most obvious symptoms is not necessarily the component that caused the incident.

Sentinel investigates the following problem:

> **How can machine learning use operational telemetry from a distributed software system to detect abnormal behavior, characterize incidents, and rank likely root-cause services?**

## ShopStream

ShopStream is a small simulated e-commerce platform that provides the environment in which Sentinel operates.

The initial architecture includes:

```text
                         ┌───────────────┐
                         │  API Gateway  │
                         └───────┬───────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
       │ User Service│   │Search Service│   │Order Service│
       └─────────────┘   └──────┬──────┘   └──────┬──────┘
                                │                  │
                                ▼                  ▼
                         ┌─────────────┐    ┌─────────────┐
                         │ Product DB  │    │Payment Svc  │
                         └─────────────┘    └──────┬──────┘
                                                  │
                                                  ▼
                                           ┌─────────────┐
                                           │ Payment DB  │
                                           └─────────────┘
```

The environment will eventually support controlled failure scenarios such as:

* CPU exhaustion
* memory leaks
* database slowdowns
* service crashes
* network degradation
* traffic spikes
* deployment regressions
* cascading failures
* multiple simultaneous incidents

Each controlled incident will have known ground truth so that Sentinel's predictions can be evaluated objectively.

## Sentinel's ML Tasks

The ML layer will eventually address several related problems:

### 1. Anomaly Detection

Determine whether current system behavior is abnormal.

### 2. Incident Classification

Determine what type of incident is occurring.

### 3. Severity Prediction

Estimate the impact of an incident.

### 4. Root-Cause Ranking

Rank services or components according to their likelihood of being the source of an incident.

The system will distinguish between **detection**, **diagnosis**, and **prediction** rather than treating incident response as a single classification problem.

## Architecture

The long-term system will evolve toward:

```text
                     SHOPSTREAM
                         │
                  Operational Data
                         │
                         ▼
                ┌─────────────────┐
                │ Data Validation │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Feature Pipeline│
                └────────┬────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      Anomaly Detection      Incident Classification
             │                       │
             └───────────┬───────────┘
                         ▼
                  Severity Prediction
                         │
                         ▼
                 Root-Cause Ranking
                         │
                         ▼
                   Sentinel API
                         │
                         ▼
                 Engineer Interface
```

This architecture will be developed incrementally rather than implemented all at once.

## Development Roadmap

### Phase 1 — Build the World

* Distributed ShopStream services
* Docker containers
* Kubernetes
* Local development with kind
* Service-to-service communication

### Phase 2 — Make the World Observable

* Operational telemetry
* Prometheus
* Grafana
* Service and infrastructure metrics

### Phase 3 — Break the World

* Failure injection
* Controlled incidents
* Ground-truth metadata
* Reproducible simulations

### Phase 4 — Understand the Data

* Telemetry datasets
* Exploratory analysis
* Temporal analysis
* Statistical baselines

### Phase 5 — Build Sentinel's Intelligence

* Anomaly detection
* Incident classification
* Severity prediction
* Root-cause ranking

### Phase 6 — Productionize the ML

* Training pipelines
* Experiment tracking
* Model registry
* FastAPI inference
* Containerized model serving

### Phase 7 — Monitor Sentinel

* Data-quality monitoring
* Data drift
* Prediction drift
* Model performance
* Inference monitoring

### Phase 8 — Continuous Improvement

* Retraining
* Candidate model evaluation
* Model promotion
* CI/CD
* Increasingly difficult incident scenarios

## Technology Stack

The stack will evolve as the project develops.

Current planned technologies include:

* **Python**
* **FastAPI**
* **Docker**
* **Kubernetes**
* **kind**
* **kubectl**
* **Helm**
* **Prometheus**
* **Grafana**
* **NumPy**
* **Pandas**
* **scikit-learn**
* **MLflow**
* **pytest**
* **GitHub Actions**

Tools will be introduced only when they solve a genuine project requirement.

## Repository Structure

```text
sentinel/
├── README.md
├── .gitignore
├── docs/
├── shopstream/
├── infrastructure/
├── scripts/
└── tests/
```

## Current Status

**Phase 1 — Build the World**

The immediate goal is to build **ShopStream v1**:

1. Create the distributed services
2. Containerize them
3. Deploy them to a local Kubernetes cluster
4. Establish service-to-service communication
5. Generate normal system behavior
6. Deliberately break a dependency
7. Observe and understand the resulting behavior

Machine learning will be introduced only after the underlying system is sufficiently reliable and observable.

## Engineering Principles

Sentinel follows a few principles throughout development:

* **Problem before technology**
* **Baseline before ML**
* **Ground truth matters**
* **Time matters**
* **Detection ≠ diagnosis**
* **Prediction ≠ certainty**
* **Production is a lifecycle**
* **Depth before breadth**
* **Complexity should be earned**

The objective is not simply to train a model that performs well on synthetic data.

The objective is to understand how machine learning can become a reliable component of a larger software system.

---

**Status:** Under active development
