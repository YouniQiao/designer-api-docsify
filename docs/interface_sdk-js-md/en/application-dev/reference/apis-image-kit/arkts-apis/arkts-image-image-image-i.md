# Image

The **Image** class is used to obtain image content.An Image instance is returned when [readNextImage](arkts-image-image-imagereceiver-i.md#readnextimage) and [readLatestImage](arkts-image-image-imagereceiver-i.md#readlatestimage) are called.Image properties are initialized only during image creation and cannot be changed later. These properties do not affect the actual image content. You should always rely on the properties written by the image producer, that is, the content actually sent to the [ImageReceiver](arkts-image-image-imagereceiver-i.md) by the data source. Images occupy a large amount of memory. When you finish using an Image instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## getBufferData

```TypeScript
getBufferData(): ImageBufferData | null
```

Obtains ImageBufferData from an image.

> **NOTE：**&gt;
> **byteBuffer** in **ImageBufferData** is a shallow copy of the internal buffer. When the lifecycle of an image
> ends, do not perform any operations on **byteBuffer**, as this may lead to undefined behavior.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageBufferData](arkts-image-image-imagebufferdata-i.md) \| null |

## getComponent

```TypeScript
getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void
```

Obtains the component buffer from the Image instance based on the color component type. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| componentType | [ComponentType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-update-componenttype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Component&gt; | Yes |

## getComponent

```TypeScript
getComponent(componentType: ComponentType): Promise<Component>
```

Obtains the component buffer from the Image instance based on the color component type. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| componentType | [ComponentType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-update-componenttype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Component & gt; |

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue | null
```

Obtains the HDR metadata from an image based on the HDR metadata type.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) \| null |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this Image instance. This API uses an asynchronous callback to return the result.The corresponding resources must be released before another image arrives.Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this Image instance. This API uses a promise to return the result.The corresponding resources must be released before another image arrives.Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## clipRect

```TypeScript
clipRect: Region
```

Image area to be cropped.

**Type:** Region

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## colorSpace

```TypeScript
readonly colorSpace: colorSpaceManager.ColorSpace
```

Color space of the image.

**Type:** colorSpaceManager.ColorSpace

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

## format

```TypeScript
readonly format: number
```

Image format. For details, see OH_NativeBuffer_Format.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
readonly size: Size
```

Image size.If the Image object stores camera preview stream data (YUV image data), the width and height in **size** reflect the dimensions of the YUV image.If the Image object stores camera capture stream data (JPEG image data), given that it is an encoded file, the width in **size** is the size of the JPEG file, while the height is set to **1**.The type of data stored in the Image object depends on whether the application passes the surface ID in the receiver to a previewOutput or captureOutput object of the camera.For details about the best practices of camera preview and photo capture, see [Dual-Channel Preview (ArkTS)](../../../media/camera/camera-dual-channel-preview.md) and [Photo Capture Sample (ArkTS)](../../../media/camera/camera-shooting-case.md).

**Type:** Size

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## timestamp

```TypeScript
readonly timestamp: number
```

Image timestamp. Timestamps, measured in nanoseconds, are usually monotonically increasing. The specific meaning and baseline of these timestamps are determined by the image producer, which is the camera in the camera preview and photo scenarios. As a result, images from different producers may carry timestamps with distinct meanings and baselines, making direct comparison between them infeasible. To obtain the generation time of a photo, you can use [getImageProperty](arkts-image-image-imagesource-i.md#getimageproperty) to read the related Exif information.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core
