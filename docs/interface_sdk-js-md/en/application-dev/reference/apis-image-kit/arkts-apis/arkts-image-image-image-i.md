# Image

Image类，供ImageReceiver和ImageCreator使用，用于传输图片对象，其实际内容由生产者决定。如相机预览流提供的Image对象存储了YUV数据、相机拍照提供的Image对象存储了JPEG文件。

调用[readNextImage](arkts-image-image-imagereceiver-i.md#readnextimage)和  
[readLatestImage](arkts-image-image-imagereceiver-i.md#readlatestimage)接口时会返回Image实例。

Image的属性仅支持在创建时初始化，后续无法再修改，且其属性不对图片内容产生实际影响，请以图片生产者写入的属性为准，即以向[ImageReceiver](arkts-image-image-imagereceiver-i.md)发送图片数据的发送方实际写入的内容为准。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](arkts-image-image-image-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> - 本Interface首批接口从API version 9开始支持。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-image-interface Image--><!--Device-image-interface Image-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## getBufferData

```TypeScript
getBufferData(): ImageBufferData | null
```

从图像中获取ImageBufferData。

> **注意：**
> 
> ImageBufferData中的byteBuffer是对内部缓存的浅拷贝，当Image的生命周期结束时，便不能对byteBuffer做任何操作，否则会导致未定义行为。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Image-getBufferData(): ImageBufferData | null--><!--Device-Image-getBufferData(): ImageBufferData | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBufferData](arkts-image-image-imagebufferdata-i.md) | 获取封装图像数据缓冲区的结构体，获取不到时返回空值。 |

## getComponent

```TypeScript
getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void
```

根据图像的组件类型从图像中获取组件缓存。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void--><!--Device-Image-getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| componentType | [ComponentType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-componenttype-e-sys.md) | Yes | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Component&gt; | Yes | 回调函数，当返回组件缓冲区成功，err为undefined，data为获取到的组件缓冲区；否则为错误对象。 |

## getComponent

```TypeScript
getComponent(componentType: ComponentType): Promise<Component>
```

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-getComponent(componentType: ComponentType): Promise<Component>--><!--Device-Image-getComponent(componentType: ComponentType): Promise<Component>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| componentType | [ComponentType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-componenttype-e-sys.md) | Yes | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回组件缓冲区。 |

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue | null
```

根据HDR元数据的类型从图像中获取HDR元数据。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Image-getMetadata(key: HdrMetadataKey): HdrMetadataValue | null--><!--Device-Image-getMetadata(key: HdrMetadataKey): HdrMetadataValue | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | Yes | HDR元数据的关键字，可用于查询对应值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) | 返回关键字对应的HDR元数据的值。如果图像没有HDR元数据，返回空值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7600206 | Invalid parameter. |
| 7600302 | Memory copy failed. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放当前图像。使用callback异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-release(callback: AsyncCallback<void>): void--><!--Device-Image-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当图像释放成功，err为undefined，否则为错误对象。 |

## release

```TypeScript
release(): Promise<void>
```

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-release(): Promise<void>--><!--Device-Image-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## clipRect

```TypeScript
clipRect: Region
```

要裁剪的图像区域。恒等于整个图像，不支持修改。

**Type:** [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-clipRect: Region--><!--Device-Image-clipRect: Region-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## colorSpace

```TypeScript
readonly colorSpace: colorSpaceManager.ColorSpace
```

图像色彩空间，色域枚举类型。

**Type:** colorSpaceManager.ColorSpace

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Image-readonly colorSpace: colorSpaceManager.ColorSpace--><!--Device-Image-readonly colorSpace: colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## format

```TypeScript
readonly format: int
```

图像格式，参考  
[OH_NativeBuffer_Format](../../../reference/apis-arkgraphics2d/capi-buffer-common-h.md#oh_nativebuffer_format)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-readonly format: int--><!--Device-Image-readonly format: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
readonly size: Size
```

图像大小。

如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。

如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。

Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId通过  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)接口还是  
[createPhotoOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createphotooutput)接口传给相机。

相机预览与拍照最佳实践请参考[双路预览(ArkTS)](../../../media/camera/camera-dual-channel-preview.md)与  
[拍照实践(ArkTS)](../../../media/camera/camera-shooting-case.md)。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Image-readonly size: Size--><!--Device-Image-readonly size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## timestamp

```TypeScript
readonly timestamp: long
```

图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过  
[getImageProperty](arkts-image-image-imagesource-i.md#getimageproperty)接口读取EXIF时间戳信息。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Image-readonly timestamp: long--><!--Device-Image-readonly timestamp: long-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

