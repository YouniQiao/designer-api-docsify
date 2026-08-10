# SimpleAnimatorOptions

animator简易动画参数对象。与AnimatorOptions相比，部分动画参数有默认值，可不设置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SimpleAnimatorOptions--><!--Device-unnamed-export declare class SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AnimatorOptions, SimpleAnimatorOptions, AnimatorResult } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(begin: double, end: double)
```

SimpleAnimatorOptions的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-constructor(begin: double, end: double)--><!--Device-SimpleAnimatorOptions-constructor(begin: double, end: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | double | Yes | 动画插值起点。 |
| end | double | Yes | 动画插值终点。 |

## delay

```TypeScript
delay(delay: int): SimpleAnimatorOptions
```

设置animator动画播放时延。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-delay(delay: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-delay(delay: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delay | int | Yes | 设置animator动画播放时延，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

## direction

```TypeScript
direction(direction: PlayMode): SimpleAnimatorOptions
```

设置animator动画播放方向。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [PlayMode](arkts-arkui-playmode-e.md) | Yes | 设置animator动画播放方向，默认值：PlayMode.Normal。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

## duration

```TypeScript
duration(duration: int): SimpleAnimatorOptions
```

设置animator动画时长。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-duration(duration: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-duration(duration: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | int | Yes | 设置动画时长，单位毫秒，默认值：1000。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

## easing

```TypeScript
easing(curve: string): SimpleAnimatorOptions
```

设置animator动画插值曲线。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | string | Yes | 设置animator动画插值曲线，默认值：“ease”。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

## fill

```TypeScript
fill(fillMode: FillMode): SimpleAnimatorOptions
```

设置animator动画填充方式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillMode | [FillMode](arkts-arkui-fillmode-e.md) | Yes | 设置animator动画填充方式，影响动画delay期间和结束时的表现，默认值：FillMode.Forwards。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

## iterations

```TypeScript
iterations(iterations: int): SimpleAnimatorOptions
```

设置animator动画播放次数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-iterations(iterations: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-iterations(iterations: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iterations | int | Yes | 设置animator动画播放次数，设置为0时不播放，设置为-1时无限次播放，默认值：1。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | Animator简易动画参数对象。 |

