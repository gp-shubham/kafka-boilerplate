What is Kafka?
==============

- Kafka is just like a messaging system.
  ![Kafka 1](img/kafka-1.jpg)
- It is distributed platform / application

    - In production environment Kafka is referred as Kafka Cluster.
    - A cluster is made up of more than one Kafka server.
    - Each Kafka server is referred as Broker.
    
    ![Kafka 2](img/kafka-2.jpg)

- Kafka is fault-tolerant
    
    - Ability of a system to continue operating without interruption when one or more of its components fail.
    - In Kafka cluster messages are replicated in multiple broker.
    - Replication Factor.

       ![Kafka 3](img/kafka-3.jpg)

- Kafka is Sclable system

    - You can add new brokers anytime.
    - You can increase the number of consumers.

Kafka Handles 1 million messages request per second.



Kafka Architecture
==================

![Kafka 4](img/kafka-4.jpg)

- A Kafka server have different topics.
- You can create multiple topics in Kafka server.
- Those topics have something called partition and every topic have multiple partition.

- Kafka ecosystem have consumer group and there can be multiple Consumer Group.
- Each Consumer Group have 1 or more consumer instances.
- A consumer has to be associate with a Consumer Group.
- Apache Zookeeper is distributed, open-source configuration, synchronization service.
    - Its configuration management system.
    - Which messages consumer has read.
    - Cluster information.
    - Topic configuration.

Install Kafka and Zookeeper
===========================

- Download the software [click here...](https://kafka.apache.org/quickstart)
-

Kafka Topic
===========

- Topic is the Kafka component where Producers are connected.
- Producer publish message in Kafka Topic.
- Topics can be considered as a logical entitiy.
- In Kafka cluster each topic is present in every cluster node.

Kafka Topic Partition
=====================

- A kafka topic id divided into multiple parts that is called as partition.
- Partitions can ve considered as the linear data structure. Just like array.
- Messages are actually published to a partition in the topic.
- Every partition has a partition number
- Each partition has increasing index called offset.
- New messages are always pushed at the read end.
- Data is immutable after publish
- In multi broker Kafka Cluster Partitions for a topic are distributed across the whole cluster.

Kafka Producers in Python
=========================

- Producers publish message to the topics of their choice.
- In reality messages are published to topic partition.
- Configuration is needed by Producer.
    - bootstrap_server
    - topic
    - value_serializer
    - Over the wire means on the network
    - send method is called on producer to publish the data.
    - modules need to user `kafka-python` and `Faker`(to test).

Example: Single Broker - 1 Partition
************************************

- All the message will be published to as single partition.

