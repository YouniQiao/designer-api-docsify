# @ohos.pasteboard

This module provides the capabilities of managing the system pasteboard to support the copy and paste functions. You can use the APIs of this module to operate pasteboard content of the plain text, HTML, URI, Want, PixelMap, and other types.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace pasteboard--><!--Device-unnamed-declare namespace pasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'pasteboard';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createData) | Creates a **PasteData** object of the specified type. |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createData) | Creates a **PasteData** object that contains multiple types of data. |
| [createHtmlData](arkts-basicservices-pasteboard-createhtmldata-f.md#createHtmlData) | Creates a **PasteData** object of the HTML type. |
| [createHtmlTextRecord](arkts-basicservices-pasteboard-createhtmltextrecord-f.md#createHtmlTextRecord) | Creates a **PasteDataRecord** object of the HTML text type. |
| [createPlainTextData](arkts-basicservices-pasteboard-createplaintextdata-f.md#createPlainTextData) | Creates a **PasteData** object of the plain text type. |
| [createPlainTextRecord](arkts-basicservices-pasteboard-createplaintextrecord-f.md#createPlainTextRecord) | Creates a **PasteDataRecord** object of the plain text type. |
| [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createRecord) | Creates a **PasteDataRecord** object of the specified type. |
| [createUriData](arkts-basicservices-pasteboard-createuridata-f.md#createUriData) | Creates a **PasteData** object of the URI type. |
| [createUriRecord](arkts-basicservices-pasteboard-createurirecord-f.md#createUriRecord) | Creates a **PasteDataRecord** object of the URI type. |
| [createWantData](arkts-basicservices-pasteboard-createwantdata-f.md#createWantData) | Creates a **PasteData** object of the Want type. |
| [createWantRecord](arkts-basicservices-pasteboard-createwantrecord-f.md#createWantRecord) | Creates a **PasteDataRecord** object of the Want type. |
| [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getSystemPasteboard) | Obtains **SystemPasteboard** object. |

### Classes

| Name | Description |
| --- | --- |
| [ProgressSignal](arkts-basicservices-pasteboard-progresssignal-c.md) | Defines a function for canceling the paste task. This parameter is valid only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md#ProgressIndicator) is set to **NONE**. |

### Interfaces

| Name | Description |
| --- | --- |
| [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | Defines parameters when an application obtains the Data from the pasteboard, including the destination path, file conflict options, and progress indicator types. |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Implements a **PasteData** object. PasteData contains one or more data records ( [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md#PasteDataRecord)) and property description objects ( [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md#PasteDataProperty)). Before calling any API in **PasteData**, you must use ** [createData()](arkts-basicservices-pasteboard-createdata-f.md#createData)** or ** [getData()](arkts-basicservices-pasteboard-systempasteboard-i.md#getData)** to create a **PasteData** object. |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Defines the properties of PasteData in the pasteboard, including the timestamp, data types, pasteable range, and additional data. The defined properties can be applied to the pasteboard only with the [setProperty](arkts-basicservices-pasteboard-pastedata-i.md#setProperty) method. |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content in the pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records. After creating a PasteDataRecord, it is not supported to modify the value of the default data type of the PasteDataRecord. The correct value for the default data type should be specified when creating the PasteDataRecord. If you need to refresh the attribute value of the PasteDataRecord, please use [addEntry](arkts-basicservices-pasteboard-pastedatarecord-i.md#addEntry). |
| [ProgressInfo](arkts-basicservices-pasteboard-progressinfo-i.md) | Defines the progress information. This information is reported only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md#ProgressIndicator) is set to **NONE**. |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) | Provides **SystemPasteboard** APIs. Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getSystemPasteboard). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i-sys.md) | Provides **SystemPasteboard** APIs. Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getSystemPasteboard). |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [FileConflictOptions](arkts-basicservices-pasteboard-fileconflictoptions-e.md) | Enumerates options for file copy conflicts. |
| [Pattern](arkts-basicservices-pasteboard-pattern-e.md) | Describes the patterns supported by the pasteboard. |
| [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) | Enumerates options for the progress indicator. You can choose whether to use the default progress indicator. |
| [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Enumerates the pasteable ranges of PasteData. |

### Types

| Name | Description |
| --- | --- |
| [ProgressListener](arkts-basicservices-pasteboard-progresslistener-t.md) | Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API to obtain the paste progress. |
| [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Callback to be invoked when the pasteboard content changes. |
| [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Indicates type of value. |

### Constants

| Name | Description |
| --- | --- |
| [MAX_RECORD_NUM](arkts-basicservices-pasteboard-con.md#MAX_RECORD_NUM) | Maximum number of records in a **PasteData** object. In versions earlier than API version 10, the value is 512, indicating that no more records can be added once the number of records reaches 512. Since API version 10, no limit is placed on the number of records in a **PasteData** object. Unit: Numbers, the value must be an integer within [512, 512]. |
| [MIMETYPE_PIXELMAP](arkts-basicservices-pasteboard-con.md#MIMETYPE_PIXELMAP) | MIME type of the PixelMap content. The value is 'pixelMap'. |
| [MIMETYPE_TEXT_HTML](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_HTML) | MIME type of the HTML content. The value is 'text/html'. |
| [MIMETYPE_TEXT_PLAIN](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_PLAIN) | MIME type of the plain text content. The value is 'text/plain'. |
| [MIMETYPE_TEXT_URI](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_URI) | MIME type of the URI content. The value is 'text/uri'. |
| [MIMETYPE_TEXT_WANT](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_WANT) | MIME type of the Want content. The value is 'text/want'. |

