# AnimationController

Define the data structure for PixelMap animations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface AnimationController--><!--Device-unnamed-export interface AnimationController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## getStatus

```TypeScript
getStatus(): AnimationStatus
```

Get animtion status of the current component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-getStatus(): AnimationStatus--><!--Device-AnimationController-getStatus(): AnimationStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [AnimationStatus](arkts-arkui-animationstatus-e.md) | Return the status of animation. |

## pause

```TypeScript
pause(): void
```

Pause animation playback, and keep it to the current frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-pause(): void--><!--Device-AnimationController-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resume

```TypeScript
resume(): void
```

Resume animation playback from the current frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-resume(): void--><!--Device-AnimationController-resume(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start(): void
```

Start animtion playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-start(): void--><!--Device-AnimationController-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

Stop animation playback, and reset to first frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-stop(): void--><!--Device-AnimationController-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

