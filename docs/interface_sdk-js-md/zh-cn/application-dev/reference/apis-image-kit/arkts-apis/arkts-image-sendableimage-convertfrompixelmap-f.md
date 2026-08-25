# convertFromPixelMap

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## convertFromPixelMap

```TypeScript
function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap
```

Creates a sendable image PixelMap from image PixelMap.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
