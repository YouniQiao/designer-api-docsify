# createImageReceiver

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createImageReceiver

```TypeScript
function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver
```

通过图片大小、图片格式、容量创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver--><!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | image.Size | Yes | 图像的默认大小。 |
| format | image.ImageFormat | Yes | 图像格式，取值为image.ImageFormat常量，目前仅支持 ImageFormat:JPEG。 |
| capacity | number | Yes | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) | 如果操作成功，则返回ImageReceiver实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. |

## Examples

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

