# FlexOptions

Describes the layout and alignment of child components within the Flex component.@interface FlexOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface FlexOptions--><!--Device-unnamed-export declare interface FlexOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
alignContent?: FlexAlign
```

Alignment mode of the child components in a multi-row Flex component along the cross axis. This parameter is valid only when wrap is set to Wrap or WrapReverse.

**Type:** [FlexAlign](../arkts-apis/arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-alignContent?: FlexAlign--><!--Device-FlexOptions-alignContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
alignItems?: ItemAlign
```

Alignment mode of the child components in the Flex component along the cross axis.

**Type:** [ItemAlign](../arkts-apis/arkts-arkui-itemalign-e.md)

**Default:** ItemAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-alignItems?: ItemAlign--><!--Device-FlexOptions-alignItems?: ItemAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: FlexDirection
```

Direction in which child components are arranged in the Flex component.

**Type:** [FlexDirection](../arkts-apis/arkts-arkui-flexdirection-e.md)

**Default:** FlexDirection.Row

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-direction?: FlexDirection--><!--Device-FlexOptions-direction?: FlexDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
justifyContent?: FlexAlign
```

Alignment mode of the child components in the Flex component along the main axis.

**Type:** [FlexAlign](../arkts-apis/arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-justifyContent?: FlexAlign--><!--Device-FlexOptions-justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: FlexSpaceOptions
```

Spacing between child components along the main axis or cross axis of the Flex component.

**Type:** [FlexSpaceOptions](arkts-arkui-flex-flexspaceoptions-i.md)

**Default:** {main: LengthMetrics.px(0), cross: LengthMetrics.px(0)}

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-space?: FlexSpaceOptions--><!--Device-FlexOptions-space?: FlexSpaceOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wrap

```TypeScript
wrap?: FlexWrap
```

Whether the Flex component has a single line or multiple lines.

**Type:** [FlexWrap](../arkts-apis/arkts-arkui-flexwrap-e.md)

**Default:** FlexWrap.NoWrap

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FlexOptions-wrap?: FlexWrap--><!--Device-FlexOptions-wrap?: FlexWrap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

