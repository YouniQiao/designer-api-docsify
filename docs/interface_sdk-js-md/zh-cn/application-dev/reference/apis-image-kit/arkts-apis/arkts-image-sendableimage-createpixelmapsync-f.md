# createPixelMapSync

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createPixelMapSync

```TypeScript
function createPixelMapSync(colors: ArrayBuffer, options: image.InitializationOptions): PixelMap
```

Create PixelMap by data buffer.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | ArrayBuffer | 是 |
| options | image.InitializationOptions | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
