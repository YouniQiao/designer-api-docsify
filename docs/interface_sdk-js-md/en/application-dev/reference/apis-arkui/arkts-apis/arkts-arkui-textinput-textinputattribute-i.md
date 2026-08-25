# TextInputAttribute

Defines the TextInput attribute functions.

**Inheritance/Implementation:** TextInputAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextInputAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## autoCapitalizationMode

```TypeScript
default autoCapitalizationMode(mode: AutoCapitalizationMode | undefined): this
```

Set text mode of automatic case mode switching.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AutoCapitalizationMode](arkts-arkui-textcommon-autocapitalizationmode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## barState

```TypeScript
default barState(value: BarState | undefined): this
```

Define bar state of the text input.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarState](arkts-arkui-barstate-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(iconOptions: CancelButtonOptions | undefined): this
```

Set the cancel button style

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iconOptions | [CancelButtonOptions](../arkts-components/arkts-arkui-cancelbuttonoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(symbolOptions: CancelButtonSymbolOptions | undefined): this
```

Set the cancel button style

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| symbolOptions | [CancelButtonSymbolOptions](../arkts-components/arkts-arkui-cancelbuttonsymboloptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretColor

```TypeScript
default caretColor(value: ResourceColor | undefined): this
```

Called when the color of the insertion cursor is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Since API version 12, this API can be used to set the text handle color, which is the same as the caret color. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretPosition

```TypeScript
default caretPosition(value: int | undefined): this
```

Define the caret position of the text input.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretStyle

```TypeScript
default caretStyle(value: CaretStyle | undefined): this
```

Define the caret style of the text input

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CaretStyle](arkts-arkui-textcommon-caretstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## compressLeadingPunctuation

```TypeScript
default compressLeadingPunctuation(enabled: boolean | undefined): this
```

Whether to compress punctuation at the beginning of line.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## contentType

```TypeScript
default contentType(value: ContentType | undefined): this
```

Called when the content type is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ContentType](arkts-arkui-textinput-contenttype-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

Called when the copy option is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this attribute is set to CopyOptions.None, the text can only be pasted; all other actions, such as copying, cutting, and sharing, are disabled. <br>Dragging is not allowed when CopyOptions.None is set. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](arkts-arkui-copyoptions-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(value: CustomBuilder | ComponentContentBase | undefined, options?: KeyboardOptions): this
```

Define custom keyboard of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method. <br>The custom keyboard's height can be set through the height attribute of the custom component's root node, and its width is fixed at the default value. <br>The custom keyboard is presented by overlaying the original screen, which is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box. <br>The custom keyboard cannot obtain the focus, but it blocks gesture events. <br>By default, the custom keyboard is closed when the input component loses the focus. <br>You can also use the TextInputController.stopEditing API to close the keyboard. <br>When a custom keyboard is set, the text box does not support camera input, even when the device supports. <br>When setting a custom keyboard, you can bind the onKeyPrelme event to prevent input from the physical keyboard. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) \| undefined | Yes |
| options | [KeyboardOptions](arkts-arkui-richeditor-keyboardoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## decoration

```TypeScript
default decoration(value: TextDecorationOptions | undefined): this
```

Called when the text decoration of the text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect for the password input mode. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextDecorationOptions](../arkts-components/arkts-arkui-textdecorationoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

Set the custom text menu. Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| editMenu | [EditMenuOptions](arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## ellipsisMode

```TypeScript
default ellipsisMode(mode: EllipsisMode | undefined): this
```

Set the ellipsis mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [EllipsisMode](arkts-arkui-ellipsismode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableAutoFill

```TypeScript
default enableAutoFill(value: boolean | undefined): this
```

Sets whether enable auto fill or not.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableAutoFillAnimation

```TypeScript
default enableAutoFillAnimation(enabled: boolean | undefined): this
```

Sets whether enable auto fill animation effect or not.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableAutoSpacing

```TypeScript
default enableAutoSpacing(enabled: boolean | undefined): this
```

Whether to enable automatic spacing between Chinese and Latin characters.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

Enable or disable haptic feedback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(value: boolean | undefined): this
```

Sets whether request keyboard or not when on focus. Sets whether to enable the input method when the TextInput component obtains focus in a way other than clicking.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Since API version 10, the TextInput component brings up the keyboard by default when it obtains focus. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enablePreviewText

```TypeScript
default enablePreviewText(enable: boolean | undefined): this
```

Define the preview text mode of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Preview text is in a temporary state and does not support text interception. <br>As such, it does not trigger onWillInsert, onDidInsert, onWillDelete, or onDidDelete callbacks. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableSelectedDataDetector

```TypeScript
default enableSelectedDataDetector(enable: boolean | undefined): this
```

Enable selected data detector.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enterKeyType

```TypeScript
default enterKeyType(value: EnterKeyType | undefined): this
```

Called when the type of soft keyboard input button is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fallbackLineSpacing

```TypeScript
default fallbackLineSpacing(enabled: boolean | undefined): this
```

Whether to include ascent/descent from fallback fonts to prevent overlapping lines.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Called when the font color is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: ResourceStr | undefined): this
```

Called when the font list of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Default font: 'HarmonyOS Sans'<br>The 'HarmonyOS Sans' font and registered custom fonts are supported for applications. <br>Only the 'HarmonyOS Sans' font is supported for widgets. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

Set font feature.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not available when type is set to an enum value that indicates the password input mode, such as Password, NEW_PASSWORD, or NUMBER_PASSWORD. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| undefined | Yes | The fontFeature. normal \|  & lt;feature-tag-value & gt;, where & lt;feature-tag-value & gt; = & lt;string & gt; [ & lt;integer & gt; \ | on \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

Called when the font size is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If fontSize is of the number type, the unit fp is used. <br>The default font size is 16 fp. <br>The value cannot be a percentage. <br>The default value on wearable devices is 18fp. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

Called when the font style of a font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

Called when the font weight is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## halfLeading

```TypeScript
default halfLeading(halfLeading: boolean | undefined): this
```

Set the text with half leading.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [halfLeading](#halfleading) | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## heightAdaptivePolicy

```TypeScript
default heightAdaptivePolicy(value: TextHeightAdaptivePolicy | undefined): this
```

Called when the height adaptive policy is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;ul&gt; &lt;li&gt;When this attribute is set to TextHeightAdaptivePolicy.MAX_LINES_FIRST, the maxLines attribute takes precedence for adjusting the text height. <br>If the maxLines setting results in a layout beyond the layout constraints, the text will shrink to a font size between minFontSize and maxFontSize to allow for more content to be shown.&lt;/li&gt; &lt;li&gt;If this attribute is set to TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST, the minFontSize attribute takes precedence for adjusting the text height. <br>If the text can fit in one line with the minFontSize setting, the text will enlarge to the largest possible font size between minFontSize and maxFontSize.&lt;/li&gt; &lt;li&gt;TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST produces the same effect as TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST.&lt;/li&gt; &lt;/ul&gt; <br>When the component is in the non-inline input style, the three values of TextHeightAdaptivePolicy have the same effect, that is, the text will shrink to a font size between minFontSize and maxFontSize to allow for more content to be shown. <br>If the text box is in inline input style, the font size in the editing state is different from that in the non-editing state. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## includeFontPadding

```TypeScript
default includeFontPadding(include: boolean | undefined): this
```

Determines whether the layout adds extra padding at the top and bottom to make space for characters.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| include | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## inputFilter

```TypeScript
default inputFilter(value: ResourceStr | undefined, error?: Callback<string> | undefined): this
```

Called when the inputFilter of text is set.Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Only inputs that comply with the regular expression can be displayed. <br>Other inputs are filtered out. <br>The specified regular expression can match single characters, but not strings. <br>Since API version 11, if inputFilter is set and the entered characters are not null, the filtering effect attached to the text box type (specified through the type attribute) does not take effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |
| error | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## keyboardAppearance

```TypeScript
default keyboardAppearance(appearance: KeyboardAppearance | undefined): this
```

Set the keyboard appearance.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appearance | [KeyboardAppearance](arkts-arkui-textcommon-keyboardappearance-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## letterSpacing

```TypeScript
default letterSpacing(value: double | string | Resource | undefined): this
```

Called when the distance between text fonts is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value specified is a percentage or 0, the default value is used. <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>If the value specified is a negative value, the text is compressed. <br>A negative value too small may result in the text being compressed to 0 and no content being displayed. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## lineBreakStrategy

```TypeScript
default lineBreakStrategy(strategy: LineBreakStrategy | undefined): this
```

Set the text line break strategy type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute takes effect when wordBreak is not set to breakAll. <br>Hyphens are not supported. <br>This attribute does not take effect for the non-inline input style. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [LineBreakStrategy](arkts-arkui-linebreakstrategy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

Called when the line height of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than or equal to 0, the line height is not limited and the font size is adaptive. <br>If the value is of the number type, the unit fp is used. <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

Called when the maximum font scale of the font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with minFontSize and maxLines (when the component is in editing state in the inline input style), or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxLength

```TypeScript
default maxLength(value: int | undefined): this
```

Called when the input of maximum text length is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this attribute is not set or is set to an invalid value, the default value is used. <br>If a decimal number is specified, the integer part is used. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxLines

```TypeScript
default maxLines(value: int | undefined): this
```

Define max lines of the text input. Value range: (0, +∞)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

Called when the minimum font scale of the font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with maxFontSize and maxLines (when the component is in editing state in the inline input style), or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: EditableTextOnChangeCallback | undefined): this
```

Called when the input of the input box changes.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In this callback, if cursor operations are performed, you need to adjust the cursor logic based on the previewText parameter to ensure it works seamlessly within the preview display scenario. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [EditableTextOnChangeCallback](arkts-arkui-editabletextonchangecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onContentScroll

```TypeScript
default onContentScroll(callback: OnContentScrollCallback | undefined): this
```

Called when the content scrolls.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnContentScrollCallback](arkts-arkui-oncontentscrollcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: Callback<string> | undefined): this
```

Called when using the Clipboard menu.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onCut

```TypeScript
default onCut(callback: Callback<string> | undefined): this
```

Called when using the Clipboard menu.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onDidDelete

```TypeScript
default onDidDelete(callback: Callback<DeleteValue> | undefined): this
```

Get text value information when the deletion has been completed<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is available only for system input methods. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DeleteValue](arkts-arkui-textcommon-deletevalue-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onDidInsert

```TypeScript
default onDidInsert(callback: Callback<InsertValue> | undefined): this
```

Get text value information when completed input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is available only for system input methods. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[InsertValue](arkts-arkui-textcommon-insertvalue-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onEditChange

```TypeScript
default onEditChange(callback: Callback<boolean> | undefined): this
```

Called when judging whether the text editing change finished.Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise. <br>It returns true if the input operation is currently in progress. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onPaste

```TypeScript
default onPaste(callback: OnPasteCallback | undefined): this
```

Called when using the Clipboard menu.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnPasteCallback](arkts-arkui-onpastecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onSecurityStateChange

```TypeScript
default onSecurityStateChange(callback: Callback<boolean> | undefined): this
```

Called when changing the password visible mode of the text input.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: OnSubmitCallback | undefined): this
```

Called when submitted.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnSubmitCallback](arkts-arkui-onsubmitcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: OnTextSelectionChangeCallback | undefined): this
```

Called when the text selection changes.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnTextSelectionChangeCallback](arkts-arkui-ontextselectionchangecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

Called before the text input component attach the InputMethod.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[IMEClient](arkts-arkui-textcommon-imeclient-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillChange

```TypeScript
default onWillChange(callback: Callback<EditableTextChangeValue, boolean> | undefined): this
```

Get text value information when about to change.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[EditableTextChangeValue](arkts-arkui-textcommon-editabletextchangevalue-i.md), boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

Called before using the Clipboard copy menu.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string, boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillCut

```TypeScript
default onWillCut(callback: Callback<string, boolean> | undefined): this
```

Called before using the Clipboard cut menu.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string, boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillDelete

```TypeScript
default onWillDelete(callback: Callback<DeleteValue, boolean> | undefined): this
```

Get text value information when about to delete.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It returns true if the text is deleted; returns false otherwise. <br>This callback is not called for text preview. <br>It is available only for system input methods. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DeleteValue](arkts-arkui-textcommon-deletevalue-i.md), boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillInsert

```TypeScript
default onWillInsert(callback: Callback<InsertValue, boolean> | undefined): this
```

Get text value information when about to input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It returns true if the text is inserted; returns false otherwise. <br>This callback is not triggered for pre-edit or candidate word operations. <br>It is available only for system input methods. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[InsertValue](arkts-arkui-textcommon-insertvalue-i.md), boolean&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## orphanCharOptimization

```TypeScript
default orphanCharOptimization(enabled: boolean | undefined): this
```

Whether to avoid an orphan word on the last line of the paragraph.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## passwordIcon

```TypeScript
default passwordIcon(value: PasswordIcon | undefined): this
```

Define the password icon of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Images in JPG, PNG, BMP, HEIC, and WEBP formats are supported. <br>By default, the system-provided icon is used. <br>The icon size is fixed at 24 vp (or 28 vp on wearable devices), regardless of the source image size. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PasswordIcon](arkts-arkui-textinput-passwordicon-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## passwordRules

```TypeScript
default passwordRules(value: string | undefined): this
```

Define the password rules of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When autofill is used, these rules are transparently transmitted to Password Vault for generating a new password. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## placeholderColor

```TypeScript
default placeholderColor(value: ResourceColor | undefined): this
```

Called when the color of the placeholder is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## placeholderFont

```TypeScript
default placeholderFont(value?: Font | undefined): this
```

Called when the font property of the placeholder is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The 'HarmonyOS Sans' font and registered custom fonts are supported. <br>The default value on wearable devices is 18fp. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## punctuationOverflow

```TypeScript
default punctuationOverflow(enabled: boolean | undefined): this
```

Whether to enable punctuation overflow at line ends.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectAll

```TypeScript
default selectAll(value: boolean | undefined): this
```

Sets selection when on focus.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not available for the inline input style. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(value: ResourceColor | undefined): this
```

Define the text selected background color of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the opacity is not set, a 20% opacity will be used. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

Used to set the selected drag preview style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SelectedDragPreviewStyle](arkts-arkui-textcommon-selecteddragpreviewstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectionMenuHidden

```TypeScript
default selectionMenuHidden(value: boolean | undefined): this
```

Controls whether the selection menu pops up.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>&lt;em&gt;true&lt;/em&gt;: <br>The system text selection menu does not appear under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. <br>&lt;em&gt;false&lt;/em&gt;: <br>The system text selection menu appears under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## setTextInputOptions

```TypeScript
default setTextInputOptions(value?: TextInputOptions): this
```

Set TextInput options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextInputOptions](arkts-arkui-textinput-textinputoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

Set the shader style of the text, such as lineargradient or radialgradient.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shader | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showCounter

```TypeScript
default showCounter(value: boolean | undefined, options?: InputCounterOptions | undefined): this
```

Show the counter when the number of characters entered exceeds the threshold through InputCounterOptions.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>options can be set only when value is set to true, in which case a character counter is displayed below the text box. <br>This attribute must be used together with maxLength. <br>The character counter is displayed in this format: Number of characters entered/Character limit. <br>It is visible when the number of characters entered is greater than the character limit multiplied by the threshold percentage value. <br>If options is not set, the text box border and character counter subscript turn red when the number of characters entered exceeds the limit. <br>If value is set to true and options is set, the text box border and character counter subscript turn red and the text box shakes when the number of characters entered reaches the limit, provided that the value of thresholdPercentage is valid. <br>If highlightBorder is set to false, the text box border does not turn red. <br>By default, highlightBorder is set to true. <br>The character counter is not displayed for text boxes in inline or password input style. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |
| options | [InputCounterOptions](../arkts-components/arkts-arkui-inputcounteroptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showError

```TypeScript
default showError(value?: ResourceStr | undefined): this
```

Define the show error of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>On wearable devices, the error message is displayed at a font size of 13 fp and center-aligned. <br>If the data type is ResourceStr and the input content does not comply with specifications, the error message is displayed. <br>If the error message does not fit in one line, an ellipsis (…) is displayed to represent clipped text. <br>If the data type is undefined, no error message is displayed. <br>By default, no error message is displayed. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showPassword

```TypeScript
default showPassword(visible: boolean | undefined): this
```

Define the password visible mode of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API has effect only when the input type is set to Password, NEWPASSWORD, or NUMBERPASSWORD mode. <br>It does not work in other modes. <br>When in password mode, there may be inconsistency between the backend state of the text box and the frontend application's state management variables. <br>This can cause issues with the icon at the end of the password text box. <br>To avoid such issues, use the onSecurityStateChange callback to sync the states. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| visible | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showPasswordIcon

```TypeScript
default showPasswordIcon(value: boolean | undefined): this
```

Called when the password show/hide icon is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API has effect only when the input type is set to Password, NEWPASSWORD, or NUMBERPASSWORD mode. It does not work in other modes. <br>When in password mode, there may be inconsistency between the backend state of the text box and the frontend application's state management variables. <br>This can cause issues with the icon at the end of the password text box. <br>To avoid such issues, use the onSecurityStateChange callback to sync the states. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showUnderline

```TypeScript
default showUnderline(value: boolean | undefined): this
```

Define the show underline of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>By default, the underline comes in the color of '#33182431', thickness of 1 px, and text box size of 48 vp. <br>The underline is only available for the InputType.Normal type. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showUnit

```TypeScript
default showUnit(value: CustomBuilder | undefined): this
```

Define the show unit of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute effective only when showUnderline is set to true. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## stopBackPress

```TypeScript
default stopBackPress(isStopped: boolean | undefined): this
```

Set whether stop backPressed callback event or not.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isStopped | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## strokeColor

```TypeScript
default strokeColor(color: ResourceColor | undefined): this
```

Set the stroke color.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## strokeJoinStyle

```TypeScript
default strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): this
```

Set the join style of the stroke.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [strokeJoinStyle](#strokejoinstyle) | [StrokeJoinStyle](arkts-arkui-textcommon-strokejoinstyle-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(width: LengthMetrics | undefined): this
```

Set the stroke width.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## style

```TypeScript
default style(value: TextInputStyle | TextContentStyle | undefined): this
```

Text input style<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The inline input style only supports InputType.Normal. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextInputStyle](arkts-arkui-textinput-textinputstyle-e.md) \| [TextContentStyle](arkts-arkui-textcontentstyle-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

Called when the text align is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Available options are TextAlign.Start, TextAlign.Center, and TextAlign.End. <br>To set vertical alignment for the text, use the align attribute. <br>The align attribute alone does not control the horizontal position of the text. <br>In other words, Alignment.TopStart, Alignment.Top, and Alignment.TopEnd produce the same effect, top-aligning the text; Alignment.Start, Alignment.Center, and Alignment.End produce the same effect, centered-aligning the text vertically; Alignment.BottomStart, Alignment.Bottom, and Alignment.BottomEnd produce the same effect, bottom-aligning the text. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextAlign](arkts-arkui-textalign-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textDirection

```TypeScript
default textDirection(direction: TextDirection | undefined): this
```

Set the text direction.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | [TextDirection](arkts-arkui-textcommon-textdirection-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textIndent

```TypeScript
default textIndent(value: Dimension | undefined): this
```

Specify the indentation of the first line in a text-block.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textOverflow

```TypeScript
default textOverflow(value: TextOverflow | undefined): this
```

Called when the overflow mode of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is only available for the inline input style. <br>Text is clipped at the transition between words. <br>To clip text in the middle of a word, set wordBreak to WordBreak.BREAK_ALL. <br>TextOverflow.None produces the same effect as TextOverflow.Clip. <br>Default value in non-editing state in the inline input style: TextOverflow.Ellipsis. <br>Default value in editing state in the inline input style: TextOverflow.Clip. <br>The TextInput component does not support the TextOverflow.MARQUEE mode. <br>If TextOverflow.MARQUEE is set, the component automatically switches to TextOverflow.Ellipsis for the non-editing state in the inline input style and TextOverflow.Clip for the non-inline input style and the editing state in the inline input style. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextOverflow](arkts-arkui-textoverflow-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## type

```TypeScript
default type(value: InputType | undefined): this
```

Called when the input type is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [InputType](arkts-arkui-textinput-inputtype-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## underlineColor

```TypeScript
default underlineColor(value: ResourceColor | UnderlineColor | undefined): this
```

Define the underline color of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The underline color changes with the underline mode. <br>If the underline color is only set for the normal state, you can directly enter a value of the ResourceColor type. <br>If the value specified is undefined, null, or invalid, all underlines are restored to the default value. <br>Default value: underline color configured for the theme, which is #33182431 by default. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [UnderlineColor](arkts-arkui-textinput-underlinecolor-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## wordBreak

```TypeScript
default wordBreak(value: WordBreak | undefined): this
```

Set the text inline style word break type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is effective for the inline input style, but does not apply to the placeholder text. <br>The component does not support the clip attribute. <br>Therefore, setting this attribute does not affect text clipping. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [WordBreak](arkts-arkui-wordbreak-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |
