<!-- Output copied to clipboard! -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 3.595 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Mon Jul 27 2020 03:56:55 GMT-0700 (PDT)
* Source doc: TelMe Documentation
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->

# TelMe**!**

The one stop web-app to tell you all about mobile subscription plans in Singapore. 

You may watch our [video](https://drive.google.com/file/d/180Lz7tcdt-3iqGldtkPNnSD71KLTyv_k/view?usp=sharing) presentation or visit the live [website](https://tel-me.herokuapp.com/home).

**Proposed level of achievement: Artemis**

**Motivation **

It’s that time of the year again, your Telco subscription is up for renewal and you’re faced with a tough decision, to recontract or to change Telco? A quick google search for the best mobile recontract promotions ends up being a 1 hour search for the best deal possible. You finally decide to recontract with Singtel, but to your dismay, after going through all that hassle, you find out that M1 was offering way more mobile data capacity for lower prices. 

 

In this day and age, information is key. However, in a bid to attract more customers, companies flood and overwhelm the market with ambiguous and irrelevant advertisements. This discourages many to do more research and choose the easiest but less worth it option. 

The issue of how fast information can be acquired also comes into play. Sifting through multiple websites is extremely time consuming and users cannot look up promotions they did not even know exists. Hence, a single place where users can view and sort through all kinds of Telco subscription plans and promotions is needed.

 

**Aim **

We hope to be able to provide users with a single place where one can view and compare all the different types of Telco subscription plans and promotions. Here, they will be able to find the best available Telco subscription plan, tailor made, according to what they are looking for. 

**Features of our web-app**


<table>
  <tr>
   <td>No.
   </td>
   <td>Feature
   </td>
   <td>Function
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>Web Scraper
   </td>
   <td>To populate the database with products extracted from each individual telco site. 
   </td>
  </tr>
  <tr>
   <td>1.1
   </td>
   <td>Starhub Scraper
   </td>
   <td>Scrapes data from Starhub's web page.
   </td>
  </tr>
  <tr>
   <td>1.2
   </td>
   <td>Singtel Scraper
   </td>
   <td>Scrapes data from Singtel’s web page.
   </td>
  </tr>
  <tr>
   <td>1.3
   </td>
   <td>M1 Scraper
   </td>
   <td>Scrapes data from M1’s web page.
   </td>
  </tr>
  <tr>
   <td>1.4
   </td>
   <td>My Republic Scraper
   </td>
   <td>Scrapes data from My Republic’s web page.
   </td>
  </tr>
  <tr>
   <td>1.5
   </td>
   <td>giga! Scraper
   </td>
   <td>Scrapes data from giga!’s web page.
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>Web Application
   </td>
   <td>Provides an interface for users to view Telco information in a clean and concise manner.
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>Home Page
   </td>
   <td>Welcomes users and shows them popular telco subscription plans.
   </td>
  </tr>
  <tr>
   <td>3.1
   </td>
   <td>Featured
   </td>
   <td>Users will be able to see what popular promotions are available. As of the end of Orbital, the features items are hard-coded in. Given time, this feature could be done through scraping.
   </td>
  </tr>
  <tr>
   <td>3.2
   </td>
   <td>Trending topics
   </td>
   <td>Users will be able to view articles related to telco discussion and reviews that users have posted on our website. As of the end of Orbital, the features items are hard-coded in. Given time, this feature could be done through scraping.
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>Products Page
   </td>
   <td>Lists down all the plans and gives users a brief overview of all the plans in our database. Filter is found here (Refer to 1.3)
   </td>
  </tr>
  <tr>
   <td>4.1
   </td>
   <td>Add to favorites button
   </td>
   <td>A button where customers can add a product to their favorite products.
   </td>
  </tr>
  <tr>
   <td>4.2
   </td>
   <td>Filter
   </td>
   <td>Users have the option of choosing and filtering to zoom in on subscription plans according to their interests.
   </td>
  </tr>
  <tr>
   <td>4.2.1
   </td>
   <td>Price Range
   </td>
   <td>Users will be able to search for plans within a price range
   </td>
  </tr>
  <tr>
   <td>4.2.2
   </td>
   <td>Data Range
   </td>
   <td>Users will be able to search for plan within a data range
   </td>
  </tr>
  <tr>
   <td>4.2.3
   </td>
   <td>Contract Length Range
   </td>
   <td>Users will be able to search for plans with a specific contract length (e.g 1 year, 2 years, no contract, etc.)
   </td>
  </tr>
  <tr>
   <td>4.3
   </td>
   <td>Submitted Filters
   </td>
   <td>Users will be able to see which filters they have submitted in one place.
   </td>
  </tr>
  <tr>
   <td>4.3.1
   </td>
   <td>Remove
   </td>
   <td>Users can remove each applied filter either individually or stop filtering altogether. 
   </td>
  </tr>
  <tr>
   <td>4.4
   </td>
   <td>Ordering
   </td>
   <td>Users can choose between the available methods ordering how the products are displayed. They can be ordered in four different ways as of now newest, cheapest, most data, shortest contract.
   </td>
  </tr>
  <tr>
   <td>4.5
   </td>
   <td>Search bar
   </td>
   <td>Users can search for any product from any page in the website.
   </td>
  </tr>
  <tr>
   <td>4.5.1
   </td>
   <td>Search in results
   </td>
   <td>Users can search for any product on the products page after filtering or ordering.
   </td>
  </tr>
  <tr>
   <td>4.6
   </td>
   <td>More details button (Product details page)
   </td>
   <td>The information provided on the product page will only touch briefly on the information of the plans. To see more details, users can click on a dropdown button on the product card to see more details.
   </td>
  </tr>
  <tr>
   <td>4.7
   </td>
   <td>Visit Site button
   </td>
   <td>This button links back to the telco website so the user can purchase it. 
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>Admin Page
   </td>
   <td>Admins will be able to visit the admin page to make changes to the website i.e modify and delete data, users and reviews.
   </td>
  </tr>
  <tr>
   <td>5.1
   </td>
   <td>Modify/Add user data
   </td>
   <td>Admins will be able to remove, edit, and add users and super users. 
   </td>
  </tr>
  <tr>
   <td>5.2
   </td>
   <td>Modify/add product data
   </td>
   <td>Admins will be able to remove, edit and add new products into the existing listing. 
   </td>
  </tr>
  <tr>
   <td>5.3
   </td>
   <td>Modify/add review and comment data
   </td>
   <td>Admins will be able to monitor the reviews and comments section, remove and flag out comments that do not adhere to the site’s code of conduct. 
   </td>
  </tr>
  <tr>
   <td>5.4
   </td>
   <td>Import/Export Data
   </td>
   <td>Through a django package, admins will be able to download any data on the site into many different file types with .csv and excel being one of them.
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>Users
   </td>
   <td>Users will be able to sign in on our web page. With an account users will be able to leave comments and reviews. This will be implemented in milestone 2.
   </td>
  </tr>
  <tr>
   <td>6.1
   </td>
   <td>Sign Up Page
   </td>
   <td>Users will be able to sign up on our web page. A prompt will be given to sign up if a user tries to make a review or comment without an account. After signing up, the user is brought back to the page he came from. This will be implemented in milestone 2.
   </td>
  </tr>
  <tr>
   <td>6.2
   </td>
   <td>Sign In Page
   </td>
   <td>Similar to sign up, users will be prompted when trying to leave a review. After signing up, users will be brought back to the page they were trying to leave a review on.
   </td>
  </tr>
  <tr>
   <td>6.3
   </td>
   <td>Forgot password reset
   </td>
   <td>In the case of a lost password, users will be able to enter their email to get a password reset email.
   </td>
  </tr>
  <tr>
   <td>6.4
   </td>
   <td>User profile page
   </td>
   <td>Users will be able to update their account details here. Their email, password and profile picture can be changed. A list of all the user liked plans can be found here.
   </td>
  </tr>
  <tr>
   <td>6.4.1
   </td>
   <td>Personal Info
   </td>
   <td>Users will be able to view their personal info here. This consists of their Displayed name and their email.
   </td>
  </tr>
  <tr>
   <td>6.4.2
   </td>
   <td>Change Password
   </td>
   <td>Users will be able to change their password should they find the need to do so.
   </td>
  </tr>
  <tr>
   <td>6.4.3
   </td>
   <td>Logout
   </td>
   <td>Users can logout from this page.
   </td>
  </tr>
  <tr>
   <td>6.5
   </td>
   <td>Favorite Products page
   </td>
   <td>This is where the User is able to view the products he has favourited. 
   </td>
  </tr>
  <tr>
   <td>6.6
   </td>
   <td>Recommended Products page
   </td>
   <td>Users will be recommended similar products using machine learning models based on the user's browsing behaviour and displayed on the profile page as well.
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>Track
   </td>
   <td>Users can choose to be notified via email, once there is a new plan or a plan that they may be interested in.
   </td>
  </tr>
  <tr>
   <td>7.1
   </td>
   <td>Email
   </td>
   <td>Given an email, a user can be added to our mailing list and be informed via email if there is a new plan or a price drop. This will be implemented in milestone 3
   </td>
  </tr>
</table>


**User Stories **

Priorities: High (must have) - `***`,  Medium (nice to have) - `**`,  Low (unlikely to have) - `*`


<table>
  <tr>
   <td>Priority
   </td>
   <td>As a...
   </td>
   <td>I want to...
   </td>
   <td>So that I can...
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>Customer looking to recontract my Telco subscription plan
   </td>
   <td>Be able to know and compare the existing promotions in the market
   </td>
   <td>Make a well-informed decision before purchase.
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>User
   </td>
   <td>Save my preferences and receive tailored recommendations
   </td>
   <td>Make better judgement and ease the process of selecting a new plan
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>User
   </td>
   <td>Be able to focus and zoom in on only products/subscription plans I am interested in
   </td>
   <td>Save precious time.
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>User
   </td>
   <td>Select specific deals and be notified when a promotion for that deal comes out.
   </td>
   <td>Save the hassle of coming back to the website for updates on the specific deal.
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>Admin
   </td>
   <td>Be able to modify product listings on my site.
   </td>
   <td>Identify false/fake promotions and remove them from the website. 
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>Admin
   </td>
   <td>Be able to moderate user accounts on my site.
   </td>
   <td>Identify and flag out users who violate code of conduct, and remove them.
   </td>
  </tr>
  <tr>
   <td>***
   </td>
   <td>Admin
   </td>
   <td>Be able to populate my database automatically
   </td>
   <td>Save time and receive information in the shortest time possible.
   </td>
  </tr>
  <tr>
   <td>**
   </td>
   <td>User
   </td>
   <td>Be able to view new plans at a glance.
   </td>
   <td>Avoid scrolling through old plans to try to find the new ones.
   </td>
  </tr>
</table>




**1. Recommend feature**







    First we get a list of plans favorited by the requester user.



1. Then we obtain the name of the cluster the user belongs to. We do this through the `User.objects.get(..).cluster_set` field that references the user side of the many-to-many relationship we have with clusters. We also exclude the requester user from that list. This is not strictly needed because of what we are going to do next, but might reduce query time.
2. Then we use the previous list of names to get favorites for those users in the cluster, excluding those favorites referring to the plans we got in step 1. From the result, we get a list of plan IDs.
3. Finally, we use the previous list of IDs to retrieve all the recommended plans.

    **Clustering**


    We used K-means clustering as a machine learning model that made use of user similarity in order to provide better plan recommendations. When a user saves a particular plan into his favorites list, the backend triggers the machine learning model and allocates him to a cluster with users of similar profiles. The backend will then suggest favorited plans of these similar users to the current user. As such, our model will perform better with more user activity.


    We chose K-means clustering because It is a fast clustering algorithm that has parallel and scalable implementations (e.g. see [Spark](http://spark.apache.org/docs/latest/mllib-clustering.html)). And overall, it is very easy to understand what K-means does and how it works. A user cluster is just a group of users close to each other based on how they favorited plans. 


**2. Web Extraction**

    First, the admin must run the command `heroku run python scrape.py`



1. Then, the scrapers are called using their respective function calls (e.g `add_starhub_products()`, etc)
2. Scraping is done through the use of both bs4 and Selenium packages. Upon having their function called, the scraper will crawl through the website, extract data and store it in a dictionary.
3. Upon completion of all the scrapers, all of the data scraped is pipelined into `add_products.py` where we can add all the products and run validators on them.
4. A filter is run on the existing models in the database. If a product with the same title already exists, the product is not added. Otherwise, `Product.objects.create()` is used to make the model object and `product.save()` is used to save the object in the database.
5. Axios is then used to fetch the products from our API and these products are mapped to our product template in React to display all the items on the webpage.

    As of milestone 3, data was scraped from the websites of Starhub, M1, giga! and My Republic. Data from Singtel was scrapped as well but due issues related to hosting and the packages we used to scrape from Singtel’s website, we are unable to run Singtel’s scraper on the server. Hence, we had to scrape Singtel’s data locally, export it, then import it into the online website’s database. 







**Deployment to Production** \
To deploy our web application, we chose to deploy with Heroku because it provides an ecosystem of cloud services, which can be used to instantly extend our application with fully-managed services. 



1. **Server**

    Integration with Heroku requires a Procfile file which is used to explicitly declare our application’s process types and entry points. It is located in the root of our repository. This Procfile requires Gunicorn, the production web server.


 \
	`web: gunicorn myproject.wsgi`



2. **Database**

    For our local database, the web application uses SQLite, but because Heroku provides its applications with a Postgresql database, a seperate database connection unique to production was created in `settings.py`


    ```
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)

    ```


**Testing**


<table>
  <tr>
   <td>
   </td>
   <td>Problem
   </td>
   <td>Solution
   </td>
  </tr>
  <tr>
   <td rowspan="3" >Frontend
   </td>
   <td><strong>Range for filter includes either “Unlimited” or “No Contract”</strong>
   </td>
   <td>When scraping, upon encountering unlimited, it is registered as “999” while No Contract is registered as “0”. Conditionals are then used in the frontend code to display “Unlimited” upon encountering “999” and “No contract” on “0” This way, the filter can work without any issues.
   </td>
  </tr>
  <tr>
   <td><strong>No recommended or favorite products</strong>
   </td>
   <td>Query database for any recommended or favorited products. If none, show a string stating that there are no products.
   </td>
  </tr>
  <tr>
   <td><strong>Search function cancels out filters</strong>
   </td>
   <td>Implement search in results
   </td>
  </tr>
  <tr>
   <td rowspan="3" >Backend
   </td>
   <td><strong>Account Registration</strong>
   </td>
   <td><strong>Email</strong>: \
The application uses an email Regex Validator to check if email keyed in by the user is valid. 
<p>
<strong>Password:</strong>
<p>
The application checks if the user has keyed in a password of at least 8 characters.
<p>
<strong>New Passwords: </strong>
<p>
The application returns “Wrong Password” if the user has entered an old password wrongly. 
   </td>
  </tr>
  <tr>
   <td><strong>Machine Learning & Clustering</strong>
   </td>
   <td>A test was carried out in the project video. 
   </td>
  </tr>
  <tr>
   <td><strong>Web-scraper</strong>
   </td>
   <td>When scraping and creating models, if a plan exists, change price of existing model if price dropped, else, do nothing.
<p>
If a field is missing, a default value is used.
   </td>
  </tr>
</table>


**Some Notable Libraries Used**


<table>
  <tr>
   <td><strong>Language</strong>
   </td>
   <td><strong>Library</strong>
   </td>
   <td><strong>Use</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="5" >Python
   </td>
   <td>django
   </td>
   <td>Provides a functional backend for the project
   </td>
  </tr>
  <tr>
   <td>djangorestframework
   </td>
   <td>Creates the link between the django-backend and the react-frontend through the creation of a django rest API
   </td>
  </tr>
  <tr>
   <td>Beautiful Soup 4 / Selenium
   </td>
   <td>Aids in the extraction of data from websites to populate the project database
   </td>
  </tr>
  <tr>
   <td>scikit-learn
   </td>
   <td>Provides K-means clustering for machine learning. 
   </td>
  </tr>
  <tr>
   <td>scipy
   </td>
   <td>Helps us easily build sparse matrices for data handling.  
   </td>
  </tr>
  <tr>
   <td rowspan="5" >Node
   </td>
   <td>react
   </td>
   <td>Provides a functional frontend for the project
   </td>
  </tr>
  <tr>
   <td>react-router-dom
   </td>
   <td>Enables the linking of multiple pages in react
   </td>
  </tr>
  <tr>
   <td>redux
   </td>
   <td>Provides the linking between django api endpoints and data queries to react frontend. 
   </td>
  </tr>
  <tr>
   <td>webpack
   </td>
   <td>Aids in the deployment of the website
   </td>
  </tr>
  <tr>
   <td>material-ui
   </td>
   <td>Provides the resources to style the website
   </td>
  </tr>
</table>


**Timeline**


<table>
  <tr>
   <td>Milestone I
   </td>
   <td>Milestone II
   </td>
   <td>Milestone III
   </td>
  </tr>
  <tr>
   <td>1. Create and format website
<p>
2. Display Telco plans from different Telcos.
<p>
3. Allow users to sort/filter information based on what they want (e.g more mobile data, handset model, etc.)
<p>
4. Allow users to like deals. 
   </td>
   <td>1. Create Sign-up and Log-in features
<p>
2. Implement Favorite Plans list. 
<p>
3. Implement a Recommendation system using machine learning algorithms.
<p>
4. Populate the database with actual promotions that have been web-scraped.
   </td>
   <td>1. Implement Tracking system.
<p>
Allow users to be notified about price reduction in deals that they have previously indicated “Notify Me!”
<p>
2. Host website on Heroku.
   </td>
  </tr>
</table>

