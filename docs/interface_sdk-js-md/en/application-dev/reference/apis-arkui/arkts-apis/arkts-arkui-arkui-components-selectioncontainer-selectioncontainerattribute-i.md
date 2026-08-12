# SelectionContainerAttribute

Defines the attributes of SelectionContainer.

**Inheritance/Implementation:** SelectionContainerAttribute extends [CommonMethod](CommonMethod)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface SelectionContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectionContainerAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SelectionContainerInstance, SelectionContainer, OnMenuItemClickWithTextCallback, SelectionContainerOptions, SelectionContainerAttribute, SelectionContainerEditMenuOptions, SelectionContainerTextJoinStyle, SelectionContainerController, SelectionContainerMenuOptions } from '@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>
    | undefined): this
```

Set the attribute modifier.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this--><!--Device-SelectionContainerAttribute-default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | AttributeModifier&lt;[SelectionContainerAttribute](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## bindSelectionMenu

```TypeScript
default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,
    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this
```

Bind to the selection menu.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The duration required for a long-press gesture is 600 ms for bindSelectionMenu and 800 ms for bindContextMenu.&lt;br&gt;When both bindSelectionMenu and bindContextMenu are set and both are configured to be triggered by a  long-press gesture, bindSelectionMenu is triggered first.&lt;br&gt;If the custom menu is too long, embed a Scroll component to prevent the keyboard from being blocked.&lt;/p&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanType | TextSpanType \| undefined | Yes | Indicates the type of selection menu. Default value is TextSpanType.TEXT. |
| content | CustomBuilder \| undefined | Yes | Indicates the content of selection menu. |
| responseType | TextResponseType \| undefined | Yes | Indicates response type of selection menu. Default value is TextResponseType.LONG_PRESS. |
| options | [SelectionContainerMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) \| undefined | No | Indicates the options of selection menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## caretColor

```TypeScript
default caretColor(color: ResourceColor | undefined): this
```

Set the caret color for selected text.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default caretColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-default caretColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | Yes | Caret color. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

Set whether to allow copy and where data can be copied.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default copyOption(value: CopyOptions | undefined): this--><!--Device-SelectionContainerAttribute-default copyOption(value: CopyOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | CopyOptions \| undefined | Yes | Copy option for selected text. Default value is CopyOptions.InApp. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this
```

Set the custom text menu.Sets the extended options of the custom context menu on selection,including the text content, icon, and callback.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [SelectionContainerEditMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) \| undefined | Yes | Customize text menu options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

Enable or disable haptic feedback.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default enableHapticFeedback(isEnabled: boolean | undefined): this--><!--Device-SelectionContainerAttribute-default enableHapticFeedback(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | Whether to enable haptic feedback. Default value is true. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onCopy

```TypeScript
default onCopy(callback: Callback<string> | undefined): this
```

Called when selected text is copied.Currently, only text can be copied.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onCopy(callback: Callback<string> | undefined): this--><!--Device-SelectionContainerAttribute-default onCopy(callback: Callback<string> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; \| undefined | Yes | Callback of copy event. The first callback parameter (string) is the selected text concatenated in the visual order of Text components. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this
```

Called when text selection changes in SelectionContainer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this--><!--Device-SelectionContainerAttribute-default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;Array&lt;string&gt;&gt; \| undefined | Yes | Callback of selection change event. The order of items in the first callback parameter array is consistent with the visual order of Text components. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

Called before using the Clipboard copy menu.Currently, only text can be copied.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onWillCopy(callback: Callback<string, boolean> | undefined): this--><!--Device-SelectionContainerAttribute-default onWillCopy(callback: Callback<string, boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string, boolean&gt; \| undefined | Yes | Callback used to check whether copy is allowed. The first callback parameter (string) is the selected text concatenated in the visual order of Text components. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(color: ResourceColor | undefined): this
```

Set selected text background color.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default selectedBackgroundColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-default selectedBackgroundColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | Yes | Selected text background color. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## setSelectionContainerOptions

```TypeScript
default setSelectionContainerOptions(): this
```

Set SelectionContainer Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default setSelectionContainerOptions(): this--><!--Device-SelectionContainerAttribute-default setSelectionContainerOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## textJoinStyle

```TypeScript
default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this
```

Set text join style for aggregated text in SelectionContainer.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;This setting affects the string value used in callbacks such as onWillCopy and onCopy.&lt;br&gt;It also affects built-in text menu item logic that depends on string concatenation, such as copy.&lt;br&gt;The default style is SelectionContainerTextJoinStyle.NEWLINE.&lt;/p&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this--><!--Device-SelectionContainerAttribute-default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SelectionContainerTextJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) \| undefined | Yes | Text join style for aggregated text. |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

