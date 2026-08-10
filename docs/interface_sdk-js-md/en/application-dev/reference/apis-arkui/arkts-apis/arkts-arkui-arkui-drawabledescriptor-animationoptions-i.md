# AnimationOptions

动画播放参数。包括播放时延，迭代次数，单帧播放时间，是否自动播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface AnimationOptions--><!--Device-unnamed-export interface AnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## autoPlay

```TypeScript
autoPlay?: boolean
```

设置动图是否自动播放。true表示自动播放，false表示不自动播放。默认值为true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationOptions-autoPlay?: boolean--><!--Device-AnimationOptions-autoPlay?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

设置图片数组播放总时间。

PixelMap数组的默认值是每张图片播放1秒。本地图片或者应用资源的默认值是图片资源中携带的播放时延。

单位：毫秒

取值范围：[0, +∞)

设置负数取默认值。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationOptions-duration?: int--><!--Device-AnimationOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## frameDurations

```TypeScript
frameDurations?: Array<int>
```

设置动图中的单帧播放时间。不设置则按照总时间播放。设置的优先级高于duration，即同时设置了duration和frameDurations时，duration不生效。当设置的frameDurations长度与图片的数量不一致时，按照总时间播放。单位：毫秒。

**Type:** Array&lt;int&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationOptions-frameDurations?: Array<int>--><!--Device-AnimationOptions-frameDurations?: Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iterations

```TypeScript
iterations?: int
```

设置图片数组播放次数。

值为-1时表示无限播放，值为0时表示不播放，值大于0时表示有限的播放次数。

默认值为1。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationOptions-iterations?: int--><!--Device-AnimationOptions-iterations?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopMode

```TypeScript
stopMode?: AnimationStopMode
```

设置动图的停止模式。

默认值：AnimationStopMode.FIRST_FRAME，表示动图停止时回到首帧。

**Type:** [AnimationStopMode](arkts-arkui-arkui-drawabledescriptor-animationstopmode-e.md)

**Default:** AnimationStopMode.FIRST_FRAME

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationOptions-stopMode?: AnimationStopMode--><!--Device-AnimationOptions-stopMode?: AnimationStopMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

