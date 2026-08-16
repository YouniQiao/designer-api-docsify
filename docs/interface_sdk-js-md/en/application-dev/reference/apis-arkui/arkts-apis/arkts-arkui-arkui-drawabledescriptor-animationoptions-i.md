# AnimationOptions

Provides the configuration options for animation playback, including the playback duration, number of playback times, and autoplay behavior.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare interface AnimationOptions--><!--Device-unnamed-declare interface AnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor } from 'DrawableDescriptor';
import { LayeredDrawableDescriptor } from 'LayeredDrawableDescriptor';
import { PixelMapDrawableDescriptor } from 'PixelMapDrawableDescriptor';
import { AnimationOptions } from 'AnimationOptions';
import { AnimatedDrawableDescriptor } from 'AnimatedDrawableDescriptor';
import { AnimationController } from 'AnimationController';
import { DrawableDescriptorLoadedResult } from 'DrawableDescriptorLoadedResult';
import { AnimationStopMode } from 'AnimationStopMode';
import { PictureDrawableDescriptor } from 'PictureDrawableDescriptor';
import { HdrCompositionConfig } from 'HdrCompositionConfig';
```

## autoPlay

```TypeScript
autoPlay?: boolean
```

Whether to enable autoplay. **true** to enable, **false** otherwise. The default value is **true**.

**Type:** boolean

**Default:** true

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-AnimationOptions-autoPlay?: boolean--><!--Device-AnimationOptions-autoPlay?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

Total playback duration for the image sequence. For **PixelMap** arrays, the default value is 1s per image. For local or application resources, the duration is determined by the playback delay embedded in the image resource. Unit: ms. Value range: [0, +∞). Negative values are treated as the default value.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimationOptions-duration?: number--><!--Device-AnimationOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## frameDurations

```TypeScript
frameDurations?: Array<number>
```

Per-frame playback duration. The setting overrides **duration** if specified. If **duration** and **frameDurations** are set, **duration** is ignored. If the value of **frameDurations** is inconsistent with the image count, animation timing distributes across the total duration. Unit: ms.

**Type:** Array&lt;number&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-AnimationOptions-frameDurations?: Array<number>--><!--Device-AnimationOptions-frameDurations?: Array<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iterations

```TypeScript
iterations?: number
```

Number of playback times for the image sequence. A value of **-1** indicates infinite playback, **0** indicates no playback, and a value greater than 0 represents the number of playback times. The default value is **1**.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimationOptions-iterations?: number--><!--Device-AnimationOptions-iterations?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopMode

```TypeScript
stopMode?: AnimationStopMode
```

Sets the stop mode for an animation. The default value is **AnimationStopMode.FIRST_FRAME**, indicating that the animation returns to the first frame when it stops.

**Type:** [AnimationStopMode](../../apis-na/arkts-apis/arkts-na-arkui-drawabledescriptor-animationstopmode-e.md)

**Default:** AnimationStopMode.FIRST_FRAME

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AnimationOptions-stopMode?: AnimationStopMode--><!--Device-AnimationOptions-stopMode?: AnimationStopMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

