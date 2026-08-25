# ImageReceiver

Image receiver class. You can use it to obtain the surface ID of a component, read the latest image and the next image, and release **ImageReceiver** instances.Before calling any APIs in ImageReceiver, you must create an ImageReceiver instance.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(): Promise<string>
```

Obtains a surface ID for the camera or other components. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## on('imageArrival')

```TypeScript
on(type: 'imageArrival', callback: AsyncCallback<void>): void
```

Listens for image arrival events. This API uses an asynchronous callback to return the result.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imageArrival' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## readLatestImage

```TypeScript
readLatestImage(): Promise<Image>
```

Reads the latest image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the [on](#onimagearrival) callback is
> triggered. When the [Image](arkts-image-sendableimage-imagesource-i.md) object returned by this API is no longer needed,
> call [release](arkts-image-sendableimage-pixelmap-i.md#release) to release the object. New data can be received only after
> the release.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Image & gt; |

## readNextImage

```TypeScript
readNextImage(): Promise<Image>
```

Reads the next image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the [on](#onimagearrival) callback is
> triggered. When the [Image](arkts-image-sendableimage-imagesource-i.md) object returned by this API is no longer needed,
> call [release](arkts-image-sendableimage-pixelmap-i.md#release) to release the object. New data can be received only after
> the release.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Image & gt; |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageReceiver instance. This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## capacity

```TypeScript
readonly capacity: number
```

Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value.The actual capacity is determined by the device hardware.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## format

```TypeScript
readonly format: image.ImageFormat
```

Image format.

**Type:** image.ImageFormat

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
readonly size: image.Size
```

Image size.

**Type:** image.Size

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver
