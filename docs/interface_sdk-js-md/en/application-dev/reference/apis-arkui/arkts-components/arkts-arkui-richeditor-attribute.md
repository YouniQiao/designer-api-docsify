# RichEditor properties/events

In addition to the universal attributes, the following attributes are supported.In addition to the universal events, [OnDidChangeCallback](../arkts-apis/arkts-arkui-ondidchangecallback-t.md), [StyledStringChangedListener](../arkts-apis/arkts-arkui-styledstringchangedlistener-i.md), [StyledStringChangeValue](../arkts-apis/arkts-arkui-styledstringchangevalue-i.md), and the following events are supported.

**Inheritance/Implementation:** RichEditorAttribute extends CommonMethod<RichEditorAttribute>

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## aboutToDelete

```TypeScript
aboutToDelete(callback: Callback<RichEditorDeleteValue, boolean>)
```

Triggered when content is about to be deleted in the input method.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorDeleteValue](arkts-arkui-richeditordeletevalue-i.md), boolean&gt; | Yes |

## aboutToIMEInput

```TypeScript
aboutToIMEInput(callback: Callback<RichEditorInsertValue, boolean>)
```

Triggered when content is about to be entered in the input method.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorInsertValue](arkts-arkui-richeditorinsertvalue-i.md), boolean&gt; | Yes |

## barState

```TypeScript
barState(state: BarState)
```

Sets the display mode of the **RichEditor** scrollbar.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 13

**ArkTS mode:** Supports only ArkTS-Dyn, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [BarState](#barstate) | Yes |

## bindSelectionMenu

```TypeScript
bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType,
    options?: SelectionMenuOptions)
```

Sets the custom context menu on text selection. If the custom menu is too long, embed a Scroll component to prevent the keyboard from being blocked.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spanType | [RichEditorSpanType](arkts-arkui-richeditorspantype-e.md) | Yes |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| responseType | ResponseType \| [RichEditorResponseType](arkts-arkui-richeditorresponsetype-e.md) | Yes |
| options | [SelectionMenuOptions](arkts-arkui-selectionmenuoptions-i.md) | No |

## caretColor

```TypeScript
caretColor(value: ResourceColor)
```

Sets the color of the caret and selection handle in the text box.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## compressLeadingPunctuation

```TypeScript
compressLeadingPunctuation(enabled: Optional<boolean>)
```

Sets whether to enable punctuation compression at the beginning of a line.

> **NOTE：**&gt;
> By default, the punctuation at the beginning of a line is not compressed.&gt;
> For details about the punctuation that supports compression, see the punctuation range of the line header
> compression of [ParagraphStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraphstyle-i.md).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## copyOptions

```TypeScript
copyOptions(value: CopyOptions)
```

Specifies whether copy and paste is allowed for text content.Since API version 20, copied or cut text from the **RichEditor** component includes HTML-formatted content in the pasteboard.  
- Only TextSpan and ImageSpan can add HTML content to the pasteboard. Other span types (such as BuilderSpan, SymbolSpan, and CustomSpan) cannot add HTML content to the pasteboard. - For styled strings, refer to [toHtml](../arkts-apis/arkts-arkui-styledstring-c.md#tohtml) for supported HTML conversion scope.  
If copyOptions is not set to CopyOptions.None, a text selection menu will be displayed when you long-press the component content. If a custom context menu is defined through **bindSelectionMenu** or other approaches, it will be displayed.If copyOptions is set to CopyOptions.None, the copy, cut, translate, share, search, and write-aid functions are disabled, and drag-and-drop operations are not supported.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](#copyoptions) | Yes |

## customKeyboard

```TypeScript
customKeyboard(value: CustomBuilder | ComponentContent | undefined,
                 options?: KeyboardOptions | undefined)
```

Sets a custom keyboard.When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method.The custom keyboard's height can be set through the **height** attribute of the custom component's root node, and its width is fixed at the default value.The custom keyboard cannot obtain focus, but it blocks gesture events.By default, the custom keyboard is closed when the input component loses the focus.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 23.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | CustomBuilder \| ComponentContent \| undefined | Yes |
| options | [KeyboardOptions](arkts-arkui-keyboardoptions-i.md) \| undefined | No |

## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig)
```

Configures special entity recognition settings, including entity types to detect, display styles for detected entities, and long-press preview options.This API must be used together with [enableDataDetector](#enabledatadetector). It takes effect only when **enableDataDetector** is set to **true**.When entities A and B overlap, the following rules are followed:
1. If A ⊂ B, retain B. Otherwise, retain A.
2. When A ⊄ B and B ⊄ A: If A.start &lt; B.start, retain A; otherwise, retain B.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [TextDataDetectorConfig](../arkts-apis/arkts-arkui-textdatadetectorconfig-i.md) | Yes |

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions)
```

Sets the extended options of the default system menu, including the text content, icon, and callback.When [disableMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems) or  
[disableSystemServiceMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems) is used to disable system service menu items in the context menu on selection, the disabled menu options will be excluded from the parameter list in the [onCreateMenu](../arkts-apis/arkts-arkui-editmenuoptions-i.md#oncreatemenu) callback of **editMenuOptions**.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| editMenu | [EditMenuOptions](#editmenuoptions) | Yes |

## enableAutoSpacing

```TypeScript
enableAutoSpacing(enable: Optional<boolean>)
```

Sets whether to enable automatic spacing between Chinese and Western characters.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | Optional & lt;boolean & gt; | Yes |

## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean)
```

Enables recognition for special entities within the text.For this API to work, the target device must provide the text recognition capability.If enableDataDetector is set to true and the [dataDetectorConfig](#datadetectorconfig) attribute is not specified, the system identifies all types of entities by default, and changes the color and decoration of these entities to the preset style.Touching and right-clicking an entity opens a context menu with actions based on entity type, while left-clicking triggers the first menu option directly.This API does not work for the node text of **addBuilderSpan**.When **copyOptions** is set to **CopyOptions.None**, the menu displayed after an entity is clicked does not provide the text selection or copy functionality.<!--RP1--><!--RP1End-->

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(isEnabled: boolean)
```

Sets whether to enable haptic feedback.

> **NOTE：**&gt;
> This API can be called in
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 20.

**Since:** 13

**ArkTS mode:** Supports only ArkTS-Dyn, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |

## enableKeyboardOnFocus

```TypeScript
enableKeyboardOnFocus(isEnabled: boolean)
```

Sets whether to enable the input method when the **RichEditor** component obtains focus in a way other than clicking.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |

## enablePreviewText

```TypeScript
enablePreviewText(enable: boolean)
```

Sets whether to enable preview text.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined)
```

Sets whether to enable the AI menu function for text selection. After this function is enabled, the email address, phone number, website address, date, and address in the selection area can be identified, and the corresponding AI menu items can be displayed in the text selection menu. By default, the AI menu feature is enabled.When the AI menu function is enabled, after a text is selected in the component, the corresponding AI menu item is displayed in the text selection menu, including the URL (opening a connection) and email (creating an email) in [TextMenuItemId](../arkts-apis/arkts-arkui-textmenuitemid-c.md)., phoneNumber (call), address (navigation), and dateTime (new event).When the AI menu takes effect, the corresponding options can be displayed only when the selected scope contains only one complete AI entity. This menu item does not appear at the same time as the askAI menu item in [TextMenuItemId](../arkts-apis/arkts-arkui-textmenuitemid-c.md).This function takes effect only when [copyOptions](#copyoptions) is set to CopyOptions.LocalDevice or CopyOptions.CROSS_DEVICE.This API depends on the text recognition capability at the bottom layer of the device. Otherwise, the setting does not take effect.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

## enterKeyType

```TypeScript
enterKeyType(value: EnterKeyType)
```

Sets the Enter key type of the soft keyboard.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [EnterKeyType](#enterkeytype) | Yes |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: Optional<boolean>)
```

For multi-line text overlay, the line height can be automatically adjusted based on the actual text height. This API is not used to set the line height. By default, the line height is not automatically adjusted based on the actual text height.This API depends on the lineHeight attribute of [RichEditorTextStyle](arkts-arkui-richeditortextstyleresult-i.md). When the value of lineHeight is less than the actual height of the text rendered under the current font size, the fallbackLineSpacing property takes effect.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## horizontalScrolling

```TypeScript
horizontalScrolling(enabled: Optional<boolean>)
```

Whether to enable horizontal scrolling when text is wider than the view. The default value is false, and text will be wrapped by the view.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## includeFontPadding

```TypeScript
includeFontPadding(include: Optional<boolean>)
```

Sets whether to add a spacing between the first and last lines to avoid text truncation. If this interface is not used, the spacing is not increased by default.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| include | Optional & lt;boolean & gt; | Yes |

## keyboardAppearance

```TypeScript
keyboardAppearance(appearance: Optional<KeyboardAppearance>)
```

Sets the keyboard appearance.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appearance | Optional & lt;KeyboardAppearance & gt; | Yes |

## maxLength

```TypeScript
maxLength(maxLength: Optional<number>)
```

Sets the maximum length of the component content. When the total length of the content (including text, images, symbols, and builders) reaches this value, no more content can be added.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [maxLength](#maxlength) | Optional & lt;number & gt; | Yes |

## maxLines

```TypeScript
maxLines(maxLines: Optional<number>)
```

Sets the maximum number of lines that the rich text can display. When **maxLines** is set, content that exceeds the specified number of lines can be scrolled to display. If both the component height and **maxLines** are set, the component height takes precedence.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [maxLines](#maxlines) | Optional & lt;number & gt; | Yes |

## onCopy

```TypeScript
onCopy(callback: Callback<CopyEvent>)
```

Triggered during copy. You can use this method to override the system's default behavior and implement the copying of text and images.The **RichEditor** component constructed using [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) supports copying of text and images by default.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[CopyEvent](arkts-arkui-copyevent-i.md)&gt; | Yes |

## onCut

```TypeScript
onCut(callback: Callback<CutEvent>)
```

Triggered during cutting. You can use this method to override the system's default behavior and implement the cutting of text and images.The **RichEditor** component constructed using [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) supports text and image cutting by default.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[CutEvent](arkts-arkui-cutevent-i.md)&gt; | Yes |

## onDeleteComplete

```TypeScript
onDeleteComplete(callback: Callback<void>)
```

Triggered when content is deleted in the input method.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onDidChange

```TypeScript
onDidChange(callback: OnDidChangeCallback) : RichEditorAttribute
```

Triggered after an addition or deletion operation is performed in the component. This callback is not executed if there is no actual addition or deletion of text.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnDidChangeCallback](../arkts-apis/arkts-arkui-ondidchangecallback-t.md) | Yes |

## onDidIMEInput

```TypeScript
onDidIMEInput(callback: Callback<TextRange>)
```

Triggered when text input in the input method is complete.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

> **NOTE：**&gt;
> This API can be called in
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;TextRange & gt; | Yes |

## onEditingChange

```TypeScript
onEditingChange(callback: Callback<boolean>)
```

Triggered when the content editing state in the component changes.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | Yes |

## onIMEInputComplete

```TypeScript
onIMEInputComplete(callback: Callback<RichEditorTextSpanResult>)
```

Triggered when text input in the input method is complete.This callback can return information about only one text span. If the editing operation involves returning information about multiple text spans, you are advised to use the [onDidIMEInput](#ondidimeinput) API.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorTextSpanResult](arkts-arkui-richeditortextspanresult-i.md)&gt; | Yes |

## onPaste

```TypeScript
onPaste(callback: PasteEventCallback)
```

Triggered when a paste operation is performed. You can use this API to override the default system behavior so that both images and text can be pasted.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PasteEventCallback](arkts-arkui-pasteeventcallback-t.md) | Yes |

## onReady

```TypeScript
onReady(callback: Callback<void>)
```

Triggered after the **RichEditor** component is initialized.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onSelect

```TypeScript
onSelect(callback: Callback<RichEditorSelection>)
```

Invoked when content is selected.If a mouse device is used for selection, this callback is invoked when the left mouse button is double-clicked to select content and invoked again when the button is released.If a finger is used for selection, this callback is invoked by a long press and invoked again when the finger is released.If the selected area is continuously modified by using a finger or mouse or if the selected area is triple-clicked, the onSelect callback is not invoked.If the selection area needs to be detected in real time or the RichEditor component constructed using [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used, use the onSelectionChange API.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorSelection](arkts-arkui-richeditorselection-i.md)&gt; | Yes |

## onSelectionChange

```TypeScript
onSelectionChange(callback: Callback<RichEditorRange>)
```

Triggered when the selection area or caret position changes in the editing state. When the caret position changes, the start and end positions of the selection area are the same.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorRange](arkts-arkui-richeditorrange-i.md)&gt; | Yes |

## onSubmit

```TypeScript
onSubmit(callback: SubmitCallback)
```

Triggered when the Enter key on the soft keyboard is pressed.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [SubmitCallback](arkts-arkui-submitcallback-t.md) | Yes |

## onWillAttachIME

```TypeScript
onWillAttachIME(callback: Callback<IMEClient> | undefined)
```

Triggers a callback before a component is bound to an input method.Call the [setExtraConfig](../arkts-apis/arkts-arkui-imeclient-i.md#setextraconfig) method of [IMEClient](../arkts-apis/arkts-arkui-imeclient-i.md) to set input method extension information. After the input method is bound, it receives this extension information, which can be used to implement custom functionality.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;IMEClient & gt; \ | undefined | Yes |

## onWillChange

```TypeScript
onWillChange(callback: Callback<RichEditorChangeValue, boolean>) : RichEditorAttribute
```

Invoked when any addition or deletion operation is about to be performed in the component.This callback is not supported when the **RichEditor** component constructed with [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[RichEditorChangeValue](arkts-arkui-richeditorchangevalue-i.md), boolean&gt; | Yes |

## orphanCharOptimization

```TypeScript
orphanCharOptimization(enabled: Optional<boolean>)
```

Whether to avoid an orphan word on the last line of the paragraph.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## placeholder

```TypeScript
placeholder(value: ResourceStr, style?: PlaceholderStyle)
```

Sets the placeholder text, which is displayed when there is no input.

> **NOTE：**&gt;
> This API can be called within
> [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)
> since API version 18.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| style | [PlaceholderStyle](arkts-arkui-placeholderstyle-i.md) | No |

## punctuationOverflow

```TypeScript
punctuationOverflow(enabled: Optional<boolean>)
```

Whether to enable punctuation overflow at line ends.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## scrollBarColor

```TypeScript
scrollBarColor(color: Optional<ColorMetrics>)
```

Sets the color of the scrollbar.

**Since:** 21

**ArkTS mode:** Supports only ArkTS-Dyn, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | Optional & lt;ColorMetrics & gt; | Yes |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor)
```

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedDragPreviewStyle

```TypeScript
selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)
```

Sets the drag and view style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | SelectedDragPreviewStyle \| undefined | Yes |

## singleLine

```TypeScript
singleLine(isEnable: boolean | undefined)
```

Sets whether to enable the single-line mode. If this interface is not used, the single-line mode is disabled by default.

> **NOTE：**&gt;
> The scroll bar is not displayed in single-line mode.&gt;
> In single-line mode, the newline character is displayed as a space.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnable | boolean \| undefined | Yes |

## stopBackPress

```TypeScript
stopBackPress(isStopped: Optional<boolean>)
```

Sets whether to prevent the back button press from being propagated to other components or applications.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isStopped | Optional & lt;boolean & gt; | Yes |

## undoStyle

```TypeScript
undoStyle(style: Optional<UndoStyle>)
```

Sets whether to retain the original content style when undoing or redoing an action.When the [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) is used to build the RichEditor component, the original content style is retained by default during undo and redo, and is not affected by the attributes set by this API.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | Optional&lt;[UndoStyle](arkts-arkui-undostyle-e.md)&gt; | Yes |
