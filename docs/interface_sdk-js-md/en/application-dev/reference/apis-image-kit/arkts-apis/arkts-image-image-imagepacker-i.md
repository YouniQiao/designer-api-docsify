# ImagePacker

ImagePacker类，用于图片压缩和编码。

在调用ImagePacker的方法前，需要先通过[image.createImagePacker](arkts-image-image-createimagepacker-f.md#createimagepacker)构建一个ImagePacker实例。

编码期间，请避免修改或释放作为输入的ImageSource/PixelMap/Picture对象，以免出现crash或其他未定义行为。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](arkts-image-image-imagepacker-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

当前支持的格式有：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同，可通过ImagePacker的supportedFormats属性查看）。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface ImagePacker--><!--Device-image-interface ImagePacker-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## packBinaryImageToTiffData

```TypeScript
packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>
```

将二值图像数据编码为TIFF数据，以ArrayBuffer的形式返回。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>--><!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes | 图像缓冲区信息。 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No | TIFF图像编码选项。 &lt;br&gt;未传入options时，默认的compression为4（CCITT G4）。 &lt;br&gt;未传入options时，默认的orientation为1（TOP_LEFT），表示图像未旋转。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回编码后的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7800301 | Encode failed. |
| 7800202 | Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm mismatch. |

## packBinaryImageToTiffFile

ArkTS-Dyn:
```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>
```

ArkTS-Sta:
```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>
```

将二值图像数据编码到入参fd对应的TIFF文件。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>--><!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | Yes | 图像缓冲区信息。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符ID。该值必须为正整数。 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | No | TIFF图像编码选项。 &lt;br&gt;未传入options时，默认的compression为4（CCITT G4）。 &lt;br&gt;未传入options时，默认的orientation为1（TOP_LEFT），表示图像未旋转。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7800301 | Encode failed. |
| 7800202 | Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm mismatch. |

## packToData

```TypeScript
packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes | 编码的ImageSource。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToData

```TypeScript
packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **注意：**
> 
> 接口如果返回401错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | 编码的PixelMap源。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToDataFromPixelmapSequence

```TypeScript
packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>
```

将多个PixelMap编码成GIF数据。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | Yes | 待编码的PixelMap序列。 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes | 动图编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回编码后的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes | 编码的ImageSource。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当编码进文件成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将ImageSource直接编码进文件。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes | 编码的ImageSource。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将PixelMap直接编码进文件。使用callback异步回调。

> **注意：**
> 
> 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | 编码的PixelMap资源。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当编码图片进文件成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将PixelMap直接编码进文件。使用Promise异步回调。

> **注意：**
> 
> 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | 编码的PixelMap资源。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980101 | The image data is abnormal. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将Picture直接编码进文件。使用Promise异步回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes | 编码的Picture资源。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

## packToFileFromPixelmapSequence

ArkTS-Dyn:
```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>
```

指定编码参数，将多个PixelMap编码成GIF文件。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>--><!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | Yes | 待编码的PixelMap序列。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。取值范围为[0，65535]。 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | Yes | 动图编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types;3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。

> **说明：**
> 
> [packToData](arkts-image-image-imagepacker-i.md#packtodata)代替。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 13

**Substitutes:** [image.ImagePacker#packToData](arkts-image-image-imagepacker-i.md#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes | 编码的ImageSource。 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **说明：**
> 
> [packToData](arkts-image-image-imagepacker-i.md#packtodata)代替。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 13

**Substitutes:** [image.ImagePacker#packToData](arkts-image-image-imagepacker-i.md#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Yes | 编码的ImageSource。 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。

> **说明：**
> 
> [packToData](arkts-image-image-imagepacker-i.md#packtodata)代替。
> > **注意：**
> 
> 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 13

**Substitutes:** [image.ImagePacker#packToData](arkts-image-image-imagepacker-i.md#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | 编码的PixelMap资源。 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **说明：**
> 
> [packToData](arkts-image-image-imagepacker-i.md#packtodata)代替。
> > **注意：**
> 
> 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 13

**Substitutes:** [image.ImagePacker#packToData](arkts-image-image-imagepacker-i.md#packtodata)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | 编码的PixelMap源。 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |

## packing

```TypeScript
packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>
```

将图像压缩或重新编码。使用Promise异步回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | Yes | 编码的Picture对象。 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | Yes | 设置编码参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放图片编码实例。使用callback异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-ImagePacker-release(callback: AsyncCallback<void>): void--><!--Device-ImagePacker-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当释放图片编码实例成功，err为undefined，否则为错误对象。 |

## release

```TypeScript
release(): Promise<void>
```

释放图片编码实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-ImagePacker-release(): Promise<void>--><!--Device-ImagePacker-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

图片编码支持的格式，包括：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同）。

**Type:** Array&lt;string&gt;

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-ImagePacker-readonly supportedFormats: Array<string>--><!--Device-ImagePacker-readonly supportedFormats: Array<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

