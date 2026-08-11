# createImageReceiver

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageReceiver

```TypeScript
function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver
```

Creates an ImageReceiver instance by specifying the image width, height, format, and capacity. The ImageReceiver acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with   
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput).Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call   
[release](arkts-image-image-imagereceiver-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver)(size:

<!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver--><!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| format | number | Yes |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

## Examples

```TypeScript
let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver
```

Creates an ImageReceiver instance by specifying the image size, format, and capacity. The ImageReceiver acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with   
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput).Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call   
[release](arkts-image-image-imagereceiver-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 11

<!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver--><!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | Yes |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | Yes |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let size: image.Size = {
  height: 8192,
  width: 8192
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined
```

Creates an ImageReceiver instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined--><!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7900201](../errorcode-image.md#7900201-invalid-parameter) |

## Examples

```TypeScript
let options: image.ImageReceiverOptions = {
  size: { width: 480, height: 480 },
  capacity: 3
}
let receiver: image.ImageReceiver | undefined = image.createImageReceiver(options);
```
