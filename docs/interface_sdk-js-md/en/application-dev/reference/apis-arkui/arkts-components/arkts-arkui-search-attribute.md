# Search properties/events

In addition to the [universal attributes](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md), the following attributes are supported.

In addition to the [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md), the following events are supported.

**Inheritance/Implementation:** SearchAttribute extends CommonMethod<SearchAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## autoCapitalizationMode

```TypeScript
autoCapitalizationMode(mode: AutoCapitalizationMode)
```

Sets the text auto-capitalization mode. This API provides the capability, but actual implementation depends on the input method application.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AutoCapitalizationMode](../arkts-apis/arkts-arkui-autocapitalizationmode-e.md) | Yes | Auto-capitalization mode. The default state is inactive. |

## cancelButton

```TypeScript
cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions)
```

Sets the style of the cancel button on the right. For details, see [Example 2: Setting Search and Delete Icons](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#example-2-setting-search-and-delete-icons) and [Example 11: Setting a Custom Symbol-Type Cancel Button](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#example-11-setting-a-custom-symbol-type-cancel-button).

The default icon size on wearable devices is 18 fp.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CancelButtonOptions](arkts-arkui-cancelbuttonoptions-i.md) \| [CancelButtonSymbolOptions](arkts-arkui-cancelbuttonsymboloptions-i.md) | Yes | Style of the cancel button on the right.Default value:{style: CancelButtonStyle.INPUT,icon: {size: '16vp',color: '#99ffffff',src: ' '}}When style is set to **CancelButtonStyle.CONSTANT**, the cancel button is displayed in a default style.<br>**Since:** 12 |

## caretStyle

```TypeScript
caretStyle(value: CaretStyle)
```

Sets the caret style.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CaretStyle](../arkts-apis/arkts-arkui-caretstyle-i.md) | Yes | Caret style.Default value:{width: '2.0vp',color: '#007DFF'} |

## compressLeadingPunctuation

```TypeScript
compressLeadingPunctuation(enabled: Optional<boolean>)
```

Sets whether to enable leading punctuation compression.

> **NOTE：**
> 
> - Leading punctuation is not compressed by default.
> 
> - For the list of punctuation marks that support compression, see the punctuation range at the beginning of a
> line in [ParagraphStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraphstyle-i.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to enable leading punctuation compression.   **true**: Leading punctuation compression is enabled. **false**: Leading punctuation compression is disabled. |

## copyOption

```TypeScript
copyOption(value: CopyOptions)
```

Sets whether the input text can be copied. If this attribute is set to **CopyOptions.None**, the **Search** component supports paste and select-all operations, while other operations such as copy, cut, translate, and share, as well as the Celia Writer assisted writing feature, are disabled.

Dragging is not allowed when **CopyOptions.None** is set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | CopyOptions | Yes | Whether the input text can be copied.Default value: **CopyOptions.LocalDevice |

## customKeyboard

```TypeScript
customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)
```

Sets the custom keyboard.

When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method.

The custom keyboard's height can be set through the **height** attribute of the custom component's root node, and its width is fixed at the default value.

The custom keyboard is presented by overlaying the original screen. It is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box.

The custom keyboard cannot obtain focus, but it blocks gesture events.

By default, the custom keyboard is closed when the input component loses focus. You can also use the [stopEditing](arkts-arkui-searchcontroller-c.md#stopediting) API to close the keyboard.

When setting a custom keyboard, you can bind the [onKeyPreIme](arkts-arkui-commonmethod-c.md#onkeypreime) event to prevent input from the physical keyboard.

From API version 23, the [setCustomKeyboardContinueFeature](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature) API can be used to enable the continuation feature for custom keyboards. When switching between custom keyboards, the system changes the keyboard directly without triggering the close and open animations.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| ComponentContent \| undefined | Yes | Custom keyboard. If the value is **undefined**, the custom keyboard is closed.<br>**Since:** 22 |
| options | [KeyboardOptions](arkts-arkui-keyboardoptions-i.md) | No | Whether to support keyboard avoidance.<br>**Since:** 12 |

## decoration

```TypeScript
decoration(value: TextDecorationOptions)
```

Sets the color, type, and style of the text decorative line.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextDecorationOptions](arkts-arkui-textdecorationoptions-i.md) | Yes | Text decorative line options.Default value: { type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID } |

## dividerColor

```TypeScript
dividerColor(color: Optional<ColorMetrics>)
```

Sets the color of the text box divider.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes | Divider color.By default, system theme colors are used: 0x33000000 in light mode (appears as light black), 0x33FFFFFF in dark mode (appears as light white). |

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions)
```

Sets the extended options of the custom menu, including the text content, icon, and callback.

When [disableMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems) or

[disableSystemServiceMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems) is used to disable system service menu items in the text selection menu, the disabled menu options will be excluded from the parameter list in the onCreateMenu callback of **editMenuOptions**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../arkts-apis/arkts-arkui-editmenuoptions-i.md) | Yes | Extended options of the custom menu. |

## enableAutoSpacing

```TypeScript
enableAutoSpacing(enabled: Optional<boolean>)
```

Sets whether to enable automatic spacing between Chinese and Western characters.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to enable automatic spacing between Chinese and Western characters.    **true**: Enabled. **false**: Disabled.Default value: **false |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(isEnabled: boolean)
```

Specifies whether to enable haptic feedback.

To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](../../../quick-start/module-configuration-file.md) file of the project.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | Whether to enable haptic feedback.   **true**: Haptic feedback is enabled. **false**: Haptic feedback is disabled.Default value: **true |

## enableKeyboardOnFocus

```TypeScript
enableKeyboardOnFocus(value: boolean)
```

Sets whether to pop up the soft keyboard when the **Search** component obtains focus in a way other than clicking.

Since API version 10, the **Search** component is bound to the input method by default when it obtains focus.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to automatically pop up the soft keyboard when the **Search** component gains focus.   **true**: The soft keyboard pops up. **false**: The soft keyboard does not pop up.Default value: **true |

## enablePreviewText

```TypeScript
enablePreviewText(enable: boolean)
```

Sets whether to enable preview text.

The preview content is defined as a temporary, uncommitted input state. Currently, the text interception function is not supported.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable preview text.   **true**: Preview text is enabled. **false**: Preview text is disabled.Default value: **true |

## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined)
```

Sets whether to enable entity recognition for selected text. This API only works on devices that provide text recognition.

When **enableSelectedDataDetector** is set to **true**, all entity types are recognized by default.

This feature is only effective when CopyOptions is set to **CopyOptions.LocalDevice** or **CopyOptions.CrossDevice**.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | Whether to enable entity recognition for selected text.   **true**: Entity recognition is enabled. **false**: Entity recognition is disabled. Default value: **true |

## enterKeyType

```TypeScript
enterKeyType(value: EnterKeyType)
```

Sets the type of the Enter key.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | EnterKeyType | Yes | Type of the Enter key.Default value: **EnterKeyType.Search |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: Optional<boolean>)
```

Adapts the line height to the actual text height for overlapped multi-line text. This API takes effect only when the line height is less than the actual text height. If this API is not set, the line height does not adapt to the actual text height by default.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether the line height is adapted to the actual text height.   **true**: Line height is adapted to the actual text height. **false**: Line height is not adapted to the actual text height. |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

Sets the font color of the input text. **fontSize**, **fontStyle**, **fontWeight**, and **fontFamily** are set in the [textFont](#textfont) attribute.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Font color of the input text.Default value: **'#FF182431'**Default value on wearable devices: **'#dbffffff' |

## fontFeature

```TypeScript
fontFeature(value: string)
```

Sets the font feature, for example, monospaced digits.

Format: normal \| \&lt;feature-tag-value\&gt;

Format of **\&lt;feature-tag-value\&gt;**: \&lt;string\&gt; \[ \&lt;integer\&gt; \| on \| off ]

There can be multiple **\&lt;feature-tag-value\&gt;** values, which are separated by commas (,).

For example, the input format for monospaced clock fonts is "ss01" on.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | Font feature. |

## halfLeading

```TypeScript
halfLeading(halfLeading: Optional<boolean>)
```

Enables half leading for text, which splits the leading equally between the top and bottom of the line.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| halfLeading | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether half leading is enabled. Half leading refers to splitting the leading in half and applying it equally to the top and bottom of the line.   **true**: Half leading is enabled. **false**: Half leading is not enabled.Default value: **false |

## includeFontPadding

```TypeScript
includeFontPadding(include: Optional<boolean>)
```

Sets whether to add spacing to the first and last lines to avoid text truncation. If this attribute is not set, no spacing is added by default.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| include | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to add spacing to the first and last lines to avoid text truncation.    **true**: Spacing is added to the first and last lines. **false**: Spacing is not added to the first and last lines. |

## inputFilter

```TypeScript
inputFilter(value: ResourceStr, error?: Callback<string>)
```

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out.

For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

If **inputFilter** is set and the entered characters are not null, the filtering effect attached to the text box type (specified through the **type** attribute) does not take effect.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | Regular expression. |
| error | Callback&lt;string&gt; | No | Filtered-out content to return when regular expression matching fails. |

## keyboardAppearance

```TypeScript
keyboardAppearance(appearance: Optional<KeyboardAppearance>)
```

Sets the keyboard appearance for the text box. This setting takes effect only after input method adaptation. For details, see [Immersive Mode of the Input Method Application](../../../inputmethod/inputmethod-immersive-mode-guide.md).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appearance | [Optional](arkts-arkui-optional-t.md)&lt;[KeyboardAppearance](../arkts-apis/arkts-arkui-keyboardappearance-e.md)&gt; | Yes | Appearance of the keyboard.Default value: **KeyboardAppearance.NONE_IMMERSIVE |

## letterSpacing

```TypeScript
letterSpacing(value: number | string | Resource)
```

Sets the letter spacing for a text style. If the value specified is a percentage or **0**, the default value is used. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

If the value specified is a negative value, the text is compressed. A negative value too small may result in the text being compressed to 0 and no content being displayed.

This setting applies to every character, including those at line endings.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Letter spacing.Unit: fp |

## lineHeight

```TypeScript
lineHeight(value: number | string | Resource)
```

Sets the text line height. If the value is less than or equal to **0**, the line height is not limited and the font size is adaptive. If the value is of the number type, the unit fp is used.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Text line height. |

## maxFontScale

```TypeScript
maxFontScale(scale: Optional<number|Resource>)
```

Sets the maximum font scale factor for text.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | [Optional](arkts-arkui-optional-t.md)&lt;number \| Resource&gt; | Yes | Maximum font scale factor for text. The **undefined** type is supported.Value range: [1, +∞)   **NOTE：**A value less than 1 is handled as **1**. Abnormal values are ineffective by default.After the **maxFontScale** attribute is set, the content of the **Search** component can be scaled up to 2 times at most.Before use, you need to configure the [configuration.json](../../../quick-start/app-configuration-file.md#tags-in-the-configuration-file) and [app.json5](../../../quick-start/app-configuration-file.md) files in the project. For details, see [Example 19: Setting the Minimum and Maximum Font Scale Factors](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#example-19-setting-the-minimum-and-maximum-font-scale-factors). |

## maxFontSize

```TypeScript
maxFontSize(value: number | string | Resource)
```

Sets the maximum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

For the setting to take effect, this attribute must be used together with [minFontSize](#minfontsize) or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If **maxFontSize** is less than or equal to 0 or **maxFontSize** is less than **minFontSize**, the adaptive font size does not take effect. In this case, the value of **size** in the [textFont](#textfont) attribute takes effect. If **size** is not set, the default value applies.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Maximum font size.Unit: fp |

## maxLength

```TypeScript
maxLength(value: number)
```

Sets the maximum number of characters for text input. By default, there is no maximum number of characters. When the maximum number is reached, no more characters can be entered.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Maximum number of characters for text input.When the value is less than 0, the default value is used and no limit is applied. |

## minFontScale

```TypeScript
minFontScale(scale: Optional<number|Resource>)
```

Sets the minimum font scale factor for text.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | [Optional](arkts-arkui-optional-t.md)&lt;number \| Resource&gt; | Yes | Minimum font scale factor for text. The **undefined** type is supported.Value range: [0, 1]   **NOTE：**A value less than 0 is handled as **0**. A value greater than 1 is handled as **1**. Abnormal values are ineffective by default.Before use, you need to configure the [configuration.json](../../../quick-start/app-configuration-file.md#tags-in-the-configuration-file) and [app.json5](../../../quick-start/app-configuration-file.md) files in the project. For details, see [Example 19: Setting the Minimum and Maximum Font Scale Factors](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#example-19-setting-the-minimum-and-maximum-font-scale-factors). |

## minFontSize

```TypeScript
minFontSize(value: number | string | Resource)
```

Sets the minimum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

For the setting to take effect, this attribute must be used together with [maxFontSize](#maxfontsize) or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If **minFontSize** is less than or equal to 0, the adaptive font size does not take effect. In this case, the value of **size** in the [textFont](#textfont) attribute takes effect. If **size** is not set, the default value applies.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Minimum font size.Unit: fp |

## onChange

```TypeScript
onChange(callback: EditableTextOnChangeCallback)
```

Called when the input in the text box changes.

In this callback, if caret operations are performed, you must adjust the caret logic based on the **previewText** parameter to ensure it works seamlessly within the preview display scenario.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [EditableTextOnChangeCallback](../arkts-apis/arkts-arkui-editabletextonchangecallback-t.md) | Yes | Callback invoked when the input in the text box changes.<br>**Since:** 12 |

## onContentScroll

```TypeScript
onContentScroll(callback: OnContentScrollCallback)
```

Called when the text content is scrolled.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | OnContentScrollCallback | Yes | Callback for text content scrolling.<br>**Since:** 18 |

## onCopy

```TypeScript
onCopy(callback: Callback<string>)
```

Called when a copy operation is performed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | Yes | Callback used to return the copied text content.<br>**Since:** 18 |

## onCut

```TypeScript
onCut(callback: Callback<string>)
```

Called when a cut operation is performed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | Yes | Callback used to return the cut text content.<br>**Since:** 18 |

## onDidDelete

```TypeScript
onDidDelete(callback: Callback<DeleteValue>)
```

Called when text is deleted.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[DeleteValue](../arkts-apis/arkts-arkui-deletevalue-i.md)&gt; | Yes | Callback invoked when text is deleted.It is available only for system input methods. |

## onDidInsert

```TypeScript
onDidInsert(callback: Callback<InsertValue>)
```

Called when text is inserted.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[InsertValue](../arkts-apis/arkts-arkui-insertvalue-i.md)&gt; | Yes | Callback invoked when text is inserted.It is available only for system input methods. |

## onEditChange

```TypeScript
onEditChange(callback: Callback<boolean>)
```

Called when the input state changes. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | Yes | Callback for editing state changes. The value **true** indicates that the text is being inserted, and **false** indicates that the text box is out of focus and text cannot be inserted. |

## onPaste

```TypeScript
onPaste(callback: OnPasteCallback)
```

Called when a paste operation is performed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | OnPasteCallback | Yes | Executed when a paste operation is performed.Callback used to return the pasted text content.<br>**Since:** 18 |

## onSubmit

```TypeScript
onSubmit(callback: Callback<string>)
```

Called when the search icon, search button, or soft keyboard search button is clicked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | Yes | Search submission callback, which returns the text content currently in the search box.<br>**Since:** 18 |

## onSubmit

```TypeScript
onSubmit(callback: SearchSubmitCallback)
```

Invoked when the search icon, search button, or soft keyboard search button is clicked. The submission event provides a method to maintain the edit state of the **Search** component.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SearchSubmitCallback](arkts-arkui-searchsubmitcallback-t.md) | Yes | Callback invoked when the search icon, search button, or soft keyboard search button is clicked. |

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: OnTextSelectionChangeCallback)
```

Called when the text selection changes or the caret position changes during editing.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | OnTextSelectionChangeCallback | Yes | Callback for text selection changes or caret position changes.<br>**Since:** 18 |

## onWillAttachIME

```TypeScript
onWillAttachIME(callback: Callback<IMEClient>)
```

Called when the search box is about to be bound to an input method.

<!--Del-->

Before the search box is bound to an input method, you can use the [setKeyboardAppearanceConfig](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c-sys.md#setkeyboardappearanceconfig) API of **UIContext** to set the keyboard style.<!--DelEnd-->

From API version 22, the [setExtraConfig](../arkts-apis/arkts-arkui-imeclient-i.md#setextraconfig) method of [IMEClient](../arkts-apis/arkts-arkui-imeclient-i.md) can be called to set input method extension information. After the input method is bound, it receives this extension information, which can be used to implement custom functionality.

**IMEClient** is valid only during the execution of **onWillAttachIME** and cannot be called asynchronously.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[IMEClient](../arkts-apis/arkts-arkui-imeclient-i.md)&gt; | Yes | Called when the search box is about to be bound to an input method. |

## onWillChange

```TypeScript
onWillChange(callback: Callback<EditableTextChangeValue, boolean>)
```

Called when the text content is about to change.

This callback is triggered after **onWillInsert** and **onWillDelete**, but before **onDidInsert** and **onDidDelete**.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[EditableTextChangeValue](../arkts-apis/arkts-arkui-editabletextchangevalue-i.md), boolean&gt; | Yes | Callback invoked when the text content is about to change.Returning **true** allows the change to proceed, while returning **false** cancels the change. |

## onWillCopy

```TypeScript
onWillCopy(callback: Callback<string, boolean>)
```

Called before a copy operation is performed. This event is triggered when the user taps the copy menu. Returning **true** allows the copy operation; returning **false** prevents it.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string, boolean&gt; | Yes | Callback used to check whether copy is allowed. |

## onWillCut

```TypeScript
onWillCut(callback: Callback<string, boolean>)
```

Called before a cut operation is performed. This event is triggered when the user taps the cut menu. Returning **true** allows the cut operation; returning **false** prevents it.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;string, boolean&gt; | Yes | Callback used to check whether cut is allowed. |

## onWillDelete

```TypeScript
onWillDelete(callback: Callback<DeleteValue, boolean>)
```

Called when text is about to be deleted.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[DeleteValue](../arkts-apis/arkts-arkui-deletevalue-i.md), boolean&gt; | Yes | Callback invoked when text is about to be deleted.It returns **true** if the text is deleted; returns **false** otherwise.This callback is not invoked for text preview.It is available only for system input methods. |

## onWillInsert

```TypeScript
onWillInsert(callback: Callback<InsertValue, boolean>)
```

Called when text is about to be inserted.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[InsertValue](../arkts-apis/arkts-arkui-insertvalue-i.md), boolean&gt; | Yes | Callback invoked when text is about to be inserted.It returns **true** if the text is inserted; returns **false** otherwise.This callback is not invoked for pre- edit or candidate word operations.It is available only for system input methods. |

## placeholderColor

```TypeScript
placeholderColor(value: ResourceColor)
```

Sets the placeholder text color. The default value on wearable devices is **'#99ffffff'**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Placeholder text color.Default value: **'#99182431' |

## placeholderFont

```TypeScript
placeholderFont(value?: Font)
```

Placeholder text style, including the font size, font weight, font family, and font style.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | No | Placeholder text style. |

## searchButton

```TypeScript
searchButton(value: ResourceStr, option?: SearchButtonOptions)
```

Sets the text on the search button located next to the search text box.

Clicking the search button triggers both **onSubmit** and **onClick** callbacks.

The default font size on wearable devices is 18 fp.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | Text on the search button located next to the search text box.The Resource type is supported since API version 20.<br>**Since:** 20 |
| option | [SearchButtonOptions](arkts-arkui-searchbuttonoptions-i.md) | No | Text style of the search button located next to the search text box.Default value:{fontSize: '16fp',fontColor: '#ff3f97e9'}<br>**Since:** 10 |

## searchIcon

```TypeScript
searchIcon(value: IconOptions | SymbolGlyphModifier)
```

Sets the style of the search icon on the left.

The default icon size on wearable devices is 16 vp.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [IconOptions](arkts-arkui-iconoptions-i.md) \| SymbolGlyphModifier | Yes | Style of the search icon on the left.<!--RP1-->Default value in light mode:{size: '16vp',color: '#99182431',src: ' '}Default value in dark mode:{size: '16vp',color: '#99ffffff',src: ' '} <!--RP1End--><br>**Since:** 12 |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor)
```

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Background color of the selected text. |

## selectedDragPreviewStyle

```TypeScript
selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)
```

Sets the drag preview style for text being dragged in the search box.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SelectedDragPreviewStyle](../arkts-apis/arkts-arkui-selecteddragpreviewstyle-i.md) \| undefined | Yes | Drag preview style for text being dragged in the search box.If this parameter is set to **undefined**, the drag preview follows the theme: white in light mode and black in dark mode. |

## selectionMenuHidden

```TypeScript
selectionMenuHidden(value: boolean)
```

Sets whether to hide the system text selection menu.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to hide the system text selection menu.   **true**: Tapping, number-pressing, number-tapping, triple-tapping, or right-clicking the text box will not trigger the system text selection menu.    **false**: Tapping, number-pressing, number-tapping, triple-tapping, or right-clicking the text box will trigger the system text selection menu.Default value: **false |

## shaderStyle

```TypeScript
shaderStyle(shader: ShaderStyle | undefined)
```

Set the shader style of the text, such as lineargradient or radialgradient.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shader | [ShaderStyle](../arkts-apis/arkts-arkui-shaderstyle-c.md) \| undefined | Yes | The shader style of the text. Passing `undefined` resets it to the default value. |

## stopBackPress

```TypeScript
stopBackPress(isStopped: Optional<boolean>)
```

Sets whether to prevent the back key event from being propagated.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isStopped | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to prevent the back key event from being propagated.   **true**: Propagation is prevented. **false**: Propagation is allowed.Default value: **true** The default value is used for abnormal values. |

## strokeColor

```TypeScript
strokeColor(color: Optional<ResourceColor>)
```

Sets the text stroke color.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes | Stroke color. Default value: font color. Invalid values are treated as the default value. |

## strokeJoinStyle

```TypeScript
strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined)
```

Set the join style of the stroke.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strokeJoinStyle | [StrokeJoinStyle](../arkts-apis/arkts-arkui-strokejoinstyle-e.md) \| undefined | Yes | The join style of stroke. Passing `undefined` resets it to the default value |

## strokeWidth

```TypeScript
strokeWidth(width: Optional<LengthMetrics>)
```

Sets the text stroke width.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | [Optional](arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes | Text stroke width. When the unit of **LengthMetrics** is px:Values&lt;0: solid text.Values&gt; 0: outlined text.Default value: **0** (no stroke) |

## textAlign

```TypeScript
textAlign(value: TextAlign)
```

Sets the text alignment mode in the search text box. Currently, the following alignment modes are supported: **TextAlign.Start**, **TextAlign.Center**, **TextAlign.End**, **TextAlign.LEFT**, and **TextAlign.RIGHT**. **TextAlign.JUSTIFY** behaves the same as **TextAlign.Start**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TextAlign | Yes | Text alignment mode in the search text box.Default value: **TextAlign.Start |

## textDirection

```TypeScript
textDirection(direction: TextDirection | undefined)
```

Specifies the text layout direction. If this attribute is not set, the default text layout direction follows the component layout direction.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | TextDirection \| undefined | Yes | Defines the text layout direction.If this parameter is set to **undefined**, the text layout direction follows the component layout direction as defined by **TextDirection.DEFAULT**. |

## textFont

```TypeScript
textFont(value?: Font)
```

Style of the text entered in the search box, including the font size, font weight, font family, and font style.

The default font size on wearable devices is 18 fp.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | No | Text font of the search text box. |

## textIndent

```TypeScript
textIndent(value: Dimension)
```

Sets the indent of the first line text.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes | Indent of the first line text.Default value: **0 |

## type

```TypeScript
type(value: SearchType)
```

Sets the text box type.

Different **SearchType** values trigger corresponding keyboard types and enforce input restrictions.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SearchType](arkts-arkui-searchtype-e.md) | Yes | Text box type.Default value: **SearchType.NORMAL |
