# Broke-Login

**What is Broke Login tool?**

Broke Login is a tool developed in Python3 that basically focuses on attacking Web Logins, based on the parameters and information the tool manages to perform more attacks and more options.

It is a modular tool and these are the modules of the tool:
 
- SQL Injection Login Bypass
- Username Enumeration via Different Responses
- Username Enumeration via Different Time Responses
- Password BruteForce  

**How works?**

**SQL Injection Login Bypass:**

This module basically makes a web request with which it saves in a variable the content lenght of the response with two invented credentials, then changes the random credentials and makes the requests with the username and password with this payload: 

**' 1=1-- -**

This payload is the most typical and I think the only one to bypass the login with a SQL Injection, once this is done send another web request but this case with this payload and compare if the server response is different than the one made previously with the random credentials.

![image](https://user-images.githubusercontent.com/79543461/194398421-a9b315c0-61dd-42c7-a6ee-009110df80d2.png)

**Username Enumeration via Different Responses:**

This module is even simpler than the previous one, to see how easy it is I explain how it works, when you have a website that responds an error message when the user is incorrect, with the option -error this script will try to make a brute force attack by modifying the username and wait to receive a request without this error message, that will mean that the user exists.

![image](https://user-images.githubusercontent.com/79543461/194400753-dea22022-7e56-4709-92ba-6f3c600d6c93.png)

**Username Enumeration via Different Time Responses:**

This module lists the users of the site thanks to a higher response time of the users that do exist, why does this happen?

This happens because if the user does not exist the web will not go directly to check if the password is correct, but if the user is correct, it will check the password, and if it also has to check the password it will take longer to respond.

![image](https://user-images.githubusercontent.com/79543461/194406430-b93bbaf6-c59c-47bf-9bd2-baa606f8c017.png)

**Password BruteForce:**

This module is not very difficult to understand, it takes the user that you have entered with the valid parameter and attacks it by brute force, which is basically based on trying all the passwords of the file that you have indicated with parameter -pwordlist.

![image](https://user-images.githubusercontent.com/79543461/194408634-5ca9597a-e0b2-4a87-9616-d61714a7f658.png)
