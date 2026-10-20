# Report Object

Reports are the middle-level objects housed under a client and contain report details. The Report object does not hold a list of findings, but each finding includes the ID of a report.

## Report Table

The following table explains the fields and data types stored for a report. Fields are presented in alphabetical order by object field name.

<table><thead><tr><th width="186">object field name</th><th width="221">description</th><th>data type</th></tr></thead><tbody><tr><td>name</td><td>name of affected assets</td><td>dict {str, {AFFECTED ASSET Object}</td></tr><tr><td>status</td><td>status of report</td><td>string ["Draft", "Ready For Review", "In Review", "Approved", "Published"]</td></tr><tr><td>includeEvidence </td><td>identifies if the report includes evidence</td><td>Boolean</td></tr><tr><td>report_id</td><td>the UUID of the report</td><td>integer</td></tr><tr><td>client_id</td><td>client that the report belongs to</td><td>integer</td></tr><tr><td>doc_type</td><td>field in database to identify object</td><td>"report": DB type identifier</td></tr><tr><td>reportType</td><td>type of report</td><td>"default"</td></tr><tr><td>tags</td><td>any tags associated with the report</td><td>string array</td></tr><tr><td>custom_field</td><td>custom field(s) added to a report</td><td>array[ { "label": str, "value": str } ]</td></tr><tr><td>custom_fields</td><td>container for fields used to track information about the report executive summary narratives; id (narrative UUID), label (title of narrative), tags (any tags applied to narrative), text (narrative content), isFromNarrativesDB (null/true value identifying if the content is from NarrativesDB).</td><td>array[ { "id": str, "label": str, "tags": array[str], "text": str, "isFromNarrativesDB": null or true</td></tr><tr><td>template</td><td>if the report did not use the default template, the custom report UUID is listed</td><td>string || null: UUID of report template</td></tr><tr><td>start_date</td><td>date report was started</td><td>null |  ISO 8601 format <code>2024-08-16T15:24:19.000Z</code></td></tr><tr><td>end_date</td><td>date report was closed</td><td>null |  ISO 8601 format <code>2024-08-16T15:24:19.000Z</code></td></tr><tr><td>fields_template</td><td>if the report did not use the default fields template, the custom fields template UUID is listed</td><td>string || null: UUID of fields/finding template</td></tr><tr><td>exec_summary</td><td>a container field that contains any custom fields created for the report</td><td>{ "custom_fields": array[ { "id": str: CUID of report narrative, "label": str, "tags": array[str], "text": str, } ] }</td></tr><tr><td>isTrackChanges</td><td>defines if the rich-text field track changes feature is turned on at the report level (a value of "true" means it is turned on, while a value of "false" means it is turned off and track changes is done per rich-text field)</td><td>null or true</td></tr></tbody></table>

## Report Structure

The report object stored in the database is a nested JSON object. Below is a screenshot and sample downloadable file that displays the structure of database objects.<br>

<div align="left"></div>

(downloadable sample file on the source page)
