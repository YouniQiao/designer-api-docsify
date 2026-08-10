# Curve

插值曲线，动效请参考&lt;!--RP1--&gt;[贝塞尔曲线](../../../../design/ux-design/animation-attributes.md)&lt;!--RP1End--&gt;。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum Curve--><!--Device-unnamed-declare enum Curve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Linear

```TypeScript
Linear
```

表示动画在整个过程中速度保持一致。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Linear--><!--Device-Curve-Linear-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Ease

```TypeScript
Ease
```

表示动画以低速开始，然后加快，在结束前减速，CubicBezier(0.25, 0.1, 0.25, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Ease--><!--Device-Curve-Ease-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EaseIn

```TypeScript
EaseIn
```

表示动画以低速开始，CubicBezier(0.42, 0.0, 1.0, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-EaseIn--><!--Device-Curve-EaseIn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EaseOut

```TypeScript
EaseOut
```

表示动画以低速结束，CubicBezier(0.0, 0.0, 0.58, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-EaseOut--><!--Device-Curve-EaseOut-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EaseInOut

```TypeScript
EaseInOut
```

表示动画以低速开始和结束，CubicBezier(0.42, 0.0, 0.58, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-EaseInOut--><!--Device-Curve-EaseInOut-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FastOutSlowIn

```TypeScript
FastOutSlowIn
```

标准曲线，CubicBezier(0.4, 0.0, 0.2, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-FastOutSlowIn--><!--Device-Curve-FastOutSlowIn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LinearOutSlowIn

```TypeScript
LinearOutSlowIn
```

减速曲线，CubicBezier(0.0, 0.0, 0.2, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-LinearOutSlowIn--><!--Device-Curve-LinearOutSlowIn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FastOutLinearIn

```TypeScript
FastOutLinearIn
```

加速曲线，CubicBezier(0.4, 0.0, 1.0, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-FastOutLinearIn--><!--Device-Curve-FastOutLinearIn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ExtremeDeceleration

```TypeScript
ExtremeDeceleration
```

急缓曲线，CubicBezier(0.0, 0.0, 0.0, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-ExtremeDeceleration--><!--Device-Curve-ExtremeDeceleration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Sharp

```TypeScript
Sharp
```

锐利曲线，CubicBezier(0.33, 0.0, 0.67, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Sharp--><!--Device-Curve-Sharp-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Rhythm

```TypeScript
Rhythm
```

节奏曲线，CubicBezier(0.7, 0.0, 0.2, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Rhythm--><!--Device-Curve-Rhythm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Smooth

```TypeScript
Smooth
```

平滑曲线，CubicBezier(0.4, 0.0, 0.4, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Smooth--><!--Device-Curve-Smooth-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Friction

```TypeScript
Friction
```

阻尼曲线，CubicBezier(0.2, 0.0, 0.2, 1.0)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Curve-Friction--><!--Device-Curve-Friction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

