# TransitionEffect

定义TransitionEffect类指定转场效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation(value: AnimateParam): TransitionEffect
```

指定该TransitionEffect的动画参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-common-animateparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## asymmetric

```TypeScript
static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect
```

设置非对称的转场效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [appear](arkts-arkui-common-asymmetrictransitionoption-i.md) | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) | 是 |
| [disappear](arkts-arkui-common-asymmetrictransitionoption-i.md) | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## combine

```TypeScript
combine(transitionEffect: TransitionEffect): TransitionEffect
```

对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transitionEffect | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## constructor('identity' | 'slideSwitch')

```TypeScript
constructor(type: 'identity' | 'slideSwitch', effect: undefined)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'identity' \| 'slideSwitch' | 是 |
| effect | undefined | 是 |

## constructor('opacity')

```TypeScript
constructor(type: 'opacity', effect: double)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'opacity' | 是 |
| effect | double | 是 |

## constructor('move')

```TypeScript
constructor(type: 'move', effect: TransitionEdge)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'move' | 是 |
| effect | [TransitionEdge](arkts-arkui-common-transitionedge-e.md) | 是 |

## constructor('translate')

```TypeScript
constructor(type: 'translate', effect: TranslateOptions)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'translate' | 是 |
| effect | [TranslateOptions](arkts-arkui-common-translateoptions-i.md) | 是 |

## constructor('rotate')

```TypeScript
constructor(type: 'rotate', effect: RotateOptions)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rotate' | 是 |
| effect | [RotateOptions](arkts-arkui-common-rotateoptions-i.md) | 是 |

## constructor('scale')

```TypeScript
constructor(type: 'scale', effect: ScaleOptions)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'scale' | 是 |
| effect | [ScaleOptions](arkts-arkui-common-scaleoptions-i.md) | 是 |

## constructor('asymmetric')

```TypeScript
constructor(type: 'asymmetric', effect: AsymmetricTransitionOption)
```

构造TransitionEffect对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'asymmetric' | 是 |
| effect | [AsymmetricTransitionOption](arkts-arkui-common-asymmetrictransitionoption-i.md) | 是 |

## move

```TypeScript
static move(edge: TransitionEdge): TransitionEffect
```

设置组件转场时从屏幕边缘滑入和滑出的效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| edge | [TransitionEdge](arkts-arkui-common-transitionedge-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## opacity

```TypeScript
static opacity(alpha: double): TransitionEffect
```

设置组件转场时的透明度效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | double | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## rotate

```TypeScript
static rotate(options: RotateOptions): TransitionEffect
```

设置组件转场时的旋转效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RotateOptions](arkts-arkui-common-rotateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## scale

```TypeScript
static scale(options: ScaleOptions): TransitionEffect
```

设置组件转场时的缩放效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScaleOptions](arkts-arkui-common-scaleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## translate

```TypeScript
static translate(options: TranslateOptions): TransitionEffect
```

设置组件转场时的平移效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TranslateOptions](arkts-arkui-common-translateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) |

## IDENTITY

```TypeScript
static get IDENTITY(): TransitionEffect
```

禁用转场效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## OPACITY

```TypeScript
static get OPACITY(): TransitionEffect
```

为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SLIDE

```TypeScript
static get SLIDE(): TransitionEffect
```

相当于TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))。从START边滑入，END边滑出。即在LTR模式下，从左侧滑入，右侧滑出；在RTL模式下，从右侧滑入，左侧滑出。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_SWITCH

```TypeScript
static get SLIDE_SWITCH(): TransitionEffect
```

指定出现时从右侧先缩小再放大滑入、消失时从左侧先缩小再放大滑出的转场效果。自带动画参数，也可覆盖动画参数，自带的动画参数时长600ms，指定动画曲线cubicBezierCurve(0.24, 0.0, 0.50, 1.0)， 最小缩放比例为0.8。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
