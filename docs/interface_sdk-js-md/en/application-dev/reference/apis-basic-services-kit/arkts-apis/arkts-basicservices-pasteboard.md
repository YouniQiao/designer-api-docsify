# @ohos.pasteboard(Pasteboard)

This module provides the capabilities of managing the system pasteboard to support the copy and paste functions. You can use the APIs of this module to operate pasteboard content of the plain text, HTML, URI, Want, PixelMap, and other types.

**Since:** 6

<!--Device-unnamed-declare namespace pasteboard--><!--Device-unnamed-declare namespace pasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createdata-1) | Creates a **PasteData** object of the specified type and creates a **PasteData** instance based on the input MIME type and data content. After this API is called, the system verifies the MIME type, encapsulates the data content, and returns a **PasteData** object that can be used in subsequent pasteboard operations. The value of **mimeType** can contain a maximum of 1024 bytes, and the value type must match the MIME type. Use this method when you need to save data of a single type (such as plain text, HTML, or images) to the pasteboard. Use the defined constant types (for example, **MIMETYPE_TEXT_PLAIN**) for **mimeType**. If you need to pass data in a custom format, you can use a custom MIME type. On API 26.1.0 and above, it can also support creating a URI-type **PasteData** object with a value of [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md). |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createdata-2) | Creates a **PasteData** object that contains multiple types of data. Multiple MIME data records can be created at a time. After this API is called, the system parses multiple key-value pairs in the record and creates multiple **PasteDataRecord** records. The first MIME type is used as the default type. Data of non-default types is read using [getData](arkts-basicservices-pasteboard-pastedatarecord-i.md#getdata). When an application needs to copy multiple types of data (such as text, URI, and HTML) to the pasteboard at the same time, this API can be used to create a **PasteData** object that contains data of multiple MIME types. |
| [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord-1) | Creates a data record of the specified type and encapsulates the data record into a **PasteDataRecord** object. After this API is called, the system encapsulates data of the specified MIME type and returns records that can be added to the **PasteData** object. The value of **mimeType** contains a maximum of 1024 bytes. The value type must match the MIME type. For example, if the MIME type is **MIMETYPE_TEXT_PLAIN**, the value must be of the string type. The parameter cannot be empty. |
| [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getsystempasteboard-1) | Obtains a **SystemPasteboard** object and returns a singleton instance of the pasteboard service. After this API is called, the **SystemPasteboard** object can be used to access the read, write, and listening functions of the pasteboard. The same instance is returned each time this API is called. Before calling this API, ensure that the pasteboard service is running properly. Before performing any read or write operation on the pasteboard, you need to call this API to obtain the **SystemPasteboard** object. |
| [createHtmlData](arkts-basicservices-pasteboard-createhtmldata-f.md#createhtmldata-1) | Creates a **PasteData** object of the HTML type. |
| [createHtmlTextRecord](arkts-basicservices-pasteboard-createhtmltextrecord-f.md#createhtmltextrecord-1) | Creates a **PasteDataRecord** object of the HTML text type. |
| [createPlainTextData](arkts-basicservices-pasteboard-createplaintextdata-f.md#createplaintextdata-1) | Creates a **PasteData** object of the plain text type. |
| [createPlainTextRecord](arkts-basicservices-pasteboard-createplaintextrecord-f.md#createplaintextrecord-1) | Creates a **PasteDataRecord** object of the plain text type. |
| [createUriData](arkts-basicservices-pasteboard-createuridata-f.md#createuridata-1) | Creates a **PasteData** object of the URI type. |
| [createUriRecord](arkts-basicservices-pasteboard-createurirecord-f.md#createurirecord-1) | Creates a **PasteDataRecord** object of the URI type. |
| [createWantData](arkts-basicservices-pasteboard-createwantdata-f.md#createwantdata-1) | Creates a **PasteData** object of the Want type. |
| [createWantRecord](arkts-basicservices-pasteboard-createwantrecord-f.md#createwantrecord-1) | Creates a **PasteDataRecord** object of the Want type. |

### Classes

| Name | Description |
| --- | --- |
| [ProgressSignal](arkts-basicservices-pasteboard-progresssignal-c.md) | Defines a function for canceling the progress indicator. The task can be canceled during pasting. The pasteboard progress indicator is valid only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) is set to **NONE**. |
| [VirtualBaseItem](arkts-basicservices-pasteboard-virtualbaseitem-c.md) | Base type for virtual file and directory items. |
| [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md) | Metadata of a virtual directory. |
| [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) | Virtual file information. |
| [VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) | Metadata of a virtual file. |

### Interfaces

| Name | Description |
| --- | --- |
| [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | Obtains parameters when an application uses the file copy capability provided by the pasteboard, including the destination path, file conflict options, and progress indicator types. Before calling this API, ensure that no other copy or paste operation is in progress. |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Implements a **PasteData** object. Paste data contains one or more data records ([PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md)) and property description objects ([PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)). |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Defines the properties of all data records on the pasteboard, including the timestamp, data type, pasteable range, and additional data. The defined properties can be applied to the pasteboard only with the [setProperty](arkts-basicservices-pasteboard-pastedata-i.md#setproperty) method. |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content on the pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records. The default data type of a **PasteDataRecord** cannot be changed after the record is created. You must specify the correct default data type when creating a **PasteDataRecord**. To update the attributes of a **PasteDataRecord**, use [addEntry](arkts-basicservices-pasteboard-pastedatarecord-i.md#addentry). |
| [ProgressInfo](arkts-basicservices-pasteboard-progressinfo-i.md) | Defines the progress information. This information is reported only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) is set to **NONE**. |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) | Provides **SystemPasteboard** APIs. |

### Types

| Name | Description |
| --- | --- |
| [ProgressListener](arkts-basicservices-pasteboard-progresslistener-t.md) | Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API to obtain the paste progress. |
| [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Callback to be invoked when the pasteboard content changes. |
| [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Indicates type of value. On API 26.1.0 and above, it can also support using [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md) in [createData](arkts-basicservices-pasteboard-createdata-f.md#createdata-1), [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord-1) and [addEntry](arkts-basicservices-pasteboard-pastedatarecord-i.md#addentry). |
| [VirtualFileOnCancel](arkts-basicservices-pasteboard-virtualfileoncancel-t.md) | Used to cancel the operation for specified virtual files. |
| [VirtualFileOnRead](arkts-basicservices-pasteboard-virtualfileonread-t.md) | Used to query the content of a specified virtual file. |
| [VirtualFileOnStat](arkts-basicservices-pasteboard-virtualfileonstat-t.md) | Used to query the metadata of a specified virtual file. |

### Enums

| Name | Description |
| --- | --- |
| [FileConflictOptions](arkts-basicservices-pasteboard-fileconflictoptions-e.md) | Enumerates the options used to resolve file copy conflicts. |
| [Pattern](arkts-basicservices-pasteboard-pattern-e.md) | Describes the patterns supported by the pasteboard. |
| [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) | Enumerates the progress indicator options. You can use the default progress indicator as required. |
| [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Enumerates the pasteable ranges of pasteboard data. |
| [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md) | Enumerates the supported virtual file types. |

### Constants

| Name | Description |
| --- | --- |
| [MAX_RECORD_NUM](arkts-basicservices-pasteboard-con.md#max_record_num) | Maximum number of records in a **PasteData** object. In versions earlier than API version 10, the value is 512, indicating that no more records can be added once the number of records reaches 512. Since API version 10, no limit is placed on the number of records in a **PasteData** object. |
| [MIMETYPE_PIXELMAP](arkts-basicservices-pasteboard-con.md#mimetype_pixelmap) | MIME type of the PixelMap content. |
| [MIMETYPE_TEXT_HTML](arkts-basicservices-pasteboard-con.md#mimetype_text_html) | MIME type of the HTML content. |
| [MIMETYPE_TEXT_PLAIN](arkts-basicservices-pasteboard-con.md#mimetype_text_plain) | MIME type of the plain text content. |
| [MIMETYPE_TEXT_URI](arkts-basicservices-pasteboard-con.md#mimetype_text_uri) | MIME type of the URI content. |
| [MIMETYPE_TEXT_WANT](arkts-basicservices-pasteboard-con.md#mimetype_text_want) | MIME type of the Want content. |
