# convertToPixelMap

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## convertToPixelMap

```TypeScript
function convertToPixelMap(pixelmap: PixelMap): image.PixelMap
```

Creates a image PixelMap from sendable image PixelMap.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
