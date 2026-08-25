# createUriRecord

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createUriRecord

```TypeScript
function createUriRecord(uri: string): PasteDataRecord
```

创建一条URI内容的条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createRecord](arkts-basicservices-pasteboard-createrecord-f.md)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |
