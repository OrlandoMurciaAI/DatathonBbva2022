# DatathonBbva2022 :rainbow: 
## Description and context
The main objective of the project is to recognize and mitigate the harm that can be caused to society when encountering biased content on the Internet that prevents inclusion in a more diverse world.

To achieve this goal, a tool would be developed for the end user that, by means of a light extension and without saturating the user, analyzes all the content available on any web page visited. This analysis would be supported by means of an artificial intelligence model which processes the natural language of the content and would provide an inference that would allow us to know if the content is biased or not.

This application will allow the user to quickly identify any bias that may be conveyed on websites, giving a more holistic view of the content itself and making the Internet a little safer to navigate. 

Despite being an extension, it has a front end development that provides a friendlier experience and removes the entry barrier to understand what the application does. It will also have an API that will be able to interact with other systems allowing its scalability. 

The extension that can be easily downloaded in the extensions marketplace is mainly developed in javascript for the front end and connects to the backend through an API made in FAST API using python that will perform a preprocessing of the texts and finally pass to the AI model deployed in Sagemaker (AWS) to determine if there is bias or not in it.

In the end the idea is to have a service that can be consumed by everyone. Therefore the development would be hosted in an ec2 instance and the model would be consumed by a sage maker api. This allows the EC2 instance not to be overloaded and the resources needed by the model to be managed automatically by the model. 

## Technologic Challenge 

The objective is to use the SageMaker service for the deployment of the Machine Learning model, where the bias is processed and determined, being this the ideal tool for such purposes. In addition, this service will provide us with an endpoint which will allow us to consume the model quickly without worrying about the resources and loads that may occur in its use.  Additionally, an API service will be deployed in an EC2 instance where the information will be preprocessed to be sent to the model. 

## Diagram Flow 
![Infraestructure drawio](https://user-images.githubusercontent.com/91997349/197352850-d0f3c0b6-0c88-48f3-84fb-6592575afa71.png)


## How To use
1. Go to chrome extensions marketplace and install **Bias Banner**
2. Surf the web safe as simple as that !

### In case you don't find the extension in the market place
1. Clone this repository
2. Go to extensions in your web browser (we have tested on brave and chrome) 
![image](https://user-images.githubusercontent.com/91997349/197349340-266c1602-f289-4f06-8045-a849c602c757.png)
3. Enable developer mode
4. Click on the button *Load unpacked* 
5. Upload **front end** folder
6 Enjoy! you are now surfing the web safer. 

You know your extension is working when a small banner appeared at the left corner of your web browser window.
