# Metadata

Metadata类，用于存储图像的元数据。目前支持的元数据类型可参考[MetadataType](arkts-image-image-metadatatype-e.md)。

> **说明：**&gt;
> - 本Interface首批接口从API version 13开始支持。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## clone

```TypeScript
clone(): Promise<Metadata>
```

对元数据进行克隆。使用Promise异步回调。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Metadata & gt; |

## getAllProperties

```TypeScript
getAllProperties(): Promise<Record<string, string | null>>
```

获取图片中所有元数据的属性和值。使用Promise异步回调。如要查询属性值信息请参考[PropertyKey](arkts-image-image-propertykey-e.md)、[FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md)、 [GifPropertyKey](arkts-image-image-gifpropertykey-e.md)和[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md)。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, string \ | null & gt; & gt; |

## getBlob

```TypeScript
getBlob(): Promise<ArrayBuffer>
```

以二进制数据的形式获取元数据。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## getProperties

```TypeScript
getProperties(key: Array<string>): Promise<Record<string, string | null>>
```

获取图像中属性的值。使用Promise异步回调。如要查询属性值信息请参考[PropertyKey](arkts-image-image-propertykey-e.md)、[FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md)、 [GifPropertyKey](arkts-image-image-gifpropertykey-e.md)和[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md)。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, string \ | null & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) |

## setBlob

```TypeScript
setBlob(blob: ArrayBuffer): Promise<void>
```

使用二进制数据替换当前元数据。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blob | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## setProperties

```TypeScript
setProperties(records: Record<string, string | null>): Promise<void>
```

批量设置图片元数据中的指定属性的值。使用Promise异步回调。如要查询属性值信息请参考[PropertyKey](arkts-image-image-propertykey-e.md)、[FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md)、 [GifPropertyKey](arkts-image-image-gifpropertykey-e.md)和[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md)。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) |
