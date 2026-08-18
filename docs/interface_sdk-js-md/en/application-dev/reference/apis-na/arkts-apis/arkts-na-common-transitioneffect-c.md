# TransitionEffect

Defines the transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class TransitionEffect--><!--Device-unnamed-export declare class TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation(value: AnimateParam): TransitionEffect
```

Set the animation of current transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect--><!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimateParam](arkts-na-common-animateparam-i.md) | Yes | animation parameters |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## asymmetric

```TypeScript
static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect
```

Creates an asymmetric transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect--><!--Device-TransitionEffect-static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appear | [TransitionEffect](arkts-na-common-transitioneffect-c.md) | Yes | the transition which will be attached when the component is appear |
| disappear | [TransitionEffect](arkts-na-common-transitioneffect-c.md) | Yes | the transition which will be attached when the component is disappear |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## combine

```TypeScript
combine(transitionEffect: TransitionEffect): TransitionEffect
```

Combines another transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect--><!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transitionEffect | [TransitionEffect](arkts-na-common-transitioneffect-c.md) | Yes | transition effect which is be combined |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) | combined transition effect |

## constructor('identity' | 'slideSwitch')

```TypeScript
constructor(type: 'identity' | 'slideSwitch', effect: undefined)
```

identity or slideSwitch TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'identity' | 'slideSwitch', effect: undefined)--><!--Device-TransitionEffect-constructor(type: 'identity' | 'slideSwitch', effect: undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'identity' \| 'slideSwitch' | Yes | transition type |
| effect | undefined | Yes | transition options |

## constructor('opacity')

```TypeScript
constructor(type: 'opacity', effect: double)
```

opacity TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'opacity', effect: double)--><!--Device-TransitionEffect-constructor(type: 'opacity', effect: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'opacity' | Yes | transition type |
| effect | double | Yes | transition options |

## constructor('move')

```TypeScript
constructor(type: 'move', effect: TransitionEdge)
```

move TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'move', effect: TransitionEdge)--><!--Device-TransitionEffect-constructor(type: 'move', effect: TransitionEdge)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'move' | Yes | transition type |
| effect | [TransitionEdge](arkts-na-common-transitionedge-e.md) | Yes | transition options |

## constructor('translate')

```TypeScript
constructor(type: 'translate', effect: TranslateOptions)
```

translate TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'translate', effect: TranslateOptions)--><!--Device-TransitionEffect-constructor(type: 'translate', effect: TranslateOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'translate' | Yes | transition type |
| effect | [TranslateOptions](arkts-na-common-translateoptions-i.md) | Yes | transition options |

## constructor('rotate')

```TypeScript
constructor(type: 'rotate', effect: RotateOptions)
```

rotate TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'rotate', effect: RotateOptions)--><!--Device-TransitionEffect-constructor(type: 'rotate', effect: RotateOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'rotate' | Yes | transition type |
| effect | [RotateOptions](arkts-na-common-rotateoptions-i.md) | Yes | transition options |

## constructor('scale')

```TypeScript
constructor(type: 'scale', effect: ScaleOptions)
```

scale TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'scale', effect: ScaleOptions)--><!--Device-TransitionEffect-constructor(type: 'scale', effect: ScaleOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scale' | Yes | transition type |
| effect | [ScaleOptions](arkts-na-common-scaleoptions-i.md) | Yes | transition options |

## constructor('asymmetric')

```TypeScript
constructor(type: 'asymmetric', effect: AsymmetricTransitionOption)
```

asymmetric TransitionEffect constructor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-constructor(type: 'asymmetric', effect: AsymmetricTransitionOption)--><!--Device-TransitionEffect-constructor(type: 'asymmetric', effect: AsymmetricTransitionOption)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'asymmetric' | Yes | transition type |
| effect | [AsymmetricTransitionOption](arkts-na-common-asymmetrictransitionoption-i.md) | Yes | transition options |

## move

```TypeScript
static move(edge: TransitionEdge): TransitionEffect
```

Creates a move transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect--><!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edge | [TransitionEdge](arkts-na-common-transitionedge-e.md) | Yes | the edge that component will move to |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## opacity

```TypeScript
static opacity(alpha: double): TransitionEffect
```

Creates an opacity transition effect with alpha value

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static opacity(alpha: double): TransitionEffect--><!--Device-TransitionEffect-static opacity(alpha: double): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | double | Yes | opacity alpha value, value range [0, 1]. Illegal values less than 0 are treated as 0, and illegal values greater than 1 are treated as 1. |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## rotate

```TypeScript
static rotate(options: RotateOptions): TransitionEffect
```

Creates a rotation transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect--><!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RotateOptions](arkts-na-common-rotateoptions-i.md) | Yes | rotate options Set the rotation effect for component transitions when inserting and deleting. The value represents the starting rotation point for the inserting animation and the ending rotation point for the deleting animation. -x: Horizontal component of the rotational vector. -y: Vertical component of the rotational vector. -z: Vertical component of the rotational vector. -centerX, centerY specify the rotation center point, with default values of "50%", meaning that the default rotation center point is the center point of the component. -The center point of (0, 0) represents the upper-left corner of the component. -centerZ refers to the Z-axis anchor point. The default value of centerZ is 0. -perspective indicates the visual distance. The perspective property does not support transition animation. |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## scale

```TypeScript
static scale(options: ScaleOptions): TransitionEffect
```

Creates a scale transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect--><!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScaleOptions](arkts-na-common-scaleoptions-i.md) | Yes | scale options |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

## translate

```TypeScript
static translate(options: TranslateOptions): TransitionEffect
```

Creates a translate transition effect

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect--><!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TranslateOptions](arkts-na-common-translateoptions-i.md) | Yes | translate options |

**Return value:**

| Type | Description |
| --- | --- |
| [TransitionEffect](arkts-na-common-transitioneffect-c.md) |  |

