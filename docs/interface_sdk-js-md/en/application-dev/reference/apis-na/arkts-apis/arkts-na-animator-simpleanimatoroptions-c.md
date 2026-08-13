# SimpleAnimatorOptions

Defines the SimpleAnimatorOptions class.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class SimpleAnimatorOptions--><!--Device-unnamed-export declare class SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(begin: double, end: double)
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-constructor(begin: double, end: double)--><!--Device-SimpleAnimatorOptions-constructor(begin: double, end: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | double | Yes | Starting point of animator interpolation. |
| end | double | Yes | Ending point of animator interpolation. |

## delay

```TypeScript
delay(delay: int): SimpleAnimatorOptions
```

Set delay for the animation start. The default value indicates no delay.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-delay(delay: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-delay(delay: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delay | int | Yes | if not set, default is 0. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

## direction

```TypeScript
direction(direction: PlayMode): SimpleAnimatorOptions
```

Set the animation playback mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-direction(direction: PlayMode): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | PlayMode | Yes | if not set, default is PlayMode.Normal. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

## duration

```TypeScript
duration(duration: int): SimpleAnimatorOptions
```

Set duration of the animation, in milliseconds.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-duration(duration: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-duration(duration: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | int | Yes | if not set, default is 1000. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

## easing

```TypeScript
easing(curve: string): SimpleAnimatorOptions
```

Set time curve of the animation. For details about the supported types. linear The animation speed keeps unchanged. ease The animation starts and ends at a low speed, cubic-bezier(0.25, 0.1, 0.25, 1.0). ease-in The animation starts at a low speed, cubic-bezier(0.42, 0.0, 1.0, 1.0). ease-out The animation ends at a low speed, cubic-bezier(0.0, 0.0, 0.58, 1.0). ease-in-out The animation starts and ends at a low speed, cubic-bezier(0.42, 0.0, 0.58, 1.0). fast-out-slow-in Standard curve, cubic-bezier(0.4, 0.0, 0.2, 1.0). linear-out-slow-in Deceleration curve, cubic-bezier(0.0, 0.0, 0.2, 1.0). fast-out-linear-in Acceleration curve, cubic-bezier(0.4, 0.0, 1.0, 1.0). friction Damping curve, cubic-bezier(0.2, 0.0, 0.2, 1.0). extreme-deceleration Extreme deceleration curve, cubic-bezier(0.0, 0.0, 0.0, 1.0). sharp Sharp curve, cubic-bezier(0.33, 0.0, 0.67, 1.0). rhythm Rhythm curve, cubic-bezier(0.7, 0.0, 0.2, 1.0). smooth Smooth curve, cubic-bezier(0.4, 0.0, 0.4, 1.0). cubic-bezier(x1, y1, x2, y2) You can customize an animation speed curve in the cubic-bezier() function. The x and y values of each input parameter must be between 0 and 1. Step curve. The number must be set and only an integer is supported, step-position is optional. It can be set to start or end. The default value is end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-easing(curve: string): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | string | Yes | if not set, default is ease. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

## fill

```TypeScript
fill(fillMode: FillMode): SimpleAnimatorOptions
```

Set FillMode of animation. FillMode indicates whether to resume to the initial state after the animation is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-fill(fillMode: FillMode): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillMode | FillMode | Yes | if not set, default is FillMode.Forwards. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

## iterations

```TypeScript
iterations(iterations: int): SimpleAnimatorOptions
```

Set number of times the animation will be played. Number indicates a fixed number of playback operations, and -1 an unlimited number of playback operations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SimpleAnimatorOptions-iterations(iterations: int): SimpleAnimatorOptions--><!--Device-SimpleAnimatorOptions-iterations(iterations: int): SimpleAnimatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iterations | int | Yes | if not set, default is 1. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) |  |

