# createHtmlData

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createHtmlData

```TypeScript
function createHtmlData(htmlText: string): PasteData
```

构建一个HTML剪贴板内容对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createData](arkts-basicservices-pasteboard-createdata-f.md)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [htmlText](arkts-basicservices-pasteboard-pastedatarecord-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |
