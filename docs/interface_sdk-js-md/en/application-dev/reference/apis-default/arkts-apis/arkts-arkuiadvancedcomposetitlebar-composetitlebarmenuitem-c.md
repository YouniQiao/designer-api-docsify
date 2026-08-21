# ComposeTitleBarMenuItem

Declaration of the menu item on the right side.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ComposeTitleBarMenuItem--><!--Device-unnamed-export declare class ComposeTitleBarMenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## accessibilityDescription

```TypeScript
public accessibilityDescription?: ResourceStr
```

Accessible description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public accessibilityDescription?: ResourceStr--><!--Device-ComposeTitleBarMenuItem-public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

Accessibility level. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Type:** string

**Default:** "auto".The options are as follows:<br/> "auto":The value is converted to "yes" or "no" based on the component. "yes": the current component is selectable for the accessibility service. "no": The current component is not selectable for the accessibility service. "no-hide-descendants":The current component and all its child components are not selectable<br/> for the accessibility service.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public accessibilityLevel?: string--><!--Device-ComposeTitleBarMenuItem-public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of the **label** property if it is set and an empty string otherwise.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public accessibilityText?: ResourceStr--><!--Device-ComposeTitleBarMenuItem-public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

Action to perform. This parameter is not available for the **item** attribute.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public action?: () => void--><!--Device-ComposeTitleBarMenuItem-public action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
public isEnabled?: boolean
```

Whether to enable the item.

Default value: **false**

**true**: The item is enabled.

**false**: The item is disabled.

This property cannot be triggered by the **item** property.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public isEnabled?: boolean--><!--Device-ComposeTitleBarMenuItem-public isEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
public label?: ResourceStr
```

Icon label.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public label?: ResourceStr--><!--Device-ComposeTitleBarMenuItem-public label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
public symbolStyle?: SymbolGlyphModifier
```

Symbol icon resource, which has higher priority than **value**. This parameter is not available for the **item** attribute.

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public symbolStyle?: SymbolGlyphModifier--><!--Device-ComposeTitleBarMenuItem-public symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: ResourceStr
```

Icon resource.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBarMenuItem-public value: ResourceStr--><!--Device-ComposeTitleBarMenuItem-public value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

