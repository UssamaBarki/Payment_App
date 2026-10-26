Running the Histogram Analyzer:

1. Clone the Repository: Download the project to your local machine using an IDE (e.g., PyCharm) or GitHub Desktop.
2. Set Up a Virtual Environment: Create and activate a Python virtual environment within your project directory.
3. Install Dependencies: Use the requirements.txt file to install all necessary packages. In PyCharm: Open the project, navigate to Tools > Sync Python Requirements, and follow the prompt to install the required packages.
4. Run the Application: Execute the Run_all.py file.
5. Launch the Interface: A local server will start, and the payment app will automatically open in your default web browser.


How the payment app works:


This section contains the graphics and instructions to use the Online Payment System web app. 

1. Home Page

After initiating the development server web app can be accessed using URL https//: 127.0.0.1:8000(development server). Upon entering the URL user will be directed to the homepage of Online Payment System Website. 
The Home Page serves as the welcoming interface of the payment system, offering users a clear entry point into the platform. Designed with a clean and intuitive layout, it provides easy navigation options for new users to register and existing users to log in. 
Users can access registration and login links via well-placed buttons, ensuring a seamless onboarding experience. The page also maintains a responsive design, making it accessible across devices like desktops, tablets, and smartphones. This page establishes a professional and user-friendly foundation, allowing users to smoothly transition into the platform’s functionalities. 



2. User Registration 

The user registration page which can be navigated to by clicking register button on the home page of the online payment system. The User Registration process allows new users to securely create an account and set up their payment preferences. To register, users need to provide a username, email, password, and preferred currency (GBP, USD, or EUR). Upon submission, the system assigns an initial balance based on the selected currency and securely stores the credentials using Django’s built-in authentication framework. The registration page features intuitive form validation to ensure users input valid details, preventing errors. Once registered, users can proceed to log in and access their personal dashboard, where they can initiate transactions and manage their account.


3. User Login 
The User Login page grants users’ access to their personalized dashboard, where they can manage transactions. To log in, users must enter their registered username and password, which are securely verified against the database. If the credentials match, users are redirected to their dashboard where they can view their balance, send or request payments, and track transaction history. In case of incorrect login details, the system provides error messages, guiding users to check their credentials. Authentication security measures, including password hashing, ensure user data remains protected.


4. Dashboard 
The User Dashboard is the central hub where registered users can view and manage their account details, transactions, and financial activities. Upon logging in, users are presented with an intuitive interface that displays their current balance, recent payments, and payment requests. The dashboard enables users to send direct payments, request money from other users, and review past transactions, ensuring complete control over their financial interactions. Additionally, key navigation buttons allow users to access the RESTful currency conversion service and securely manage their profile. Security measures are enforced, ensuring that users can only see their own data, maintaining privacy and protection. The dashboard layout is designed to be user-friendly, responsive, and easy to navigate, allowing seamless interaction with all payment functionalities.
At the bottom of the dashboard, users can access the notification tabs, which display important financial alerts. Notifications include received payment requests, unread transactions, and successful payments. Each notification is dynamically updated, ensuring users stay informed about their account activity. Users can mark notifications as read to streamline their dashboard view. This system ensures smooth communication and allows users to react promptly to financial interactions.


5. Direct Payments 
First section of the dashboard is a "Make Direct Payment", which feature allows users to send money instantly to other registered users. From the dashboard, users enter the recipient's email, and payment amount before confirming the transfer. The system verifies sufficient funds in the sender’s account and ensures the recipient exists before completing the transaction. If approved, the payment is processed within a single Django transaction, maintaining ACID compliance. Users receive an on-screen confirmation of the transaction and can track sent payments in their transaction history. Users can send the amount in the desired currency. In case the sent amount is in different currency for the sender or recipient account's currency, proper currency conversions will be carried out using the REST Currency conversion and deducted and added from the sender and recipients accounts respectively. 
The message notification for payment sent with the amount sent and deduction from sender's account will be shown on the top of the dashboard on clicking the "Send Payment' button, to confirm the payment has been sent. The details of the sent payment can then be seen in the notification area at the bottom of the dashboard, this detail can be seen any time later as well. These transactions will be shown in the notification panel at the bottom of the dashboard. for sender the details will be shown in "Sent Direct Payments" tabs and receiver will see the received amount in the "received direct payments" tab. 


6. Payment Requests
Second section of the dashboard is a "Create Payment Request" section which enables users to request funds from another registered user. Users input the recipient's email, requested amount, and currency type within the dashboard interface. The system generates a payment request notification for the recipient, allowing them to either accept or reject the request. If accepted, the amount is transferred from the requester’s account, updating both users’ transaction histories. This feature provides a seamless way for users to manage financial interactions while ensuring all requests are tracked within the system.
The message notification for payment requested will be shown on the top of the dashboard on clicking the "Requested Payment" button, to confirm the payment request has been sent. The details of the sent payment request can then be seen in the notification area at the bottom of the dashboard, this detail can be seen any time later as well. For user requesting the details of request will be shown in "Requested Payments" tabs along with its status either pending, approved or rejected and if the payment requested is accepted the amount received will be shown under "Received Payments from Request" tab. On the requestee's side details of the new request will be shown under the pending request tab with the option to either accept or reject the payment request. After when the requestee accepts the payment the details of the amount send will be shown under the tab "Sent Payments Form the Requests". In case of requestee rejects the payment, the user who initiated will be notified with the statis of payment rejected under the tab "Requested Payments".


7.  REST Conversion API
The RESTful API for currency conversion in this project provides a dynamic way to exchange amounts between different currencies—GBP, USD, and EUR—using predefined exchange rates. Implemented within the payapp module, this API operates as a Django-based endpoint that responds exclusively to GET requests. The core functionality is structured around the /conversion/{currency1}/{currency2}/{amount}/ URL format, where users specify the source currency, target currency, and amount for conversion. Upon receiving a request, the API retrieves the relevant exchange rate from a hardcoded dictionary and applies the appropriate calculation to return the converted amount. If either currency is unsupported, the service responds with an error message and an appropriate HTTP status code. This RESTful design ensures seamless integration with the payment processing system, allowing all financial transactions to reference real-time currency exchange values while maintaining simplicity and efficiency within the backend architecture. 


8. Apache Thrift Base Time Stamping
The Thrift-based timestamp service in this project is designed to provide precise transaction timestamps by interfacing with a lightweight remote service running on the same server. Implemented using Apache Thrift, this service listens on port 10000 and responds to requests for the current system date and time. When a transaction is initiated—whether a direct payment or an accepted payment request, the Django application sends a request to the Thrift service, which returns the exact timestamp at that moment. This ensures that all financial operations are accurately logged, maintaining a consistent timeline for transactions. Using Thrift makes the service efficient and scalable, allowing future extensions such as external logging or multi-server synchronization. By integrating this timestamp mechanism, the application guarantees data integrity, making it easier to track payments while enhancing security and auditability within the system.  


9. Admin Features 
The administrator functionalities in this payment system provide complete access to user accounts and transactions, ensuring secure management of financial activities. Admins have access to a dedicated admin dashboard, where they can view all user accounts, check balances, and track transactions in real-time. Unlike regular users, administrators can also register new superusers, maintaining oversight of the platform’s operations. Access to admin pages is strictly restricted, ensuring that only authorized personnel can make administrative modifications, where entering a simple user account restricted the entry by an error message “you are not an admin". Additionally, admins can see user account, their balances and all transactions. This structured implementation ensures that the payment system remains transparent, secure, and properly managed, giving admins full visibility and control over financial interactions within the platform. 
Admin login can be accessed from the top right corner button on the user login page. Same way user login page can be accessed from admin login page using the button at top right corner of the admin login box.                

10. Security Measures 
Security is a critical component of this web-based payment system, ensuring that user transactions remain protected, private, and tamper-proof. To achieve this, we implemented HTTPS encryption, securing all data exchanges between the client and server to prevent interception or unauthorized access. The authentication system ensures that only registered users can access their accounts, with role-based restrictions distinguishing regular users from administrators (as seen in Figure 10). Login credentials are securely stored using password hashing, preventing exposure of raw passwords. Additionally, Django’s built-in security mechanisms, such as Cross-Site Request Forgery (CSRF) protection, SQL injection prevention, and Clickjacking defense, safeguard the application against potential cyber threats. Access control measures ensure that non-admin users cannot view or modify sensitive administrative data, maintaining proper isolation between different account types. These security implementations collectively reinforce the integrity and reliability of the system, ensuring safe user interactions


11. Cloud Deployment 
The AWS EC2 deployment of this project ensures that the web-based payment system runs efficiently in a cloud-based environment, making it accessible beyond a local development setup. By hosting the Django application on Amazon EC2, we achieved scalability, reliability, and security, allowing users to interact with the platform seamlessly. Additionally, we secured communication using HTTPS to protect sensitive user transactions and credentials. This deployment structure ensures that the system can handle multiple concurrent users, offering a professional and production-ready setup. The inclusion of AWS cloud services in this project demonstrates a real-world approach to hosting a financial application, reinforcing security and availability while enabling potential future scaling.


13. Deployment Process
Created an AWS EC2 virtual machine running Ubuntu to host the Django application.
Configured necessary dependencies, including Python and Django, REST, Apache Thrift. etc.
Set up a virtual environment to manage dependencies.
Enabled SSL/TLS encryption to enforce secure communication.
Applied AWS security groups to allow only necessary ports (80, 443, and 22 for SSH).
Restricted unauthorized access to ensure secure transactions and user authentication
Made adjustments to setting.py/allowed hosts, and added the public server for deployment.
Started Thrift service to insure timestamping works on the web app.
Started the https server.
Screenshots provided below demonstrate: Deployment commands executed on the AWS EC2 console live application running on AWS with a visible URL, successful user interactions on the cloud-hosted platform. 
