# AnimationController

动画控制器对象。包含控制动画播放、停止、恢复、暂停和状态查询等方法。

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

获取当前动图播放的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-getStatus(): AnimationStatus--><!--Device-AnimationController-getStatus(): AnimationStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [AnimationStatus](arkts-arkui-animationstatus-e.md) | 动图的播放状态。包含4种状态：初始态、播放态、暂停态、停止态。 |

## pause

```TypeScript
pause(): void
```

暂停动图的播放，保持在当前帧。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-pause(): void--><!--Device-AnimationController-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resume

```TypeScript
resume(): void
```

在当前帧恢复播放动图。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-resume(): void--><!--Device-AnimationController-resume(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start(): void
```

从首帧开始播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-start(): void--><!--Device-AnimationController-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

停止动图的播放并回到首帧。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationController-stop(): void--><!--Device-AnimationController-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

