# createAuxiliaryPictureUsingAllocator

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

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture--><!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| auxiliaryPictureInfo | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | 是 |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 |
| [pixels](arkts-image-image-positionarea-i.md) | ArrayBuffer | 否 |

**返回值：**

| 类型 |
| --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-无效参数) |
| [7600205](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-image-kit/errorcode-image.md#7600205-不支持的内存格式或像素格式) |
| [7600301](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-申请内存失败) |

## 示例

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
