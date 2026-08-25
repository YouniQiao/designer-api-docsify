# FlexOptions

Describes the layout and alignment of child components within the Flex component.@interface FlexOptions

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
alignContent?: FlexAlign
```

Alignment mode of the child components in a multi-row Flex component along the cross axis. This parameter is valid only when wrap is set to Wrap or WrapReverse.

**Type:** [FlexAlign](arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
alignItems?: ItemAlign
```

Alignment mode of the child components in the Flex component along the cross axis.

**Type:** [ItemAlign](arkts-arkui-itemalign-e.md)

**Default:** ItemAlign.Start

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: FlexDirection
```

Direction in which child components are arranged in the Flex component.

**Type:** [FlexDirection](arkts-arkui-flexdirection-e.md)

**Default:** FlexDirection.Row

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
justifyContent?: FlexAlign
```

Alignment mode of the child components in the Flex component along the main axis.

**Type:** [FlexAlign](arkts-arkui-flexalign-e.md)

**Default:** FlexAlign.Start

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: FlexSpaceOptions
```

Spacing between child components along the main axis or cross axis of the Flex component.

**Type:** [FlexSpaceOptions](arkts-arkui-flex-flexspaceoptions-i.md)

**Default:** {main: LengthMetrics.px(0), cross: LengthMetrics.px(0)}

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wrap

```TypeScript
wrap?: FlexWrap
```

Whether the Flex component has a single line or multiple lines.

**Type:** [FlexWrap](arkts-arkui-flexwrap-e.md)

**Default:** FlexWrap.NoWrap

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
