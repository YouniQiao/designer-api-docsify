# EditableTitleBarMenuItem

Declaration of the menu item on the right side.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class EditableTitleBarMenuItem--><!--Device-unnamed-export declare class EditableTitleBarMenuItem-End-->

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

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public accessibilityDescription?: ResourceStr--><!--Device-EditableTitleBarMenuItem-public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

Accessibility level. It determines whether the component can be recognized by accessibility services.

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

<!--Device-EditableTitleBarMenuItem-public accessibilityLevel?: string--><!--Device-EditableTitleBarMenuItem-public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of the **label** property if it is set and an empty string otherwise.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public accessibilityText?: ResourceStr--><!--Device-EditableTitleBarMenuItem-public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

Right-side custom button click event of the title bar.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public action?: () => void--><!--Device-EditableTitleBarMenuItem-public action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
public defaultFocus?: boolean
```

Whether to set the item as the default focus.

**true**: Set the item as the default focus.

**false**: Do not set the item as the default focus.

Default value: **false**

The **defaultFocus** attribute requires the **isEnabled** attribute to be set to **true** beforehand; otherwise, **defaultFocus** will be treated as **false**.

**Type:** boolean

**Default:** { false }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public defaultFocus?: boolean--><!--Device-EditableTitleBarMenuItem-public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
public isEnabled?: boolean
```

Whether to enable the item. Default value: **true**.

**true**: The item is enabled.

**false**: The item is disabled.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public isEnabled?: boolean--><!--Device-EditableTitleBarMenuItem-public isEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
public label?: ResourceStr
```

Icon label.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public label?: ResourceStr--><!--Device-EditableTitleBarMenuItem-public label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
public symbolStyle?: SymbolGlyphModifier
```

Symbol icon resource, which has higher priority than **value**.

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public symbolStyle?: SymbolGlyphModifier--><!--Device-EditableTitleBarMenuItem-public symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: ResourceStr
```

Icon resource.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItem-public value: ResourceStr--><!--Device-EditableTitleBarMenuItem-public value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

