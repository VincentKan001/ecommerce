LIVE DEMO LINK
==============
https://project3-hr.herokuapp.com/


BACKGROUND:
==========
* This app is meant for users to purchase fight gear online via ecommerce 

* CRUD is done on the admin side as this is a ecommerce website. Therefore the site administrator has to Create/Update/Delete products accordingly.

* Django allow for ease of CRUD on the admin backend and hence its very suitable for ecommerce.
 
* Users are allowed to view the catalog after registering for an account.

* Users will then get to choose their desired product which will then be loaded onto their shopping cart and thereafter they will decide if they want to check out.

* Different users will get to see different products in their shopping cart according to which products they have indicated interests on. 

* Users will then pay for their items via credit card and stripe will be the one administering the payments.

* inventory will then be updated to reflect the current status/quantity of a particular goods. 



UX DESIGN:
==========
* The data is presented in a card format which allows users to see clearly at a glance the products which are currently available.  

* The card shows the picture of the items, quantity which the user wish to purchase, and the selling price of the items. 

* upon selecting the desired product, users will then click proceed to check out to be redirected to their shopping cart.

* in shopping cart, they will get to review their items and decide if they want to purchase or remove it from cart. 

* in the event when customers made a successful purchase, the status and quantity of the items will be updated in real time. 

* site owners can also log in to stripe to see the amount of money being charged to the customers card. 

* users can sign up easily for an account using the register function. 

* images are uploaded using uploadcare of ease of deployment.  

USER STORIES:
============
My considerations while designing the app
* For ecommerce, users would like to see the products displayed at a glance
* How does the shop owner keep track of inventory  
* What if the customer accidentally added a wrong item to his cart.
* is the payment function safe and secure 
* ecommerce usually have many products hence would the database be enough shd the shop wishes to expand/bring in more items. 
* how to scale this app for future expansion. 



FEATURES 
========
* This project makes use of django which allows me to create different apps for different purposes 
* uploadcare was used for the loading of the product images 
* end to end ecommerce process was the main consideration while doing this assignment. 
* stripe was used for the payment system. 
* Website is design using mobile-first approach.



TECHNOLOGIES 
=============
The following languages, frameworks, libraries, and tools were used to construct this project. 
* HTML
* CSS
* Bootstrap (https://getbootstrap.com/) : This project uses Bootstrap to simplify the development of the webpage
* Python 3 
* Django
* Sqlite3
* Heroku
* uploadcare
* stripe 



TESTING
=======
* Testing was done across multiple viewports sizes to ensure responsiveness. 

* Manual testing was constantly conducted to ensure successful deployment across the different platforms.

 

DEPLOYMENT
==========
* This site is hosted using heroku.


Credit
======
The picture taken from pexels.com
