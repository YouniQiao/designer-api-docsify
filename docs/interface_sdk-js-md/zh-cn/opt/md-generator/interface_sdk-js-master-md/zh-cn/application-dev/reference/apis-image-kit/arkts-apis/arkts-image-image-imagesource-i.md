# ImageSource

ImageSource类，用于获取图片相关信息。 在调用ImageSource的方法前，需要先通过[image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)构建一个ImageSource实例。 ImageSource的所有方法均不支持并发调用。 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-image-interface ImageSource--><!--Device-image-interface ImageSource-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

## 导入模块

```TypeScript
```

## createImageRawData

```TypeScript
createImageRawData(): Promise<ImageRawData>
```

获取图片原始数据。使用Promise异步回调。目前仅支持获取DNG图片类型的原始数据。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-createImageRawData(): Promise<ImageRawData>--><!--Device-ImageSource-createImageRawData(): Promise<ImageRawData>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageRawData](arkts-image-image-imagerawdata-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |

## createPicture

```TypeScript
createPicture(options?: DecodingOptionsForPicture): Promise<Picture>
```

通过图片解码参数创建Picture对象。使用Promise异步回调。 由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法，及时释放内存。 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 13

<!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture>--><!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPicture

```TypeScript
createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>
```

Creates a Picture object based on image decoding parameters. This method uses a promise to return the object.

**起始版本：** 23

<!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>--><!--Device-ImageSource-createPicture(options?: DecodingOptionsForPicture): Promise<Picture | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700301](../errorcode-image.md#7700301-解码失败) |

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index: number): Promise<Picture>
```

通过指定序号的图片创建Picture对象。使用Promise异步回调。 > **说明：** > > - 支持GIF和HEIF&lt;sup&gt;23+&lt;/sup&gt;图像序列格式。从API版本26.0.0开始，增加支持AVIS格式。 > > - 由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 20

<!--Device-ImageSource-createPictureAtIndex(index: int): Promise<Picture>--><!--Device-ImageSource-createPictureAtIndex(index: int): Promise<Picture>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index : number): Promise<Picture | undefined>
```

Decodes an image at the specified index into a Picture object.

**起始版本：** 23

<!--Device-ImageSource-createPictureAtIndex(index : int): Promise<Picture | undefined>--><!--Device-ImageSource-createPictureAtIndex(index : int): Promise<Picture | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap>
```

通过图片解码参数创建PixelMap对象。使用Promise异步回调。 从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md#createpixelmapusingallocator)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md#allocatortype)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap>--><!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>
```

Creates a PixelMap object based on image decoding parameters. This method uses a promise to return the object.

**起始版本：** 23

<!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>--><!--Device-ImageSource-createPixelMap(options?: DecodingOptions): Promise<PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

## createPixelMap

```TypeScript
createPixelMap(callback: AsyncCallback<PixelMap>): void
```

通过默认参数创建PixelMap对象。使用callback异步回调。 从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md#createpixelmapusingallocator)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md#allocatortype)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap>): void--><!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

## createPixelMap

```TypeScript
createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void
```

Creates a PixelMap object. This method uses a callback to return the object.

**起始版本：** 23

<!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void--><!--Device-ImageSource-createPixelMap(callback: AsyncCallback<PixelMap | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap \| undefined & gt; | 是 |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void
```

通过图片解码参数创建PixelMap对象。使用callback异步回调。 从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md#createpixelmapusingallocator)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md#allocatortype)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void--><!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void
```

Creates a PixelMap object based on image decoding parameters. This method uses a callback to return the object.

**起始版本：** 23

<!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void--><!--Device-ImageSource-createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap \| undefined & gt; | 是 |

## createPixelMapList

```TypeScript
createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>
```

通过图片解码参数创建PixelMap数组。使用Promise异步回调。 针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 > > - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时（如2000×3000像素的100帧GIF动图），会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接 > 口少。

**起始版本：** 23

<!--Device-ImageSource-createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>--><!--Device-ImageSource-createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;PixelMap & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980099](../errorcode-image.md#62980099-共享内存数据异常) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |

## createPixelMapList

```TypeScript
createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void
```

通过默认参数创建PixelMap数组。使用callback异步回调。 针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 > > - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**起始版本：** 23

<!--Device-ImageSource-createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void--><!--Device-ImageSource-createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980099](../errorcode-image.md#62980099-共享内存数据异常) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |

## createPixelMapList

```TypeScript
createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void
```

通过图片解码参数创建PixelMap数组。使用callback异步回调。 针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 > > - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**起始版本：** 23

<!--Device-ImageSource-createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void--><!--Device-ImageSource-createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980099](../errorcode-image.md#62980099-共享内存数据异常) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap
```

通过图片解码参数同步创建PixelMap对象。 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 从API version 15开始，推荐使用[createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md#createpixelmapusingallocatorsync)，该接口可以指定输出 pixelMap的内存类型[AllocatorType](arkts-image-image-allocatortype-e.md#allocatortype)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 > **说明：** > > 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考 > [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 12

<!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap--><!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap | undefined
```

Create a PixelMap object based on image decoding parameters synchronously.

**起始版本：** 23

<!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap | undefined--><!--Device-ImageSource-createPixelMapSync(options?: DecodingOptions): PixelMap | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>
```

使用指定的分配器根据图像解码参数异步创建PixelMap对象。使用Promise异步回调。接口使用详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 > **说明：** > > - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 15

<!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>--><!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)
      : Promise<PixelMap | undefined>
```

Creates a PixelMap based on decoding parameters, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**起始版本：** 23

<!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)      : Promise<PixelMap | undefined>--><!--Device-ImageSource-createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)      : Promise<PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap
```

根据指定的分配器同步创建一个基于图像解码参数的PixelMap对象。接口使用详情请参考[图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 > **说明：** > > 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考 > [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 15

<!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap--><!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined
```

Creates a PixelMap based on decoding parameters synchronously, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**起始版本：** 23

<!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined--><!--Device-ImageSource-createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |

## createThumbnail

```TypeScript
createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>
```

通过图片解码参数创建缩略图PixelMap对象。使用Promise异步回调。 当前支持对JPEG和HEIF格式的图片创建缩略图PixelMap对象。 优先解码图片文件中包含的缩略图。若图片文件中没有缩略图，则对原图进行解码。 > **说明：** > > - 不支持在同一个ImageSource实例上并发调用。 > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>--><!--Device-ImageSource-createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700305](../errorcode-image.md#7700305-缩略图生成失败) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700303](../errorcode-image.md#7700303-图片不包含缩略图数据) |

## createThumbnailSync

```TypeScript
createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined
```

通过图片解码参数同步创建缩略图。返回创建结果对应的[PixelMap](arkts-image-image-pixelmap-i.md#pixelmap)对象。 当前支持对JPEG和HEIF格式的图片创建缩略图PixelMap对象。 优先解码图片文件中包含的缩略图。若图片文件中没有缩略图，则对原图进行解码。 > **说明：** > > - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。 > > - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。 > > - 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考 > [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined--><!--Device-ImageSource-createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700305](../errorcode-image.md#7700305-缩略图生成失败) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700303](../errorcode-image.md#7700303-图片不包含缩略图数据) |

## getDelayTimeList

```TypeScript
getDelayTimeList(): Promise<Array<number>>
```

获取图像延迟时间数组。使用Promise异步回调。此接口仅用于gif图片和webp图片。

**起始版本：** 23

<!--Device-ImageSource-getDelayTimeList(): Promise<Array<int>>--><!--Device-ImageSource-getDelayTimeList(): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |

## getDelayTimeList

```TypeScript
getDelayTimeList(callback: AsyncCallback<Array<number>>): void
```

获取图像延迟时间数组。使用callback异步回调。此接口仅用于gif图片和webp图片。

**起始版本：** 23

<!--Device-ImageSource-getDelayTimeList(callback: AsyncCallback<Array<int>>): void--><!--Device-ImageSource-getDelayTimeList(callback: AsyncCallback<Array<int>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |

## getDisposalTypeList

```TypeScript
getDisposalTypeList(): Promise<Array<number>>
```

获取图像帧过渡模式数组。使用Promise异步回调。此接口仅用于gif图片。

**起始版本：** 23

<!--Device-ImageSource-getDisposalTypeList(): Promise<Array<int>>--><!--Device-ImageSource-getDisposalTypeList(): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |

## getFrameCount

```TypeScript
getFrameCount(): Promise<number>
```

获取图像帧数。使用Promise异步回调。

**起始版本：** 23

<!--Device-ImageSource-getFrameCount(): Promise<int>--><!--Device-ImageSource-getFrameCount(): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |

## getFrameCount

```TypeScript
getFrameCount(callback: AsyncCallback<number>): void
```

获取图像帧数。使用callback异步回调。

**起始版本：** 23

<!--Device-ImageSource-getFrameCount(callback: AsyncCallback<int>): void--><!--Device-ImageSource-getFrameCount(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |

## getImageInfo

```TypeScript
getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void
```

获取指定序号的图片信息。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo>): void--><!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(index: number, callback: AsyncCallback<ImageInfo | undefined>): void
```

Obtains information about an image with the specified sequence number and uses a callback to return the result.

**起始版本：** 23

<!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo | undefined>): void--><!--Device-ImageSource-getImageInfo(index: int, callback: AsyncCallback<ImageInfo | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined & gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

获取图片信息。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo>): void--><!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void
```

Obtains information about this image and uses a callback to return the result.

**起始版本：** 23

<!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void--><!--Device-ImageSource-getImageInfo(callback: AsyncCallback<ImageInfo | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined & gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(index?: number): Promise<ImageInfo>
```

获取图片信息。使用Promise异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo>--><!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

## getImageInfo

```TypeScript
getImageInfo(index?: number): Promise<ImageInfo | undefined>
```

Get image information from image source.

**起始版本：** 23

<!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo | undefined>--><!--Device-ImageSource-getImageInfo(index?: int): Promise<ImageInfo | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md) \| undefined & gt; |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: number): ImageInfo
```

获取指定序号的图片信息，使用同步形式返回图片信息。 > **说明：** > > 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考 > [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 12

<!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo--><!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: number): ImageInfo | undefined
```

Get image information from image source synchronously.

**起始版本：** 23

<!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo | undefined--><!--Device-ImageSource-getImageInfoSync(index?: int): ImageInfo | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

## getImageProperties

```TypeScript
getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>
```

批量获取图片中的指定属性键的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**起始版本：** 12

<!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>--><!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | Array&lt;[PropertyKey](arkts-image-image-propertykey-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;[PropertyKey](arkts-image-image-propertykey-e.md), string \| null & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |

## getImageProperties

```TypeScript
getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>
```

Obtains the value of properties in an image. This method uses a promise to return the property values in array of records.

**起始版本：** 23

<!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>--><!--Device-ImageSource-getImageProperties(key: Array<PropertyKey>): Promise<Record<string, string|null>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | Array&lt;[PropertyKey](arkts-image-image-propertykey-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, string \ | null & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |

## getImageProperty

```TypeScript
getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>
```

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**起始版本：** 23

<!--Device-ImageSource-getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>--><!--Device-ImageSource-getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | 是 |
| options | [ImagePropertyOptions](arkts-image-image-imagepropertyoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |

## getImageProperty

```TypeScript
getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>
```

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > 从API version 7开始支持，从API version 11废弃，建议使用 > [getImageProperty](#getimageproperty)代 > 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>--><!--Device-ImageSource-getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getImageProperty

```TypeScript
getImageProperty(key: string, callback: AsyncCallback<string>): void
```

获取图片中给定索引处图像的指定属性键的值。使用callback异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > 从API version 7开始支持，从API version 11废弃，建议使用 > [getImageProperty](#getimageproperty)代 > 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, callback: AsyncCallback<string>): void--><!--Device-ImageSource-getImageProperty(key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getImageProperty

```TypeScript
getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void
```

获取图片指定属性键的值。使用callback异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > 从API version 7开始支持，从API version 11废弃，建议使用 > [getImageProperty](#getimageproperty)代 > 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

<!--Device-ImageSource-getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void--><!--Device-ImageSource-getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string
```

获取图片Exif指定属性键的值，使用同步形式返回结果。 > **说明：** > > - 该方法仅支持JPEG、PNG、HEIF、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > > - Exif信息是图片的元数据，包含拍摄时间、相机型号、光圈、焦距、ISO等。 > > - 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考 > [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 20

<!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string--><!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string | undefined
```

Obtains the value of a property in the image.

**起始版本：** 23

<!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string | undefined--><!--Device-ImageSource-getImagePropertySync(key: PropertyKey): string | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## modifyImageProperties

```TypeScript
modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>
```

批量通过指定的键修改图片属性的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > - 调用modifyImageProperties修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperties会导致buffer内容覆盖，目前buffer创建的 > ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。 > > - 调用modifyImageProperties接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 12

<!--Device-ImageSource-modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| records | Record&lt;[PropertyKey](arkts-image-image-propertykey-e.md), string \| null & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980146](../errorcode-image.md#62980146-图片属性值写入文件失败) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |

## modifyImageProperties

```TypeScript
modifyImageProperties(records: Record<string, string|null>): Promise<void>
```

Modify the value of properties in an image with the specified keys.

**起始版本：** 23

<!--Device-ImageSource-modifyImageProperties(records: Record<string, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageProperties(records: Record<string, string|null>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980146](../errorcode-image.md#62980146-图片属性值写入文件失败) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |

## modifyImagePropertiesEnhanced

```TypeScript
modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>
```

批量修改图片属性。使用Promise异步回调。 > **说明：** > > - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例或通过传入的uri创建 > [image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例。 > > - 该方法在内存中完成批量数据修改后会一次性写入文件，相比 > [modifyImageProperties](#modifyimageproperties) > 更高效。 > > - 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。 > > - 调用modifyImagePropertiesEnhanced接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 23

<!--Device-ImageSource-modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>--><!--Device-ImageSource-modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700304](../errorcode-image.md#7700304-图片信息写入文件失败) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: PropertyKey, value: string): Promise<void>
```

通过指定的键修改图片属性的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的 > ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。 > > - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 23

<!--Device-ImageSource-modifyImageProperty(key: PropertyKey, value: string): Promise<void>--><!--Device-ImageSource-modifyImageProperty(key: PropertyKey, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [PropertyKey](arkts-image-image-propertykey-e.md) | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980146](../errorcode-image.md#62980146-图片属性值写入文件失败) |
| [62980133](../errorcode-image.md#62980133-图片属性赋值超出范围) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string): Promise<void>
```

通过指定的键修改图片属性的值。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的 > ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。 > > - 从API version 9开始支持，从API version 11废弃，建议使用 > [modifyImageProperty](#modifyimageproperty)代替。 > > - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

<!--Device-ImageSource-modifyImageProperty(key: string, value: string): Promise<void>--><!--Device-ImageSource-modifyImageProperty(key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void
```

通过指定的键修改图片属性的值。使用callback异步回调。 仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的 > ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。 > > - 从API version 9开始支持，从API version 11废弃，建议使用 > [modifyImageProperty](#modifyimageproperty)代替。 > > - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

<!--Device-ImageSource-modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-ImageSource-modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## readImageMetadata

```TypeScript
readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>
```

读取图像源的元数据，使用propertyKeys指定元数据字段。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF、WebP、DNG、GIF、TIFF、HEIFS、JFIF和AVIS（不同硬件设备支持情况不同）文件，且需要包含Exif信息。 > **说明：** > > 读取DNG格式图片时，该接口对部分propertyKeys有特殊处理。以下字段的字符串取值请参考[PropertyKey](arkts-image-image-propertykey-e.md#propertykey)中的值： > > - NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、 > PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、 > YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。 > > - ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。 > > - ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。 > > - DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。 > > - GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。 > > - GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。 > > - ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。 > > - 从API version 24开始，支持读取DNG元数据。要查询的属性的具体信息请参考[DngPropertyKey](arkts-image-image-dngpropertykey-e.md#dngpropertykey)。 > > - 从API version 24开始，支持读取HEIFS元数据。要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#heifspropertykey)。 > > - 从API版本26.0.0开始，支持读取PNG元数据。要查询的属性的具体信息请参考[PngPropertyKey](arkts-image-image-pngpropertykey-e.md#pngpropertykey)。 > > - 从API版本26.0.0开始，支持读取JFIF元数据。要查询的属性的具体信息请参考[JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md#jfifpropertykey)。 > > - 从API版本26.0.0开始，支持读取TIFF元数据。要查询的属性的具体信息请参考[TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md#tiffpropertykey)。 > > - 从API版本26.0.0开始，支持读取GIF元数据。要查询的属性的具体信息请参考[GifPropertyKey](arkts-image-image-gifpropertykey-e.md#gifpropertykey)。 > > - 从API版本26.0.0开始，支持读取JPEG、PNG、GIF、DNG、TIFF格式图片的XMP元数据。XMP元数据的操作方法可以参考 > [XMPMetadata](../../../reference/apis-image-kit/arkts-apis-image-XMPMetadata.md)。 > > - 从API版本26.0.0开始，支持读取AVIS元数据。要查询的属性的具体信息请参考[AvisPropertyKey](arkts-image-image-avispropertykey-e.md#avispropertykey)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-readImageMetadata(propertyKeys?: string[], index?: int): Promise<ImageMetadata>--><!--Device-ImageSource-readImageMetadata(propertyKeys?: string[], index?: int): Promise<ImageMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyKeys | string[] | 否 |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## readImageMetadataByType

```TypeScript
readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>
```

读取图像源的元数据，使用metadataTypes指定元数据类型。若未指定metadataTypes，则返回所有支持的元数据。使用Promise异步回调。 该接口仅支持JPEG、PNG、HEIF、WebP、DNG、GIF、TIFF、HEIFS、JFIF和AVIS（不同硬件设备支持情况不同）文件。 > **说明：** > > - EXIF_METADATA元数据类型适用于JPEG、PNG、HEIF、WEBP和DNG格式图片。 > > - HEIFS_METADATA元数据类型适用于HEIFS格式图片。 > > - 当传入的MetadataType与图片格式无法匹配时，返回错误码7700102。 > > - 从API version 24开始，支持读取DNG元数据。要查询的属性的具体信息请参考[DngPropertyKey](arkts-image-image-dngpropertykey-e.md#dngpropertykey)。 > > - 从API version 24开始，支持读取HEIFS元数据。要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#heifspropertykey)。 > > - 从API版本26.0.0开始，支持读取PNG元数据。要查询的属性的具体信息请参考[PngPropertyKey](arkts-image-image-pngpropertykey-e.md#pngpropertykey)。 > > - 从API版本26.0.0开始，支持读取JFIF元数据。要查询的属性的具体信息请参考[JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md#jfifpropertykey)。 > > - 从API版本26.0.0开始，支持读取TIFF元数据。要查询的属性的具体信息请参考[TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md#tiffpropertykey)。 > > - 从API版本26.0.0开始，支持读取GIF元数据。要查询的属性的具体信息请参考[GifPropertyKey](arkts-image-image-gifpropertykey-e.md#gifpropertykey)。 > > - 从API版本26.0.0开始，支持读取JPEG、PNG、GIF、DNG、TIFF格式图片的XMP元数据。XMP元数据的操作方法可以参考 > [XMPMetadata](../../../reference/apis-image-kit/arkts-apis-image-XMPMetadata.md)。 > > - 从API版本26.0.0开始，支持读取AVIS元数据。要查询的属性的具体信息请参考[AvisPropertyKey](arkts-image-image-avispropertykey-e.md#avispropertykey)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-readImageMetadataByType(metadataTypes?: MetadataType[], index?: int): Promise<ImageMetadata>--><!--Device-ImageSource-readImageMetadataByType(metadataTypes?: MetadataType[], index?: int): Promise<ImageMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadataTypes | [MetadataType](arkts-image-image-metadatatype-e.md)[] | 否 |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageMetadata](arkts-image-image-imagemetadata-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放ImageSource实例。使用callback异步回调。 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。 释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageSource-release(callback: AsyncCallback<void>): void--><!--Device-ImageSource-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放ImageSource实例。使用Promise异步回调。 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。 释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageSource-release(): Promise<void>--><!--Device-ImageSource-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## updateData

```TypeScript
updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>
```

更新增量数据。使用Promise异步回调。

**起始版本：** 23

<!--Device-ImageSource-updateData(buf: ArrayBuffer, isFinished: boolean, offset: int, length: int): Promise<void>--><!--Device-ImageSource-updateData(buf: ArrayBuffer, isFinished: boolean, offset: int, length: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| isFinished | boolean | 是 |
| offset | number | 是 |
| length | number | 是 |

**返回值：**

| 类型 |
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

更新增量数据。使用callback异步回调。

**起始版本：** 23

<!--Device-ImageSource-updateData(      buf: ArrayBuffer,      isFinished: boolean,      offset: int,      length: int,      callback: AsyncCallback<void>    ): void--><!--Device-ImageSource-updateData(      buf: ArrayBuffer,      isFinished: boolean,      offset: int,      length: int,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| isFinished | boolean | 是 |
| offset | number | 是 |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## writeImageMetadata

```TypeScript
writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>
```

批量修改图片属性。使用Promise异步回调。 > **说明：** > > - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例或通过传入的uri创建 > [image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例。 > > - 该方法在内存中完成批量数据修改后会一次性写入文件，相比 > [modifyImageProperties](#modifyimageproperties) > 更高效。 > > - 支持修改JPEG、PNG和HEIF文件类型的图片属性，图片需要包含Exif信息。修改属性前，先通过supportedFormats属性查询设备是否支持HEIF格式的Exif读写。 > > - 从API版本26.0.0开始，支持修改JPEG、PNG、GIF格式图片的XMP元数据。XMP元数据的操作方法可以参考 > [XMPMetadata](../../../reference/apis-image-kit/arkts-apis-image-XMPMetadata.md)。 > > - 调用writeImageMetadata接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageSource-writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>--><!--Device-ImageSource-writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageMetadata | [ImageMetadata](arkts-image-image-imagemetadata-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

支持的图片格式。 包括：PNG、JPEG、BMP、GIF、WebP、DNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、WBMP&lt;sup&gt;23+&lt;/sup&gt;、HEIFS&lt;sup&gt;23+&lt;/sup&gt;、TIFF&lt;sup&gt;23+&lt;/sup&gt;。从API版本2 6.0.0开始，增加支持AVIF、AVIS格式。 部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats](arkts-image-image-getimagesourcesupportedformats-f.md#getimagesourcesupportedformats)接口， 动态查询当前设备上的解码能力。

**类型：** Array&lt;string&gt;

**起始版本：** 23

<!--Device-ImageSource-readonly supportedFormats: Array<string>--><!--Device-ImageSource-readonly supportedFormats: Array<string>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource
