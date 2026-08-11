# createImageReceiver

## createImageReceiver

```TypeScript
function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver
```

通过图片大小、图片格式、容量创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 12

<!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver--><!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | image.Size | 是 |
| format | image.ImageFormat | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function CreateImageReceiver() {
    let size: image.Size = {
        height: 8192,
        width: 8
    } 
    let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
}
```
