# ImageSource

The **ImageSource** class provides APIs to obtain image information.Before calling any API in ImageSource, you must use [image.createImageSource](arkts-image-image-createimagesource-f.md) to create an ImageSource instance.All APIs in ImageSource cannot be called concurrently.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageRawData

```TypeScript
createImageRawData(): Promise<ImageRawData>
```

Obtains raw data from an image.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ImageRawData](arkts-image-image-imagerawdata-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |

## createPicture

```TypeScript
createPicture(options?: DecodingOptionsForPicture): Promise<Picture>
```

Creates a Picture object based on decoding options. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using a Picture instance, call [release](arkts-image-image-picture-i.md#release) to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |
| [7700203](../errorcode-image.md#7700203-unsupported-options) |

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index: number): Promise<Picture>
```

Creates a **Picture** object using a specified image (only GIF and HEIF&lt;sup&gt;23+&lt;/sup&gt; images currently). This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using a Picture instance, call [release](arkts-image-image-picture-i.md#release) to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700203](../errorcode-image.md#7700203-unsupported-options) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses a promise to return the result.Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator). This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

## createPixelMap

```TypeScript
createPixelMap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object based on the default parameters. This API uses an asynchronous callback to return the result.Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator). This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | Yes |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses an asynchronous callback to return the result.Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator). This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | Yes |

## createPixelMapList

```TypeScript
createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>
```

Creates an array of PixelMap objects based on decoding options. This API uses a promise to return the result.For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.&gt;
> - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
> large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
> for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
> function.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;PixelMap & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980109](../errorcode-image.md#62980109-cropping-error) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) |

## createPixelMapList

```TypeScript
createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void
```

Creates an array of PixelMap objects based on the default parameters. This API uses an asynchronous callback to return the result.For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.&gt;
> - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
> large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
> for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
> function.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980109](../errorcode-image.md#62980109-cropping-error) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) |

## createPixelMapList

```TypeScript
createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void
```

Creates an array of PixelMap objects based on decoding options. This API uses an asynchronous callback to return the result.For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.&gt;
> - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
> large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
> for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
> function.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980109](../errorcode-image.md#62980109-cropping-error) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap
```

Creates a PixelMap object based on decoding options. This API returns the result synchronously.Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.Starting from API version 15, you are advised to use [createPixelMapUsingAllocatorSync](#createpixelmapusingallocatorsync). This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).

> **NOTE：**&gt;
> This API operates synchronously and will block the current thread during execution. It should not be invoked
> from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
> details, see
> [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options and memory type. This API uses a promise to return the result. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).

> **NOTE：**&gt;
> - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.&gt;
> - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
> [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.&gt;
> - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
> finished and the instance is no longer needed.

**Since:** 15

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) |
| [7700203](../errorcode-image.md#7700203-unsupported-options) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap
```

Creates a PixelMap object based on decoding options and memory type. This API returns the result synchronously. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md).Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

> **NOTE：**&gt;
> This API operates synchronously and will block the current thread during execution. It should not be invoked
> from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
> details, see
> [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 15

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) |
| [7700203](../errorcode-image.md#7700203-unsupported-options) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) |

## createThumbnail

```TypeScript
createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>
```

Creates a thumbnail image based on image decoding parameters. This method uses a promise to return the PixelMap object, which represents the thumbnail.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |
| [7700303](../errorcode-image.md#7700303-image-does-not-contain-thumbnail-data) |
| [7700305](../errorcode-image.md#7700305-thumbnail-generation-failed) |

## createThumbnailSync

```TypeScript
createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined
```

Synchronously creates a thumbnail image based on image decoding parameters. This method returns a `PixelMap` object, which represents the generated thumbnail.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| PixelMap \| undefined |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |
| [7700303](../errorcode-image.md#7700303-image-does-not-contain-thumbnail-data) |
| [7700305](../errorcode-image.md#7700305-thumbnail-generation-failed) |

## getDelayTimeList

```TypeScript
getDelayTimeList(): Promise<Array<number>>
```

Obtains an array of delay times. This API uses a promise to return the result. This API applies only to images in GIF or WebP format.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) |

## getDelayTimeList

```TypeScript
getDelayTimeList(callback: AsyncCallback<Array<number>>): void
```

Obtains an array of delay times. This API uses an asynchronous callback to return the result. This API applies only to images in GIF or WebP format.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) |

## getDisposalTypeList

```TypeScript
getDisposalTypeList(): Promise<Array<number>>
```

Obtains the list of disposal types. This API uses a promise to return the result. It is used only for GIF images.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) |

## getFrameCount

```TypeScript
getFrameCount(): Promise<number>
```

Obtains the number of frames. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |

## getFrameCount

```TypeScript
getFrameCount(callback: AsyncCallback<number>): void
```

Obtains the number of frames. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) |

## getImageInfo

```TypeScript
getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information with the specified index. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes |

## getImageInfo

```TypeScript
getImageInfo(index?: number): Promise<ImageInfo>
```

Obtains the image information. This API uses a promise to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: number): ImageInfo
```

Obtains the image information with the specified index. This API returns the result synchronously.

> **NOTE：**&gt;
> This API operates synchronously and will block the current thread during execution. It should not be invoked
> from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
> details, see
> [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

## getImageProperties

```TypeScript
getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>
```

Obtains the values of properties with the given names in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/sup&gt;format and contain Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | Array & lt;PropertyKey & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Record & lt;PropertyKey, string \ | null & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980116](../errorcode-image.md#62980116-decoding-failure) |

## getImageProperty

```TypeScript
getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>
```

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/ sup&gt; format and contain Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | Yes |
| options | [ImagePropertyOptions](arkts-image-image-imagepropertyoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) |

## getImageProperty

```TypeScript
getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>
```

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getImageProperty

```TypeScript
getImageProperty(key: string, callback: AsyncCallback<string>): void
```

Obtains the value of a property with the specified index in this image. This API uses an asynchronous callback to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getImageProperty

```TypeScript
getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void
```

Obtains the value of a property in this image. This API uses an asynchronous callback to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string
```

Obtains the value of a specified Exif property. This API returns the result synchronously.

> **NOTE：**&gt;
> - This API applies only to images that are in JPEG, PNG, HEIF, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/sup&gt;format
> and contain Exif information. (The supported formats may vary depending on the hardware.)&gt;
> - Exif information is metadata of the image, including shooting time, camera model, aperture, focal length, and
> ISO.&gt;
> - This API operates synchronously and will block the current thread during execution. It should not be invoked
> from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
> details, see
> [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 20

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |

## modifyImageProperties

```TypeScript
modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>
```

Modifies the values of properties in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> The property byte length is changed when the **modifyImageProperties** API is called to modify the values of
> properties. Currently, you can call the API in an ImageSource instance created based on a file descriptor or
> path, but not an ImageSource instance created based on buffers.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| records | Record & lt;PropertyKey, string \ | null & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) |
| [62980146](../errorcode-image.md#62980146-failed-to-write-image-property-values-to-the-file) |

## modifyImagePropertiesEnhanced

```TypeScript
modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>
```

Modifies image properties in batches. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Calling this API to modify properties alters the property byte length. You are advised to create an
> [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by passing a
> file descriptor or an
> [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by
> passing a URI.&gt;
> - This API modifies batch data in memory and writes the data to the file in a single operation. It is more
> efficient than
> [modifyImageProperties](#modifyimageproperties)
> .&gt;
> - This API applies only to images that are in JPEG, PNG, HEIF, or WEBP format and contain the Exif information.

**Since:** 22

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |
| [7700304](../errorcode-image.md#7700304-failed-to-write-image-information-to-the-file) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: PropertyKey, value: string): Promise<void>
```

Modifies the value of a property in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
> property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
> , but not an ImageSource instance created based on buffers.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) |
| [62980133](../errorcode-image.md#62980133-image-property-value-out-of-range) |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) |
| [62980146](../errorcode-image.md#62980146-failed-to-write-image-property-values-to-the-file) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string): Promise<void>
```

Modifies the value of a property in this image. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
> property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
> , but not an ImageSource instance created based on buffers.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void
```

Modifies the value of a property in this image. This API uses an asynchronous callback to return the result.This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
> property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
> , but not an ImageSource instance created based on buffers.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## readImageMetadata

```TypeScript
readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>
```

Reads image metadata. You can use **propertyKeys** to specify the keys of metadata. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF, WEBP, or DNG format and contain Exif information. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> When reading a DNG image, this API applies special handling to some **propertyKeys**. For details about the
> values of the following properties, see [PropertyKey](arkts-image-image-propertykey-e.md):&gt;
> - **NewSubfileType**, **ImageWidth**, **ImageLength**, **DefaultCropSize**, **Orientation**, **Compression**,
> **PhotometricInterpretation**, **PlanarConfiguration**, **RowsPerStrip**, **StripOffsets**, **StripByteCounts**
> , **SamplesPerPixel**, **BitsPerSample**, **YCbCrCoefficients**, **YCbCrSubSampling**, **YCbCrPositioning**,
> **ReferenceBlackWhite**, **XResolution**, **YResolution**, and **ResolutionUnit**: For these properties, values
> related to the main image are returned.&gt;
> - **ImageUniqueID**: The value is verified based on the specifications. If the value fails to comply with the
> specifications, an empty string is returned.&gt;
> - **ExifVersion**, **FlashpixVersion**, and **ColorSpace**: If the image does not contain these properties, an
> error code is returned.&gt;
> - **DNGVersion**: If the value is earlier than **1.0.0.0**, **1.0.0.0** is returned.&gt;
> - **GPSVersionID**: If there is no valid GPS data, the GPS version number is cleared and **0** is returned.&gt;
> - **GPSAltitudeRef**: If **GPSAltitude** is not set, this property is set to **0xFFFFFFFF**.&gt;
> - **ISOSpeedRatings**: If its value is **0** or **65535**, the recommended exposure index is used first. If the
> recommended exposure index does not exist, the standard output sensitivity, ISO speed, and exposure index are
> used in sequence.&gt;
> This API supports reading metadata in the following formats:&gt;
> - Since API version 24, DNG metadata can be read. For details about the properties, see
> [DngPropertyKey](arkts-image-image-dngpropertykey-e.md).&gt;
> - Since API version 24, HEIFS metadata can be read. For details about the properties, see
> [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md).&gt;
> - Since API version 26.0.0, PNG metadata can be read. For details about the properties, see
> [PngPropertyKey](arkts-image-image-pngpropertykey-e.md).&gt;
> - Since API version 26.0.0, JFIF metadata can be read. For details about the properties, see
> [JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md).&gt;
> - Since API version 26.0.0, TIFF metadata can be read. For details about the properties, see
> [TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md).&gt;
> - Since API version 26.0.0, GIF metadata can be read. For details about the properties, see
> [GifPropertyKey](arkts-image-image-gifpropertykey-e.md).&gt;
> - Since API version 26.0.0, XMP metadata of JPEG, PNG, GIF, DNG, and TIFF images can be read. For details about
> how to operate XMP metadata, see [XMPMetadata](arkts-image-image-xmpmetadata-c.md).&gt;
> - Since API version 26.0.0, AVIS metadata can be read. For details about the properties, see [AvisPropertyKey](arkts-image-image-avispropertykey-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propertyKeys | string[] | No |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |

## readImageMetadataByType

```TypeScript
readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>
```

Reads the metadata of an image source. You can use **metadataTypes** to specify the metadata types. If **metadataTypes** is not specified, all supported metadata is returned. This API uses a promise to return the result.This API applies only to images that are in JPEG, PNG, HEIF, WEBP, DNG, or HEIFS format. (The supported formats may vary depending on the hardware.)

> **NOTE：**&gt;
> - **EXIF_METADATA** applies to JPEG, PNG, HEIF, WEBP, and DNG images.&gt;
> - **HEIFS_METADATA** applies to HEIFS images.&gt;
> - If the input **MetadataType** does not match the image format, error code **7700102** will be returned.&gt;
> - Since API version 24, DNG metadata can be read. For details about the properties, see
> [DngPropertyKey](arkts-image-image-dngpropertykey-e.md).&gt;
> - Since API version 24, HEIFS metadata can be read. For details about the properties, see
> [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md).&gt;
> - Since API version 26.0.0, PNG metadata can be read. For details about the properties, see
> [PngPropertyKey](arkts-image-image-pngpropertykey-e.md).&gt;
> - Since API version 26.0.0, JFIF metadata can be read. For details about the properties, see
> [JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md).&gt;
> - Since API version 26.0.0, TIFF metadata can be read. For details about the properties, see
> [TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md).&gt;
> - Since API version 26.0.0, GIF metadata can be read. For details about the properties, see
> [GifPropertyKey](arkts-image-image-gifpropertykey-e.md).&gt;
> - Since API version 26.0.0, XMP metadata of JPEG, PNG, GIF, DNG, and TIFF images can be read. For details
> about how to operate XMP metadata, see [XMPMetadata](arkts-image-image-xmpmetadata-c.md).&gt;
> - Since API version 26.0.0, AVIS metadata can be read. For details about the properties, see
> [AvisPropertyKey](arkts-image-image-avispropertykey-e.md).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataTypes | [MetadataType](arkts-image-image-metadatatype-e.md)[] | No |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageSource instance. This API uses an asynchronous callback to return the result.Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageSource instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## updateData

```TypeScript
updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>
```

Updates incremental data. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| isFinished | boolean | Yes |
| offset | number | Yes |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## updateData

```TypeScript
updateData(
      buf: ArrayBuffer,
      isFinished: boolean,
      offset: number,
      length: number,
      callback: AsyncCallback<void>
    ): void
```

Updates incremental data. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| isFinished | boolean | Yes |
| offset | number | Yes |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## writeImageMetadata

```TypeScript
writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>
```

Modifies image properties in batches. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Calling this API to modify properties alters the property byte length. You are advised to create an
> [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by passing a
> file descriptor or an
> [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by
> passing a URI.&gt;
> - This API modifies batch data in memory and writes the data to the file in a single operation. It is more
> efficient than
> [modifyImageProperties](#modifyimageproperties)
> .&gt;
> - This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information.
> Before modifying properties, use the **supportedFormats** property to check whether the device supports Exif
> information read/write in HEIF format.&gt;
> - Since API version 26.0.0, XMP metadata of JPEG, PNG, and GIF images can be read. For details about how to
> operate XMP metadata, see [XMPMetadata](arkts-image-image-xmpmetadata-c.md).&gt;
> - When calling the **writeImageMetadata** API to modify the **Exif** field, ensure that the corresponding
> image file has write permission. Otherwise, the field modification will fail.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageMetadata | [ImageMetadata](arkts-image-image-imagemetadata-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

Supported image formats.

**Type:** Array&lt;string&gt;

**Since:** 10

**System capability:** SystemCapability.Multimedia.Image.ImageSource
