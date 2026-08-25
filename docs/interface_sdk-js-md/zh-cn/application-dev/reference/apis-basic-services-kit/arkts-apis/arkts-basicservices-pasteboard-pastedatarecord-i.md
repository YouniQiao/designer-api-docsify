# PasteDataRecord

对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI或者一个Want。 不支持在创建PasteDataRecord之后，修改PasteDataRecord的默认数据类型的值，应在创建PasteDataRecord时指定正确的默认数据类型的值。 如需刷新PasteDataRecord的属性值，请使用[addEntry](#addentry)。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

往一个PasteDataRecord中额外添加一种样式的数据。此方式添加的MIME类型都不是Record的默认类型， 粘贴时只能使用[getData](#getdata)接口读取对应数据。

**起始版本：** 14

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## convertToText

```TypeScript
convertToText(callback: AsyncCallback<string>): void
```

将一个PasteData中的内容强制转换为文本内容，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [toPlainText](#toplaintext)()

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## convertToText

```TypeScript
convertToText(): Promise<string>
```

将一个PasteData中的内容强制转换为文本内容，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [toPlainText](#toplaintext)()

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getData

```TypeScript
getData(type: string): Promise<ValueType>
```

从PasteDataRecord中获取指定MIME类型的自定义数据，使用Promise异步回调。

**起始版本：** 14

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getValidTypes

```TypeScript
getValidTypes(types: Array<string>): Array<string>
```

根据传入的MIME类型，返回传入的MIME类型和剪贴板中数据的MIME类型的交集。在粘贴前，检查剪贴板数据是否包含应用支持的格式。 例如，若应用仅支持纯文本和HTML格式，可调用此接口检查剪贴板数据是否包含这些格式，并根据返回结果决定是否执行粘贴操作。

**起始版本：** 14

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

## toPlainText

```TypeScript
toPlainText(): string
```

将一个PasteDataRecord中的html、plain、uri内容强制转换为文本内容。若PasteDataRecord包含其他数据类型（如PixelMap、Want等），转换结果为空字符串。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

## data

```TypeScript
data: Record<string, ArrayBuffer>
```

自定义数据内容。对此属性的修改无效。

**类型：** Record&lt;string, ArrayBuffer&gt;

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## htmlText

```TypeScript
htmlText: string
```

HTML内容，需符合标准HTML格式。 对此属性的修改无效，如需刷新属性值，请使用[addEntry](#addentry)。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## mimeType

```TypeScript
mimeType: string
```

默认数据类型。对此属性的修改无效。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

PixelMap内容。对此属性的修改无效，如需刷新属性值，请使用[addEntry](#addentry)。

**类型：** image.PixelMap

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## plainText

```TypeScript
plainText: string
```

纯文本内容。对此属性的修改无效，如需刷新属性值，请使用[addEntry](#addentry)。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## uri

```TypeScript
uri: string
```

URI内容，需符合标准URI格式。对此属性的修改无效，如需刷新属性值，请使用[addEntry](#addentry)。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

## want

```TypeScript
want: Want
```

Want内容。对此属性的修改无效，如需刷新属性值，请使用[addEntry](#addentry)。

**类型：** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard
