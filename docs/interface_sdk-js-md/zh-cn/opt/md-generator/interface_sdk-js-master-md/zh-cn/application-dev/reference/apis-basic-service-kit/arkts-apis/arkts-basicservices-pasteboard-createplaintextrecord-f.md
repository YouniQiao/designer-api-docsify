# createPlainTextRecord

## createPlainTextRecord

```TypeScript
function createPlainTextRecord(text: string): PasteDataRecord
```

创建一条纯文本内容条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [pasteboard.createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord)(mimeType:

<!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord--><!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

## 示例

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```
