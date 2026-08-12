# createImageReceiver

## Modules to Import

```TypeScript
import { sendableImage } from '@kit.ImageKit';
```

## createImageReceiver

```TypeScript
function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver
```

Creates an ImageReceiver instance based on the specified image size, format, and capacity.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call   
[release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

<!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver--><!--Device-sendableImage-function createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | image.Size | Yes |
| format | image.ImageFormat | Yes |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
