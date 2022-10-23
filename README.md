# HackathonBbva2022 :rainbow: 
## Description and context
The main objective of the project is to recognize and mitigate the harm that can be caused to society when encountering biased content on the Internet that prevents inclusion in a more diverse world.

To achieve this goal, a tool would be developed for the end user that, by means of a light extension and without saturating the user, analyzes all the content available on any web page visited. This analysis would be supported by means of an artificial intelligence model which processes the natural language of the content and would provide an inference that would allow us to know if the content is biased or not.

This application will allow the user to quickly identify any bias that may be conveyed on websites, giving a more holistic view of the content itself and making the Internet a little safer to navigate. 

Despite being an extension, it has a front end development that provides a friendlier experience and removes the entry barrier to understand what the application does. It will also have an API that will be able to interact with other systems allowing its scalability. 

The extension that can be easily downloaded in the extensions marketplace is mainly developed in javascript for the front end and connects to the backend through an API made in FAST API using python that will perform a preprocessing of the texts and finally pass to the AI model deployed in Sagemaker (AWS) to determine if there is bias or not in it.

In the end the idea is to have a service that can be consumed by everyone. Therefore the development would be hosted in an ec2 instance and the model . This allows the EC2 instance not to be overloaded and the resources needed by the model to be managed automatically by the model. 

## Technologic Challenge 

EL objetivo es integrar diferentes herramientas desde el lado del frontend y del backend con el objetivo de prestar un servicio agil y funcional. El reto principal estuvo alrededor de la selección, entrenamiento y despliege del modelo que permitiría hacer inferenicias sobre los sesgos de género en los sitios web. No nos conformamos con solo realizar una revisión del texto, sino se desarrollo un almacenamiento en S3 de Amazon para almacenar todos los análisis que se hagan para que en un futuro se puedan lograr resultados cada vez más acertivos ya que el sesgo de género es un campo que aún tiene bastante por ser explorado. Toda esta información fue almacenada de forma tabular gracias a un proceso automatizado implementado en una lambda function permitiendo mantener la integridad y estructura de los datos.

Como objetivo final y con miras a ayudar a mejorar el campo de la investigación de la diversidad e inclusión se incluyó un dashboard que permite realizar diversos análisis de una forma más visual, así se hizo uso del servicio de QuickSight de Amazon.

The trained model 

## Diagram Flow 
![model](https://user-images.githubusercontent.com/65092255/197395103-973d0722-e9ee-4d80-bc94-49461aab9373.png)


## How To use
1. Go to chrome extensions marketplace and install **Bias Banner**
2. Surf the web safe as simple as that !

### In case you don't find the extension in the market place
### En caso de que no encuentres la extensión en el market place (los tiempos de google para revisión pueden tardar semanas)
1. Clone this repository
3. Go to extensions in your web browser (we have tested on brave and chrome) 
![image](https://user-images.githubusercontent.com/91997349/197349340-266c1602-f289-4f06-8045-a849c602c757.png)
3. Enable developer mode
![3](https://user-images.githubusercontent.com/65092255/197394829-36e2d87f-637e-43cd-bc63-cd697cc03c62.png)


4. Click on the button *Load unpacked* 
![4](https://user-images.githubusercontent.com/65092255/197394841-f0903dbb-f862-4152-acc2-5972fcf43fd1.png)

5. Upload **front end** folder

![1](https://user-images.githubusercontent.com/65092255/197394616-5de9f19d-8b6b-492b-bcb8-718cdb1f68f9.png)

6.Check that your extension is on.
![2](https://user-images.githubusercontent.com/65092255/197394696-66c1cb5c-2d89-4812-935d-271236b46b49.png)


7. Enjoy! you are now surfing the web safer. 

You know your extension is working when a small banner appeared at the left corner of your web browser window, and if there is any text with some bias it will be highlighted and it will have an small badge indicating the porbability to be a bias text.
