# ProgressConfiguration

进度条配置。继承自[CommonConfiguration](../arkts-apis/arkts-arkui-common-commonconfiguration-i.md/arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** ProgressConfiguration extends [CommonConfiguration<ProgressConfiguration>](CommonConfiguration<ProgressConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface ProgressConfiguration extends CommonConfiguration<ProgressConfiguration>--><!--Device-unnamed-declare interface ProgressConfiguration extends CommonConfiguration<ProgressConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## total

```TypeScript
total: number
```

进度总长。

取值范围：(0, +∞)

**说明：**

total小于等于0时，按照100处理。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ProgressConfiguration-total: number--><!--Device-ProgressConfiguration-total: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: number
```

当前进度值。当设置的数值小于0时，将其置为0。当设置的数值大于total时，将其置为total。

默认值：0

取值范围：[0, total]

**说明：** 当Ring类型进度条的status设置为ProgressStatus.LOADING时，设置进度值不生效。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ProgressConfiguration-value: number--><!--Device-ProgressConfiguration-value: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

