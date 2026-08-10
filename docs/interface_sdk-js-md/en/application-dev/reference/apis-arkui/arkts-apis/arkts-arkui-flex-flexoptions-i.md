# FlexOptions

设置Flex子组件的排列对齐方式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface FlexOptions--><!--Device-unnamed-export declare interface FlexOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
alignContent?: FlexAlign
```

当交叉轴存在额外空间时，多行内容之间的对齐方式。仅在wrap为Wrap或WrapReverse下生效。

**Type:** [FlexAlign](arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-alignContent?: FlexAlign--><!--Device-FlexOptions-alignContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
alignItems?: ItemAlign
```

所有子组件在Flex容器交叉轴上的对齐格式。

**Type:** [ItemAlign](arkts-arkui-itemalign-e.md)

**Default:** ItemAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-alignItems?: ItemAlign--><!--Device-FlexOptions-alignItems?: ItemAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: FlexDirection
```

子组件在Flex容器上排列的方向，即主轴的方向。

**Type:** [FlexDirection](arkts-arkui-flexdirection-e.md)

**Default:** FlexDirection.Row

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-direction?: FlexDirection--><!--Device-FlexOptions-direction?: FlexDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
justifyContent?: FlexAlign
```

所有子组件在Flex容器主轴上的对齐格式。

**Type:** [FlexAlign](arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-justifyContent?: FlexAlign--><!--Device-FlexOptions-justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: FlexSpaceOptions
```

所有子组件在Flex容器主轴或交叉轴的间距。

**Type:** [FlexSpaceOptions](../arkts-components/arkts-arkui-flexspaceoptions-i.md)

**Default:** {main: LengthMetrics.px(0), cross: LengthMetrics.px(0)}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-space?: FlexSpaceOptions--><!--Device-FlexOptions-space?: FlexSpaceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wrap

```TypeScript
wrap?: FlexWrap
```

Flex容器是单行/列还是多行/列排列。

**Type:** [FlexWrap](arkts-arkui-flexwrap-e.md)

**Default:** FlexWrap.NoWrap

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-wrap?: FlexWrap--><!--Device-FlexOptions-wrap?: FlexWrap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

