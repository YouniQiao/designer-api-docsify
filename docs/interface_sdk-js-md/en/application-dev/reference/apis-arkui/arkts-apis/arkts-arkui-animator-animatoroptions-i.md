# AnimatorOptions

定义动画选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface AnimatorOptions--><!--Device-unnamed-export interface AnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AnimatorOptions, SimpleAnimatorOptions, AnimatorResult } from 'kits/@kit.ArkUI';
```

## begin

```TypeScript
begin: double
```

动画插值起点。

默认值：0

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-begin: double--><!--Device-AnimatorOptions-begin: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay: int
```

动画延时播放时长，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-delay: int--><!--Device-AnimatorOptions-delay: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: "normal" | "reverse" | "alternate" | "alternate-reverse"
```

动画播放模式。

**Type:** "normal" \| "reverse" \| "alternate" \| "alternate-reverse"

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-direction: "normal" | "reverse" | "alternate" | "alternate-reverse"--><!--Device-AnimatorOptions-direction: "normal" | "reverse" | "alternate" | "alternate-reverse"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration: int
```

动画播放的时长，单位毫秒。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-duration: int--><!--Device-AnimatorOptions-duration: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## easing

```TypeScript
easing: string
```

动画插值曲线，非法字符串时取:"ease"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-easing: string--><!--Device-AnimatorOptions-easing: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end: double
```

动画插值终点。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-end: double--><!--Device-AnimatorOptions-end: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fill

```TypeScript
fill: "none" | "forwards" | "backwards" | "both"
```

动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。

**Type:** "none" \| "forwards" \| "backwards" \| "both"

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-fill: "none" | "forwards" | "backwards" | "both"--><!--Device-AnimatorOptions-fill: "none" | "forwards" | "backwards" | "both"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iterations

```TypeScript
iterations: int
```

动画播放次数。设置为0时不播放，设置为-1时无限次播放，设置大于0时为播放次数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorOptions-iterations: int--><!--Device-AnimatorOptions-iterations: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

