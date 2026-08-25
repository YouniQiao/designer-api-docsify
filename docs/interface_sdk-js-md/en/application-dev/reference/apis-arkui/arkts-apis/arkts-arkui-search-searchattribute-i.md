# SearchAttribute

The attribute function of search

**Inheritance/Implementation:** SearchAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SearchAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SearchAttribute](arkts-arkui-search-searchattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions | undefined): this
```

Set the cancel button style<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The default icon size on wearable devices is 18 vp. <br>When style is set to CancelButtonStyle.CONSTANT, the Cancel button is always displayed. <br>Default value: &lt;code&gt; {style: CancelButtonStyle.INPUT, icon: {size: '16vp', color: '#99ffffff', src: ' '}} &lt;/code&gt; </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CancelButtonOptions](arkts-arkui-search-cancelbuttonoptions-i.md) \| [CancelButtonSymbolOptions](arkts-arkui-search-cancelbuttonsymboloptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## caretStyle

```TypeScript
default caretStyle(value: CaretStyle | undefined): this
```

Set the cursor style<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Since API version 12, this API can be used to set the text handle color, which is the same as the caret color. <br>Default value: &lt;code&gt; {width: '1.5vp', color: '#007DFF'} &lt;/code&gt; </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(
      value: CustomBuilder | ComponentContentBase | undefined, options?: KeyboardOptions): this
```

Define custom keyboard.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method. <br>The custom keyboard's height can be set through the height attribute of the custom component's root node, and its width is fixed at the default value. <br>The custom keyboard is presented by overlaying the original screen. <br>It is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box. <br>The custom keyboard cannot obtain the focus, but it blocks gesture events. <br>By default, the custom keyboard is closed when the input component loses the focus. <br>You can also use the stopEditing API to close the keyboard. <br>When a custom keyboard is set, the text box does not support camera input, even when the device supports. <br>When setting a custom keyboard, you can bind the onKeyPrelme event to prevent input from the physical keyboard. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## decoration

```TypeScript
default decoration(value: TextDecorationOptions | undefined): this
```

Called when the text decoration of the text is set.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## dividerColor

```TypeScript
default dividerColor(color: ColorMetrics | undefined): this
```

Set the divider color.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

Enable or disable haptic feedback.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>To enable haptic feedback, you must declare the ohos.permission.VIBRATE permission under requestPermissions in the module.json5 file of the project. &lt;code&gt;"requestPermissions": [{"name": "ohos.permission.VIBRATE",}] &lt;/code&gt; </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(value: boolean | undefined): this
```

Sets whether request keyboard or not when on focus.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Since API version 10, the Search component brings up the keyboard by default when it obtains focus. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enterKeyType

```TypeScript
default enterKeyType(value: EnterKeyType | undefined): this
```

Set enter key type of soft keyboard

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Set the text Color<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Universal text attributes fontSize, fontStyle, fontWeight, and fontFamily are set in the textFont attribute. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

Set font feature.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## inputFilter

```TypeScript
default inputFilter(value: ResourceStr | undefined, error?: Callback<string> | undefined): this
```

Called when the inputFilter of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Only inputs that comply with the regular expression can be displayed. <br>Other inputs are filtered out. <br>The specified regular expression can match single characters, but not strings. <br>If inputFilter is set and the entered characters are not null, the filtering effect attached to the text box type (specified through the type attribute) does not take effect. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

Called when the line height of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than or equal to 0, the line height is not limited and the font size is adaptive. <br>If the value is of the number type, the unit fp is used. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

Called when the maximum font scale of the font is set. Value range: [1, +∞)<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The undefined type is supported. <br>A value less than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with minFontSize or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxLength

```TypeScript
default maxLength(value: int | undefined): this
```

Called when the input of maximum text length is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>By default, there is no maximum number of characters. <br>When the maximum number is reached, no more characters can be entered. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

Called when the minimum font scale of the font is set. Value range: [0, 1]<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The undefined type is supported. <br>A value less than 0 is handled as 0. <br>A value greater than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with maxFontSize or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: EditableTextOnChangeCallback | undefined): this
```

Call the function when editing the input text<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In this callback, if cursor operations are performed, developers need to adjust the cursor logic based on the previewText parameter to ensure it works seamlessly within the preview display scenario. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onEditChange

```TypeScript
default onEditChange(callback: Callback<boolean> | undefined): this
```

Called when judging whether the text editing change finished. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: SearchSubmitCallback | undefined): this
```

Call the function when clicked the search button.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [SearchSubmitCallback](arkts-arkui-searchsubmitcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

Called before the search component attach the InputMethod.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillChange

```TypeScript
default onWillChange(callback: Callback<EditableTextChangeValue, boolean> | undefined): this
```

Get text value information when about to change.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This callback is triggered after onWillInsert and onWillDelete, but before onDidInsert and onDidDelete. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

Called before a copy operation is performed. This event is triggered when the user taps the copy menu. Returning **true** allows the copy operation; returning **false** prevents it.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillCut

```TypeScript
default onWillCut(callback: Callback<string, boolean> | undefined): this
```

Called before a cut operation is performed. This event is triggered when the user taps the cut menu. Returning **true** allows the cut operation; returning **false** prevents it.

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillDelete

```TypeScript
default onWillDelete(callback: Callback<DeleteValue, boolean> | undefined): this
```

Get text value information when about to delete.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It returns true if the text is deleted; returns false otherwise. <br>This callback is not invoked for text preview. <br>It is available only for system input methods. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## placeholderColor

```TypeScript
default placeholderColor(value: ResourceColor | undefined): this
```

Set the place hold text color

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## placeholderFont

```TypeScript
default placeholderFont(value?: Font | undefined): this
```

Set the font used for place holder text<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The 'HarmonyOS Sans' font and registered custom fonts are supported. <br>The default font size on wearable devices is 18 px. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## searchButton

```TypeScript
default searchButton(value: string | undefined, option?: SearchButtonOptions | undefined): this
```

Set the search button text, fontSize and fontColor

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| undefined | Yes |
| option | [SearchButtonOptions](arkts-arkui-search-searchbuttonoptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## searchIcon

```TypeScript
default searchIcon(value: IconOptions | SymbolGlyphModifier | undefined): this
```

Set the search icon style<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The default icon size on wearable devices is 16 vp. <br>Default value in light mode: &lt;code&gt; {size: '16vp', color: '#99182431', src: ' '} &lt;/code&gt; <br>Default value in dark mode: &lt;code&gt; {size: '16vp', color: '#99ffffff', src: ' '} &lt;/code&gt; </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [IconOptions](arkts-arkui-search-iconoptions-i.md) \| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## selectionMenuHidden

```TypeScript
default selectionMenuHidden(value: boolean | undefined): this
```

Controls whether the selection menu pops up.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>&lt;em&gt;true&lt;/em&gt;: Tapping, long-pressing, double-tapping, triple-tapping, or right-clicking the text box will not trigger the system text selection menu. <br>&lt;em&gt;false&lt;/em&gt;: Tapping, long-pressing, double-tapping, triple-tapping, or right-clicking the text box will trigger the system text selection menu. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## setSearchOptions

```TypeScript
default setSearchOptions(options?: SearchOptions): this
```

Set Search options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SearchOptions](arkts-arkui-search-searchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

Called when the text align is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Currently, the following alignment modes are supported: Start, Center, and End. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textFont

```TypeScript
default textFont(value?: Font | undefined): this
```

Set the font used for input text<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Currently, only the default font family is supported. <br>The default font size on wearable devices is 18 fp. </p>

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## type

```TypeScript
default type(value: SearchType | undefined): this
```

Called when the search type is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SearchType](arkts-arkui-search-searchtype-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |
