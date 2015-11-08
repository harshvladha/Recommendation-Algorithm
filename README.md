# RecommendMe - Recommendation Engine for everything!

[![Join the chat at https://gitter.im/harshvladha/RecommendMe](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/harshvladha/RecommendMe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Network Based Recommendation Engine using Map-Reduce (in Python) to run on top of Hadoop!

The recommendation engine is divided into three parts :

1. Pre-process Job
2. Resource Allocation Job
3. Recommendation Job

Each job has their own mapper and reducer.

MongoDB is used in this version for real-time data storage and streaming. 

[Algorithm explanation link](http://2wicklers.com/recommendme-recommendation-engine/)

Movie-Lens data set : ml-1m is used as reference!

## Hadoop Streaming
To run python map-reduce programs we need Hadoop Streaming. Command for hadoop streaming is inside bin directory of this project, please replace directories as per your need.
