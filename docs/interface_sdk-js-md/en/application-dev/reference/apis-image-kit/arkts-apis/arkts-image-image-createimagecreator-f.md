# createImageCreator

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageCreator

```TypeScript
function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator
```

通过宽、高、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> 从API version 9开始支持，从API version 11废弃，建议使用[createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator)代替。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [image.createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator)(size:

<!--Device-image-function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator--><!--Device-image-function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 图像的默认宽度。单位：像素（px）。 |
| height | number | Yes | 图像的默认高度。单位：像素（px）。 |
| format | number | Yes | 图像格式，如YCBCR_422_SP，JPEG。 |
| capacity | number | Yes | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) | 如果操作成功，则返回ImageCreator实例。 |

## Examples

```TypeScript
let creator: image.ImageCreator = image.createImageCreator(8192, 8192, image.ImageFormat.JPEG, 8);
```


## createImageCreator

```TypeScript
function createImageCreator(size: Size, format: ImageFormat, capacity: int): ImageCreator
```

通过图片大小、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-image-function createImageCreator(size: Size, format: ImageFormat, capacity: int): ImageCreator--><!--Device-image-function createImageCreator(size: Size, format: ImageFormat, capacity: int): ImageCreator-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | Yes | 图像的默认大小。单位：像素（px）。 |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | Yes | 图像格式，如YCBCR_422_SP，JPEG。 |
| capacity | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) | 如果操作成功，则返回ImageCreator实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; |

## Examples

```TypeScript
let size: image.Size = {
  height: 8192,
  width: 8192
}
let creator: image.ImageCreator = image.createImageCreator(size, image.ImageFormat.JPEG, 8);
```

