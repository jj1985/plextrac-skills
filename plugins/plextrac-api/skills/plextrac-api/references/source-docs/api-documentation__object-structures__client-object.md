# Client Object

Client objects contain the client's details and are one of the highest-level objects in the database, as all other objects are within the context of a specific client.

The client object does not hold a list of assets or reports; instead, each asset and report contains the ID of a client.

Clients hold a list of client assets representing a physical asset or web application. This list is dynamically populated as files with assets imported via a scan or manually added within PlexTrac.

<div align="left"></div>

## Client Table

The following table explains the fields and data types stored for a client. Fields are presented in alphabetical order by object field name.

> **info:**
The `name` field is the only required field when creating a client.

<table><thead><tr><th width="186">object field name</th><th width="221">description</th><th>data type</th></tr></thead><tbody><tr><td>client_id</td><td>UUID of client</td><td>integer</td></tr><tr><td>classificationId</td><td>CUID of the Classification Level for an authorized user for each client</td><td>string or null</td></tr><tr><td>custom_field</td><td>custom fields related to client</td><td>array[ { "label": str, "value": str } ]</td></tr><tr><td>custom_field/label</td><td>label of the custom field</td><td>string</td></tr><tr><td>custom_field/value</td><td>plain text value of the custom field</td><td>string</td></tr><tr><td>description</td><td>description of client</td><td>string</td></tr><tr><td>doc_type</td><td>field in database to identify object </td><td>"client": DB type identifier</td></tr><tr><td>name</td><td>name of Client</td><td>string</td></tr><tr><td>poc</td><td>point of contact for client</td><td>string</td></tr><tr><td>poc_email</td><td>email address of point of contact</td><td>string</td></tr><tr><td>role</td><td>type of role of user associated with a client; will be one of three values to represent roles of Administrator, Standard User, and Analyst</td><td>string containing one of the following values: ["ADMIN", "STD_USER", "ANALYST"] </td></tr><tr><td>tenant_id</td><td>UUID of tenant</td><td>integer</td></tr><tr><td>users</td><td>list of users and roles within a client</td><td>dict { str: user email: Dict{ "classificationId": str || null: CUID, "role": str: ["ADMIN", "STD_USER", "ANALYST"] } }</td></tr><tr><td>tags</td><td>any tags associated with a client</td><td>string array</td></tr></tbody></table>

## Client Structure

The client object stored in the database is a nested JSON object. Below is a screenshot and sample downloadable file that displays the structure of database objects.

<div align="left"></div>

(downloadable sample file on the source page)
