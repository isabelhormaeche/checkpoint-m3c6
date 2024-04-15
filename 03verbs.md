<sub>[<<2. Which method is automatically executed when a class is instantiated?](02init.md)| [Back to README index](README.md)| [4. Is MongoDB a SQL or NoSQL database?>>](04mongoDB.md)</sub>

# 3. What are the three API verbs?

In REST (Representational State Transfer), an **API (Application Programming Interface)** allows one application to access features of the other application through its functions and procedures.

It is also considered as a set of rules for interacting with a web service. These rules define how clients (a person or application) can send requests to the web service (application or database) and how the service should respond to those requests. (You can find further information here: [5. What is an API?](05API.md)).



<br>
<figure>
    <img src="images/rest-api.png"  alt="image of class and objects">
    <figcaption>By mannhowie.com</figcaption>
</figure>
<br>


<br>


APIs use HTTP protocol to facilitate the processing of data and to define the type of operation you want to perform on a resource. The **HTTP verbs** (also known as **REST verbs**) indicate the action you want to take. The three **HTTP verbs** commonly used in APIs are:


1.-`GET`(read data): used to **retrieve** data from a web service (server). A GET request should only retrieve data and should have no other effect. It is like When you browse the web, your browser sends GET requests to fetch resources (like web pages) from servers. A successful GET operation returns an OK (200 status code). 

For example, fetching details of a movie from a movie API would involve a GET request.

     
2.-`POST`(create data): used to send data to a web service to **create** a new resource on the server. For example, When you submit a form on a website, it typically sends a POST request to save your data. 
    
For example, creating a new user account or adding a new item to an online store.

3.-`PUT`(update data): used to send data to a web service to **update** an existing resource.If you want to modify an existing record, you send a PUT request. 

For instance, updating a user's profile information.
<br>

The bellow table  explains the operation, target resources, and what happens if a request fail or succeeds. ( Image By [Dev.to](https://dev.to/atanda0x/rest-api-best-practice-understanding-verbs-and-status-code-fei) ).

<br>
<figure>
    <img src="images/REST Verbs API.png"  alt="image of class and objects">
    <figcaption></figcaption>
</figure>
<br>


 **HTTP Status Codes**:
   - Responses with codes in the **"200"** range indicate successful requests.
   - Errors in the **"400"** range are client-related, while errors in the **"500"** range are server-related.
<br>

<br>

Some other popular HTTP verbs are: DELETE, and PATCH. 

`DELETE`(delete data): This verb is used to *delete* or remove a resource from a web service.

For example, When you delete a file or cancel a subscription, a DELETE request is sent.

`PATCH` : This verb is used to send data to a web service to **update** only a portion of an existing resource.
   
<br>

In summary, APIs allow applications to talk to each other using well-defined rules, and HTTP verbs play a crucial role in specifying the desired action on resources. Whether you are fetching data, creating, updating, or deleting, these verbs play a crucial role in  the communication between client and server.





# References

[REST API Best Practice: Understanding Verbs and status code](https://dev.to/atanda0x/rest-api-best-practice-understanding-verbs-and-status-code-fei))

[The 5 Verbs of REST APIs: A Beginner’s Guide](https://artofdataengineering.com/5-verbs-of-rest-apis/)

[REST API VERBS](https://www.chubbydeveloper.com/rest-api-verbs-make-sure-you-follow-the-best-rest-practices/)

 [REST APIs Explained - 4 Components - mannhowie.com](https://mannhowie.com/rest-api)

<br>


[<<Back to README index](README.md)