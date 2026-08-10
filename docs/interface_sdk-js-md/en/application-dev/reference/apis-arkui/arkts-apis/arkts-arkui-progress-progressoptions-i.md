# ProgressOptions

进度条选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ProgressOptions--><!--Device-unnamed-export declare interface ProgressOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## total

```TypeScript
total?: double
```

指定进度总长。设置小于等于0的数值时置为100。默认值：100。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressOptions-total?: double--><!--Device-ProgressOptions-total?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: ProgressType
```

指定进度条类型。默认值：ProgressType.Linear。

**Type:** [ProgressType](arkts-arkui-progress-progresstype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressOptions-type?: ProgressType--><!--Device-ProgressOptions-type?: ProgressType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: double
```

指定当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。取值范围：[0, total]。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressOptions-value: double--><!--Device-ProgressOptions-value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

