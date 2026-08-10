# ExpectedFrameRateRange

设置动画期望的帧率。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface ExpectedFrameRateRange--><!--Device-unnamed-declare interface ExpectedFrameRateRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expected

```TypeScript
expected: number
```

期望的最优帧率，单位为帧/秒（fps）。

取值范围为[min, max]。设置为0时，将跟随应用的帧率。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpectedFrameRateRange-expected: number--><!--Device-ExpectedFrameRateRange-expected: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max: number
```

期望的最大帧率，单位为帧/秒（fps）。

取值范围为[min, 设备最大帧率]。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpectedFrameRateRange-max: number--><!--Device-ExpectedFrameRateRange-max: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min: number
```

期望的最小帧率，单位为帧/秒（fps）。

取值范围为[0, 设备最大帧率]。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpectedFrameRateRange-min: number--><!--Device-ExpectedFrameRateRange-min: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

