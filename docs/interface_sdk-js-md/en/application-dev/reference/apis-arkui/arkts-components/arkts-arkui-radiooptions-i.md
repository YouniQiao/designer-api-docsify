# RadioOptions

单选框的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface RadioOptions--><!--Device-unnamed-declare interface RadioOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## group

```TypeScript
group: string
```

当前单选框的所属群组名称，相同group的单选框只能有一个被选中。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RadioOptions-group: string--><!--Device-RadioOptions-group: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorBuilder

```TypeScript
indicatorBuilder?: CustomBuilder
```

配置单选框的选中样式为自定义组件。自定义组件与Radio组件以中心点对齐显示。indicatorBuilder设置为undefined时，按照RadioIndicatorType.TICK进行显示。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RadioOptions-indicatorBuilder?: CustomBuilder--><!--Device-RadioOptions-indicatorBuilder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorType

```TypeScript
indicatorType?: RadioIndicatorType
```

配置单选框的选中样式。未设置时按照RadioIndicatorType.TICK进行显示。

**Type:** [RadioIndicatorType](../arkts-apis/arkts-arkui-radio-radioindicatortype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RadioOptions-indicatorType?: RadioIndicatorType--><!--Device-RadioOptions-indicatorType?: RadioIndicatorType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string
```

当前单选框的值。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RadioOptions-value: string--><!--Device-RadioOptions-value: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

