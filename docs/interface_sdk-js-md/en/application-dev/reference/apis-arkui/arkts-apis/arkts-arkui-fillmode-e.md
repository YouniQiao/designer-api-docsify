# FillMode

设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正播的最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum FillMode--><!--Device-unnamed-declare enum FillMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None
```

动画未执行时，不应用任何样式到目标；播放完成后，恢复初始默认状态。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-FillMode-None--><!--Device-FillMode-None-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Forwards

```TypeScript
Forwards
```

目标将保留动画执行期间最后一个关键帧的状态。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-FillMode-Forwards--><!--Device-FillMode-Forwards-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Backwards

```TypeScript
Backwards
```

动画应用于目标时，立即采用第一个关键帧定义的值，并在delay期间保留此值。第一个关键帧取决于playMode，playMode为Normal或Alternate时，帧为from状态；playMode为Reverse或AlternateReverse时，帧为to状态。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-FillMode-Backwards--><!--Device-FillMode-Backwards-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Both

```TypeScript
Both
```

动画将遵循Forwards和Backwards的规则，从而在两个方向上扩展动画属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-FillMode-Both--><!--Device-FillMode-Both-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

