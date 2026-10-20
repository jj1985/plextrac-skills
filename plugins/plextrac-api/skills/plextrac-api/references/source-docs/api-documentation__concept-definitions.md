# Concept Definitions

## PlexTrac Application

PlexTrac is an application that helps users collect, transform, display, and analyze vulnerability data. It consists of two parts: the **backend**, which stores and manages the data, and the **frontend** (the PlexTrac platform), which allows the user to view and interact with it.&#x20;

The API is the connecting link between the two parts. It's a set of instructions that informs the backend to create, delete, update, or return data to the user.

The frontend sends requests to the backend to store or modify data and queries it to display the required information to the user. The backend executes these requests and returns the necessary data.&#x20;

Each customer instance of PlexTrac is an independent app with a frontend, backend, and API.

<div align="left"></div>

## Self-Consumed API

Developers can benefit from using a web app that self-consumes its API, allowing it to utilize its API resources. This ensures the API is tested and reliable as the app uses it. PlexTrac is an example of a web app that self-consumes its API, enabling UI interactions to be treated as API requests directly sent to the server.

This allows external applications to integrate with PlexTrac and will enable users to manage data with custom scripts. All functionality within the platform is accessible through the API, making it a reliable and efficient way for developers to access data or services that would typically require manual processes or multiple UI interactions.

## Driving Action

To use the backend database, a user must initiate an action by sending requests. This is made possible through the PlexTrac platform, which serves as the frontend interface for sending API requests. By interacting with the UI components, users can become the driving force behind the requests sent to the backend by simply clicking a button on the Plextrac platform.

When interacting with the backend, one can send API requests through various means, including the PlexTrac platform, command line, Postman API Platform, custom scripts, or a personalized frontend. Regardless of the chosen method, the process involves the user initiating a driving action, such as:

* entering the request on the command line
* creating and sending a Postman request
* executing a script

The extent of what can be achieved with the API depends on the resources involved, whether a simple command-line request or a custom frontend that replaces the PlexTrac platform.

## API vs. PlexTrac Platform

Some key factors should be considered when deciding whether to use the API or the platform. One of the main advantages of using the platform is its simplicity. The API may not be needed if a task can be completed with just one click.

The API is a superior option for interacting with and managing data. It offers developers a dependable and effective way to access data or services that would otherwise require manual procedures or numerous user interface interactions.&#x20;

In addition, using APIs instead of the platform is beneficial because scripts allow for automation. Scripts can perform multiple interactions simultaneously, enabling bulk operations and saving time.

<div align="left"></div>
