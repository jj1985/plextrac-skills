# Retrieving Parameter IDs

Parameters are essential components that can be included with an endpoint to modify the behavior and response obtained from the PlexTrac API. These parameters serve as options, allowing users to customize their requests, retrieve specific information, or perform specific actions.&#x20;

The following is a compilation of commonly used parameters in various PlexTrac API endpoints, accompanied by an explanation of locating the corresponding values within the platform to fulfill each request's specific requirements.

## Tenant IDs

The `tenantId` is returned when an authentication API is requested, as shown here:&#x20;

<div align="left"></div>

## Client IDs

The `clientId` can be retrieved from the platform by going to the **Clients** module, clicking the desired client, and looking at the numerical value in the URL between "clients" and "reports" in the URL path.

<div align="left"></div>

## Finding IDs

The `findingId` can be retrieved from the platform by going to a client or report, clicking the **Findings** tab, clicking the desired finding, and looking at the **Finding ID** field.

<div align="left"></div>

## Report IDs

The `reportId` can be retrieved from the platform by going to the **Reports** module, clicking the desired report, and looking at the numerical value at the end of the URL.

<div align="left"></div>

## Repository IDs

The `repositoryId` for DBs can be retrieved from the platform by going to the desired module under the **Content Library**, clicking the appropriate repository card, and looking at the value at the end of the URL.

<div align="left"></div>

## Role IDs

The `roleId` for default roles are:

* **ADMIN:** cljhc9ggj000008l99gkyai90
* **STD\_USER:** cljhc9rvn000208l9g4lpai54
* **ANALYST:** cljhc9yh1000308l9ar7j8mux

The `roleId` for custom roles can be identified by looking at the URL of the role within the platform.&#x20;

<mark style="background-color:yellow;">Step 1:</mark> Click **Account Admin** under the user name pulldown menu.

<div align="left"></div>

<mark style="background-color:yellow;">Step 2:</mark> Click **Security** under "Security & User Management."

<div align="left"></div>

<mark style="background-color:yellow;">Step 3:</mark> Click **Role Based Access**.

<div align="left"></div>

<mark style="background-color:yellow;">Step 4:</mark> Click the box of the custom role.

<div align="left"></div>

The `roleId` is the value at the end of the URL.

<div align="left"></div>
