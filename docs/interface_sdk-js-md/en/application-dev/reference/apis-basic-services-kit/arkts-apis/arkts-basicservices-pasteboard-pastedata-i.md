# PasteData

```TypeScript
interface PasteData
```

Implements a **PasteData** object. Paste data contains one or more data records ([PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md)) and property description objects ([PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)).

Before calling any API in **PasteData**, you must use **[createData()](arkts-basicservices-pasteboard-createdata-f.md)** or **[getData()](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata-1)** to create a **PasteData** object.

**Since:** 6

<!--Device-pasteboard-interface PasteData--><!--Device-pasteboard-interface PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## addRecord

```TypeScript
addRecord(record: PasteDataRecord): void
```

Adds a data record to this pasteboard, and adds its type to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-addRecord(record: PasteDataRecord): void--><!--Device-PasteData-addRecord(record: PasteDataRecord): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | Record to be added. After this parameter is set, the record is added to the pasteboard and the **mimeTypes** attribute list is updated. |

**Examples**

```TypeScript
// Create a PasteData object of the URI type.
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
// Create a data record of the plain text type.
let textRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let htmlRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, html);
pasteData.addRecord(textRecord);
pasteData.addRecord(htmlRecord);
```

## addRecord

```TypeScript
addRecord(mimeType: string, value: ValueType): void
```

Adds a data record to this pasteboard, and adds its type to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails. Use this method to add additional data records to an existing **PasteData** object when the pasteboard needs to contain multiple types of data, for example, plain text and HTML.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-addRecord(mimeType: string, value: ValueType): void--><!--Device-PasteData-addRecord(mimeType: string, value: ValueType): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | MIME type of data. The value contains a maximum of 1024 bytes. If the value is out of range, error code 401 is returned. |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes | Data content. After this parameter is set, the pasteboard data properties are updated, including the timestamp, data type, and pasteable scope. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types;         3. Parameter verification failed. |
| [12900002](../errorcode-pasteboard.md#12900002-maximum-number-of-records-reached) | The number of records exceeds the upper limit.<br>**Applicable version:** 9 |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
// Create ArrayBuffer data.
let dataXml = new ArrayBuffer(256);
pasteData.addRecord('app/xml', dataXml);
```

## getMimeTypes

```TypeScript
getMimeTypes(): Array<string>
```

Obtains MIME types of [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) on the pasteboard. If an exception occurs during API invoking, **undefined** is returned.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getMimeTypes(): Array<string>--><!--Device-PasteData-getMimeTypes(): Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Non-repeating data types of the data records on the pasteboard. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let types: string[] = pasteData.getMimeTypes();
```

## getPrimaryHtml

```TypeScript
getPrimaryHtml(): string
```

Obtains the HTML content of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryHtml(): string--><!--Device-PasteData-getPrimaryHtml(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | HTML content. If the **PasteData** object does not contain HTML content, **undefined** is returned by default. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let htmlText: string = pasteData.getPrimaryHtml();
}).catch((err: BusinessError) => {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getPrimaryMimeType

```TypeScript
getPrimaryMimeType(): string
```

Obtains the data type of the primary record in this pasteboard.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryMimeType(): string--><!--Device-PasteData-getPrimaryMimeType(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | Data type of the primary record. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let type: string = pasteData.getPrimaryMimeType();
```

## getPrimaryPixelMap

```TypeScript
getPrimaryPixelMap(): image.PixelMap
```

Obtains the pixel map of the primary record.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryPixelMap(): image.PixelMap--><!--Device-PasteData-getPrimaryPixelMap(): image.PixelMap-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Pixel map. If the **PasteData** object does not contain the pixel map, **undefined** is returned by default. |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';

// Create a buffer for storing image data.
let buffer = new ArrayBuffer(128);
// Define the image size.
let realSize: image.Size = { height: 3, width: 5 };
let opt: image.InitializationOptions = {
    size: realSize,
    pixelFormat: 3,
    editable: true,
    alphaType: 1,
    scaleMode: 1
};
image.createPixelMap(buffer, opt).then((pixelMap: image.PixelMap) => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
    let PixelMap: image.PixelMap = pasteData.getPrimaryPixelMap();
});
```

## getPrimaryText

```TypeScript
getPrimaryText(): string
```

Obtains the plain text of the primary record.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryText(): string--><!--Device-PasteData-getPrimaryText(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | Plain text. If the **PasteData** object does not contain plain text, **undefined** is returned by default. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Asynchronously read the pasteboard data.
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    // Handle the failure of obtaining the content.
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getPrimaryUri

```TypeScript
getPrimaryUri(): string
```

Obtains the URI of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryUri(): string--><!--Device-PasteData-getPrimaryUri(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | URI content. If the **PasteData** object does not contain the URI, **undefined** is returned by default. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let uri: string = pasteData.getPrimaryUri();
}).catch((err: BusinessError) => {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getPrimaryWant

```TypeScript
getPrimaryWant(): Want
```

Obtains the **Want** object of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryWant(): Want--><!--Device-PasteData-getPrimaryWant(): Want-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Want object. If the **PasteData** object does not contain the **Want** object, **undefined** is returned by default. |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let want: Want = pasteData.getPrimaryWant();
}).catch((err: BusinessError) => {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getProperty

```TypeScript
getProperty(): PasteDataProperty
```

Obtains the property of the pasteboard data.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getProperty(): PasteDataProperty--><!--Device-PasteData-getProperty(): PasteDataProperty-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Property of the pasteboard data. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let property: pasteboard.PasteDataProperty = pasteData.getProperty();
```

## getRecord

```TypeScript
getRecord(index: number): PasteDataRecord
```

Obtains the record with a specific index from the pasteboard.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getRecord(index: int): PasteDataRecord--><!--Device-PasteData-getRecord(index: int): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the target record. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 12900001 is triggered. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Record with the specified index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:         1. Mandatory parameters are left unspecified;         2. Incorrect parameter types;         3. Parameter verification failed. |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) | The index is out of range. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);
```

## getRecordCount

```TypeScript
getRecordCount(): number
```

Obtains the number of records in the pasteboard.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getRecordCount(): int--><!--Device-PasteData-getRecordCount(): int-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of records. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let count: number = pasteData.getRecordCount();
```

## getTag

```TypeScript
getTag(): string
```

Obtains the custom tag from the pasteboard. If no custom tag is set, empty string is returned.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getTag(): string--><!--Device-PasteData-getTag(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | Custom tag. If no custom tag is set, empty string is returned. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let tag: string = pasteData.getTag();
```

## hasType

```TypeScript
hasType(mimeType: string): boolean
```

Checks whether the pasteboard contains data of the specified MIME type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-hasType(mimeType: string): boolean--><!--Device-PasteData-hasType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | Type of the data to query. The value can be a predefined type listed in [Constants](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want, plain text, URI, and pixel map, or a custom MIME type. The length of the data type string cannot exceed 1024 bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the specified data type exists; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes:         1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

## pasteComplete

```TypeScript
pasteComplete(): void
```

Notifies the pasteboard service that the paste is complete, and resources such as the cross-device channel can be released. This API should be called after **pasteStart()** is called and data processing is complete to prevent resource waste. If this API is not called, the cross-device channel may be occupied for a long time, affecting subsequent cross-device paste operations.

For details about how to use **pasteComplete()** and other APIs, see the following:

1. Obtain the pasteboard data by calling **getData()**.
2. Reserve the cross-device channel by calling **pasteStart()**.
3. Use the pasteboard data.
4. Release the channel by calling **pasteComplete()**.

**Since:** 12

<!--Device-PasteData-pasteComplete(): void--><!--Device-PasteData-pasteComplete(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

## pasteStart

```TypeScript
pasteStart(): void
```

Notifies the pasteboard service to retain the cross-device channel before reading data from the pasteboard. The cross-device link is used to connect to the peer device and transfer files from the peer device to the local device. If this API is not called, the cross-device link will be automatically disconnected 30 seconds later. It is applicable to the cross-device pasting scenario. This API is used when you need to ensure that the cross-device channel for pasteboard data transfer remains connected for subsequent reading of the pasteboard data from the peer device.

- This API must be used with [pasteComplete](#pastecomplete) in pairs.  
- Calling sequence: Call **pasteStart()** to notify the system to reserve the channel. After data processing is  
complete, call **pasteComplete()** to notify the system that the processing is complete.  
- If **pasteComplete()** is not called, the cross-device channel will not be correctly closed, affecting  
subsequent cross-device pasteboard operations.

**Since:** 12

<!--Device-PasteData-pasteStart(): void--><!--Device-PasteData-pasteStart(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

## removeRecord

```TypeScript
removeRecord(index: number): void
```

Removes the record with a specific index from the pasteboard.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-removeRecord(index: int): void--><!--Device-PasteData-removeRecord(index: int): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Specified index. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 12900001 is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:         1. Mandatory parameters are left unspecified;         2. Incorrect parameter types;         3. Parameter verification failed. |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) | The index is out of range. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
pasteData.removeRecord(0);
```

## replaceRecord

```TypeScript
replaceRecord(index: number, record: PasteDataRecord): void
```

Replaces the record with a specific index from the pasteboard.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-replaceRecord(index: int, record: PasteDataRecord): void--><!--Device-PasteData-replaceRecord(index: int, record: PasteDataRecord): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Specified index. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 12900001 is triggered. |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | New record. After this parameter is set, the original record with the specified index is replaced. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:         1. Mandatory parameters are left unspecified;         2. Incorrect parameter types;         3. Parameter verification failed. |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) | The index is out of range. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

## setProperty

```TypeScript
setProperty(property: PasteDataProperty): void
```

Sets a [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-setProperty(property: PasteDataProperty): void--><!--Device-PasteData-setProperty(property: PasteDataProperty): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| property | [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Yes | Data properties. After this parameter is set, the pasteboard data properties updated, including the timestamp, data type, and pasteable scope. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
// Define the type of the additional property.
type AdditionType = Record<string, Record<string, Object>>;

// Create a PasteData object of the HTML type.
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_HTML, 'application/xml');
// Obtain a PasteDataProperty object.
let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
prop.shareOption = pasteboard.ShareOption.INAPP;
// Note that attributes cannot be added to additions. Attributes can be added only by re-assigning values.
prop.additions = { 'TestOne': { 'Test': 123 }, 'TestTwo': { 'Test': 'additions' } } as AdditionType;
prop.tag = 'TestTag';
pasteData.setProperty(prop);
```

The localOnly and shareOption attributes of [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) are mutually exclusive. The shareOption attribute is prioritized, and its value affects the value of localOnly.

```TypeScript
(async () => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
    let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
    prop.shareOption = pasteboard.ShareOption.INAPP;
    prop.localOnly = false;
    pasteData.setProperty(prop);
    const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });

    prop.shareOption = pasteboard.ShareOption.LOCALDEVICE;
    prop.localOnly = false;
    pasteData.setProperty(prop);

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });
})
```

## addHtmlRecord

```TypeScript
addHtmlRecord(htmlText: string): void
```

Adds an HTML record to this pasteboard, and adds **MIMETYPE_TEXT_HTML** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord-2)(mimeType: string, value: ValueType)

<!--Device-PasteData-addHtmlRecord(htmlText: string): void--><!--Device-PasteData-addHtmlRecord(htmlText: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| htmlText | string | Yes | HTML text. The value must comply with the standard HTML format. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
pasteData.addHtmlRecord(html);
```

## addTextRecord

```TypeScript
addTextRecord(text: string): void
```

Adds a plain text record to this pasteboard, and adds **MIMETYPE_TEXT_PLAIN** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord-2)(mimeType: string, value: ValueType)

<!--Device-PasteData-addTextRecord(text: string): void--><!--Device-PasteData-addTextRecord(text: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Plain text. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addTextRecord('good');
```

## addUriRecord

```TypeScript
addUriRecord(uri: string): void
```

Adds a URI record to this pasteboard, and adds **MIMETYPE_TEXT_URI** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord-2)(mimeType: string, value: ValueType)

<!--Device-PasteData-addUriRecord(uri: string): void--><!--Device-PasteData-addUriRecord(uri: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI content. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');
```

## addWantRecord

```TypeScript
addWantRecord(want: Want): void
```

Adds a Want record to this pasteboard, and adds **MIMETYPE_TEXT_WANT** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord-2)(mimeType: string, value: ValueType)

<!--Device-PasteData-addWantRecord(want: Want): void--><!--Device-PasteData-addWantRecord(want: Want): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want object. |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
pasteData.addWantRecord(object);
```

## getRecordAt

```TypeScript
getRecordAt(index: number): PasteDataRecord
```

Obtains the record with a specific index from the pasteboard.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getRecord](#getrecord)(index: number)

<!--Device-PasteData-getRecordAt(index: number): PasteDataRecord--><!--Device-PasteData-getRecordAt(index: number): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the target record. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Record with the specified index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);
```

## hasMimeType

```TypeScript
hasMimeType(mimeType: string): boolean
```

Checks whether the pasteboard contains data of the specified type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasType](#hastype)(mimeType: string)

<!--Device-PasteData-hasMimeType(mimeType: string): boolean--><!--Device-PasteData-hasMimeType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | Type of the data to query. The value can be a predefined type listed in [Constants](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want, plain text, URI, and pixel map, or a custom MIME type. The length cannot exceed 1024 bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the specified data type exists; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

## removeRecordAt

```TypeScript
removeRecordAt(index: number): boolean
```

Removes the record with a specific index from the pasteboard.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeRecord](#removerecord)(index: number)

<!--Device-PasteData-removeRecordAt(index: number): boolean--><!--Device-PasteData-removeRecordAt(index: number): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Specified index. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** is returned if the record with the specified index is successfully removed; the value **false** is returned if the record fails to be removed (for example, the specified index does not exist or is out of range). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let isRemove: boolean = pasteData.removeRecordAt(0);
```

## replaceRecordAt

```TypeScript
replaceRecordAt(index: number, record: PasteDataRecord): boolean
```

Replaces the record with a specific index from the pasteboard.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [replaceRecord](#replacerecord)(index: number, record: PasteDataRecord)

<!--Device-PasteData-replaceRecordAt(index: number, record: PasteDataRecord): boolean--><!--Device-PasteData-replaceRecordAt(index: number, record: PasteDataRecord): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Specified index. The value ranges from 0 to the value of **getRecordCount()** minus 1. If the value is out of range, error code 401 is returned. |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | New record. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** is returned if the record with the specified index is successfully replaced; the value **false** is returned if the record fails to be removed (for example, the specified index does not exist or is out of range, or the parameter is empty). |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
let isReplace: boolean = pasteData.replaceRecordAt(0, record);
```
