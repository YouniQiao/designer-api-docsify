# SelectionContainerAttribute

Defines the attributes of SelectionContainer.

**Inheritance/Implementation:** SelectionContainerAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface SelectionContainerAttribute--><!--Device-unnamed-export declare interface SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>
    | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this--><!--Device-SelectionContainerAttribute-attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | AttributeModifier&lt;[SelectionContainerAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindSelectionMenu

```TypeScript
bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,
    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanType | TextSpanType \| undefined | Yes |  |
| content | CustomBuilder \| undefined | Yes |  |
| responseType | TextResponseType \| undefined | Yes |  |
| options | [SelectionContainerMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## caretColor

```TypeScript
caretColor(color: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-caretColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-caretColor(color: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## copyOption

```TypeScript
copyOption(value: CopyOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-copyOption(value: CopyOptions | undefined): this--><!--Device-SelectionContainerAttribute-copyOption(value: CopyOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | CopyOptions \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [SelectionContainerEditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-enableHapticFeedback(isEnabled: boolean | undefined): this--><!--Device-SelectionContainerAttribute-enableHapticFeedback(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onCopy

```TypeScript
onCopy(callback: Callback<string> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-onCopy(callback: Callback<string> | undefined): this--><!--Device-SelectionContainerAttribute-onCopy(callback: Callback<string> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: Callback<Array<string>> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-onTextSelectionChange(callback: Callback<Array<string>> | undefined): this--><!--Device-SelectionContainerAttribute-onTextSelectionChange(callback: Callback<Array<string>> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;Array&lt;string&gt;&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onWillCopy

```TypeScript
onWillCopy(callback: Callback<string, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-onWillCopy(callback: Callback<string, boolean> | undefined): this--><!--Device-SelectionContainerAttribute-onWillCopy(callback: Callback<string, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string, boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-selectedBackgroundColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-selectedBackgroundColor(color: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setSelectionContainerOptions

```TypeScript
setSelectionContainerOptions(): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-setSelectionContainerOptions(): this--><!--Device-SelectionContainerAttribute-setSelectionContainerOptions(): this-End-->

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## textJoinStyle

```TypeScript
textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-SelectionContainerAttribute-textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this--><!--Device-SelectionContainerAttribute-textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SelectionContainerTextJoinStyle](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Set SelectionContainer Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default--><!--Device-SelectionContainerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

