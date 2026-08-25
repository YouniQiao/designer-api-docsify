# createPixelMapFromParcel

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createPixelMapFromParcel

```TypeScript
function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap
```

Creates a PixelMap object based on MessageSequence parameter.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |
| [62980177](../errorcode-image.md#62980177-api环境异常) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980179](../errorcode-image.md#62980179-缓冲区大小异常) |
| [62980180](../errorcode-image.md#62980180-文件描述符映射失败) |
| [62980246](../errorcode-image.md#62980246-读取pixelmap失败) |
