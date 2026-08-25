# ImageReceiver

The **ImageReceiver** class provides APIs to obtain the surface ID of a component, read the latest image, read the next image, and release the ImageReceiver instance. The ImageReceiver acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with [createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md#createpreviewoutput). Before calling any APIs in ImageReceiver, you must use [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md) to create an ImageReceiver instance. Since API version 23, you are advised to use [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md) to create an **ImageReceiver** instance based on the passed [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md). Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(callback: AsyncCallback<string>): void
```

Obtains a surface ID for the camera or other components. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(): Promise<string>
```

Obtains a surface ID for the camera or other components. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## off('imageArrival')

```TypeScript
off(type: 'imageArrival', callback?: AsyncCallback<void>): void
```

Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous callback to return the result.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imageArrival' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## on('imageArrival')

```TypeScript
on(type: 'imageArrival', callback: AsyncCallback<void>): void
```

Listens for image arrival events. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imageArrival' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## readLatestImage

```TypeScript
readLatestImage(callback: AsyncCallback<Image>): void
```

Reads the latest image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the
> on callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes |

## readLatestImage

```TypeScript
readLatestImage(): Promise<Image>
```

Reads the latest image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the
> on callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Image & gt; |

## readNextImage

```TypeScript
readNextImage(callback: AsyncCallback<Image>): void
```

Reads the next image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the
> on callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes |

## readNextImage

```TypeScript
readNextImage(): Promise<Image>
```

Reads the next image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called to receive data only after the
> on callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Image & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageReceiver instance. This API uses an asynchronous callback to return the result.Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageReceiver instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## capacity

```TypeScript
readonly capacity: number
```

Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## format

```TypeScript
readonly format: ImageFormat
```

Image format. The value is an enum value of [ImageFormat](arkts-image-image-imageformat-e.md). (Currently, only **ImageFormat:JPEG** is supported. The format actually returned depends on the producer, for example, camera.)

**Type:** [ImageFormat](arkts-image-image-imageformat-e.md)

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
readonly size: Size
```

Image size. This parameter does not affect the size of the received image. The actual returned size is determined by the producer, for example, the camera.

**Type:** Size

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver
