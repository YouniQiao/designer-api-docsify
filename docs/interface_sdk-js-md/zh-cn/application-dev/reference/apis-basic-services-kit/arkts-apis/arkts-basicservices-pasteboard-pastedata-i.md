# PasteData

剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（[PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md)） 以及属性描述对象（[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)）。 在调用PasteData的接口前，需要先通过[createData()](arkts-basicservices-pasteboard-createdata-f.md) 或[getData()](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)获取一个PasteData对象。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## addHtmlRecord

```TypeScript
addHtmlRecord(htmlText: string): void
```

向当前剪贴板内容中添加一条HTML内容条目，并将MIMETYPE_TEXT_HTML添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [htmlText](arkts-basicservices-pasteboard-pastedatarecord-i.md) | string | 是 |

## addRecord

```TypeScript
addRecord(record: PasteDataRecord): void
```

向当前剪贴板内容中添加一条条目，同时也会将条目类型添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 是 |

## addRecord

```TypeScript
addRecord(mimeType: string, value: ValueType): void
```

向当前剪贴板内容中添加一条数据内容条目，同时也会将数据类型添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。当剪贴板内容需要包含多种类型的数据（如同时包含纯文本和HTML）时，使用此方法向已有的PasteData对象添加额外的数据条目。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900002](../errorcode-pasteboard.md#12900002-record数量超过最大限制) |

## addTextRecord

```TypeScript
addTextRecord(text: string): void
```

向当前剪贴板内容中添加一条纯文本条目，并将MIMETYPE_TEXT_PLAIN添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

## addUriRecord

```TypeScript
addUriRecord(uri: string): void
```

向当前剪贴板内容中添加一条URI条目，并将MIMETYPE_TEXT_URI添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

## addWantRecord

```TypeScript
addWantRecord(want: Want): void
```

向当前剪贴板内容中添加一条Want条目，并将MIMETYPE_TEXT_WANT添加到[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes中。 入参均不能为空，否则添加失败。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## getMimeTypes

```TypeScript
getMimeTypes(): Array<string>
```

获取剪贴板中[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)的mimeTypes列表，接口调用异常时返回undefined。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getPrimaryHtml

```TypeScript
getPrimaryHtml(): string
```

获取第一条的HTML内容。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## getPrimaryMimeType

```TypeScript
getPrimaryMimeType(): string
```

获取剪贴板内容中首个条目的数据类型。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## getPrimaryPixelMap

```TypeScript
getPrimaryPixelMap(): image.PixelMap
```

获取第一条的PixelMap内容。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

## getPrimaryText

```TypeScript
getPrimaryText(): string
```

获取第一条纯文本内容。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## getPrimaryUri

```TypeScript
getPrimaryUri(): string
```

获取第一条的URI内容。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## getPrimaryWant

```TypeScript
getPrimaryWant(): Want
```

获取第一条的Want对象内容。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) |

## getProperty

```TypeScript
getProperty(): PasteDataProperty
```

获取剪贴板内容的属性描述对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) |

## getRecord

```TypeScript
getRecord(index: number): PasteDataRecord
```

获取剪贴板内容中指定下标的条目。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900001](../errorcode-pasteboard.md#12900001-索引超过范围) |

## getRecordAt

```TypeScript
getRecordAt(index: number): PasteDataRecord
```

获取剪贴板内容中指定下标的条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getRecord](#getrecord)(index: int)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getRecordCount

```TypeScript
getRecordCount(): number
```

获取剪贴板内容中条目的个数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| number |

## getTag

```TypeScript
getTag(): string
```

获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## hasMimeType

```TypeScript
hasMimeType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定的数据类型。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [hasType](#hastype)(mimeType: string)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## hasType

```TypeScript
hasType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定的MIME数据类型。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## pasteComplete

```TypeScript
pasteComplete(): void
```

通知剪贴板服务数据使用已完成，可释放跨设备通道等资源。 应在调用pasteStart之后、完成数据处理后调用，避免资源浪费。未调用可能导致跨设备通道长时间占用，影响后续跨设备粘贴操作。 pasteComplete与其他接口的使用步骤可参考：
1. getData()获取剪贴板数据
2. pasteStart()保留跨设备通道
3. 使用剪贴板数据
4. pasteComplete()释放通道

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.Pasteboard

## pasteStart

```TypeScript
pasteStart(): void
```

读取剪贴板数据前，通知剪贴板服务保留跨设备通道。访问剪贴板数据中的跨端文件数据前，通知剪贴板服务保留跨设备链路。 跨设备链路用于连接远端设备并提供传输远端设备文件到本端设备的能力，如未调用此方法则跨设备链路将在30秒后自动断开。 适用于跨设备粘贴场景。当需要确保跨设备剪贴板数据通道保持连接，以便后续读取远端设备剪贴板数据时使用。  
- 必须与[pasteComplete](#pastecomplete)方法配对使用。  
- 调用顺序：先调用pasteStart()通知保留通道，数据处理完成后必须调用pasteComplete()通知完成。  
- 未调用pasteComplete()会导致跨设备通道未正确关闭，影响后续跨设备剪贴板操作。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.Pasteboard

## removeRecord

```TypeScript
removeRecord(index: number): void
```

移除剪贴板内容中指定下标的条目。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900001](../errorcode-pasteboard.md#12900001-索引超过范围) |

## removeRecordAt

```TypeScript
removeRecordAt(index: number): boolean
```

移除剪贴板内容中指定下标的条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeRecord](#removerecord)(index: int)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## replaceRecord

```TypeScript
replaceRecord(index: number, record: PasteDataRecord): void
```

替换剪贴板内容中指定下标的条目。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900001](../errorcode-pasteboard.md#12900001-索引超过范围) |

## replaceRecordAt

```TypeScript
replaceRecordAt(index: number, record: PasteDataRecord): boolean
```

替换剪贴板内容中指定下标的条目。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [replaceRecord](#replacerecord)(index: int, record: PasteDataRecord)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setProperty

```TypeScript
setProperty(property: PasteDataProperty): void
```

设置剪贴板内容的属性描述对象[PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
