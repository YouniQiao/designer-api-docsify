# PasteData

剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（[PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md)）以及属性描述对象（[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)）。在调用PasteData的接口前，需要先通过[createData()](arkts-basicservices-pasteboard-createdata-f.md#createdata)或[getData()](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)获取一个PasteData对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-pasteboard-interface PasteData--><!--Device-pasteboard-interface PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## addHtmlRecord

```TypeScript
addHtmlRecord(htmlText: string): void
```

向当前剪贴板内容中添加一条HTML内容条目，并将MIMETYPE_TEXT_HTML添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord)(mimeType:

<!--Device-PasteData-addHtmlRecord(htmlText: string): void--><!--Device-PasteData-addHtmlRecord(htmlText: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| htmlText | string | Yes | HTML内容，需符合标准HTML格式。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
pasteData.addHtmlRecord(html);
```

## addRecord

```TypeScript
addRecord(record: PasteDataRecord): void
```

向当前剪贴板内容中添加一条条目，同时也会将条目类型添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-addRecord(record: PasteDataRecord): void--><!--Device-PasteData-addRecord(record: PasteDataRecord): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | 待添加的条目，设置后会将该条目添加到剪贴板内容中，同时更新mimeTypes属性列表。 |

## Examples

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

向当前剪贴板内容中添加一条数据内容条目，同时也会将数据类型添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。当剪贴板内容需要包含多种类型的数据（如同时包含纯文本和HTML）时，使用此方法向已有的PasteData对象添加额外的数据条目。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-addRecord(mimeType: string, value: ValueType): void--><!--Device-PasteData-addRecord(mimeType: string, value: ValueType): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | 数据的MIME类型，取值范围：长度不超过1024字节。超出范围时返回错误码401。 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 数据内容，设置后更新剪贴板内容的属性信息，包括时间戳、数据类型、粘贴范围等。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 12900002 | The number of records exceeds the upper limit.<br>**Applicable version:** 9 and later |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
// Create ArrayBuffer data.
let dataXml = new ArrayBuffer(256);
pasteData.addRecord('app/xml', dataXml);
```

## addTextRecord

```TypeScript
addTextRecord(text: string): void
```

向当前剪贴板内容中添加一条纯文本条目，并将MIMETYPE_TEXT_PLAIN添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord)(mimeType:

<!--Device-PasteData-addTextRecord(text: string): void--><!--Device-PasteData-addTextRecord(text: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 纯文本内容。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addTextRecord('good');
```

## addUriRecord

```TypeScript
addUriRecord(uri: string): void
```

向当前剪贴板内容中添加一条URI条目，并将MIMETYPE_TEXT_URI添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord)(mimeType:

<!--Device-PasteData-addUriRecord(uri: string): void--><!--Device-PasteData-addUriRecord(uri: string): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI内容。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');
```

## addWantRecord

```TypeScript
addWantRecord(want: Want): void
```

向当前剪贴板内容中添加一条Want条目，并将MIMETYPE_TEXT_WANT添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。入参均不能为空，否则添加失败。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord)(mimeType:

<!--Device-PasteData-addWantRecord(want: Want): void--><!--Device-PasteData-addWantRecord(want: Want): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want对象内容。 |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
pasteData.addWantRecord(object);
```

## getMimeTypes

```TypeScript
getMimeTypes(): Array<string>
```

获取剪贴板中[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes列表，接口调用异常时返回undefined。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getMimeTypes(): Array<string>--><!--Device-PasteData-getMimeTypes(): Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 剪贴板内容条目的数据类型，非重复的类型列表。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let types: string[] = pasteData.getMimeTypes();
```

## getPrimaryHtml

```TypeScript
getPrimaryHtml(): string
```

获取第一条的HTML内容。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryHtml(): string--><!--Device-PasteData-getPrimaryHtml(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | HTML内容。剪贴板内容对象中没有HTML内容时，默认返回为undefined。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let htmlText: string = pasteData.getPrimaryHtml();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getPrimaryMimeType

```TypeScript
getPrimaryMimeType(): string
```

获取剪贴板内容中首个条目的数据类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryMimeType(): string--><!--Device-PasteData-getPrimaryMimeType(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | 首个条目的数据类型。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let type: string = pasteData.getPrimaryMimeType();
```

## getPrimaryPixelMap

```TypeScript
getPrimaryPixelMap(): image.PixelMap
```

获取第一条的PixelMap内容。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryPixelMap(): image.PixelMap--><!--Device-PasteData-getPrimaryPixelMap(): image.PixelMap-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | PixelMap内容。剪贴板内容对象中没有PixelMap内容时，默认返回为undefined。 |

## Examples

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

获取第一条纯文本内容。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryText(): string--><!--Device-PasteData-getPrimaryText(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | 纯文本内容。剪贴板内容对象中没有纯文本内容时，默认返回为undefined。 |

## Examples

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
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getPrimaryUri

```TypeScript
getPrimaryUri(): string
```

获取第一条的URI内容。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryUri(): string--><!--Device-PasteData-getPrimaryUri(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | URI内容。剪贴板内容对象中没有URI内容时，默认返回为undefined。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let uri: string = pasteData.getPrimaryUri();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getPrimaryWant

```TypeScript
getPrimaryWant(): Want
```

获取第一条的Want对象内容。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getPrimaryWant(): Want--><!--Device-PasteData-getPrimaryWant(): Want-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Want对象内容。剪贴板内容对象中没有Want内容时，默认返回为undefined。 |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let want: Want = pasteData.getPrimaryWant();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getProperty

```TypeScript
getProperty(): PasteDataProperty
```

获取剪贴板内容的属性描述对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getProperty(): PasteDataProperty--><!--Device-PasteData-getProperty(): PasteDataProperty-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | 属性描述对象。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let property: pasteboard.PasteDataProperty = pasteData.getProperty();
```

## getRecord

ArkTS-Dyn:
```TypeScript
getRecord(index: number): PasteDataRecord
```

ArkTS-Sta:
```TypeScript
getRecord(index: int): PasteDataRecord
```

获取剪贴板内容中指定下标的条目。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getRecord(index: int): PasteDataRecord--><!--Device-PasteData-getRecord(index: int): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定条目的下标。有效取值范围：[0, getRecordCount()-1]，超出范围会触发错误码12900001。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 指定下标的条目。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12900001 | The index is out of the record. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);
```

## getRecordAt

```TypeScript
getRecordAt(index: number): PasteDataRecord
```

获取剪贴板内容中指定下标的条目。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.getRecord](arkts-basicservices-pasteboard-pastedata-i.md#getrecord)(index:

<!--Device-PasteData-getRecordAt(index: number): PasteDataRecord--><!--Device-PasteData-getRecordAt(index: number): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定条目的下标。有效取值范围：[0, getRecordCount()-1]，超出范围返回错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 指定下标的条目。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);
```

## getRecordCount

ArkTS-Dyn:
```TypeScript
getRecordCount(): number
```

ArkTS-Sta:
```TypeScript
getRecordCount(): int
```

获取剪贴板内容中条目的个数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getRecordCount(): int--><!--Device-PasteData-getRecordCount(): int-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 条目的个数。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let count: number = pasteData.getRecordCount();
```

## getTag

```TypeScript
getTag(): string
```

获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-getTag(): string--><!--Device-PasteData-getTag(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回用户自定义的标签内容，如果没有设置用户自定义的标签内容，将返回空。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let tag: string = pasteData.getTag();
```

## hasMimeType

```TypeScript
hasMimeType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定的数据类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.hasType](arkts-basicservices-pasteboard-pastedata-i.md#hastype)(mimeType:

<!--Device-PasteData-hasMimeType(mimeType: string): boolean--><!--Device-PasteData-hasMimeType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | 待查询的数据类型。可以是 [常量](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#常量)中已定义的类型， 包括：HTML类型、Want类型、纯文本类型、URI类型、PixelMap类型，也可以是自定义的MIME类型，长度不能超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

## hasType

```TypeScript
hasType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定的MIME数据类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-hasType(mimeType: string): boolean--><!--Device-PasteData-hasType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | 待查询的数据类型。 可以是[常量](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#常量)中已定义的类型， 包括：HTML类型、Want类型、纯文本类型、URI类型、PixelMap类型；也可以是自定义的MIME类型，数据类型的字符串长度不能超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

## pasteComplete

```TypeScript
pasteComplete(): void
```

通知剪贴板服务数据使用已完成，可释放跨设备通道等资源。应在调用pasteStart之后、完成数据处理后调用，避免资源浪费。未调用可能导致跨设备通道长时间占用，影响后续跨设备粘贴操作。pasteComplete与其他接口的使用步骤可参考：1. getData()获取剪贴板数据2. pasteStart()保留跨设备通道3. 使用剪贴板数据4. pasteComplete()释放通道

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PasteData-pasteComplete(): void--><!--Device-PasteData-pasteComplete(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
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

读取剪贴板数据前，通知剪贴板服务保留跨设备通道。访问剪贴板数据中的跨端文件数据前，通知剪贴板服务保留跨设备链路。跨设备链路用于连接远端设备并提供传输远端设备文件到本端设备的能力，如未调用此方法则跨设备链路将在30秒后自动断开。适用于跨设备粘贴场景。当需要确保跨设备剪贴板数据通道保持连接，以便后续读取远端设备剪贴板数据时使用。

- 必须与[pasteComplete](arkts-basicservices-pasteboard-pastedata-i.md#pastecomplete)方法配对使用。  
- 调用顺序：先调用pasteStart()通知保留通道，数据处理完成后必须调用pasteComplete()通知完成。  
- 未调用pasteComplete()会导致跨设备通道未正确关闭，影响后续跨设备剪贴板操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PasteData-pasteStart(): void--><!--Device-PasteData-pasteStart(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

## removeRecord

ArkTS-Dyn:
```TypeScript
removeRecord(index: number): void
```

ArkTS-Sta:
```TypeScript
removeRecord(index: int): void
```

移除剪贴板内容中指定下标的条目。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-removeRecord(index: int): void--><!--Device-PasteData-removeRecord(index: int): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的下标。有效取值范围：[0, getRecordCount()-1]，超出范围会触发错误码12900001。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12900001 | The index is out of the record. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
pasteData.removeRecord(0);
```

## removeRecordAt

```TypeScript
removeRecordAt(index: number): boolean
```

移除剪贴板内容中指定下标的条目。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.removeRecord](arkts-basicservices-pasteboard-pastedata-i.md#removerecord)(index:

<!--Device-PasteData-removeRecordAt(index: number): boolean--><!--Device-PasteData-removeRecordAt(index: number): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定的下标。有效取值范围：[0, getRecordCount()-1]，超出范围返回错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 移除指定下标的条目成功返回true，移除失败（如指定下标不存在或超出范围）返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let isRemove: boolean = pasteData.removeRecordAt(0);
```

## replaceRecord

ArkTS-Dyn:
```TypeScript
replaceRecord(index: number, record: PasteDataRecord): void
```

ArkTS-Sta:
```TypeScript
replaceRecord(index: int, record: PasteDataRecord): void
```

替换剪贴板内容中指定下标的条目。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-replaceRecord(index: int, record: PasteDataRecord): void--><!--Device-PasteData-replaceRecord(index: int, record: PasteDataRecord): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的下标。有效取值范围：[0, getRecordCount()-1]，超出范围会触发错误码12900001。 |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | 被替换后的条目数据内容，设置后会替换指定下标位置的原始条目。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12900001 | The index is out of the record. |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

## replaceRecordAt

```TypeScript
replaceRecordAt(index: number, record: PasteDataRecord): boolean
```

替换剪贴板内容中指定下标的条目。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.PasteData.replaceRecord](arkts-basicservices-pasteboard-pastedata-i.md#replacerecord)(index:

<!--Device-PasteData-replaceRecordAt(index: number, record: PasteDataRecord): boolean--><!--Device-PasteData-replaceRecordAt(index: number, record: PasteDataRecord): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定的下标。有效取值范围：[0, getRecordCount()-1]，超出范围返回错误码401。 |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes | 替换后的条目。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 替换指定下标的条目成功返回true，替换失败（如指定下标不存在或超出范围、参数为空）返回false。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
let isReplace: boolean = pasteData.replaceRecordAt(0, record);
```

## setProperty

```TypeScript
setProperty(property: PasteDataProperty): void
```

设置剪贴板内容的属性描述对象[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteData-setProperty(property: PasteDataProperty): void--><!--Device-PasteData-setProperty(property: PasteDataProperty): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| property | [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Yes | 属性描述对象，设置后更新剪贴板内容的属性信息，包括时间戳、数据类型、粘贴范围等。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

The localOnly and shareOption attributes of [PasteDataProperty](#pastedataproperty7) are mutually exclusive. The shareOption attribute is prioritized, and its value affects the value of localOnly.

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

