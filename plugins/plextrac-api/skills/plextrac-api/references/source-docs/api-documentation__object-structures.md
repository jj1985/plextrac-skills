# Object Structures

PlexTrac data is categorized into clients, reports, findings, and assets, which are the primary containers holding information stored in Plextrac. The Clients module holds assets and reports, while reports hold findings.

While these objects exist as their type in the database, some fields about an object are stored both on the object and as values inside other objects. The most common example of this is affected assets and vulnerabilities.&#x20;

Here is a list of object structures that have been defined:

* [Client Object](/plextrac-documentation/api-documentation/object-structures/client-object.md)
* [Report Object](/plextrac-documentation/api-documentation/object-structures/report-object.md)
* [Finding Object](/plextrac-documentation/api-documentation/object-structures/finding-object.md)
* [Asset Object](/plextrac-documentation/api-documentation/object-structures/asset-object.md)
  * [Client Asset](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview/object-structures/asset-object#child-asset-structure)&#x20;
  * [Affected Asset (finding asset)](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview/object-structures/asset-object#affected-asset-structure)
* [Evidence Object](/plextrac-documentation/api-documentation/object-structures/evidence-object.md)

<div align="left"></div>
