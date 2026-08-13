# createUriData

## createUriData

```TypeScript
function createUriData(uri: string): PasteData
```

构建一个URI剪贴板内容对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createData](arkts-basicservices-pasteboard-createdata-f.md#createData)(mimeType: string, value: ValueType)

<!--Device-pasteboard-function createUriData(uri: string): PasteData--><!--Device-pasteboard-function createUriData(uri: string): PasteData-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |

## 示例

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');
```
