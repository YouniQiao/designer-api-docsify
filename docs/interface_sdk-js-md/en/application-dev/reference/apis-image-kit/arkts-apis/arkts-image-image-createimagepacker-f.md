# createImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImagePacker

```TypeScript
function createImagePacker(): ImagePacker
```

创建ImagePacker实例。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](arkts-image-image-imagepacker-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImagePacker(): ImagePacker--><!--Device-image-function createImagePacker(): ImagePacker-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| [ImagePacker](arkts-image-image-imagepacker-i.md) | 返回ImagePacker实例。 |

## Examples

```TypeScript
async function CreateImagePacker() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
}
```

