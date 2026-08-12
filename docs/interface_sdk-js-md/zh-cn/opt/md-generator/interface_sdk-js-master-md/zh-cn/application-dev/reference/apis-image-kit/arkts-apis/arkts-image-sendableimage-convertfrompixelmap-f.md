# convertFromPixelMap

## convertFromPixelMap

```TypeScript
function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap
```

Creates a sendable image PixelMap from image PixelMap.

**起始版本：** 12

<!--Device-sendableImage-function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap--><!--Device-sendableImage-function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-arkui/arkts-apis/arkts-arkui-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [62980104](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-image-kit/errorcode-image.md#62980104-图片初始化错误) |

## 示例

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function ConvertFromPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
  let sendablePixelMap : sendableImage.PixelMap = sendableImage.convertFromPixelMap(pixelMap);
  return sendablePixelMap;
}
```
