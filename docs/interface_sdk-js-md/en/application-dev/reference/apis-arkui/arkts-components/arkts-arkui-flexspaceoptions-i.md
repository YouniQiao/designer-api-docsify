# FlexSpaceOptions

设置Flex容器的子组件在主轴或交叉轴的间距。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface FlexSpaceOptions--><!--Device-unnamed-declare interface FlexSpaceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cross

```TypeScript
cross?: LengthMetrics
```

Flex容器交叉轴上相邻行之间的间距。设置后，交叉轴方向相邻行之间将按指定间距进行分隔，仅在多行布局（wrap为Wrap或WrapReverse）时生效。当space.cross为负数，或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，该参数不生效。

默认值：LengthMetrics.px(0)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FlexSpaceOptions-cross?: LengthMetrics--><!--Device-FlexSpaceOptions-cross?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## main

```TypeScript
main?: LengthMetrics
```

Flex容器主轴上相邻子组件之间的间距。设置后，主轴方向相邻子组件之间将按指定间距进行分隔，在单行或多行布局时均生效。当space.main为负数，或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，该参数不生效。

默认值：LengthMetrics.px(0)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FlexSpaceOptions-main?: LengthMetrics--><!--Device-FlexSpaceOptions-main?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

