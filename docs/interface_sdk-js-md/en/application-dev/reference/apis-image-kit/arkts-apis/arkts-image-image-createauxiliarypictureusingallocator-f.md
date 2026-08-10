# createAuxiliaryPictureUsingAllocator

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createAuxiliaryPictureUsingAllocator

```TypeScript
function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,
    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture
```

使用指定的内存类型，根据辅助图信息和像素数据创建辅助图对象。

> **说明：**
> 
> - 在处理此接口返回的AuxiliaryPicture时，需要考虑内存中每行像素所占的空间的影响。
> 
> - 创建的辅助图像会使用输入的像素进行初始化。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture--><!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| auxiliaryPictureInfo | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Yes | 辅助图图像信息。 &lt;br&gt;- 输入的ArrayBuffer的pixelFormat和最终创建出的辅助图的实际pixelFormat需与auxiliaryPictureInfo中指定的pixelFormat保持一致。 &lt;br&gt;- 当AuxiliaryPictureType为GAINMAP时，AllocatorType仅支持传入AUTO/DMA。 &lt;br&gt;- 当传入SHARE_MEMORY时，返回错误码7600205。 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | 图像解码的内存类型，AUTO及默认情况下按照DMA处理。 |
| pixels | ArrayBuffer | No | 以buffer形式存放的图像数据。 &lt;br&gt;当未提供ArrayBuffer参数时，默认创建空白辅助图。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) | 如果操作成功，则返回AuxiliaryPicture实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7600206 | Invalid parameter, size.height or size.width is less than or equal to 0. |
| 7600205 | Unsupported allocator type, e.g., use shared memory to create a gainmap as only DMA supported hdr metadata. |
| 7600301 | Alloc memory failed. |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';

function CreateAuxiliaryPictureUsingAllocator(info: image.AuxiliaryPictureInfo,  allocatorType?: image.AllocatorType, pixels?: ArrayBuffer ) {
  let res : image.AuxiliaryPicture;
  try {
    res = image.createAuxiliaryPictureUsingAllocator(info, allocatorType, pixels);
  } catch (error) {
    console.error(`Failed to create auxiliary picture using allocator=${allocatorType} and pixels=${pixels?.byteLength}.`);
  }
}
```

