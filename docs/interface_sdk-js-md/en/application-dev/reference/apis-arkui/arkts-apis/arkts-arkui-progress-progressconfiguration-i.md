# ProgressConfiguration

进度条配置。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** ProgressConfiguration extends [CommonConfiguration<ProgressConfiguration>](CommonConfiguration<ProgressConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ProgressConfiguration extends CommonConfiguration<ProgressConfiguration>--><!--Device-unnamed-export declare interface ProgressConfiguration extends CommonConfiguration<ProgressConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## total

```TypeScript
total: double
```

进度总长。

默认值：100

**说明：**

total是负数时，按照100处理。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressConfiguration-total: double--><!--Device-ProgressConfiguration-total: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: double
```

当前进度值。当设置的数值小于0时，将其置为0。当设置的数值大于total时，将其置为total。

默认值：0

取值范围：[0, total]

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressConfiguration-value: double--><!--Device-ProgressConfiguration-value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

