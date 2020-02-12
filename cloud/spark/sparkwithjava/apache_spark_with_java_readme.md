# master apache with java 

NB: this course has a lot of simple demo spark programs.   They are in
subpackages of `com.sparkTutorial` 

additional resources
check: udemy:
Apache Spark for Java Developers  (21 h) chapter on streaming

todo: gradle crash tutorial


demo code is set in szi/sparkTutorial ide project generated with gradel

## plan: 

* ch 1 getting started with apache
* ch 2 RDD (resilient reliable dataset)
* ch 3 spark architecture and components
* ch 4 pair rdd
* ch 5 advanced spark topic
* ch6 spark sql 
* ch7 running spark in cluster


## NBs 

* ch2 RDD, caching
* ch3 core bits of architecture

### intro to spark
* spark is fast in-memory data processing engine over distributed nodes
* computations are in memory
* povides a general programming model , enables application by composing arbitrary operators
such as filtering and grouing 

## setting project with idea

Java gradle project
```bash
cd sparkTutorial
./gradlew idea
```
this downloads gradle-3.2.1-bin.zip and all maven dependencies 

`./build.gradle`  is the file with instructions about the java project and its dependencies 

java first example counts words in in/word_count.text
in `src/main`
com.spark.Tutorial.WordCount  

It initiates  JavaSparkContext object
JavaRDD is a resilient distributed dataset.


## ch2 RDD

**RDD**  is a spark core concept:
* a dataset is a collection of data. think of a table in RDB
* in spark all ops are: 
    * create new RDD
    * transform existing RDDs
    * call operations on RDDs to compute a result

* spark automatically distribures an RDD among all cluster nodes and parallyzes calculations on it

#### demo first spark program  sparkTutorial/WordCount
v reads  from in/word_count.txt # < 1K words



#### demo: sparkTutorial/rdd/airports  airport problems
* run main() in AirportsBy* problems

the source file is a csv with 2 lines  below
```
1665,"Geneve Cointrin","Geneva","Switzerland","GVA","LSGG",46.238064,6.10895,1411,1,"E","Europe/Paris"
502,"Gatwick","London","United Kingdom","LGW","EGKK",51.148056,-0.190278,202,0,"E","Europe/London"
2985,"Sheremetyevo","Moscow","Russia","SVO","UUEE",55.972642,37.414589,622,4,"N","Europe/Moscow"
3797,"John F Kennedy Intl","New York","United States","JFK","KJFK",40.639751,-73.778925,13,-5,"A","America/New_York"
```

this file calls com.SparkTutorial.rdd.commons.Utils.COMMA_DELIMETER

* MapFunction vs FlatMapFunction transforms. 
    * flatmap flattens Iterables with n>1 levels into a flat list
        * eg. WordCount 

    * map : 1 to 1 relationship, flatMap 1 to many relationship
    * WordCount  example

* passing functions to spark.  org.apache.spark.api.java.function
    * Function
    * Function2
    * FlatMapFunction

* we can define and pass an anonymous inner class, a named java class or a lambda expression (lambda since java 8)

#### Set Operations

* sample   get a sample fro RDD, with, without replacement
* distinct() transform it is expensive. avoid using it unless necesswary
* union, inersection subtract cartesian product
    * 2 RDDs are intput, 1 RDD is an output
    * untion does not remove duplicates
    * intersection removes dupblicates, expensive
    * subtract : S1 - (S1 /\ S2)  expensive 
    * cartesion  returns all possible pairs of a and b coming from S1 and S2

**demo**   rdd/nasaApacheWebLogs/SameHostSolution.java 
    * calls intersection()  the set operatino

#### Actions
actions are the operations which will return a final value to the driver program or persist data to external storage 

* collect
    * from String Rdd you would get a list of strings
    * !! entire DS must fit in a single node  memory
    * widely used in unit tests
    * ** demo rdd/collect/CollectExample.java **
* count, countByValue
    * count() total number of elements in RDD, 
    * countByValue makes a map of value - counts.  Useful for duplicates detection
    * **demo rdd/count/CountExmaple**
* take
    * takes n elements from RDD. 
    * used in unit tes 
    * **demo rdd/take/TakeExample**

* savAsTextFile
    * saves file to FS, AWS, Hadoop

* reduce
    * eg. `Integer product = integerRdd.reduce((x,y) -> x*y);`
    *  **demo rdd/reduce/ReduceExample.java**   applies reduce to all elements in RDD on all depth devels resulting in a single value.


#### demo  rdd/sumOfNumbers/SumOfNumbersProblem  

for debugging it is useful to evaluation expression rddVar.collect()  to see the RDD contents


#### RDD importance  aspects

* each rdd is broken in partitions  amount cluster nodes.

* partitioning is done automatically by spread

* Rdds are immutable, necessary for concurrent calculations. 

* RDDs are resilient. They can be recreated at any time. Can be recovered if a node in cluster fails. 

* RDDS are lazily evaluated. No execution until an action is called. 

* You can think of RDDs as of consisting instructions on how to compute the data that we build up through tranformations. 

* Transformations **return RDDs** whereas actions **return some other data types**


### Caching and Persistence

* important for iterative transformations on Rdds 
* persist()
* **demo rdd/persist/PersistExample**
    * persist in MEMORY or MEMORY_AND_DISK, MEMORY_ONLY_SER, ..
    * MEMORY_ONLY is fastests, MEMORY_ONLY_SER make objects more space-efficient but still quite fast to access.  do not save to disk unldess the functions that computed your datasets are expensive, or they filter a significant amount of the data. 

## ch Spark Architecture and components

* 1 master node with a driver program and spark Contenxt,  n slave worker nodes
* a driver Program  through sparkContext converts jobs in tasks  run by Executor
* driver program creates partitions of RDD, sends them to executors, gets back the results
* spark in local mode.  all components are run in the same process on the local machine

#### spark components
* spark core {execution model, the shuffle, caching} connects to hdfs  : engine
* spark sql, spark streaming, MLlib, GraphX : UI/API components


* spark sql : sql-like interface  for working with structured data.  trending up in workflows 
* spark streaming: api for manipulating data streams.  enables powerful interactive and analytical applications across both streaming and historical data
    * connects to HDFS, Flume, Kafka 
* spark MLlib  a scalable machine learning library with high-quality algos
    * usable in java, scala, python
    * models: classification, regression, clustering, collaborative filtering, dimensionality reduction

* GraphX  graph computation engine: create transform and reason about graph structured data at scale. extends spark RDD with a new graph abstraction with properties attached to vertices and edges + lib of common algos including PageRank and Triangle Counting. 

#### users of spark
* data scientists
    * indentify patterns, risks, opportunities in data. analyzing data to discover insights
    * spark helps accelerate data science workflow from data access, ad-hoc analysis and integration to machine learning and visualization. 
* data engineers
    * build application that lever advanced analytics in partnership with the data scientist.  general classes of apps are moving to Spark, including compute-intensive apps. that require input from data streams such as sensors or social data. 

## ch Pair RDD 

pair rdd are key value pair
* 1 row = 1 key  and 1 or n values
* pair RDD is an efficient data structure for this
* scala.Tuple2 class

#### demo  pairRdd.create.PairRddFromtupleList  
* to create PairRDDs

* transformations on pair RDDs operate on pairs, not individual elements

#### demo pairRdd.filter.AirportsNotInUsaSolution


#### demo pairRdd.mapValues.AirportsUpperCaseSolution
* mapValues()

**Aggregation**
* aggregate statics over all values of the same key : reduceByKey

#### demo  com.sparkTutorial.pairRdd.aggregation.reducebykey.wordCount 


### demo om.sparkTutorial.pairRdd.aggregation.reducebykey.housePrice


### demo realEstate
`com.sparkTutorial.pairRdd.aggregation.reducebykey.housePrice.AverageHousePriceSolution` 

csv data format: 1:UUId of house, 2:location of house, 3:price of house in usd, 4:number of bedrooms in house, 5: num of bathrooms of the property, 6: size of house in sq feet

goal: compute average price for houses with different bedrooms


