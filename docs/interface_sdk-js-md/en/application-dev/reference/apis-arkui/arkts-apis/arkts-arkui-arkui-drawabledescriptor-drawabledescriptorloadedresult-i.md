# DrawableDescriptorLoadedResult

Represents the result of loading an image resource or URI.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## imageHeight

```TypeScript
imageHeight: number
```

Image height.Unit: px.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageWidth

```TypeScript
imageWidth: number
```

Image width.Unit: px.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { AnimatedDrawableDescriptor, AnimationOptions, DrawableDescriptor, DrawableDescriptorLoadedResult } from '@kit.ArkUI';

let options: AnimationOptions = { duration: 2000, iterations: 1 };
let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
try {
    // You can preload animated image resources into the memory.
    let result: DrawableDescriptorLoadedResult = drawable.loadSync()
    console.info(`load result = ${JSON.stringify(result)}`)
} catch(e) {
    console.error("load failed")
}
```
