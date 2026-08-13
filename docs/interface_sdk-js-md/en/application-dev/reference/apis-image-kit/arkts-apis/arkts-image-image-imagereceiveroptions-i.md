# ImageReceiverOptions

Describes the initialization options for ImageReceiver.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-image-interface ImageReceiverOptions--><!--Device-image-interface ImageReceiverOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## capacity

```TypeScript
capacity?: int
```

Maximum number of images that can be accessed simultaneously. The value range is all integers, The value must be a positive integer less than or equal to 64.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageReceiverOptions-capacity?: int--><!--Device-ImageReceiverOptions-capacity?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
size?: Size
```

Image size, with both the width and height greater than 0.

**Type:** Size

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageReceiverOptions-size?: Size--><!--Device-ImageReceiverOptions-size?: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

