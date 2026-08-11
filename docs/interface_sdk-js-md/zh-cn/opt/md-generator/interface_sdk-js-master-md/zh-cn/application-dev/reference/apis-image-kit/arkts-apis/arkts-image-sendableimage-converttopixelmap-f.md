# convertToPixelMap

## convertToPixelMap

```TypeScript
function convertToPixelMap(pixelmap: PixelMap): image.PixelMap
```

Creates a image PixelMap from sendable image PixelMap.

**起始版本：** 12

<!--Device-sendableImage-function convertToPixelMap(pixelmap: PixelMap): image.PixelMap--><!--Device-sendableImage-function convertToPixelMap(pixelmap: PixelMap): image.PixelMap-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |

## 示例

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function ConvertToPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  let sendablePixelMap : sendableImage.PixelMap = sendableImage.createPixelMapSync(color, opts);
  let pixelMap : image.PixelMap = sendableImage.convertToPixelMap(sendablePixelMap);
  return pixelMap;
}
```
