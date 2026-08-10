# ProgressOptions

进度条选项。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface ProgressOptions<Type extends keyof ProgressStyleMap>--><!--Device-unnamed-declare interface ProgressOptions<Type extends keyof ProgressStyleMap>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ProgressStyle
```

指定进度条样式。

从API version 7开始支持，从API version 8开始废弃。建议使用[type](arkts-arkui-progresstype-e.md)替代。

默认值：ProgressStyle.Linear

**Type:** [ProgressStyle](arkts-arkui-progressstyle-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** [type](arkts-arkui-progressoptions-i.md#type)

<!--Device-ProgressOptions-style?: ProgressStyle--><!--Device-ProgressOptions-style?: ProgressStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## total

```TypeScript
total?: number
```

指定进度总长。设置小于0的数值时置为100。

默认值：100

取值范围：(0, +∞)。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressOptions-total?: number--><!--Device-ProgressOptions-total?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: Type
```

指定进度条类型。

默认值：ProgressType.Linear

**说明：** 不同的type需分别对应相应的[style](ProgressAttribute#style)属性设置，详细映射关系参考
[ProgressStyleMap](../../../reference/apis-arkui/arkui-ts/ts-basic-components-progress.md#progressstylemap10)。

**Type:** [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressOptions-type?: Type--><!--Device-ProgressOptions-type?: Type-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: number
```

指定当前进度值。

默认值：0

取值范围：[0, total]，设置小于0的数值时置为0，设置大于total的数值时置为total，设置非法值时按默认值处理。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressOptions-value: number--><!--Device-ProgressOptions-value: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

