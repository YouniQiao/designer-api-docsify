# createRecord

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## createRecord

```TypeScript
function createRecord(mimeType: string, value: ValueType): PasteDataRecord
```

Creates a data record of the specified type and encapsulates the data record into a **PasteDataRecord** object. After this API is called, the system encapsulates data of the specified MIME type and returns records that can be added to the **PasteData** object. The value of **mimeType** contains a maximum of 1024 bytes. The value type must match the MIME type. For example, if the MIME type is **MIMETYPE_TEXT_PLAIN**, the value must be of the string type. The parameter cannot be empty.

- The created record takes effect only after being added to the [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) object  
using [addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord-1).  
- The typical process is as follows: Use [createData](arkts-basicservices-pasteboard-createdata-f.md) to create a **PasteData**  
object, use **createRecord** to create a record, and then use **addRecord** to add the record.

On API 26.1.0 and above, it can also support creating a URI-type data record with a value of [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord--><!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | MIME type of custom data. The value can be a predefined MIME type listed in [Constants](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want, plain text, URI, and pixel map, or a custom MIME type. The value of **mimeType** cannot exceed 1024 bytes. |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes | Data content of the specified type. You are advised to select a proper data type based on the actual scenario. Using a large data object will affect the pasteboard performance and memory usage. For the **ArrayBuffer** type, you are advised to set a proper data size. For the **PixelMap** type, you are advised to release objects that are no longer used in a timely manner. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | A new paste data record of a specified type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types;         3. Parameter verification failed. |
