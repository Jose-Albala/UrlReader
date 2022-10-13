# UrlReader

Photoslurp imports catalogs from our clients in order to allow them to link
each photo with the products contained in the imported catalog that appears
in that photo. The client, when sets up their catalog in our platform, provides
us with an URL to import their catalog from.
The catalogs can be provided in three different formats : 

CSV, using pipes ( | ) as separators.
TSV, in the end is a csv file using tabs ( \t ) as separators.
XML, using Google Shopping Feed format, an extension of RSS
The fields included in those files would not be something relevant to this test.
It's possible to read the corresponding documentation page for informative
purposes.


Proposed Solutions.

We will use flask forms to validate the URL.

Then will use csv libraries (Sniffer) to check the content if it is CSV  or TSV.

Then will use BeautifulSoup to check XML code to confirm the xml format.

Requirements : 
1. We need to pull the docker image by using -docker pull josealbala17/docker-test:latest- in our terminal.
1. We run the Image in Docker Desktop to create a container and run the container.
2. Container will install requirements.txt and run the program.
3. Go to "localhost/create/" and complete the form.

