# ImageSource

The **ImageSource** class provides APIs to obtain image information. Before calling any API in ImageSource, you must use [image.createImageSource](arkts-image-image-createimagesource-f.md) to create an ImageSource instance. All APIs in ImageSource cannot be called concurrently. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface ImageSource--><!--Device-image-interface ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createImageRawData

```TypeScript
createImageRawData(): Promise<ImageRawData>
```

Obtains raw data from an image.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-createImageRawData(): Promise<ImageRawData>--><!--Device-ImageSource-createImageRawData(): Promise<ImageRawData>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageRawData](arkts-image-image-imagerawdata-i.md)&gt; | A Promise instance used to return image raw data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |

## createPicture

```TypeScript
createPicture(options?: DecodingOptionsForPicture): Promise<Picture>
```

Creates a Picture object based on decoding options. This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using a Picture instance, call [release](arkts-image-image-picture-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 13

<!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture>--><!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) | No | Decoding options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; | Promise used to return the Picture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Decode failed. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options. For example, unsupported desiredPixelFormat causes a failure in converting an image into the desired pixel format.<br>**Applicable version:** 24 and later |

## createPicture

```TypeScript
createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>
```

Creates a Picture object based on image decoding parameters. This method uses a promise to return the object.

**Since:** 23

<!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>--><!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) | No | Image decoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined&gt; | A Promise instance used to return the Picture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Failed to decode image. |

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index: int): Promise<Picture>
```

Creates a **Picture** object using a specified image (only GIF and HEIF&lt;sup&gt;23+&lt;/sup&gt; images currently). This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using a Picture instance, call [release](arkts-image-image-picture-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 20

<!--Device-ImageSource-createPictureAtIndex(index: int): Promise<Picture>--><!--Device-ImageSource-createPictureAtIndex(index: int): Promise<Picture>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the image. The value range is [0, Number of frames – 1]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; | Promise used to return the Picture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Decoding failed. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options. For example, index is invalid. |

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index : int): Promise<Picture | undefined>
```

Decodes an image at the specified index into a Picture object.

**Since:** 23

<!--Device-ImageSource-createPictureAtIndex(index : int): Promise<Picture | undefined>--><!--Device-ImageSource-createPictureAtIndex(index : int): Promise<Picture | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Image index. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined&gt; | Promise that returns the Picture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Decoding failed. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options. For example, index is invalid. |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses a promise to return the result. Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator) . This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap>--><!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Decoding options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>
```

Creates a PixelMap object based on image decoding parameters. This method uses a promise to return the object.

**Since:** 23

<!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>--><!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Image decoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | A Promise instance used to return the PixelMap object. |

## createPixelMap

```TypeScript
createPixelMap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object based on the default parameters. This API uses an asynchronous callback to return the result. Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator) . This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap>): void--><!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

## createPixelMap

```TypeScript
createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void
```

Creates a PixelMap object. This method uses a callback to return the object.

**Since:** 23

<!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void--><!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;PixelMap \| undefined&gt; | Yes | Callback used to return the PixelMap object. |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses an asynchronous callback to return the result. Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator) . This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void--><!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | Yes | Decoding options. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void
```

Creates a PixelMap object based on image decoding parameters. This method uses a callback to return the object.

**Since:** 23

<!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void--><!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | Yes | Image decoding parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;PixelMap \| undefined&gt; | Yes | Callback used to return the PixelMap object. |

## createPixelMapList

```TypeScript
createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>
```

Creates an array of PixelMap objects based on decoding options. This API uses a promise to return the result. For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image. &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed. &gt; &gt; - This function decodes all frames at once. If the number of frames is high or the size of individual frames is &gt; large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component &gt; for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this &gt; function.

**Since:** 23

<!--Device-ImageSource-createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>--><!--Device-ImageSource-createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Decoding options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PixelMap&gt;&gt; | Promise used to return an array of PixelMap objects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) | The shared memory data is abnormal. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980109](../errorcode-image.md#62980109-cropping-error) | Failed to crop the image. |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) | The DMA memory data is abnormal. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |

## createPixelMapList

```TypeScript
createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void
```

Creates an array of PixelMap objects based on the default parameters. This API uses an asynchronous callback to return the result. For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image. &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed. &gt; &gt; - This function decodes all frames at once. If the number of frames is high or the size of individual frames is &gt; large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component &gt; for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this &gt; function.

**Since:** 23

<!--Device-ImageSource-createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void--><!--Device-ImageSource-createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;PixelMap&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) | The shared memory data is abnormal. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980109](../errorcode-image.md#62980109-cropping-error) | Failed to crop the image. |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) | The DMA memory data is abnormal. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |

## createPixelMapList

```TypeScript
createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void
```

Creates an array of PixelMap objects based on decoding options. This API uses an asynchronous callback to return the result. For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image. &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed. &gt; &gt; - This function decodes all frames at once. If the number of frames is high or the size of individual frames is &gt; large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component &gt; for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this &gt; function.

**Since:** 23

<!--Device-ImageSource-createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void--><!--Device-ImageSource-createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | Yes | Decoding options. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;PixelMap&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980099](../errorcode-image.md#62980099-data-error-in-the-shared-memory) | The shared memory data is abnormal. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980109](../errorcode-image.md#62980109-cropping-error) | Failed to crop the image. |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980174](../errorcode-image.md#62980174-abnormal-dma-memory-data) | The DMA memory data is abnormal. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap
```

Creates a PixelMap object based on decoding options. This API returns the result synchronously. Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed. Starting from API version 15, you are advised to use [createPixelMapUsingAllocatorSync](#createpixelmapusingallocatorsync) . This API can be used to specify the memory type [AllocatorType](arkts-image-image-allocatortype-e.md) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). &gt; **NOTE：**&gt; &gt; This API operates synchronously and will block the current thread during execution. It should not be invoked &gt; from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For &gt; details, see &gt; [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 12

<!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap--><!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Decoding options. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap | undefined
```

Create a PixelMap object based on image decoding parameters synchronously.

**Since:** 23

<!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap | undefined--><!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Image decoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap \| undefined | Return the PixelMap. If decoding fails, return undefined. |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options and memory type. This API uses a promise to return the result. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). &gt; **NOTE：**&gt; &gt; - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance. &gt; &gt; - Images occupy a large amount of memory. When you finish using a PixelMap instance, call &gt; [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. &gt; &gt; - Before releasing the instance, ensure that all asynchronous operations associated with the instance have &gt; finished and the instance is no longer needed.

**Since:** 15

<!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>--><!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Decoding options. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Type of the memory. The default value is **AllocatorType.AUTO**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types; 3.Parameter verification failed. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported mimetype. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Failed to decode image. |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) | Failed to allocate memory. |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options, e.g, cannot convert image into desired pixel format. |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)
      : Promise<PixelMap | undefined>
```

Creates a PixelMap based on decoding parameters, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**Since:** 23

<!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)      : Promise<PixelMap | undefined>--><!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)      : Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Image decoding parameters. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Indicate which memory type will be used by the returned PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | A Promise instance used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported mimetype. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Failed to decode image. |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) | Failed to allocate memory. |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) | Unsupported allocator type. For example, use share memory to decode HDR image as only DMA supported HDR metadata. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options, For example, unsupported desiredPixelFormat causes a failure in converting an imagge into the desired pixel format. |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap
```

Creates a PixelMap object based on decoding options and memory type. This API returns the result synchronously. For details, see [Optimizing Memory for Image Decoding (ArkTS)](../../../media/image/image-allocator-type.md). Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-image-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed. &gt; **NOTE：**&gt; &gt; This API operates synchronously and will block the current thread during execution. It should not be invoked &gt; from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For &gt; details, see &gt; [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 15

<!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap--><!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Decoding options. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Type of the memory. The default value is **AllocatorType.AUTO**. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types; 3.Parameter verification failed. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported mimetype. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Failed to decode image. |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) | Failed to allocate memory. |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options, e.g, cannot convert image into desired pixel format. |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined
```

Creates a PixelMap based on decoding parameters synchronously, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**Since:** 23

<!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined--><!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | No | Image decoding parameters. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Indicate which memory type will be used by the returned PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap \| undefined | Return the PixelMap. If decoding fails, return undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Failed to decode image. |
| [7700302](../errorcode-image.md#7700302-memory-allocation-failed) | Failed to allocate memory. |
| [7700201](../errorcode-image.md#7700201-unsupported-memory-allocation-type) | Unsupported allocator type. For example, use share memory to decode HDR image as only DMA supported HDR metadata. |
| [7700203](../errorcode-image.md#7700203-unsupported-options) | Unsupported options, For example, unsupported desiredPixelFormat cause a failure in converting an image into the desired pixel format. |

## createThumbnail

```TypeScript
createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>
```

Creates a thumbnail image based on image decoding parameters. This method uses a promise to return the PixelMap object, which represents the thumbnail.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>--><!--Device-ImageSource-createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | No | Image decoding parameters for creating the thumbnail. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | A Promise instance used to return the PixelMap object representing the thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported mimetype. |
| [7700305](../errorcode-image.md#7700305-thumbnail-generation-failed) | Thumbnail generation failed. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Decode failed. |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Invalid parameter, e.g, invalid generate size. |
| [7700303](../errorcode-image.md#7700303-image-does-not-contain-thumbnail-data) | Image does not carry thumbnail data. |

## createThumbnailSync

```TypeScript
createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined
```

Synchronously creates a thumbnail image based on image decoding parameters. This method returns a `PixelMap` object, which represents the generated thumbnail.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined--><!--Device-ImageSource-createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | No | Image decoding parameters for creating the thumbnail. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap \| undefined | The PixelMap object representing the generated thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700103](../errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported mimetype. |
| [7700305](../errorcode-image.md#7700305-thumbnail-generation-failed) | Thumbnail generation failed. |
| [7700301](../errorcode-image.md#7700301-decoding-failure) | Decode failed. |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Invalid parameter, e.g, invalid generate size. |
| [7700303](../errorcode-image.md#7700303-image-does-not-contain-thumbnail-data) | Image does not carry thumbnail data. |

## getDelayTimeList

```TypeScript
getDelayTimeList(): Promise<Array<int>>
```

Obtains an array of delay times. This API uses a promise to return the result. This API applies only to images in GIF or WebP format.

**Since:** 23

<!--Device-ImageSource-getDelayTimeList(): Promise<Array<int>>--><!--Device-ImageSource-getDelayTimeList(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | Promise used to return an array of delay times. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) | Invalid MIME type for the image source. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) | Failed to decode the image header. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) | The image source data is incorrect. |

## getDelayTimeList

```TypeScript
getDelayTimeList(callback: AsyncCallback<Array<int>>): void
```

Obtains an array of delay times. This API uses an asynchronous callback to return the result. This API applies only to images in GIF or WebP format.

**Since:** 23

<!--Device-ImageSource-getDelayTimeList(callback: AsyncCallback<Array<int>>): void--><!--Device-ImageSource-getDelayTimeList(callback: AsyncCallback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;int&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the array of delay times obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) | Invalid MIME type for the image source. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) | Failed to decode the image header. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) | The image source data is incorrect. |

## getDisposalTypeList

```TypeScript
getDisposalTypeList(): Promise<Array<int>>
```

Obtains the list of disposal types. This API uses a promise to return the result. It is used only for GIF images.

**Since:** 23

<!--Device-ImageSource-getDisposalTypeList(): Promise<Array<int>>--><!--Device-ImageSource-getDisposalTypeList(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | Promise used to return an array of disposal types. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980149](../errorcode-image.md#62980149-invalid-image-parameter) | Invalid MIME type for the image source. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |

## getFrameCount

```TypeScript
getFrameCount(): Promise<int>
```

Obtains the number of frames. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImageSource-getFrameCount(): Promise<int>--><!--Device-ImageSource-getFrameCount(): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the number of frames. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) | The image format does not match. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) | Failed to decode the image header. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |

## getFrameCount

```TypeScript
getFrameCount(callback: AsyncCallback<int>): void
```

Obtains the number of frames. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImageSource-getFrameCount(callback: AsyncCallback<int>): void--><!--Device-ImageSource-getFrameCount(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of frames obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) | The image format does not match. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid media operation. |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) | Failed to decode the image header. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |

## getImageInfo

```TypeScript
getImageInfo(index: int, callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information with the specified index. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo>): void--><!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

## getImageInfo

```TypeScript
getImageInfo(index: int, callback: AsyncCallback<ImageInfo | undefined>): void
```

Obtains information about an image with the specified sequence number and uses a callback to return the result.

**Since:** 23

<!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo | undefined>): void--><!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Sequence number of an image. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined&gt; | Yes | Callback used to return the image information. |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo>): void--><!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void
```

Obtains information about this image and uses a callback to return the result.

**Since:** 23

<!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void--><!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined&gt; | Yes | Callback used to return the image information. |

## getImageInfo

```TypeScript
getImageInfo(index?: int): Promise<ImageInfo>
```

Obtains the image information. This API uses a promise to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo>--><!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Promise used to return the image information. |

## getImageInfo

```TypeScript
getImageInfo(index?: int): Promise<ImageInfo | undefined>
```

Get image information from image source.

**Since:** 23

<!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo | undefined>--><!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | Sequence number of an image. If this parameter is not specified, the default value 0 is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined&gt; | A Promise instance used to return the image information. |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: int): ImageInfo
```

Obtains the image information with the specified index. This API returns the result synchronously. &gt; **NOTE：**&gt; &gt; This API operates synchronously and will block the current thread during execution. It should not be invoked &gt; from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For &gt; details, see &gt; [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 12

<!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo--><!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) | Image information. |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: int): ImageInfo | undefined
```

Get image information from image source synchronously.

**Since:** 23

<!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo | undefined--><!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | Index of sequence image. If this parameter is specified, default value is 0 <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined | The image information. |

## getImageProperties

```TypeScript
getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>
```

Obtains the values of properties with the given names in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/sup&gt;format and contain Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 12

<!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>--><!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | Array&lt;PropertyKey&gt; | Yes | Array of properties names. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;PropertyKey, string \| null&gt;&gt; | Promise used to return the property values. If the operation fails, **null** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2 .Incorrect parameter types; 3.Parameter verification failed; |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) | The image source data is incorrect. |

## getImageProperties

```TypeScript
getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>
```

Obtains the value of properties in an image. This method uses a promise to return the property values in array of records.

**Since:** 23

<!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>--><!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | Array&lt;PropertyKey&gt; | Yes | Name of the properties whose value is to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; | Array of Records instance used to return the property values. If the operation fails, the null is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980116](../errorcode-image.md#62980116-decoding-failure) | Failed to decode the image. |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) | The image source data is incorrect. |

## getImageProperty

```TypeScript
getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>
```

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/ sup&gt; format and contain Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 23

<!--Device-ImageSource-getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>--><!--Device-ImageSource-getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | PropertyKey | Yes | Name of the property. |
| options | [ImagePropertyOptions](arkts-image-image-imagepropertyoptions-i.md) | No | Image properties, including the image index and default property value. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the property value. If the operation fails, the default value is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2 .Incorrect parameter types;3.Parameter verification failed; |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980112](../errorcode-image.md#62980112-image-format-mismatch) | The image format does not match. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) | The EXIF value is invalid. |
| [62980118](../errorcode-image.md#62980118-plugin-creation-failure) | Failed to create the image plugin. |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) | The image does not support EXIF decoding. |
| [62980122](../errorcode-image.md#62980122-failure-in-decoding-the-image-header) | Failed to decode the image header. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980110](../errorcode-image.md#62980110-incorrect-image-source-data) | The image source data is incorrect. |

## getImageProperty

```TypeScript
getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>
```

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>--><!--Device-ImageSource-getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Name of the property. |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | No | Image properties, including the image index and default property value. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the property value. If the operation fails, the default value is returned. |

## getImageProperty

```TypeScript
getImageProperty(key: string, callback: AsyncCallback<string>): void
```

Obtains the value of a property with the specified index in this image. This API uses an asynchronous callback to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, callback: AsyncCallback<string>): void--><!--Device-ImageSource-getImageProperty(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Name of the property. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object. |

## getImageProperty

```TypeScript
getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void
```

Obtains the value of a property in this image. This API uses an asynchronous callback to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.)

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void--><!--Device-ImageSource-getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Name of the property. |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | Yes | Image properties, including the image index and default property value. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object. |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string
```

Obtains the value of a specified Exif property. This API returns the result synchronously. &gt; **NOTE：**&gt; &gt; - This API applies only to images that are in JPEG, PNG, HEIF, WEBP&lt;sup&gt;23+&lt;/sup&gt;, or DNG&lt;sup&gt;23+&lt;/sup&gt;format &gt; and contain Exif information. (The supported formats may vary depending on the hardware.) &gt; &gt; - Exif information is metadata of the image, including shooting time, camera model, aperture, focal length, and &gt; ISO. &gt; &gt; - This API operates synchronously and will block the current thread during execution. It should not be invoked &gt; from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For &gt; details, see &gt; [Overview of Concurrency in Time-Consuming Tasks](../../../arkts-utils/time-consuming-task-overview.md).

**Since:** 20

<!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string--><!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | PropertyKey | Yes | Name of the property. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the specified Exif property. If retrieval fails, the default value of the property is returned. For details about the meaning of each data value, see [PropertyKey]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. For example, key is not supported. |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string | undefined
```

Obtains the value of a property in the image.

**Since:** 23

<!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string | undefined--><!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | PropertyKey | Yes | Property name. |

**Return value:**

| Type | Description |
| --- | --- |
| string \| undefined | Value of the property. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. For example, key is not supported. |

## modifyImageProperties

```TypeScript
modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>
```

Modifies the values of properties in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; The property byte length is changed when the **modifyImageProperties** API is called to modify the values of &gt; properties. Currently, you can call the API in an ImageSource instance created based on a file descriptor or &gt; path, but not an ImageSource instance created based on buffers.

**Since:** 12

<!--Device-ImageSource-modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | Record&lt;PropertyKey, string \| null&gt; | Yes | Array of property names and property values. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2 .Incorrect parameter types; 3.Parameter verification failed; |
| [62980146](../errorcode-image.md#62980146-failed-to-write-image-property-values-to-the-file) | The EXIF data failed to be written to the file. |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) | The EXIF value is invalid. |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) | The image does not support EXIF decoding. |

## modifyImageProperties

```TypeScript
modifyImageProperties(records: Record<string, string|null>): Promise<void>
```

Modify the value of properties in an image with the specified keys.

**Since:** 23

<!--Device-ImageSource-modifyImageProperties(records: Record<string, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageProperties(records: Record<string, string|null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | Record&lt;string, string \| null&gt; | Yes | Array of the property Records whose values are to be modified. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980146](../errorcode-image.md#62980146-failed-to-write-image-property-values-to-the-file) | The EXIF data failed to be written to the file. |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) | The EXIF value is invalid. |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) | The image does not support EXIF decoding. |

## modifyImagePropertiesEnhanced

```TypeScript
modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>
```

Modifies image properties in batches. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; - Calling this API to modify properties alters the property byte length. You are advised to create an &gt; [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by passing a &gt; file descriptor or an &gt; [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by &gt; passing a URI. &gt; &gt; - This API modifies batch data in memory and writes the data to the file in a single operation. It is more &gt; efficient than &gt; [modifyImageProperties](#modifyimageproperties) &gt; . &gt; &gt; - This API applies only to images that are in JPEG, PNG, HEIF, or WEBP format and contain the Exif information.

**Since:** 23

<!--Device-ImageSource-modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>--><!--Device-ImageSource-modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | Record&lt;string, string \| null&gt; | Yes | Key-value pairs of image property names and property values. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700304](../errorcode-image.md#7700304-failed-to-write-image-information-to-the-file) | Failed to write image properties to the file. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: PropertyKey, value: string): Promise<void>
```

Modifies the value of a property in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a &gt; property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path &gt; , but not an ImageSource instance created based on buffers.

**Since:** 23

<!--Device-ImageSource-modifyImageProperty(key: PropertyKey, value: string): Promise<void>--><!--Device-ImageSource-modifyImageProperty(key: PropertyKey, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | PropertyKey | Yes | Name of the property. |
| value | string | Yes | New value of the property. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2 .Incorrect parameter types; |
| [62980146](../errorcode-image.md#62980146-failed-to-write-image-property-values-to-the-file) | The EXIF data failed to be written to the file. |
| [62980133](../errorcode-image.md#62980133-image-property-value-out-of-range) | The EXIF data is out of range. |
| [62980135](../errorcode-image.md#62980135-invalid-image-property-value) | The EXIF value is invalid. |
| [62980123](../errorcode-image.md#62980123-exif-decoding-not-supported) | The image does not support EXIF decoding. |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string): Promise<void>
```

Modifies the value of a property in this image. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a &gt; property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path &gt; , but not an ImageSource instance created based on buffers.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

<!--Device-ImageSource-modifyImageProperty(key: string, value: string): Promise<void>--><!--Device-ImageSource-modifyImageProperty(key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Name of the property. |
| value | string | Yes | New value of the property. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void
```

Modifies the value of a property in this image. This API uses an asynchronous callback to return the result. This API applies only to images that are in JPEG, PNG, HEIF&lt;sup&gt;12+&lt;/sup&gt;, or WEBP&lt;sup&gt;23+&lt;/sup&gt; format and contain the Exif information. (The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a &gt; property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path &gt; , but not an ImageSource instance created based on buffers.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

<!--Device-ImageSource-modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-ImageSource-modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Name of the property. |
| value | string | Yes | New value of the property. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## readImageMetadata

```TypeScript
readImageMetadata(propertyKeys?: string[], index?: int): Promise<ImageMetadata>
```

Reads image metadata. You can use **propertyKeys** to specify the keys of metadata. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF, WEBP, or DNG format and contain Exif information. ( The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; When reading a DNG image, this API applies special handling to some **propertyKeys**. For details about the &gt; values of the following properties, see [PropertyKey](arkts-image-image-propertykey-e.md): &gt; &gt; - **NewSubfileType**, **ImageWidth**, **ImageLength**, **DefaultCropSize**, **Orientation**, **Compression**, &gt; **PhotometricInterpretation**, **PlanarConfiguration**, **RowsPerStrip**, **StripOffsets**, **StripByteCounts** &gt; , **SamplesPerPixel**, **BitsPerSample**, **YCbCrCoefficients**, **YCbCrSubSampling**, **YCbCrPositioning**, &gt; **ReferenceBlackWhite**, **XResolution**, **YResolution**, and **ResolutionUnit**: For these properties, values &gt; related to the main image are returned. &gt; &gt; - **ImageUniqueID**: The value is verified based on the specifications. If the value fails to comply with the &gt; specifications, an empty string is returned. &gt; &gt; - **ExifVersion**, **FlashpixVersion**, and **ColorSpace**: If the image does not contain these properties, an &gt; error code is returned. &gt; &gt; - **DNGVersion**: If the value is earlier than **1.0.0.0**, **1.0.0.0** is returned. &gt; &gt; - **GPSVersionID**: If there is no valid GPS data, the GPS version number is cleared and **0** is returned. &gt; &gt; - **GPSAltitudeRef**: If **GPSAltitude** is not set, this property is set to **0xFFFFFFFF**. &gt; &gt; - **ISOSpeedRatings**: If its value is **0** or **65535**, the recommended exposure index is used first. If the &gt; recommended exposure index does not exist, the standard output sensitivity, ISO speed, and exposure index are &gt; used in sequence.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-readImageMetadata(propertyKeys?: string[], index?: int): Promise<ImageMetadata>--><!--Device-ImageSource-readImageMetadata(propertyKeys?: string[], index?: int): Promise<ImageMetadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propertyKeys | string[] | No | Array of properties names. If **propertyKeys** is not specified, all supported metadata is returned. |
| index | int | No | Index of the property to be obtained. The default value is **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; | Promise used to return the **ImageMetadata** object, which contains the metadata object corresponding to the image property name. You can obtain the image property values through this metadata object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Invalid parameter. Possible causes: 1. The index is negative. 2. The index is greater than or equal to the number of frames in the image. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. |

## readImageMetadataByType

```TypeScript
readImageMetadataByType(metadataTypes?: MetadataType[], index?: int): Promise<ImageMetadata>
```

Reads the metadata of an image source. You can use **metadataTypes** to specify the metadata types. If **metadataTypes** is not specified, all supported metadata is returned. This API uses a promise to return the result. This API applies only to images that are in JPEG, PNG, HEIF, WEBP, DNG, or HEIFS format. (The supported formats may vary depending on the hardware.) &gt; **NOTE：**&gt; &gt; - **EXIF_METADATA** applies to JPEG, PNG, HEIF, WEBP, and DNG images. &gt; &gt; - **HEIFS_METADATA** applies to HEIFS images. &gt; &gt; - If the input **MetadataType** does not match the image format, error code **7700102** will be returned.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-readImageMetadataByType(metadataTypes?: MetadataType[], index?: int): Promise<ImageMetadata>--><!--Device-ImageSource-readImageMetadataByType(metadataTypes?: MetadataType[], index?: int): Promise<ImageMetadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataTypes | [MetadataType](arkts-image-image-metadatatype-e.md)[] | No | Metadata type array. If this parameter is left empty, all supported metadata is obtained. |
| index | int | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; | Promise used to return the **ImageMetadata** object, which contains the corresponding metadata object. You can obtain the image property values through this metadata object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Invalid parameter. Possible causes: 1.The index is negative. 2. The index is greater than or equal to the number of frames in the image. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageSource instance. This API uses an asynchronous callback to return the result. Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ImageSource-release(callback: AsyncCallback<void>): void--><!--Device-ImageSource-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageSource instance. This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ImageSource-release(): Promise<void>--><!--Device-ImageSource-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## updateData

```TypeScript
updateData(buf: ArrayBuffer, isFinished: boolean, offset: int, length: int): Promise<void>
```

Updates incremental data. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImageSource-updateData(buf: ArrayBuffer, isFinished: boolean, offset: int, length: int): Promise<void>--><!--Device-ImageSource-updateData(buf: ArrayBuffer, isFinished: boolean, offset: int, length: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | Buffer for storing the incremental data. |
| isFinished | boolean | Yes | Whether data update is complete. The value **true** means that the data update is complete and the last segment of data is stored in the buffer. The value **false** means that the data update is still in progress. |
| offset | int | Yes | Offset of the data in the buffer, measured from the start of the entire image file, in bytes.<br>**Since:** 11 |
| length | int | Yes | Length of the buffer, in bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## updateData

```TypeScript
updateData(
      buf: ArrayBuffer,
      isFinished: boolean,
      offset: int,
      length: int,
      callback: AsyncCallback<void>
    ): void
```

Updates incremental data. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImageSource-updateData(      buf: ArrayBuffer,      isFinished: boolean,      offset: int,      length: int,      callback: AsyncCallback<void>    ): void--><!--Device-ImageSource-updateData(      buf: ArrayBuffer,      isFinished: boolean,      offset: int,      length: int,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | Buffer for storing the incremental data. |
| isFinished | boolean | Yes | Whether data update is complete. The value **true** means that the data update is complete and the last segment of data is stored in the buffer. The value **false** means that the data update is still in progress. |
| offset | int | Yes | Offset of the data in the buffer, measured from the start of the entire image file, in bytes.<br>**Since:** 11 |
| length | int | Yes | Length of the buffer, in bytes. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## writeImageMetadata

```TypeScript
writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>
```

Modifies image properties in batches. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; - Calling this API to modify properties alters the property byte length. You are advised to create an &gt; [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by passing a &gt; file descriptor or an &gt; [image.createImageSource](arkts-image-image-createimagesource-f.md) instance by &gt; passing a URI. &gt; &gt; - This API modifies batch data in memory and writes the data to the file in a single operation. It is more &gt; efficient than &gt; [modifyImageProperties](#modifyimageproperties) &gt; . &gt; &gt; - This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information. &gt; Before modifying properties, use the **supportedFormats** property to check whether the device supports Exif &gt; information read/write in HEIF format.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>--><!--Device-ImageSource-writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageMetadata | [ImageMetadata](arkts-image-image-imagemetadata-i.md) | Yes | Image metadata set. If all property values in **imageMetadata** are empty, all Exif metadata is cleared. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Invalid parameter. Possible causes: The imageSource object is released. |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

Supported image formats.

**Type:** Array&lt;string&gt;

**Since:** 23

<!--Device-ImageSource-readonly supportedFormats: Array<string>--><!--Device-ImageSource-readonly supportedFormats: Array<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

