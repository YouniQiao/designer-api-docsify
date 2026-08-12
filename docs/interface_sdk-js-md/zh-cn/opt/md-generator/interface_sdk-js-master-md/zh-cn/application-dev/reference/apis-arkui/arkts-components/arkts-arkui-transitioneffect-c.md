# TransitionEffect

定义TransitionEffect类指定转场效果。

**起始版本：** 10

<!--Device-unnamed-declare class TransitionEffect<  Type extends keyof TransitionEffects = keyof TransitionEffects,  Effect extends TransitionEffects[Type] = TransitionEffects[Type]>--><!--Device-unnamed-declare class TransitionEffect<  Type extends keyof TransitionEffects = keyof TransitionEffects,  Effect extends TransitionEffects[Type] = TransitionEffects[Type]>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation(value: AnimateParam): TransitionEffect
```

指定该TransitionEffect的动画参数。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect--><!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-animateparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md) |

## asymmetric

```TypeScript
static asymmetric(
    appear: TransitionEffect,
    disappear: TransitionEffect
  ): TransitionEffect<"asymmetric">
```

设置非对称的转场效果，即出现、消失为两套独立不同的动画，效果不互为逆过程。具体效果可参考  
[示例2](../../../reference/apis-arkui/arkui-ts/ts-transition-animation-component.md#示例2使用不同接口实现图片出现消失)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static asymmetric(    appear: TransitionEffect,    disappear: TransitionEffect  ): TransitionEffect<"asymmetric">--><!--Device-TransitionEffect-static asymmetric(    appear: TransitionEffect,    disappear: TransitionEffect  ): TransitionEffect<"asymmetric">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [appear](../arkts-apis/arkts-arkui-common-asymmetrictransitionoption-i.md) | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | 是 |
| [disappear](../arkts-apis/arkts-arkui-common-asymmetrictransitionoption-i.md) | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"asymmetric"&gt; |

## combine

```TypeScript
combine(transitionEffect: TransitionEffect): TransitionEffect
```

对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect--><!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transitionEffect | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md) |

## constructor

```TypeScript
constructor(type: Type, effect: Effect)
```

构造TransitionEffect对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-constructor(type: Type, effect: Effect)--><!--Device-TransitionEffect-constructor(type: Type, effect: Effect)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | 是 |
| effect | [Effect](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-effect-i.md) | 是 |

## move

```TypeScript
static move(edge: TransitionEdge): TransitionEffect<"move">
```

设置组件转场时从屏幕边缘滑入和滑出的效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect<"move">--><!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect<"move">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| edge | [TransitionEdge](arkts-arkui-transitionedge-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"move"&gt; |

## opacity

```TypeScript
static opacity(alpha: number): TransitionEffect<"opacity">
```

设置组件转场时的透明度效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static opacity(alpha: number): TransitionEffect<"opacity">--><!--Device-TransitionEffect-static opacity(alpha: number): TransitionEffect<"opacity">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | number | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"opacity"&gt; |

## rotate

```TypeScript
static rotate(options: RotateOptions): TransitionEffect<"rotate">
```

设置组件转场时的旋转效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect<"rotate">--><!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect<"rotate">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RotateOptions](arkts-arkui-rotateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"rotate"&gt; |

## scale

```TypeScript
static scale(options: ScaleOptions): TransitionEffect<"scale">
```

设置组件转场时的缩放效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect<"scale">--><!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect<"scale">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"scale"&gt; |

## translate

```TypeScript
static translate(options: TranslateOptions): TransitionEffect<"translate">
```

设置组件转场时的平移效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect<"translate">--><!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect<"translate">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TranslateOptions](arkts-arkui-translateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"translate"&gt; |

## IDENTITY

```TypeScript
static readonly IDENTITY: TransitionEffect<"identity">
```

禁用转场效果。

**类型：** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"identity"&gt;

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static readonly IDENTITY: TransitionEffect<"identity">--><!--Device-TransitionEffect-static readonly IDENTITY: TransitionEffect<"identity">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## OPACITY

```TypeScript
static readonly OPACITY: TransitionEffect<"opacity">
```

为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0)。

**类型：** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"opacity"&gt;

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static readonly OPACITY: TransitionEffect<"opacity">--><!--Device-TransitionEffect-static readonly OPACITY: TransitionEffect<"opacity">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SLIDE

```TypeScript
static readonly SLIDE: TransitionEffect<
    "asymmetric",
    {
      appear: TransitionEffect<"move", TransitionEdge>;
      disappear: TransitionEffect<"move", TransitionEdge>;
    }
  >
```

相当于TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))。从START边滑入，END边滑出。即在LTR模式下，从左侧滑入，右侧滑出；在RTL模式下，从右侧滑入，左侧滑出。

**类型：** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"asymmetric", {       appear: TransitionEffect&lt;"move", [TransitionEdge](arkts-arkui-transitionedge-e.md)&gt;;       disappear: TransitionEffect&lt;"move", TransitionEdge&gt;;     }&gt;

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static readonly SLIDE: TransitionEffect<    "asymmetric",    {      appear: TransitionEffect<"move", TransitionEdge>;      disappear: TransitionEffect<"move", TransitionEdge>;    }  >--><!--Device-TransitionEffect-static readonly SLIDE: TransitionEffect<    "asymmetric",    {      appear: TransitionEffect<"move", TransitionEdge>;      disappear: TransitionEffect<"move", TransitionEdge>;    }  >-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_SWITCH

```TypeScript
static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">
```

指定出现时从右侧先缩小再放大滑入、消失时从左侧先缩小再放大滑出的转场效果。自带动画参数，也可覆盖动画参数，自带的动画参数时长600ms，指定动画曲线cubicBezierCurve(0.24, 0.0, 0.50, 1.0)，最小缩放比例为0.8。

**类型：** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"slideSwitch"&gt;

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-TransitionEffect-static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">--><!--Device-TransitionEffect-static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
