# TransitionEffect

Defines the transition effect by using the provided APIs, as listed below.

**Since:** 10

<!--Device-unnamed-declare class TransitionEffect<  Type extends keyof TransitionEffects = keyof TransitionEffects,  Effect extends TransitionEffects[Type] = TransitionEffects[Type]>--><!--Device-unnamed-declare class TransitionEffect<  Type extends keyof TransitionEffects = keyof TransitionEffects,  Effect extends TransitionEffects[Type] = TransitionEffects[Type]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation(value: AnimateParam): TransitionEffect
```

Animation settings.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect--><!--Device-TransitionEffect-animation(value: AnimateParam): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-animateparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md) |

## asymmetric

```TypeScript
static asymmetric(
    appear: TransitionEffect,
    disappear: TransitionEffect
  ): TransitionEffect<"asymmetric">
```

Sets the asymmetric transition effect.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static asymmetric(    appear: TransitionEffect,    disappear: TransitionEffect  ): TransitionEffect<"asymmetric">--><!--Device-TransitionEffect-static asymmetric(    appear: TransitionEffect,    disappear: TransitionEffect  ): TransitionEffect<"asymmetric">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appear | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | Yes |
| disappear | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"asymmetric"&gt; |

## combine

```TypeScript
combine(transitionEffect: TransitionEffect): TransitionEffect
```

Combination of transition effects.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect--><!--Device-TransitionEffect-combine(transitionEffect: TransitionEffect): TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transitionEffect | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md) |

## constructor

```TypeScript
constructor(type: Type, effect: Effect)
```

Constructs a **TransitionEffect** object.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-constructor(type: Type, effect: Effect)--><!--Device-TransitionEffect-constructor(type: Type, effect: Effect)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Yes |
| effect | [Effect](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-effect-i.md) | Yes |

## move

```TypeScript
static move(edge: TransitionEdge): TransitionEffect<"move">
```

Sets the slide-in and slide-out effects for component transitions from the screen edges.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect<"move">--><!--Device-TransitionEffect-static move(edge: TransitionEdge): TransitionEffect<"move">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| edge | [TransitionEdge](arkts-arkui-transitionedge-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"move"&gt; |

## opacity

```TypeScript
static opacity(alpha: number): TransitionEffect<"opacity">
```

Sets the opacity for component transition.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static opacity(alpha: number): TransitionEffect<"opacity">--><!--Device-TransitionEffect-static opacity(alpha: number): TransitionEffect<"opacity">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alpha | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"opacity"&gt; |

## rotate

```TypeScript
static rotate(options: RotateOptions): TransitionEffect<"rotate">
```

Sets the rotation effect for component transitions.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect<"rotate">--><!--Device-TransitionEffect-static rotate(options: RotateOptions): TransitionEffect<"rotate">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RotateOptions](arkts-arkui-rotateoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"rotate"&gt; |

## scale

```TypeScript
static scale(options: ScaleOptions): TransitionEffect<"scale">
```

Sets the scaling effect for component transitions.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect<"scale">--><!--Device-TransitionEffect-static scale(options: ScaleOptions): TransitionEffect<"scale">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"scale"&gt; |

## translate

```TypeScript
static translate(options: TranslateOptions): TransitionEffect<"translate">
```

Sets the translation effect for component transitions.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect<"translate">--><!--Device-TransitionEffect-static translate(options: TranslateOptions): TransitionEffect<"translate">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TranslateOptions](arkts-arkui-translateoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"translate"&gt; |

## IDENTITY

```TypeScript
static readonly IDENTITY: TransitionEffect<"identity">
```

Disables the transition effect.

**Type:** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"identity"&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static readonly IDENTITY: TransitionEffect<"identity">--><!--Device-TransitionEffect-static readonly IDENTITY: TransitionEffect<"identity">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OPACITY

```TypeScript
static readonly OPACITY: TransitionEffect<"opacity">
```

Applies a transition effect with the opacity changing from 0 to 1 when the component appears and from 1 to 0 when the component disappears. This is equivalent to **TransitionEffect.opacity(0)**.

**Type:** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"opacity"&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static readonly OPACITY: TransitionEffect<"opacity">--><!--Device-TransitionEffect-static readonly OPACITY: TransitionEffect<"opacity">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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

Applies a transition effect of sliding in from the start edge when the component appears and sliding out from the end edge when the component disappears. This means sliding in from the left edge and sliding out from the right edge for left-to-right scripts, and sliding in from the right edge and sliding out from the left edge for right-to-left scripts. This is equivalent to   
**TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))**.

**Type:** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"asymmetric", {       appear: TransitionEffect&lt;"move", TransitionEdge&gt;;       disappear: TransitionEffect&lt;"move", TransitionEdge&gt;;     }&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static readonly SLIDE: TransitionEffect<    "asymmetric",    {      appear: TransitionEffect<"move", TransitionEdge>;      disappear: TransitionEffect<"move", TransitionEdge>;    }  >--><!--Device-TransitionEffect-static readonly SLIDE: TransitionEffect<    "asymmetric",    {      appear: TransitionEffect<"move", TransitionEdge>;      disappear: TransitionEffect<"move", TransitionEdge>;    }  >-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_SWITCH

```TypeScript
static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">
```

Applies a transition effect of sliding in from the right with first scaling down and then scaling up when the component appears and sliding out from the left with first scaling down and then scaling up when the component disappears. This transition effect comes with its own animation parameters, which can also be overridden. The default animation duration is 600 milliseconds, with a specified animation curve of cubicBezierCurve(0.24, 0.0, 0.50, 1.0) and a minimum scale factor of 0.8.

**Type:** [TransitionEffect](arkts-arkui-transitioneffect-c.md)&lt;"slideSwitch"&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TransitionEffect-static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">--><!--Device-TransitionEffect-static readonly SLIDE_SWITCH: TransitionEffect<"slideSwitch">-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
