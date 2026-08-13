# createRecord

## createRecord

```TypeScript
function createRecord(mimeType: string, value: ValueType): PasteDataRecord
```

创建一条指定类型的数据内容条目，将数据内容封装为PasteDataRecord对象。调用此方法后，系统将根据MIME类型封装数据内容，返回可添加到PasteData中的条目对象。 参数mimeType长度不能超过1024字节，value类型需与mimeType对应（如mimeType为MIMETYPE_TEXT_PLAIN，则value类型必须是string），参数不能为空。 - 创建的条目通常需要通过[addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addRecord)方法添加到 [PasteData](arkts-basicservices-pasteboard-pastedata-i.md#PasteData)对象中才能生效。 - 典型使用流程：先通过[createData](arkts-basicservices-pasteboard-createdata-f.md#createData)创建PasteData对象， 再使用createRecord创建条目，最后通过addRecord添加条目。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord--><!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
