<div id="index"></div>

<sub>[<< 3. What are the three API verbs?](03verbs.md) | [<<Back to README index](README.md)| [5. What is an API?>>](05API.md)</sub>
<br>

# 4. Is MongoDB a SQL or NoSQL database?
<br>
<br>

<div style="text-align: center;">
    <img src="images/mongoDB.jpg" alt="Polymorphism" />
    <p>By MongoDB</P>
</div>
<br>

Table of contents
* [4.1. What is MongoDB?](#41-what-is-mongodb)
* [4.2. How does it look like a MongoDB Document Database?](#42-how-does-it-look-like-a-mongodb-document-database)
* [4.3. What is NoSQL?](#43-what-is-nosql)
* [4.4. What is SQL?](#44-what-is-sql)
* [4.5. Main differences between NoSQL and SQL](#45-main-differences-between-nosql-and-sql)
* [4.6. Pros and cons of NoSQL](#46-pros-and-cons-of-nosql)
* [4.7. SQL vs MongoDB (or NoSQL databases in general) — When to use](#47-sql-vs-mongodb-or-nosql-databases-in-general--when-to-use)
* [4.8. How to download MongoDB?](#48-how-to-download-mongodb)
* [4.9. How to use MongoDB?](#49-how-to-use-mongodb)
* [4.10. References](#410-references)

<br>

<br>




# 4.1. What is MongoDB?
<sub>[<<Back index](#index) | [4.2. How does it look like a MongoDB Document Database?>>](#42-how-does-it-look-like-a-mongodb-document-database)</sub>

MongoDB is a popular document-oriented database management system that falls under the **NoSQL** category.
<br>

It is designed to store, retrieve, and manage unstructured data in a flexible and scalable manner. 

<br>

<div style="text-align: center;">
    <img src="images/MongoDB collections.png" width="80%" height="80%" alt="MongoDB collections" />
    <p>By MongoDB</P>
</div>
<br>
MongoDB uses a JSON-like document model, allowing developers to store data in a format that closely resembles their application's data structures. All instead of storing data into columns and rows like a traditional relational DB. 

<br>

This flexibility makes MongoDB an excellent choice for applications with evolving schemas or complex data models.

<br>
<br>


# 4.2. How does it look like a MongoDB Document Database?
<sub>[<<4.1. What is MongoDB?](#41-what-is-mongodb)| [<<Back to index](#index) | [4.3.What is NoSQL?>>](#43-what-is-nosql) </sub>




A record in MongoDB is a `document`, which is a data structure composed of `field and value pairs`. MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays, and arrays of documents.

MongoDB stores documents in collections. `Collections` are analogous to tables in relational databases.

In MongoDB, each document stored in a collection requires a unique `_id field` that acts as a primary key. If an inserted document omits the *_id* field, the MongoDB driver automatically generates an ObjectId for the *_id* field.



For an example of how NoSQL looks, let's consider an example of storing information about a user and their hobbies. 

We need to store a user's first name, last name, cell phone number, city, and hobbies. Let's see, with the snippet code bellow, how the information, about a user and their hobbies, is stored in a MongoDB database: 

```
{
   "_id": 1,                              <--------FIELD:VALUE
   "first_name": "Leslie",                  <--------FIELD:VALUE
   "last_name": "Yepp",                     <--------FIELD:VALUE
   "cell": "8125552344",                    <--------FIELD:VALUE
   "city": "Pawnee",                        <--------FIELD:VALUE
   "hobbies": ["scrapbooking", "eating waffles", "working"]         <--------FIELD:VALUE
}
```
In order to retrieve all of the information about a user and their hobbies, a single document can be retrieved from the database. No joins are required, resulting in faster queries than in a SQL one.


The advantages of using documents are:

* Documents correspond to native data types in many programming languages.

* Embedded documents and arrays reduce need for expensive joins.

* Dynamic schema supports fluent [polymorphism](07polymorphism.md).




<br>

<br>

# 4.3. What is NoSQL?
<sub>[<<4.2. How does it look like a MongoDB Document Database?](#42-how-does-it-look-like-a-mongodb-document-database)   | [<<Back to index](#index) | [4.4.What is SQL?>>](#44-what-is-sql)</sub>

NoSQL (which stands for “not only SQL”) refers to a group of database systems that work differently from the traditional relational database models. Unlike traditional SQL databases, NoSQL databases are `schema-less`, meaning they do not enforce a fixed structure for data storage.
<br>

NoSQL databases are designed to handle large volumes of unstructured or semi-structured data, making them suitable for applications that require high scalability and performance. 

<br>

<br>

# 4.4. What is SQL?
<sub>[<<4.3.What is NoSQL?](#43-what-is-nosql)  | [<<Back to index](#index) | [4.5.Main differences between NoSQL and SQL>>](#45-main-differences-between-nosql-and-sql)</sub>
<br>

<br>

SQL is a classic relational database. It stores data in tables with rows and columns. It has a tabular structure, similar to what you’d see in an Excel spreadsheet. It stores relational data in a separate join table that uses the id of one model to be declared as being related to another. It’s most commonly used for relationships between models.

<br>

<div style="text-align: center;">
    <img src="images/SQL-MongoDB Correspondence.PNG" width="70%" height="70%"alt="SQL vs MongoDB" />
    <p>By codeinsightacademy.com</P>
</div>
<br>



<br>

# 4.5. Main differences between NoSQL and SQL
<sub>[<<4.4.What is SQL?](#44-what-is-sql)  | [<<Back to index](#index)| [4.6. Pros and cons of NoSQL>>](#46-pros-and-cons-of-nosql) </sub>
<br>



<br>

At a high level, NoSQL and SQL databases have many similarities. In addition to supporting data storage and queries, they both also allow us to retrieve, update, and delete stored data. 

However, there are some significant differences that affect NoSQL versus SQL performance, scalability, and flexibility:

* **Structure**

    *SQL* databases are table based, while

    *NoSQL* databases can be document-oriented, key-value pairs, or graph structures. In a NoSQL database, a document can contain key value pairs, which can then be ordered and nested.

* **Scalability**

    *SQL* databases scale vertically, usually on a single server, and require users to increase physical hardware to increase their storage capacities. In effect, while cloud-storage options are available, SQL databases can be prohibitively expensive for businesses when dealing with vast amounts of big data.

    *NoSQL* databases offer horizontal scalability, meaning that more servers simply need to be added to increase their data load. This means that NoSQL databases are better for modern cloud-based infrastructures, which offer distributed resources.

* **Language**

    *SQL* databases use SQL (Structured Query Language). 

    *NoSQL* databases use JSON (JavaScript Object Notation), XML, YAML, or binary schema, facilitating unstructured data. SQL has a fixed-defined schema, while NoSQL databases are more flexible.

* **Support**

    *SQL* is a popular standard language that is well supported by many different database systems, while

    *NoSQL* has varying levels of support in various database systems.It is still relatively new, with less help available on forums or through the community.

<br>

<br>

# 4.6. Pros and Cons of NoSQL
<sub>[<<4.5.Main differences between NoSQL and SQL](#45-main-differences-between-nosql-and-sql) | [<<Back to index](#index) | [4.8. How to download MongoDB?>>](#48-how-to-download-mongodb)</sub>

A significant benefit of NoSQL is that you don't have to define a schema upfront (or ever). This makes it easy to add new columns without dealing with all the issues involved in altering a vast table with lots of data already in it. It also means that if your queries don't require SQL, you can avoid the overhead of parsing and compiling SQL statements, modeling, and storing, providing an enormous performance boost when dealing with large amounts of data.

However, NoSQL is less mature than SQL. Here’s a look at **NoSQL's pros and cons**.

**Pros :**


* Flexible schema

* Usable on distributed infrastructure platforms

* Low-cost infrastructure

*High availability and throughput

**Cons  :**


* Less mature technology and difficult to manage

* Limited query capabilities

* Data inconsistency and poor performance in some complex scenarios

<br>

<br>

# 4.7. SQL vs MongoDB (or NoSQL databases in general) — When to use
<sub>[<<4.6. Pros and cons of NoSQL](#46-pros-and-cons-of-nosql) | [<<Back to index](#index) | [4.8. How to download MongoDB?>>](#48-how-to-download-mongodb)</sub>
<br>

<br>


`NoSQL`

If you have an unstructured data set that needs flexibility, then it may be the best option to go with a database that is Not SQL, such as a NoSQL database.

NoSQL databases like `MongoDB` are going to be perfect when you need to store data that doesn’t have relation and you need to hold a lot of data. You’ll be able to pull data very quickly and pull tons of it. Additionally for storing data in the cloud, you won’t hit limitations so quickly compared to if you were to use SQL for cloud storage. Furthermore, if you need relationships you can still use NoSQL but it most likely won’t be your best bet if you need to make specific and complex queries to the database.
<br>

<br>

`SQL`<br>

If you have data that relies heavily on relationships then it’s probably the best fit to utilize a relational SQL database.

SQL is going to be your best bet if you don’t anticipate huge changes in data storage and rely heavily on model relationships. SQL is also going to be great if you need complex queries and reports because you’ll be able to find very specific data with JOIN queries.

<br>
<br>

# 4.8. How to download MongoDB?
<sub>[<<4.7.SQL vs MongoDB (or NoSQL databases in general) — When to use](#47-sql-vs-mongodb-or-nosql-databases-in-general--when-to-use)  | [<<Back to index](#index) | [4.9.How to use MongoDB?>>](#49-how-to-use-mongodb)</sub>
<br>

<br>

You can create a MongoDB database in the following environments:

* **MongoDB Community :** The source-available, free-to-use, and self-managed version of MongoDB. You can download MongoDB for Windows, Linux or MAc, [here.](https://www.mongodb.com/docs/current/installation/)

* **MongoDB Atlas :** The fully managed service for MongoDB deployments in the cloud.

    MongoDB was developed for the cloud and has been widely used there for some time.

    However, more and more users are also interested in creating their applications with components that are offered as a “service”. To meet this need, [“MongoDB Atlas”](https://www.mongodb.com/atlas/database) has been released as a service offering. Atlas allows users to use MongoDB as a service without having to worry about managing the database. MongoDB Atlas is available on the leading cloud platforms AWS (amazon web services), Microsoft Azure and the Google Cloud Platform. This provides the flexibility to choose a public cloud provider without vendor lock-in and without having to rewrite code. These innovations are driving more and more companies to incorporate the MongoDB platform.

* **MongoDB Enterprise :** The subscription-based, self-managed version of MongoDB

<br>

When working with MongoDB, apart from using the command line, we can use the `MongoDB Compass` which is a graphical user interface (GUI) designed for working with MongoDB databases.

It is like a friendly dashboard for MongoDB. It helps you interact with your data in a more visual and intuitive way. Think of it as a tool that simplifies your interactions with MongoDB, making tasks easier and more efficient.

You can download MongoDB Compass for free for development environments from the official [MongoDB website](https://www.mongodb.com/docs/compass/current/install/). In fact, it is jointly downloaded when you download MongoDB.

<br>



<div style="text-align: center;">
    <img src="images/MongoDB Compass screenshot.png" width="80%" height="80%"alt="Polymorphism" />
    <p>Screenshot of MongoDB Compass dashboard</P>
</div>

<br>
<br>
<br>

# 4.9. How to use MongoDB?
<sub>[<<4.8. How to download MongoDB?](#48-how-to-download-mongodb)  | [<<Back to index](#index) | [4.10. References>>](#410-references)</sub>

Here are some resources where you can find a summary of the main `MongoDB commands`:


<div style="text-align: center;">
    <img src="images/MongoDB cheatsheet screenshot.png" width="80%" height="80%"alt="Polymorphism" />
    <p>MongoDB cheat-sheet. By cheatography.com</P>
</div>
<br>


* [MongoDB Manual: Database Commands:](https://www.mongodb.com/docs/current/reference/command/) The official MongoDB documentation provides detailed information about each command, including available parameters and examples. If you want to explore specific commands in depth, this resource is a great reference.

* [MongoDB Shell Commands: The Complete Cheat Sheet:](https://www.slingacademy.com/article/mongodb-shell-commands-the-complete-cheat-sheet/) This comprehensive guide covers MongoDB commands from basic to advanced. It’s suitable for both beginners and experienced developers. You’ll find commands related to working with databases, collections, querying, data management, monitoring, and troubleshooting.

* [MongoDB Cheat Sheet:](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/) This cheat sheet offers handy tips, quick references, and commands for connecting to MongoDB, performing CRUD operations, and more. It’s perfect for getting started with MongoDB.

<br>

For further information about how to download and use MongoDB, visit this condensed tutorial that I find very clear and useful: [Learn MongoDB in 1 Hour](https://www.youtube.com/watch?v=c2M-rlkkT5o&list=PLGVmXxqBGrPwP1vUQOlAyEhG93YlSTu2O&index=3)


<br>

<br>

# 4.10. References
[<<Back to index](#index)

For further information about MongoDB you can check these links:

* [Real Python: Python and MongoDB: Connecting to NoSQL Databases](https://realpython.com/introduction-to-mongodb-and-python/)
* [SQL vs. NoSQL: The Differences Explained + When to Use Each](https://www.coursera.org/articles/nosql-vs-sql)
* [MongoDB vs. NoSQL](https://thisvsthat.io/mongodb-vs-nosql)
* [SQL vs MongoDB(noSQL)! How to decide between databases](https://emrichmp.medium.com/sql-vs-mongodb-nosql-how-to-decide-between-databases-41e9ab178b03)

<br>


[<<Back to README index](README.md)