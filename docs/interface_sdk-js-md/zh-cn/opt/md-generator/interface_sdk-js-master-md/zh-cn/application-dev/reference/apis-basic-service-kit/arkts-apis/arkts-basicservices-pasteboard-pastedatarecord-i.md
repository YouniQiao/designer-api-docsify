# PasteDataRecord

对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI或者一个Want。不支持在创建PasteDataRecord之后，修改PasteDataRecord的默认数据类型的值，应在创建PasteDataRecord时指定正确的默认数据类型的值。如需刷新PasteDataRecord的属性值，请使用[addEntry](#addEntry)。

**起始版本：** 7

<!--Device-pasteboard-interface PasteDataRecord--><!--Device-pasteboard-interface PasteDataRecord-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

往一个PasteDataRecord中额外添加一种样式的数据。此方式添加的MIME类型都不是Record的默认类型，粘贴时只能使用[getData](#getData)接口读取对应数据。

**起始版本：** 14

<!--Device-PasteDataRecord-addEntry(type: string, value: ValueType): void--><!--Device-PasteDataRecord-addEntry(type: string, value: ValueType): void-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
// 构建HTML内容字符串
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
// 创建URI类型数据条目
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
// 添加纯文本类型数据
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
// 添加HTML类型数据
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
```

## convertToText

```TypeScript
convertToText(callback: AsyncCallback<string>): void
```

将一个PasteData中的内容强制转换为文本内容，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [toPlainText](#toPlainText)()

<!--Device-PasteDataRecord-convertToText(callback: AsyncCallback<string>): void--><!--Device-PasteDataRecord-convertToText(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText((err: BusinessError, data: string) => {
    if (err) {
        console.error(`Failed to convert to text. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info(`Succeeded in converting to text. Data: ${data}`);
});
```

## convertToText

```TypeScript
convertToText(): Promise<string>
```

将一个PasteData中的内容强制转换为文本内容，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [toPlainText](#toPlainText)()

<!--Device-PasteDataRecord-convertToText(): Promise<string>--><!--Device-PasteDataRecord-convertToText(): Promise<string>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText().then((data: string) => {
    console.info(`Succeeded in converting to text. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to convert to text. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getData

```TypeScript
getData(type: string): Promise<ValueType>
```

从PasteDataRecord中获取指定MIME类型的自定义数据，使用Promise异步回调。

**起始版本：** 14

<!--Device-PasteDataRecord-getData(type: string): Promise<ValueType>--><!--Device-PasteDataRecord-getData(type: string): Promise<ValueType>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ValueType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

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
    console.error(`Failed to get text/plain value. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
record.getData(pasteboard.MIMETYPE_TEXT_URI).then((value: pasteboard.ValueType) => {
    let uri = value as string;
    console.info('Success to get text/uri value. value is: ' + uri);
}).catch((err: BusinessError) => {
    console.error(`Failed to get text/uri value. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getValidTypes

```TypeScript
getValidTypes(types: Array<string>): Array<string>
```

根据传入的MIME类型，返回传入的MIME类型和剪贴板中数据的MIME类型的交集。在粘贴前，检查剪贴板数据是否包含应用支持的格式。例如，若应用仅支持纯文本和HTML格式，可调用此接口检查剪贴板数据是否包含这些格式，并根据返回结果决定是否执行粘贴操作。

**起始版本：** 14

<!--Device-PasteDataRecord-getValidTypes(types: Array<string>): Array<string>--><!--Device-PasteDataRecord-getValidTypes(types: Array<string>): Array<string>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

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

将一个PasteDataRecord中的html、plain、uri内容强制转换为文本内容。若PasteDataRecord包含其他数据类型（如PixelMap、Want等），转换结果为空字符串。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-toPlainText(): string--><!--Device-PasteDataRecord-toPlainText(): string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, '<html>hello</html>');
let text: string = record.toPlainText();
console.info(`Succeeded in converting to text. Text: ${text}`);
```

## data

```TypeScript
data: Record<string, ArrayBuffer>
```

自定义数据内容。

**类型：** Record&lt;string, ArrayBuffer&gt;

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-data: Record<string, ArrayBuffer>--><!--Device-PasteDataRecord-data: Record<string, ArrayBuffer>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## htmlText

```TypeScript
htmlText: string
```

HTML内容，需符合标准HTML格式。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-htmlText: string--><!--Device-PasteDataRecord-htmlText: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## mimeType

```TypeScript
mimeType: string
```

默认数据类型。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-mimeType: string--><!--Device-PasteDataRecord-mimeType: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

PixelMap内容。

**类型：** image.PixelMap

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-pixelMap: image.PixelMap--><!--Device-PasteDataRecord-pixelMap: image.PixelMap-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## plainText

```TypeScript
plainText: string
```

纯文本内容。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-plainText: string--><!--Device-PasteDataRecord-plainText: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## uri

```TypeScript
uri: string
```

URI内容，需符合标准URI格式。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-uri: string--><!--Device-PasteDataRecord-uri: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## want

```TypeScript
want: Want
```

Want内容。

**类型：** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PasteDataRecord-want: Want--><!--Device-PasteDataRecord-want: Want-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard
