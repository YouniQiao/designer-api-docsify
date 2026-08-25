# ImageSource

ImageSource类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过[image.createImageSource](arkts-image-image-createimagesource-f.md)构建一个ImageSource实例。ImageSource的所有方法均不支持并发调用。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageRawData

```TypeScript
createImageRawData(): Promise<ImageRawData>
```

获取图片原始数据。使用Promise异步回调。目前仅支持获取DNG图片类型的原始数据。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

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

通过图片解码参数创建Picture对象。使用Promise异步回调。由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法，及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 13

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

## createPictureAtIndex

```TypeScript
createPictureAtIndex(index: number): Promise<Picture>
```

通过指定序号的图片创建Picture对象。使用Promise异步回调。

> **说明：**&gt;
> - 支持GIF和HEIF&lt;sup&gt;23+&lt;/sup&gt;图像序列格式。从API版本26.0.0开始，增加支持AVIS格式。&gt;
> - 由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 20

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
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |
| [7700301](../errorcode-image.md#7700301-解码失败) |

## createPixelMap

```TypeScript
createPixelMap(options?: DecodingOptions): Promise<PixelMap>
```

通过图片解码参数创建PixelMap对象。使用Promise异步回调。从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

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
createPixelMap(callback: AsyncCallback<PixelMap>): void
```

通过默认参数创建PixelMap对象。使用callback异步回调。从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

## createPixelMap

```TypeScript
createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void
```

通过图片解码参数创建PixelMap对象。使用callback异步回调。从API version 15开始，推荐使用[createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md)，该接口可以指定输出pixelMap的 内存类型[AllocatorType](arkts-image-image-allocatortype-e.md)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

## createPixelMapList

```TypeScript
createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>
```

通过图片解码参数创建PixelMap数组。使用Promise异步回调。针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。&gt;
> - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时（如2000×3000像素的100帧GIF动图），会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接
> 口少。

**起始版本：** 10

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
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |

## createPixelMapList

```TypeScript
createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void
```

通过默认参数创建PixelMap数组。使用callback异步回调。针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。&gt;
> - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980099](../errorcode-image.md#62980099-共享内存数据异常) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |

## createPixelMapList

```TypeScript
createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void
```

通过图片解码参数创建PixelMap数组。使用callback异步回调。针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。&gt;
> - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PixelMap&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980099](../errorcode-image.md#62980099-共享内存数据异常) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980109](../errorcode-image.md#62980109-裁剪错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980174](../errorcode-image.md#62980174-dma内存数据异常) |

## createPixelMapSync

```TypeScript
createPixelMapSync(options?: DecodingOptions): PixelMap
```

通过图片解码参数同步创建PixelMap对象。由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。从API version 15开始，推荐使用[createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md)，该接口可以指定输出 pixelMap的内存类型[AllocatorType](arkts-image-image-allocatortype-e.md)，详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。

> **说明：**&gt;
> 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考
> [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

## createPixelMapUsingAllocator

```TypeScript
createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>
```

使用指定的分配器根据图像解码参数异步创建PixelMap对象。使用Promise异步回调。接口使用详情请参考 [图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。

> **说明：**&gt;
> - 该方法为非线程安全的方法，不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 15

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |

## createPixelMapUsingAllocatorSync

```TypeScript
createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap
```

根据指定的分配器同步创建一个基于图像解码参数的PixelMap对象。接口使用详情请参考[图片解码内存优化(ArkTS)](../../../media/image/image-allocator-type.md)。由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

> **说明：**&gt;
> 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考
> [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 15

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptions](arkts-image-image-decodingoptions-i.md) | 否 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700201](../errorcode-image.md#7700201-不支持的内存分配类型) |
| [7700203](../errorcode-image.md#7700203-不支持的选项) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700302](../errorcode-image.md#7700302-内存分配失败) |

## createThumbnail

```TypeScript
createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>
```

通过图片解码参数创建缩略图PixelMap对象。使用Promise异步回调。当前支持对JPEG和HEIF格式的图片创建缩略图PixelMap对象。优先解码图片文件中包含的缩略图。若图片文件中没有缩略图，则对原图进行解码。

> **说明：**&gt;
> - 不支持在同一个ImageSource实例上并发调用。&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700303](../errorcode-image.md#7700303-图片不包含缩略图数据) |
| [7700305](../errorcode-image.md#7700305-缩略图生成失败) |

## createThumbnailSync

```TypeScript
createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined
```

通过图片解码参数同步创建缩略图。返回创建结果对应的[PixelMap](arkts-image-image-pixelmap-i.md)对象。当前支持对JPEG和HEIF格式的图片创建缩略图PixelMap对象。优先解码图片文件中包含的缩略图。若图片文件中没有缩略图，则对原图进行解码。

> **说明：**&gt;
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-image-pixelmap-i.md#release)方法，及时释放内存。&gt;
> - 释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。&gt;
> - 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考
> [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| PixelMap \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700204](../errorcode-image.md#7700204-无效参数) |
| [7700301](../errorcode-image.md#7700301-解码失败) |
| [7700303](../errorcode-image.md#7700303-图片不包含缩略图数据) |
| [7700305](../errorcode-image.md#7700305-缩略图生成失败) |

## getDelayTimeList

```TypeScript
getDelayTimeList(): Promise<Array<number>>
```

获取图像延迟时间数组。使用Promise异步回调。此接口仅用于gif图片和webp图片。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |

## getDelayTimeList

```TypeScript
getDelayTimeList(callback: AsyncCallback<Array<number>>): void
```

获取图像延迟时间数组。使用callback异步回调。此接口仅用于gif图片和webp图片。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |

## getDisposalTypeList

```TypeScript
getDisposalTypeList(): Promise<Array<number>>
```

获取图像帧过渡模式数组。使用Promise异步回调。此接口仅用于gif图片。

**起始版本：** 12

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
| [62980137](../errorcode-image.md#62980137-图片操作无效) |
| [62980149](../errorcode-image.md#62980149-图片参数无效) |

## getFrameCount

```TypeScript
getFrameCount(): Promise<number>
```

获取图像帧数。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |

## getFrameCount

```TypeScript
getFrameCount(callback: AsyncCallback<number>): void
```

获取图像帧数。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980116](../errorcode-image.md#62980116-解码失败) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |

## getImageInfo

```TypeScript
getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void
```

获取指定序号的图片信息。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

获取图片信息。使用callback异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

## getImageInfo

```TypeScript
getImageInfo(index?: number): Promise<ImageInfo>
```

获取图片信息。使用Promise异步回调。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

## getImageInfoSync

```TypeScript
getImageInfoSync(index?: number): ImageInfo
```

获取指定序号的图片信息，使用同步形式返回图片信息。

> **说明：**&gt;
> 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考
> [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 12

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

批量获取图片中的指定属性键的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980116](../errorcode-image.md#62980116-解码失败) |

## getImageProperty

```TypeScript
getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>
```

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**起始版本：** 11

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980110](../errorcode-image.md#62980110-图片源数据错误) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980112](../errorcode-image.md#62980112-图片格式不匹配) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980118](../errorcode-image.md#62980118-创建插件失败) |
| [62980122](../errorcode-image.md#62980122-解码图片头异常) |
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |

## getImageProperty

```TypeScript
getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>
```

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> 从API version 7开始支持，从API version 11废弃，建议使用
> [getImageProperty](#getimageproperty)代
> 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

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

获取图片中给定索引处图像的指定属性键的值。使用callback异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> 从API version 7开始支持，从API version 11废弃，建议使用
> [getImageProperty](#getimageproperty)代
> 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getImageProperty

```TypeScript
getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void
```

获取图片指定属性键的值。使用callback异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> 从API version 7开始支持，从API version 11废弃，建议使用
> [getImageProperty](#getimageproperty)代
> 替。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [getImageProperty](#getimageproperty)(key: PropertyKey, options?: ImagePropertyOptions)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| options | [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getImagePropertySync

```TypeScript
getImagePropertySync(key: PropertyKey): string
```

获取图片Exif指定属性键的值，使用同步形式返回结果。

> **说明：**&gt;
> - 该方法仅支持JPEG、PNG、HEIF、WEBP&lt;sup&gt;23+&lt;/sup&gt;和DNG&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。&gt;
> - Exif信息是图片的元数据，包含拍摄时间、相机型号、光圈、焦距、ISO等。&gt;
> - 该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考
> [耗时任务并发场景简介](../../../arkts-utils/time-consuming-task-overview.md)。

**起始版本：** 20

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

批量通过指定的键修改图片属性的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> - 调用modifyImageProperties修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperties会导致buffer内容覆盖，目前buffer创建的
> ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。&gt;
> - 调用modifyImageProperties接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 12

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
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980146](../errorcode-image.md#62980146-图片属性值写入文件失败) |

## modifyImagePropertiesEnhanced

```TypeScript
modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>
```

批量修改图片属性。使用Promise异步回调。

> **说明：**&gt;
> - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md)实例或通过传入的uri创建
> [image.createImageSource](arkts-image-image-createimagesource-f.md)实例。&gt;
> - 该方法在内存中完成批量数据修改后会一次性写入文件，相比
> [modifyImageProperties](#modifyimageproperties)
> 更高效。&gt;
> - 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。&gt;
> - 调用modifyImagePropertiesEnhanced接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 22

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
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |
| [7700304](../errorcode-image.md#7700304-图片信息写入文件失败) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: PropertyKey, value: string): Promise<void>
```

通过指定的键修改图片属性的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的
> ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。&gt;
> - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 11

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
| [62980123](../errorcode-image.md#62980123-图片不支持exif解码) |
| [62980133](../errorcode-image.md#62980133-图片属性赋值超出范围) |
| [62980135](../errorcode-image.md#62980135-图片属性值无效) |
| [62980146](../errorcode-image.md#62980146-图片属性值写入文件失败) |

## modifyImageProperty

```TypeScript
modifyImageProperty(key: string, value: string): Promise<void>
```

通过指定的键修改图片属性的值。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的
> ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。&gt;
> - 从API version 9开始支持，从API version 11废弃，建议使用
> [modifyImageProperty](#modifyimageproperty)代替。&gt;
> - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

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

通过指定的键修改图片属性的值。使用callback异步回调。仅支持JPEG、PNG、HEIF&lt;sup&gt;12+&lt;/sup&gt;和WEBP&lt;sup&gt;23+&lt;/sup&gt;（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> - 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的
> ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。&gt;
> - 从API version 9开始支持，从API version 11废弃，建议使用
> [modifyImageProperty](#modifyimageproperty)代替。&gt;
> - 调用modifyImageProperty接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [modifyImageProperty](#modifyimageproperty)(key: PropertyKey, value: string)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## readImageMetadata

```TypeScript
readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>
```

读取图像源的元数据，使用propertyKeys指定元数据字段。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF、WebP、DNG、GIF、TIFF、HEIFS、JFIF和AVIS（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**&gt;
> 读取DNG格式图片时，该接口对部分propertyKeys有特殊处理。以下字段的字符串取值请参考[PropertyKey](arkts-image-image-propertykey-e.md)中的值：&gt;
> - NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、
> PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、
> YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。&gt;
> - ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。&gt;
> - ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。&gt;
> - DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。&gt;
> - GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。&gt;
> - GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。&gt;
> - ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。&gt;
> 该接口支持读取以下格式的元数据：&gt;
> - 从API version 24开始，支持读取DNG元数据。要查询的属性的具体信息请参考[DngPropertyKey](arkts-image-image-dngpropertykey-e.md)。&gt;
> - 从API version 24开始，支持读取HEIFS元数据。要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取PNG元数据。要查询的属性的具体信息请参考[PngPropertyKey](arkts-image-image-pngpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取JFIF元数据。要查询的属性的具体信息请参考[JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取TIFF元数据。要查询的属性的具体信息请参考[TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取GIF元数据。要查询的属性的具体信息请参考[GifPropertyKey](arkts-image-image-gifpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取JPEG、PNG、GIF、DNG、TIFF格式图片的XMP元数据。XMP元数据的操作方法可以参考
> [XMPMetadata](arkts-image-image-xmpmetadata-c.md)。&gt;
> - 从API版本26.0.0开始，支持读取AVIS元数据。要查询的属性的具体信息请参考[AvisPropertyKey](arkts-image-image-avispropertykey-e.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |
| [7700204](../errorcode-image.md#7700204-无效参数) |

## readImageMetadataByType

```TypeScript
readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>
```

读取图像源的元数据，使用metadataTypes指定元数据类型。若未指定metadataTypes，则返回所有支持的元数据。使用Promise异步回调。该接口仅支持JPEG、PNG、HEIF、WebP、DNG、GIF、TIFF、HEIFS、JFIF和AVIS（不同硬件设备支持情况不同）文件。

> **说明：**&gt;
> - EXIF_METADATA元数据类型适用于JPEG、PNG、HEIF、WEBP和DNG格式图片。&gt;
> - HEIFS_METADATA元数据类型适用于HEIFS格式图片。&gt;
> - 当传入的MetadataType与图片格式无法匹配时，返回错误码7700102。&gt;
> - 从API version 24开始，支持读取DNG元数据。要查询的属性的具体信息请参考[DngPropertyKey](arkts-image-image-dngpropertykey-e.md)。&gt;
> - 从API version 24开始，支持读取HEIFS元数据。要查询的属性的具体信息请参考[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取PNG元数据。要查询的属性的具体信息请参考[PngPropertyKey](arkts-image-image-pngpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取JFIF元数据。要查询的属性的具体信息请参考[JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取TIFF元数据。要查询的属性的具体信息请参考[TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取GIF元数据。要查询的属性的具体信息请参考[GifPropertyKey](arkts-image-image-gifpropertykey-e.md)。&gt;
> - 从API版本26.0.0开始，支持读取JPEG、PNG、GIF、DNG、TIFF格式图片的XMP元数据。XMP元数据的操作方法可以参考
> [XMPMetadata](arkts-image-image-xmpmetadata-c.md)。&gt;
> - 从API版本26.0.0开始，支持读取AVIS元数据。要查询的属性的具体信息请参考[AvisPropertyKey](arkts-image-image-avispropertykey-e.md)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |
| [7700204](../errorcode-image.md#7700204-无效参数) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放ImageSource实例。使用callback异步回调。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放ImageSource实例。使用Promise异步回调。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

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

**起始版本：** 9

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

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| isFinished | boolean | 是 |
| offset | number | 是 |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## writeImageMetadata

```TypeScript
writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>
```

批量修改图片属性。使用Promise异步回调。

> **说明：**&gt;
> - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md)实例或通过传入的uri创建
> [image.createImageSource](arkts-image-image-createimagesource-f.md)实例。&gt;
> - 该方法在内存中完成批量数据修改后会一次性写入文件，相比
> [modifyImageProperties](#modifyimageproperties)
> 更高效。&gt;
> - 支持修改JPEG、PNG和HEIF文件类型的图片属性，图片需要包含Exif信息。修改属性前，先通过supportedFormats属性查询设备是否支持HEIF格式的Exif读写。&gt;
> - 从API版本26.0.0开始，支持修改JPEG、PNG、GIF格式图片的XMP元数据。XMP元数据的操作方法可以参考
> [XMPMetadata](arkts-image-image-xmpmetadata-c.md)。&gt;
> - 调用writeImageMetadata接口修改Exif字段时，必须确保对应的图片文件有写权限，否则会导致字段修改不成功。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |
| [7700204](../errorcode-image.md#7700204-无效参数) |

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

支持的图片格式。包括：PNG、JPEG、BMP、GIF、WebP、DNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、WBMP&lt;sup&gt;23+&lt;/sup&gt;、HEIFS&lt;sup&gt;23+&lt;/sup&gt;、TIFF&lt;sup&gt;23+&lt;/sup&gt;。从API版本2 6.0.0开始，增加支持AVIF、AVIS格式。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats](arkts-image-image-getimagesourcesupportedformats-f.md)接口， 动态查询当前设备上的解码能力。

**类型：** Array&lt;string&gt;

**起始版本：** 6

**系统能力：** SystemCapability.Multimedia.Image.ImageSource
