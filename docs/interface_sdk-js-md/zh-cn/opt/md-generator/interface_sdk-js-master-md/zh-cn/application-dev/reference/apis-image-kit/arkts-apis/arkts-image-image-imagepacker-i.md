# ImagePacker

ImagePacker类，用于图片压缩和编码。 在调用ImagePacker的方法前，需要先通过[image.createImagePacker](arkts-image-image-createimagepacker-f.md#createImagePacker)构建一个ImagePacker实例。 编码期间，请避免修改或释放作为输入的ImageSource/PixelMap/Picture对象，以免出现crash或其他未定义行为。 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。 当前支持的格式有：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同，可通过ImagePacker的 supportedFormats属性查看）。

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-interface ImagePacker--><!--Device-image-interface ImagePacker-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

## packBinaryImageToTiffData

```TypeScript
packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>
```

将二值图像数据编码为TIFF数据，以ArrayBuffer的形式返回。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>--><!--Device-ImagePacker-packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | 是 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7800301](../errorcode-image.md#7800301-编码失败) |
| [7800202](../errorcode-image.md#7800202-imagepacker无效参数) |

## packBinaryImageToTiffFile

```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>
```

将二值图像数据编码到入参fd对应的TIFF文件。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>--><!--Device-ImagePacker-packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | 是 |
| fd | number | 是 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7800301](../errorcode-image.md#7800301-编码失败) |
| [7800202](../errorcode-image.md#7800202-imagepacker无效参数) |

## packToData

```TypeScript
packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToData

```TypeScript
packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。 > **注意：** > > 接口如果返回401错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToDataFromPixelmapSequence

```TypeScript
packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>
```

将多个PixelMap编码成GIF数据。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>--><!--Device-ImagePacker-packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | 是 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| fd | number | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToFile

```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>
```

指定编码参数，将ImageSource直接编码进文件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| fd | number | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将PixelMap直接编码进文件。使用callback异步回调。 > **注意：** > > 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| fd | number | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToFile

```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>
```

指定编码参数，将PixelMap直接编码进文件。使用Promise异步回调。 > **注意：** > > 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| fd | number | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

## packToFile

```TypeScript
packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>
```

指定编码参数，将Picture直接编码进文件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>--><!--Device-ImagePacker-packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | 是 |
| fd | number | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

## packToFileFromPixelmapSequence

```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>
```

指定编码参数，将多个PixelMap编码成GIF文件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>--><!--Device-ImagePacker-packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | 是 |
| fd | number | 是 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。 > **说明：** > > [packToData](#packToData)代替。

**起始版本：** 6

**废弃版本：** 13

**替代接口：** [packToData](#packToData)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | 是 |

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。 > **说明：** > > [packToData](#packToData)代替。

**起始版本：** 6

**废弃版本：** 13

**替代接口：** [packToData](#packToData)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。 > **说明：** > > [packToData](#packToData)代替。 > > **注意：** > > 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 8

**废弃版本：** 13

**替代接口：** [packToData](#packToData)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | 是 |

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。 > **说明：** > > [packToData](#packToData)代替。 > > **注意：** > > 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 8

**废弃版本：** 13

**替代接口：** [packToData](#packToData)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## packing

```TypeScript
packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>
```

将图像压缩或重新编码。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>--><!--Device-ImagePacker-packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放图片编码实例。使用callback异步回调。 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。 释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-release(callback: AsyncCallback<void>): void--><!--Device-ImagePacker-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放图片编码实例。使用Promise异步回调。 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。 释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-release(): Promise<void>--><!--Device-ImagePacker-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

图片编码支持的格式，包括：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同）。

**类型：** Array&lt;string&gt;

**起始版本：** 23

**废弃版本：** -1

<!--Device-ImagePacker-readonly supportedFormats: Array<string>--><!--Device-ImagePacker-readonly supportedFormats: Array<string>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker
