# createHtmlTextRecord

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createHtmlTextRecord

```TypeScript
function createHtmlTextRecord(htmlText: string): PasteDataRecord
```

创建一条HTML内容的条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createRecord](arkts-basicservices-pasteboard-createrecord-f.md)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [htmlText](arkts-basicservices-pasteboard-pastedatarecord-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |
