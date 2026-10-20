# module 07

**Source:** [`module 07.pdf`](../archive/canvas-submissions/module%2007.pdf)  
**Course:** IA 445 - Ethical Hacking and Offensive Security (EMU)  
**Author:** Julio Barros

## Page 1

Name: Julio Barros 
Understanding Web Applications and SQL Injection 
Attacks 
 
Web applications have become integral to modern digital experiences, offering dynamic content 
and interactive services to users worldwide. However, their complexity and connectivity also 
expose them to various security vulnerabilities, notably SQL Injection attacks. This report aims to 
elucidate the types of web applications and delve into the intricacies of SQL Injection attacks, 
adopting a structured approach for clarity and comprehensiveness. 
Types of Web Applications 
Web applications can be broadly classified based on their functionality and the nature of content 
they deliver: 
 Static Web Applications 
Static web applications deliver content without any server-side processing, primarily consisting of 
HTML, CSS, and JavaScript files. These applications do not interact with databases or perform 
complex processing, presenting the same content to every user. 
Dynamic Web Applications 
Contrary to static ones, dynamic web applications involve server-side processing to dynamically 
generate content. They interact with databases and backend services, providing personalized 
content to users based on their inputs or actions. 
Single Page Applications (SPAs) 
SPAs represent a modern web application paradigm where the entire application loads within a 
single web page. They offer a seamless user experience by dynamically updating content in 
response to user actions without reloading the page. 
Content Management Systems (CMS) 
CMS platforms enable users to create, manage, and modify website content without direct code 
interaction. Popular examples include WordPress, Joomla, and Drupal, which offer extensive 
customization and plugin ecosystems. 
E-commerce Applications 
These applications facilitate online buying and selling activities, featuring product catalogs, 
shopping carts, and payment processing functionalities to mimic physical retail experiences in a 
digital environment.

## Page 2

Portal Web Applications 
Portal applications serve as gateways to a variety of features or sections, often incorporating user 
authentication to provide personalized experiences. They may include forums, email services, and 
search engines under a unified interface. 
Progressive Web Applications (PWAs) 
PWAs blend features of traditional web applications and native mobile apps, bringing offline 
capabilities, background processing, and a mobile-friendly interface to enhance user engagement 
and performance. 
SQL Injection Attacks 
SQL Injection attacks exploit vulnerabilities in a web application's database interaction to execute 
unauthorized SQL commands, potentially compromising data integrity and confidentiality. 
In-band SQLi (Classic SQLi) 
This most straightforward form of SQLi involves using the same communication channel for both 
attack delivery and gathering results. It includes: 
- **Error-based SQLi**: Exploits error messages from the database to glean its structure or extract 
data. 
- **Union-based SQLi**: Utilizes the UNION SQL operator to combine and retrieve data from 
multiple database tables. 
Inferential SQLi (Blind SQLi) 
Inferential SQLi involves formulating queries that provoke behavior or responses from the database, 
thereby inferring data or structure without directly fetching data: 
- **Boolean-based SQLi**: Relies on crafting SQL queries that result in a boolean value, affecting 
the content returned to the user based on the truthiness of the condition. 
- **Time-based SQLi**: Involves queries that cause the database to delay its response, with the 
delay duration indicating the query's truth value. 
Out-of-band SQLi 
This technique is used when the attacker cannot use the same channel for attack and response. It 
depends on the database server's capability to make external requests, such as DNS or HTTP , to 
transmit data to the attacker.

## Page 3

Compounded SQLi 
Compound SQL Injection, also known as second-order SQL Injection or compounded attack, is a 
more sophisticated form of SQL Injection. In this type of attack, the malicious SQL code is not 
executed in the first instance when the user input is initially processed by the application. Instead, 
the malicious input is stored in the database and only executed later, in a different context. This can 
happen when the application retrieves the stored data and uses it as part of a SQL query without 
proper sanitization or escaping. Compounded SQLi integrates SQL injection with other attack 
vectors, such as cross-site scripting (XSS) or buffer overflows, to amplify the attack's impact or 
bypass security measures. 
Conclusion 
Understanding the various types of web applications and the potential SQL Injection attacks they 
may face is crucial for developing robust, secure applications. Employing secure coding practices, 
validating user inputs, and using prepared statements are key strategies in mitigating the risks 
associated with SQL Injection attacks. By fostering an awareness of these vulnerabilities and 
defenses, developers and security professionals can better protect sensitive data and maintain the 
integrity of web applications. 
Reference 
 
SayOne Technologies. (n.d.). Explore the 10 Different Types of Web Applications & Their Uses. 
Retrieved from https://www.sayonetech.com.
