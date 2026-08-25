# createPixelMapFromSurface

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |


## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**起始版本：** 15

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
