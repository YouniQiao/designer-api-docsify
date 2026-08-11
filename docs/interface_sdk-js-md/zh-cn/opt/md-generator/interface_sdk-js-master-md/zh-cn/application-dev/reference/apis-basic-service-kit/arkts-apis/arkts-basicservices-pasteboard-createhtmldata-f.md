# createHtmlData

## createHtmlData

```TypeScript
function createHtmlData(htmlText: string): PasteData
```

构建一个HTML剪贴板内容对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [pasteboard.createData](arkts-basicservices-pasteboard-createdata-f.md#createdata)(mimeType:

<!--Device-pasteboard-function createHtmlData(htmlText: string): PasteData--><!--Device-pasteboard-function createHtmlData(htmlText: string): PasteData-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| htmlText | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |

## 示例

```TypeScript
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let pasteData: pasteboard.PasteData = pasteboard.createHtmlData(html);
```
