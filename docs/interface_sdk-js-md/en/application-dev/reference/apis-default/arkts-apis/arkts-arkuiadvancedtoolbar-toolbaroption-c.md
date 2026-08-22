# ToolBarOption

Defines the content and attributes of a toolbar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ToolBarOption--><!--Device-unnamed-export declare class ToolBarOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## accessibilityDescription

```TypeScript
public accessibilityDescription?: ResourceStr
```

Accessible description of the toolbar item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public accessibilityDescription?: ResourceStr--><!--Device-ToolBarOption-public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

Accessibility level of the toolbar item. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Type:** string

**Default:** "auto"

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public accessibilityLevel?: string--><!--Device-ToolBarOption-public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

Accessibility text, that is, accessible label name, of the toolbar item. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of **content**

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public accessibilityText?: ResourceStr--><!--Device-ToolBarOption-public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

Click event of the toolbar item.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public action?: () => void--><!--Device-ToolBarOption-public action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedIconColor

```TypeScript
public activatedIconColor?: ResourceColor
```

Icon fill color of the toolbar option in the activated state.

Default value: **\$r('sys.color.icon_emphasize')**

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public activatedIconColor?: ResourceColor--><!--Device-ToolBarOption-public activatedIconColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedTextColor

```TypeScript
public activatedTextColor?: ResourceColor
```

Font color of the toolbar item in the activated state.

Default value: **\$r('sys.color.font_emphasize')**

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public activatedTextColor?: ResourceColor--><!--Device-ToolBarOption-public activatedTextColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
public content: ResourceStr
```

Text of the toolbar item.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public content: ResourceStr--><!--Device-ToolBarOption-public content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
public icon?: Resource
```

Icon of the toolbar item.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

If **toolBarSymbolOptions** has input parameters, **icon** is ineffective.

**Type:** Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public icon?: Resource--><!--Device-ToolBarOption-public icon?: Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
public iconColor?: ResourceColor
```

Icon fill color of the toolbar item.

Default value: **\$r('sys.color.icon_primary')**

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public iconColor?: ResourceColor--><!--Device-ToolBarOption-public iconColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
public state?: ItemState
```

State of the toolbar item.

Default value: **ItemState.ENABLE**

**Type:** [ItemState](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbar-itemstate-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public state?: ItemState--><!--Device-ToolBarOption-public state?: ItemState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
public textColor?: ResourceColor
```

Font color of the toolbar item.

Default value: **\$r('sys.color.font_primary')**

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public textColor?: ResourceColor--><!--Device-ToolBarOption-public textColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarSymbolOptions

```TypeScript
public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions
```

Icon symbol options of the toolbar item.

**Type:** [ToolBarSymbolGlyphOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbar-toolbarsymbolglyphoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarOption-public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions--><!--Device-ToolBarOption-public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

