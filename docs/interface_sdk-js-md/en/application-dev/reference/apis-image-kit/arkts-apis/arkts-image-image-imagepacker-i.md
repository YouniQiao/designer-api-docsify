# ImagePacker

The **ImagePacker** class provides APIs to compress and encode images.

Before calling any API in ImagePacker, you must use [image.createImagePacker](arkts-image-image-createimagepacker-f.md) to create an ImagePacker instance. During encoding, do not modify or release the ImageSource, PixelMap, or Picture object that is being used as the input. Otherwise, a crash or other undefined behavior may occur.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

Currently, the following formats are supported: jpeg, webp, png, heic&lt;sup&gt;12+&lt;/sup&gt;, and gif&lt;sup&gt;18+&lt;/sup&gt;. (The supported formats may vary depending on the hardware. You can refer to the **supportedFormats** property of ImagePacker to see which ones are supported.)

**Since:** 23

<!--Device-image-interface ImagePacker--><!--Device-image-interface ImagePacker-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## packBinaryImageToTiffData

```TypeScript
packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>
```

Compresses or packs an image into a file and uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>--><!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes | image buffer info. |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No | Options for tiff image packing. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | A Promise instance used to return the compressed or packed data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7800202](../errorcode-image.md#7800202-invalid-imagepacker-parameter) | Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm mismatch. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Encode failed. |

## packBinaryImageToTiffFile

```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>
```

Compresses or packs an image into a file and uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>--><!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes | image buffer info. |
| fd | int | Yes | ID of a file descriptor <br>The value must be a positive integer. |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No | Options for tiff image packing. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7800202](../errorcode-image.md#7800202-invalid-imagepacker-parameter) | Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm mismatch. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Encode failed. |

## packToData

```TypeScript
packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | ImageSource | Yes | Image source to compress or re-encode. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the compressed or encoded image data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | If the parameter is invalid. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToData

```TypeScript
packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

> **NOTE：**
> 
> If error code 401 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is
> released in advance. You need to check the code and ensure that the PixelMap object is released after this API
> is called.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | PixelMap | Yes | PixelMap to compress or re-encode. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the compressed or encoded image data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | If the parameter is invalid. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToDataFromPixelmapSequence

```TypeScript
packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>
```

Encodes multiple PixelMap objects into GIF data. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | Yes | PixelMaps to encode. |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes | Options for encoding animated images. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the encoded data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Failed to encode image. |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

Encodes the image source into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | ImageSource | Yes | Image source to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>
```

Encodes the image source into a file based on the specified encoding parameters. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | ImageSource | Yes | Image source to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
> object is released in advance. You need to check the code and ensure that the PixelMap object is released after
> this API is called.

**Since:** 23

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | PixelMap | Yes | PixelMap to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>
```

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses a promise to return the result.

> **NOTE：**
> 
> If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
> object is released in advance. You need to check the code and ensure that the PixelMap object is released after
> this API is called.

**Since:** 23

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | PixelMap | Yes | PixelMap to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) | Failed to encode the image. |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) | Add pixelmap out of range. |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) | Failed to encode icc. |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) | Failed to create surface. |

## packToFile

```TypeScript
packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>
```

Encodes the Picture into a file based on the specified encoding parameters. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes | Picture to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Encode failed. |

## packToFileFromPixelmapSequence

```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>
```

Encodes multiple PixelMaps into a GIF file. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>--><!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | Yes | PixelMaps to encode. |
| fd | int | Yes | File descriptor. |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes | Options for encoding animated images. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types;3.Parameter verification failed. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Failed to encode image. |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | ImageSource | Yes | Image source to compress or re-encode. |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;ArrayBuffer&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err** is an error object. |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | ImageSource | Yes | Image source to compress or re-encode. |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the compressed or encoded image data. |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
> PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
> released after this API is called.

**Since:** 8

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | PixelMap | Yes | PixelMap to compress or re-encode. |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;ArrayBuffer&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err** is an error object. |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

> **NOTE：**
> 
> If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
> PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
> released after this API is called.

**Since:** 8

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | PixelMap | Yes | PixelMap to compress or re-encode. |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the compressed or encoded image data. |

## packing

```TypeScript
packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes | Picture to compress or re-encode. |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | Encoding parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the compressed or encoded image data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7800301](../errorcode-image.md#7800301-encoding-failure) | Encode failed. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImagePacker instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImagePacker-release(callback: AsyncCallback<void>): void--><!--Device-ImagePacker-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImagePacker instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImagePacker-release(): Promise<void>--><!--Device-ImagePacker-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

Supported formats for image encoding, including jpeg, webp, png, heic&lt;sup&gt;12+&lt;/sup&gt;, and gif&lt;sup&gt;18+&lt;/sup&gt;. (The supported formats may vary depending on the hardware.)

**Type:** Array&lt;string&gt;

**Since:** 23

<!--Device-ImagePacker-readonly supportedFormats: Array<string>--><!--Device-ImagePacker-readonly supportedFormats: Array<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

