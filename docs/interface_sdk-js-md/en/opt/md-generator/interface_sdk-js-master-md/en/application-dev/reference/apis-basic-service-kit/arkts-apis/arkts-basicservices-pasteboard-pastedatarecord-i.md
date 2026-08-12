# PasteDataRecord

Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content in the pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records.After creating a PasteDataRecord, it is not supported to modify the value of the default data type of the PasteDataRecord. The correct value for the default data type should be specified when creating the PasteDataRecord.If you need to refresh the attribute value of the PasteDataRecord,please use [addEntry](#addEntry).

**Since:** 7

<!--Device-pasteboard-interface PasteDataRecord--><!--Device-pasteboard-interface PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

Adds PasteData of an extra type to **PasteDataRecord**. The type added using this method is not the default type of **Record**. You can only use the  
[getData](#getData) API to read the corresponding data.

**Since:** 14

<!--Device-PasteDataRecord-addEntry(type: string, value: ValueType): void--><!--Device-PasteDataRecord-addEntry(type: string, value: ValueType): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
// Build an HTML string.
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
// Create an URI data record.
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
// Add plain text data.
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
// Add HTML data.
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
```

## convertToText

```TypeScript
convertToText(callback: AsyncCallback<string>): void
```

Forcibly converts the content in a **PasteData** object to text. This API uses an asynchronous callback to return  the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [toPlainText](#toPlainText)()

<!--Device-PasteDataRecord-convertToText(callback: AsyncCallback<string>): void--><!--Device-PasteDataRecord-convertToText(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText((err: BusinessError, data: string) => {
    if (err) {
        console.error(`Failed to convert to text. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in converting to text. Data: ${data}`);
});
```

## convertToText

```TypeScript
convertToText(): Promise<string>
```

Forcibly converts the content in a **PasteData** object to text. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [toPlainText](#toPlainText)()

<!--Device-PasteDataRecord-convertToText(): Promise<string>--><!--Device-PasteDataRecord-convertToText(): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText().then((data: string) => {
    console.info(`Succeeded in converting to text. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to convert to text. Cause: ${err.message}`);
});
```

## getData

```TypeScript
getData(type: string): Promise<ValueType>
```

Obtains data of the specified type from **PasteDataRecord**.

**Since:** 14

<!--Device-PasteDataRecord-getData(type: string): Promise<ValueType>--><!--Device-PasteDataRecord-getData(type: string): Promise<ValueType>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ValueType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
record.getData(pasteboard.MIMETYPE_TEXT_PLAIN).then((value: pasteboard.ValueType) => {
    let textPlainContent = value as string;
    console.info('Success to get text/plain value. value is: ' + textPlainContent);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/plain value. Cause: ' + err.message);
});
record.getData(pasteboard.MIMETYPE_TEXT_URI).then((value: pasteboard.ValueType) => {
    let uri = value as string;
    console.info('Success to get text/uri value. value is: ' + uri);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/uri value. Cause: ' + err.message);
});
```

## getValidTypes

```TypeScript
getValidTypes(types: Array<string>): Array<string>
```

Obtains the intersection of the input types and the types of the PasteData.

**Since:** 14

<!--Device-PasteDataRecord-getValidTypes(types: Array<string>): Array<string>--><!--Device-PasteDataRecord-getValidTypes(types: Array<string>): Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
let types: string[] = record.getValidTypes([
    pasteboard.MIMETYPE_TEXT_PLAIN,
    pasteboard.MIMETYPE_TEXT_HTML,
    pasteboard.MIMETYPE_TEXT_URI,
    pasteboard.MIMETYPE_TEXT_WANT,
    pasteboard.MIMETYPE_PIXELMAP
]);
```

## toPlainText

```TypeScript
toPlainText(): string
```

Forcibly converts HTML, plain, and URI content in a **PasteDataRecord** to the plain text.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-toPlainText(): string--><!--Device-PasteDataRecord-toPlainText(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, '<html>hello</html>');
let text: string = record.toPlainText();
console.info(`Succeeded in converting to text. Text: ${text}`);
```

## data

```TypeScript
data: Record<string, ArrayBuffer>
```

Content of custom data.

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ArrayBuffer&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-data: Record<string, ArrayBuffer>--><!--Device-PasteDataRecord-data: Record<string, ArrayBuffer>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## htmlText

```TypeScript
htmlText: string
```

HTML content.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-htmlText: string--><!--Device-PasteDataRecord-htmlText: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## mimeType

```TypeScript
mimeType: string
```

Default type of PasteDataRecord.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-mimeType: string--><!--Device-PasteDataRecord-mimeType: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

PixelMap content.

**Type:** image.PixelMap

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-pixelMap: image.PixelMap--><!--Device-PasteDataRecord-pixelMap: image.PixelMap-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## plainText

```TypeScript
plainText: string
```

Plain text.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-plainText: string--><!--Device-PasteDataRecord-plainText: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## uri

```TypeScript
uri: string
```

URI content.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-uri: string--><!--Device-PasteDataRecord-uri: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## want

```TypeScript
want: Want
```

Want content.

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataRecord-want: Want--><!--Device-PasteDataRecord-want: Want-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
