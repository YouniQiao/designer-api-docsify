# createData

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## createData

```TypeScript
function createData(mimeType: string, value: ValueType): PasteData
```

Creates a **PasteData** object of the specified type and creates a **PasteData** instance based on the input MIME type and data content. After this API is called, the system verifies the MIME type, encapsulates the data content, and returns a **PasteData** object that can be used in subsequent pasteboard operations. The value of **mimeType** can contain a maximum of 1024 bytes, and the value type must match the MIME type. Use this method when you need to save data of a single type (such as plain text, HTML, or images) to the pasteboard. Use the defined constant types (for example, **MIMETYPE_TEXT_PLAIN**) for **mimeType**. If you need to pass data in a custom format, you can use a custom MIME type. On API 26.1.0 and above, it can also support creating a URI-type **PasteData** object with a value of [VirtualFileInfo](arkts-basicservices-pasteboard-virtualfileinfo-c.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function createData(mimeType: string, value: ValueType): PasteData--><!--Device-pasteboard-function createData(mimeType: string, value: ValueType): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | MIME type of custom data. The value can be a predefined MIME type listed in [Constants](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want, plain text, URI, and pixel map, or a custom MIME type. The value of **mimeType** cannot exceed 1024 bytes. |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes | Content of custom data. You are advised to select a proper data type based on the actual scenario. Using a large data object will affect the app's copy and paste performance and memory usage. For the **ArrayBuffer** type, you are advised to set a proper data size. For the **PixelMap** type, you are advised to release objects that are no longer used in a timely manner. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | **PasteData** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types;         3. Parameter verification failed. |


## createData

```TypeScript
function createData(data: Record<string, ValueType>): PasteData
```

Creates a **PasteData** object that contains multiple types of data. Multiple MIME data records can be created at a time. After this API is called, the system parses multiple key-value pairs in the record and creates multiple **PasteDataRecord** records. The first MIME type is used as the default type. Data of non-default types is read using [getData](arkts-basicservices-pasteboard-pastedatarecord-i.md#getdata). When an application needs to copy multiple types of data (such as text, URI, and HTML) to the pasteboard at the same time, this API can be used to create a **PasteData** object that contains data of multiple MIME types.

**Since:** 14

<!--Device-pasteboard-function createData(data: Record<string, ValueType>): PasteData--><!--Device-pasteboard-function createData(data: Record<string, ValueType>): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [ValueType](arkts-basicservices-pasteboard-valuetype-t.md)&gt; | Yes | The key of **Record** can be the MIME type corresponding to the pasteboard data, including HTML, Want, plain text, URI, and pixel map defined in [Constants](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#constants). Alternatively, the key could be a custom MIME type, whose parameter, the length of **mimeType**, cannot exceed 1024 bytes. <br>The value of **Record** is the data corresponding to the MIME type specified in the key. <br>The first MIME type specified by the key-value in **Record** is used as the default MIME type of the first **PasteDataRecord** in the **PasteData** object. Data of non-default types can be read only by using the [getData](arkts-basicservices-pasteboard-pastedatarecord-i.md#getdata) API. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | **PasteData** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types;         3. Parameter verification failed. |
