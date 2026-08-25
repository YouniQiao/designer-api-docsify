# UnifiedRecord

对UDMF支持的数据内容的抽象定义，称为数据记录。一个统一数据对象内包含一条或多条数据记录，例如一条文本记录、一条图片记录、一条HTML记录等。从API version 15开始，支持往数据记录中增加同一内容的不同数据格式（例如同 一文本可同时以纯文本、HTML或超链接等格式存储），数据使用方根据业务需要通过getEntry方法获取对应格式。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

在当前数据记录中添加一条指定数据类型和内容的数据，通过该方法增加的数据类型和内容为同一内容的不同表现样式。调用成功后，指定的数据类型和内容被添加到当前数据记录中。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## constructor

```TypeScript
constructor()
```

用于创建数据记录。调用成功后，返回一个空的UnifiedRecord对象。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## constructor

```TypeScript
constructor(type: string, value: ValueType)
```

用于创建指定类型和值的数据记录。调用成功后，返回包含指定类型和值的UnifiedRecord对象。当参数value为[image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)类型时，参数type必须对应为 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)中 OPENHARMONY_PIXEL_MAP的值；当参数value为[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)类型时，参数type必须对应为 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)中OPENHARMONY_WANT的 值。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getEntries

```TypeScript
getEntries(): Record<string, ValueType>
```

获取当前数据记录中所有数据的类型和内容。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 |
| --- |
| Record & lt;string, ValueType & gt; |

## getEntry

```TypeScript
getEntry(type: string): ValueType
```

通过数据类型获取数据记录中的数据内容。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getType

```TypeScript
getType(): string
```

获取当前数据记录的类型。由于从统一数据对象中调用[getRecords](arkts-arkdata-unifieddatachannel-unifieddata-c.md#getrecords)所取出的数据是UnifiedRecord对象，因此需要通 过本接口查询此记录的具体类型，再将该UnifiedRecord对象转换为其子类，调用子类接口。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 |
| --- |
| string |

## getTypes

```TypeScript
getTypes(): Array<string>
```

获取数据记录中数据的所有类型集合。可通过UnifiedRecord数据记录对象调用本接口，查询出此记录中数据的所有类型集合，包括使用 [addEntry](#addentry)函数添加的数据类型。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getValue

```TypeScript
getValue(): ValueType
```

获取当前数据记录的值。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |
