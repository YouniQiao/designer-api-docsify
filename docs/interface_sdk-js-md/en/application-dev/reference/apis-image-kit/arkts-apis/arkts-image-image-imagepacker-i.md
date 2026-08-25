# ImagePacker

The **ImagePacker** class provides APIs to compress and encode images.Before calling any API in ImagePacker, you must use [image.createImagePacker](arkts-image-image-createimagepacker-f.md) to create an ImagePacker instance. During encoding, do not modify or release the ImageSource, PixelMap, or Picture object that is being used as the input. Otherwise, a crash or other undefined behavior may occur.Images occupy a large amount of memory. When you finish using an ImagePacker instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.Currently, the following formats are supported: jpeg, webp, png, heic&lt;sup&gt;12+&lt;/sup&gt;, and gif&lt;sup&gt;18+&lt;/sup&gt;. (The supported formats may vary depending on the hardware. You can refer to the **supportedFormats** property of ImagePacker to see which ones are supported.)

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## packBinaryImageToTiffData

```TypeScript
packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>
```

Compresses or packs an image into a file and uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7800202](../errorcode-image.md#7800202-invalid-imagepacker-parameter) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## packBinaryImageToTiffFile

```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>
```

Compresses or packs an image into a file and uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7800202](../errorcode-image.md#7800202-invalid-imagepacker-parameter) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
> PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
> released after this API is called.

**Since:** 8

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
> PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
> released after this API is called.

**Since:** 8

**Deprecated since:** 13

**Substitutes:** [packToData](#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## packing

```TypeScript
packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## packToData

```TypeScript
packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToData

```TypeScript
packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>
```

Compresses or re-encodes an image. This API uses a promise to return the result.

> **NOTE：**&gt;
> If error code 401 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is
> released in advance. You need to check the code and ensure that the PixelMap object is released after this API
> is called.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToDataFromPixelmapSequence

```TypeScript
packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>
```

Encodes multiple PixelMap objects into GIF data. This API uses a promise to return the result.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | Yes |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

Encodes the image source into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>
```

Encodes the image source into a file based on the specified encoding parameters. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
> object is released in advance. You need to check the code and ensure that the PixelMap object is released after
> this API is called.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>
```

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses a promise to return the result.

> **NOTE：**&gt;
> If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
> object is released in advance. You need to check the code and ensure that the PixelMap object is released after
> this API is called.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) |
| [62980113](../errorcode-image.md#62980113-unknown-image-format) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980119](../errorcode-image.md#62980119-image-encoding-failure) |
| [62980120](../errorcode-image.md#62980120-failure-in-adding-pixel-mappings) |
| [62980172](../errorcode-image.md#62980172-failed-to-encode-icc) |
| [62980252](../errorcode-image.md#62980252-failed-to-create-a-surface) |

## packToFile

```TypeScript
packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>
```

Encodes the Picture into a file based on the specified encoding parameters. This API uses a promise to return the result.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes |
| fd | number | Yes |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## packToFileFromPixelmapSequence

```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>
```

Encodes multiple PixelMaps into a GIF file. This API uses a promise to return the result.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | Yes |
| fd | number | Yes |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7800301](../errorcode-image.md#7800301-encoding-failure) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImagePacker instance. This API uses an asynchronous callback to return the result.Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImagePacker instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

Supported formats for image encoding, including jpeg, webp, png, heic&lt;sup&gt;12+&lt;/sup&gt;, and gif&lt;sup&gt;18+&lt;/sup&gt;. (The supported formats may vary depending on the hardware.)

**Type:** Array&lt;string&gt;

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImagePacker
