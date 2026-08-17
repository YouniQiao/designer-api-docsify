# ComposeTitleBarV2

Declaration of the composable title bar. Composable title bar represents a common title bar that contains a title, subtitle (optional), and profile picture (optional). It can come with a Back button for switching between pages of different levels.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare struct ComposeTitleBarV2--><!--Device-unnamed-export declare struct ComposeTitleBarV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarV2-@Builder  build(): void--><!--Device-ComposeTitleBarV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## item

```TypeScript
@Param
  item?: ComposeTitleBarV2MenuItem
```

A single menu item for the profile picture on the left.

**Type:** [ComposeTitleBarV2MenuItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-composetitlebarv2-composetitlebarv2menuitem-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarV2-@Param  item?: ComposeTitleBarV2MenuItem--><!--Device-ComposeTitleBarV2-@Param  item?: ComposeTitleBarV2MenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
@Param
  menuItems?: Array<ComposeTitleBarV2MenuItem>
```

Menu items on the right side.

**Type:** Array&lt;[ComposeTitleBarV2MenuItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-composetitlebarv2-composetitlebarv2menuitem-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarV2-@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>--><!--Device-ComposeTitleBarV2-@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
@Param
  subtitle?: ResourceStr
```

Sub-title of this title bar.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarV2-@Param  subtitle?: ResourceStr--><!--Device-ComposeTitleBarV2-@Param  subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Param
  title: ResourceStr
```

Title of this title bar.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarV2-@Param  title: ResourceStr--><!--Device-ComposeTitleBarV2-@Param  title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

