# ExpectedFrameRateRange

设置动画期望的帧率。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ExpectedFrameRateRange--><!--Device-unnamed-export declare interface ExpectedFrameRateRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expected

```TypeScript
expected: int
```

期望的最优帧率，单位为帧/秒（fps）。

取值范围为[min, max]。设置为0时，将跟随应用的帧率。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpectedFrameRateRange-expected: int--><!--Device-ExpectedFrameRateRange-expected: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max: int
```

期望的最大帧率，单位为帧/秒（fps）。

取值范围为[min, 设备最大帧率]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpectedFrameRateRange-max: int--><!--Device-ExpectedFrameRateRange-max: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min: int
```

期望的最小帧率，单位为帧/秒（fps）。

取值范围为[0, 设备最大帧率]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpectedFrameRateRange-min: int--><!--Device-ExpectedFrameRateRange-min: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

