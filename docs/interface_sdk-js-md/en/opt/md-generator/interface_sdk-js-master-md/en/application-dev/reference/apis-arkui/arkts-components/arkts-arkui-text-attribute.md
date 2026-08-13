# Text properties/events

In addition to the [universal attributes](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md), the following attributes are supported. In addition to the [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md), the following events are supported.

**Inheritance/Implementation:** TextAttribute extends CommonMethod<TextAttribute>

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-declare class TextAttribute--><!--Device-unnamed-declare class TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## baselineOffset

```TypeScript
baselineOffset(value: number | ResourceStr)
```

Sets the offset of the text baseline. Percentage values follow default display behavior. A positive value moves the content upwards, while a negative value moves it downwards.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-baselineOffset(value: number | ResourceStr): TextAttribute--><!--Device-TextAttribute-baselineOffset(value: number | ResourceStr): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## bindSelectionMenu

```TypeScript
bindSelectionMenu(spanType: TextSpanType, content: CustomBuilder, responseType: TextResponseType,
    options?: SelectionMenuOptions)
```

Sets the custom selection menu. The long-press response duration of **bindSelectionMenu** is 600 ms while that of [bindContextMenu](arkts-arkui-commonmethod-c.md#bindContextMenu) is 800 ms. When both are bound and their triggering methods are set to long press, **bindSelectionMenu** takes precedence. When the custom menu is too long, it is recommended that nest a Scroll component inside to prevent the keyboard from being obscured. > **NOTE：**> > This API cannot be called within attributeModifier. > > When [editMenuOptions](#editMenuOptions) is used for configuring the text selection menu, the > system's default style and trigger conditions are preserved. > > In contrast, when [bindSelectionMenu](#bindSelectionMenu) is used, both the menu style and the > trigger conditions are fully customizable.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-bindSelectionMenu(spanType: TextSpanType, content: CustomBuilder, responseType: TextResponseType,    options?: SelectionMenuOptions): TextAttribute--><!--Device-TextAttribute-bindSelectionMenu(spanType: TextSpanType, content: CustomBuilder, responseType: TextResponseType,    options?: SelectionMenuOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spanType | [TextSpanType](arkts-arkui-textspantype-e.md) | Yes |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| responseType | [TextResponseType](arkts-arkui-textresponsetype-e.md) | Yes |
| options | SelectionMenuOptions | No |

## caretColor

```TypeScript
caretColor(color: ResourceColor)
```

Sets the color of the text selection handle, also known as the caret, in the text box.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-TextAttribute-caretColor(color: ResourceColor): TextAttribute--><!--Device-TextAttribute-caretColor(color: ResourceColor): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## compressLeadingPunctuation

```TypeScript
compressLeadingPunctuation(enabled: Optional<boolean>)
```

Sets whether to enable leading punctuation compression. > **NOTE：**> > - Leading punctuation is not compressed by default. > > - For the range of punctuation marks that support leading compression, see > [ParagraphStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraphstyle-i.md#ParagraphStyle).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextAttribute-compressLeadingPunctuation(enabled: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-compressLeadingPunctuation(enabled: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## contentTransition

```TypeScript
contentTransition(transition: Optional<ContentTransition>)
```

Applies a transition animation to text content. Supports numeric flip animation via [NumericTextTransition](../arkts-apis/arkts-arkui-numerictexttransition-c.md#NumericTextTransition).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-contentTransition(transition: Optional<ContentTransition>): TextAttribute--><!--Device-TextAttribute-contentTransition(transition: Optional<ContentTransition>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | [Optional](arkts-arkui-optional-t.md)&lt;[ContentTransition](../arkts-apis/arkts-arkui-contenttransition-c.md)&gt; | Yes |

## copyOption

```TypeScript
copyOption(value: CopyOptions)
```

Sets whether copy and paste operations are allowed. Since API version 20, copied text from the **Text** component includes HTML-formatted content in the pasteboard. - When the **Text** component contains child elements, only Span and ImageSpan support HTML-formatted pasteboard content. - For styled strings, refer to [toHtml](../arkts-apis/arkts-arkui-styledstring-c.md#toHtml) for supported HTML conversion scope. When **copyOption** is set to **CopyOptions.InApp** or **CopyOptions.LocalDevice**: - A long press on the text will display a menu that offers the copy and select-all options. - By default, selected text is draggable. To disable dragging, set **draggable** to **false**. - To support **Ctrl+C** copying, also set [textSelectable](#textSelectable) to **TextSelectableMode.SELECTABLE_FOCUSABLE**. The **Text** component listens for **onClick**, which is a non-bubbling event. To allow parent components to respond to clicks within the **Text** area, use [parallelGesture](arkts-arkui-commonmethod-c.md#parallelGesture) on the parent. For implementation guidance, see [Example 7: Setting Text Recognition](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#example-7-setting-text-recognition). Because widgets do not have the long press event, the menu will not be displayed when users long press text.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-copyOption(value: CopyOptions): TextAttribute--><!--Device-TextAttribute-copyOption(value: CopyOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](../arkts-apis/arkts-arkui-copyoptions-e.md) | Yes |

## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig)
```

Configures text recognition settings, including entity types to detect, display styles for detected entities, and long-press preview options. This API must be used together with [enableDataDetector](#enableDataDetector). It takes effect only when **enableDataDetector** is set to **true**.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-dataDetectorConfig(config: TextDataDetectorConfig): TextAttribute--><!--Device-TextAttribute-dataDetectorConfig(config: TextDataDetectorConfig): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [TextDataDetectorConfig](../arkts-apis/arkts-arkui-textdatadetectorconfig-i.md) | Yes |

## decoration

```TypeScript
decoration(value: DecorationStyleInterface)
```

Style and color of the text decorative line. > **NOTE：**> > When the bottom contour of a character intersects with the decoration, underline avoidance is triggered, commonly > affecting characters like "g", "j", "y", "q", and "p." > > If the decoration color is set to **Color.Transparent**, it inherits the text color of the first character in > each line. If the decoration color is set to **"#00FFFFFF"**, the line becomes fully transparent.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-decoration(value: DecorationStyleInterface): TextAttribute--><!--Device-TextAttribute-decoration(value: DecorationStyleInterface): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DecorationStyleInterface](../arkts-apis/arkts-arkui-decorationstyleinterface-i.md) | Yes |

## draggable

```TypeScript
draggable(value: boolean)
```

Sets the drag effect of the selected text. This attribute cannot be used together with the onDragStart event. If set to **true**, **draggable** must be used in conjunction with CopyOptions. When **copyOptions** is set to **CopyOptions.InApp** or **CopyOptions.LocalDevice**, the selected text becomes draggable and can be copied into a text box.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-draggable(value: boolean): TextAttribute--><!--Device-TextAttribute-draggable(value: boolean): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions)
```

Sets the extended options for the custom menu, including the text content, icon, and callback. When [disableMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disableMenuItems) or [disableSystemServiceMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disableSystemServiceMenuItems) is used to disable system service menu items in the text selection menu, the disabled menu options will be excluded from the parameter list in the onCreateMenu callback of **editMenuOptions**. > **NOTE：**> > When [editMenuOptions](#editMenuOptions) is used for configuring the text selection menu, the > system's default style and trigger conditions are preserved. > > In contrast, when [bindSelectionMenu](#bindSelectionMenu) is used, both the menu style and the > trigger conditions are fully customizable.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-editMenuOptions(editMenu: EditMenuOptions): TextAttribute--><!--Device-TextAttribute-editMenuOptions(editMenu: EditMenuOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| editMenu | [EditMenuOptions](../arkts-apis/arkts-arkui-editmenuoptions-i.md) | Yes |

## ellipsisMode

```TypeScript
ellipsisMode(value: EllipsisMode)
```

Sets the ellipsis position. For the settings to work, **overflow** must be set to **TextOverflow.Ellipsis** and **maxLines** must be specified. Setting **ellipsisMode** alone does not take effect. **EllipsisMode.START** and **EllipsisMode.CENTER** take effect only when text overflows in a single line.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-ellipsisMode(value: EllipsisMode): TextAttribute--><!--Device-TextAttribute-ellipsisMode(value: EllipsisMode): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [EllipsisMode](#ellipsisMode) | Yes |

## enableAutoSpacing

```TypeScript
enableAutoSpacing(enabled: Optional<boolean>)
```

Sets whether to enable automatic spacing between Chinese and Western characters.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-enableAutoSpacing(enabled: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-enableAutoSpacing(enabled: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean)
```

Sets whether to enable special entity detection within the text. Special entities are detected when **enableDataDetector** is set to **true**. The style of detected entities is as follows: the font color is changed to blue, and a blue underline is added. > **NOTE：**> > - This API takes effect only when the device has an underlying text detection capability. > > - When [textOverflow](#textOverflow) is set to **TextOverflow.MARQUEE**, text special entity > detection is not performed. &lt;!--RP2--&gt;&lt;!--RP2End--&gt;

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-enableDataDetector(enable: boolean): TextAttribute--><!--Device-TextAttribute-enableDataDetector(enable: boolean): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(isEnabled: boolean)
```

Sets whether to enable haptic feedback. To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](../../../quick-start/module-configuration-file.md) file of the project. > **NOTE：**> > This API can be called within attributeModifier since API version 18.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-TextAttribute-enableHapticFeedback(isEnabled: boolean): TextAttribute--><!--Device-TextAttribute-enableHapticFeedback(isEnabled: boolean): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |

## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined)
```

Sets whether to enable entity recognition for selected text. This API only works on devices that provide text recognition. When **enableSelectedDataDetector** is set to **true**, all entity types are recognized by default. This feature is only effective when CopyOptions is set to **CopyOptions.LocalDevice** or **CopyOptions.CrossDevice**.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextAttribute-enableSelectedDataDetector(enable: boolean | undefined): TextAttribute--><!--Device-TextAttribute-enableSelectedDataDetector(enable: boolean | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing(enabled: Optional<boolean>)
```

Adapts the line height to the actual text height for overlapped multi-line text. This API takes effect only when the line height is less than the actual text height. If this API is not set, the line height does not adapt to the actual text height by default.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextAttribute-fallbackLineSpacing(enabled: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-fallbackLineSpacing(enabled: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## font

```TypeScript
font(value: Font)
```

Sets the text style, covering the font size, font width, font family, and font style.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-font(value: Font): TextAttribute--><!--Device-TextAttribute-font(value: Font): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Font](#font) | Yes |

## font

```TypeScript
font(fontValue: Font, options?: FontSettingOptions)
```

Sets the font style, with support for font settings. It is only effective for the **Text** component, not for its child components.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-TextAttribute-font(fontValue: Font, options?: FontSettingOptions): TextAttribute--><!--Device-TextAttribute-font(fontValue: Font, options?: FontSettingOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontValue | [Font](#font) | Yes |
| options | [FontSettingOptions](../arkts-apis/arkts-arkui-fontsettingoptions-i.md) | No |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

Sets the font color.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-fontColor(value: ResourceColor): TextAttribute--><!--Device-TextAttribute-fontColor(value: ResourceColor): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## fontFamily

```TypeScript
fontFamily(value: string | Resource)
```

Sets the font family. > **NOTE：**> > You can use [loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md#loadFontSync) to register custom fonts.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-fontFamily(value: string | Resource): TextAttribute--><!--Device-TextAttribute-fontFamily(value: string | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## fontFeature

```TypeScript
fontFeature(value: string)
```

Sets the font feature, for example, monospaced digits. Format: normal \| \&lt;feature-tag-value\&gt; Format of **\&lt;feature-tag-value\&gt;**: \&lt;string\&gt; \[ \&lt;integer\&gt; \| on \| off ] There can be multiple **\&lt;feature-tag-value\&gt;** values, which are separated by commas (,). For example, the input format for monospaced clock fonts is "ss01" on. > **NOTE：**> > The **Text** component cannot contain both text and the child component **Span** or **ImageSpan**. If both of > them exist, only the content in **Span** or **ImageSpan** is displayed. > > The typesetting engine rounds down the value of width to ensure that > the value is an integer. If the typesetting engine rounds up the value instead, the right side of the text may be > clipped. > > When multiple **Text** components are placed in the Row container with no specific layout or space > allocation settings configured, the components are laid out based on the maximum size of the container. To make > sure the sum of the components' main axis sizes does not exceed the main axis size of the container, you can set > [layoutWeight](arkts-arkui-commonmethod-c.md#layoutWeight) or use the flex layout. > > The system's default font supports the following ligatures: Th, fb, ff, fb, ffb, ffh, ffi, ffk, ffl, fh, fi, fk, > fl, rf, rt, rv, rx, ry. These ligatures may cause unexpected effects of spans and styled strings. Disabling the > ligature feature can avoid this issue. > > Text rendering behavior is closely tied to the font file in use. For instance, the system's default font supports > 8-punctuation compression only for left-side punctuation marks. Right-side punctuation, including exclamation > marks, enumeration commas, and question marks, is not affected by this feature.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-TextAttribute-fontFeature(value: string): TextAttribute--><!--Device-TextAttribute-fontFeature(value: string): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## fontSize

```TypeScript
fontSize(value: number | string | Resource)
```

Sets the text size.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-fontSize(value: number | string | Resource): TextAttribute--><!--Device-TextAttribute-fontSize(value: number | string | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## fontStyle

```TypeScript
fontStyle(value: FontStyle)
```

Sets the font style.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-fontStyle(value: FontStyle): TextAttribute--><!--Device-TextAttribute-fontStyle(value: FontStyle): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [FontStyle](#fontStyle) | Yes |

## fontVariations

```TypeScript
fontVariations(fontVariations: Array<FontVariation>)
```

Set the font variation.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-fontVariations(fontVariations: Array<FontVariation>): TextAttribute--><!--Device-TextAttribute-fontVariations(fontVariations: Array<FontVariation>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fontVariations](#fontVariations) | Array & lt;FontVariation & gt; | Yes |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | ResourceStr)
```

Sets the font weight. If the value is too large, the text may be clipped depending on the font.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-fontWeight(value: number | FontWeight | ResourceStr): TextAttribute--><!--Device-TextAttribute-fontWeight(value: number | FontWeight | ResourceStr): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| FontWeight \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## fontWeight

```TypeScript
fontWeight(weight: number | FontWeight | ResourceStr, options?: FontSettingOptions)
```

Sets the text font weight, with support for font settings. It is only effective for the **Text** component, not for its child components.&lt;!--RP4--&gt;&lt;!--RP4End--&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-TextAttribute-fontWeight(weight: number | FontWeight | ResourceStr, options?: FontSettingOptions): TextAttribute--><!--Device-TextAttribute-fontWeight(weight: number | FontWeight | ResourceStr, options?: FontSettingOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| weight | number \| FontWeight \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| options | [FontSettingOptions](../arkts-apis/arkts-arkui-fontsettingoptions-i.md) | No |

## halfLeading

```TypeScript
halfLeading(halfLeading: boolean)
```

Whether half leading is enabled. Half leading refers to splitting the leading in half and applying it equally to the top and bottom of the line.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-halfLeading(halfLeading: boolean): TextAttribute--><!--Device-TextAttribute-halfLeading(halfLeading: boolean): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [halfLeading](#halfLeading) | boolean | Yes |

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy(value: TextHeightAdaptivePolicy)
```

Sets the font size adjustment strategy for adaptive text layout. The available modes are as follows: - **MAX_LINES_FIRST**: prioritizes using the [maxLines](#maxLines) attribute to control text height. If the **maxLines** setting results in a layout beyond the layout constraints, the text will shrink to a font size between [minFontSize](#minFontSize) and [maxFontSize](#maxFontSize) to allow for more content to be shown. - **MIN_FONT_SIZE_FIRST**: prioritizes using the **minFontSize** attribute to control text height. If the text fits on one line at **minFontSize**, the system attempts to increase the font size between **minFontSize** and **maxFontSize** to fill the line with the largest available font size. If the text cannot fit on a single line even at **minFontSize**, it sticks with **minFontSize**. - **LAYOUT_CONSTRAINT_FIRST**: prioritizes using layout constraints to control text height. If the resultant layout is beyond the layout constraints, the text will shrink to a font size between **minFontSize** and **maxFontSize** to respect the layout constraints. If the text still extends beyond the layout constraints after shrinking to **minFontSize**, the lines that exceed the constraints are deleted.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAttribute--><!--Device-TextAttribute-heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextHeightAdaptivePolicy](../arkts-apis/arkts-arkui-textheightadaptivepolicy-e.md) | Yes |

## includeFontPadding

```TypeScript
includeFontPadding(include: Optional<boolean>)
```

Sets whether to add spacing to the first and last lines to avoid text truncation. If this attribute is not set, no spacing is added by default.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextAttribute-includeFontPadding(include: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-includeFontPadding(include: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| include | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## incrementalUpdatePolicy

```TypeScript
incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined)
```

Sets the incremental update policy for text rendering. This API takes effect only when Text content contains a StyledString. Default value is IncrementalUpdatePolicy.NONE.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): TextAttribute--><!--Device-TextAttribute-incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [IncrementalUpdatePolicy](../arkts-apis/arkts-arkui-incrementalupdatepolicy-e.md) \| undefined | Yes |

## letterSpacing

```TypeScript
letterSpacing(value: number | ResourceStr)
```

Sets the letter spacing for a text style. If the value specified is a percentage or **0**, the default value is used. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported. Negative values compress text. Excessive compression may reduce content area to zero, hiding content. This setting applies to every character, including those at line endings.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-letterSpacing(value: number | ResourceStr): TextAttribute--><!--Device-TextAttribute-letterSpacing(value: number | ResourceStr): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## lineBreakStrategy

```TypeScript
lineBreakStrategy(strategy: LineBreakStrategy)
```

Sets the line break rule. This attribute takes effect only when [wordBreak](#wordBreak) is not **WordBreak.BREAK_ALL**. Hyphens are not supported.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-lineBreakStrategy(strategy: LineBreakStrategy): TextAttribute--><!--Device-TextAttribute-lineBreakStrategy(strategy: LineBreakStrategy): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [LineBreakStrategy](../arkts-apis/arkts-arkui-linebreakstrategy-e.md) | Yes |

## lineHeight

```TypeScript
lineHeight(value: number | string | Resource)
```

Sets the text line height. If the value is less than or equal to **0**, the line height is unrestricted and adapts to the font size. When the value is a number, the unit is fp. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported. > **NOTE：**> > If certain characters have significantly taller glyphs than others in the same line, layout anomalies such as > clipping, overlapping, or misalignment may occur. In this case, adjust component attributes such as height and > line height to ensure proper layout rendering.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-lineHeight(value: number | string | Resource): TextAttribute--><!--Device-TextAttribute-lineHeight(value: number | string | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## lineHeightMultiple

```TypeScript
lineHeightMultiple(value: number | undefined)
```

Sets the line height of text in multiple mode. The line height equals the input parameter **value** multiplied by **fontHeight**. > **NOTE：**> > When both this API and [lineHeight](#lineHeight) are set, only **lineHeightMultiple** takes > effect.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-TextAttribute-lineHeightMultiple(value: number | undefined): TextAttribute--><!--Device-TextAttribute-lineHeightMultiple(value: number | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| undefined | Yes |

## lineSpacing

```TypeScript
lineSpacing(value: LengthMetrics)
```

Sets the line spacing of the text. If the value specified is less than or equal to 0, the default value **0** is used.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-lineSpacing(value: LengthMetrics): TextAttribute--><!--Device-TextAttribute-lineSpacing(value: LengthMetrics): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) | Yes |

## lineSpacing

```TypeScript
lineSpacing(value: LengthMetrics, options?: LineSpacingOptions)
```

Sets the line spacing for text. When **LineSpacingOptions** is not specified, line spacing is applied above the first line and below the last line by default.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAttribute--><!--Device-TextAttribute-lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) | Yes |
| options | [LineSpacingOptions](../arkts-apis/arkts-arkui-linespacingoptions-i.md) | No |

## marqueeOptions

```TypeScript
marqueeOptions(options: Optional<TextMarqueeOptions>)
```

Sets the marquee effect for text. The **marqueeOptions** settings take effect only when **textOverflow** is set to **TextOverflow.MARQUEE**.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TextAttribute-marqueeOptions(options: Optional<TextMarqueeOptions>): TextAttribute--><!--Device-TextAttribute-marqueeOptions(options: Optional<TextMarqueeOptions>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[TextMarqueeOptions](arkts-arkui-textmarqueeoptions-i.md)&gt; | Yes |

## maxFontScale

```TypeScript
maxFontScale(scale: number | Resource)
```

Sets the maximum font scale factor for text.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-maxFontScale(scale: number | Resource): TextAttribute--><!--Device-TextAttribute-maxFontScale(scale: number | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## maxFontSize

```TypeScript
maxFontSize(value: number | string | Resource)
```

Sets the maximum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported. For the setting to take effect, this attribute must be used together with [minFontSize](#minFontSize) and [maxLines](#maxLines), or layout constraint settings. When the adaptive font size is used, the **fontSize** settings do not take effect. If the value of **maxFontSize** is less than or equal to 0 or is less than the value of **minFontSize**, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontSize) attribute is used instead. If **fontSize** is not set, the default value will apply. Since API version 18, adaptive font sizing is supported on child components and styled strings, and text segments without an explicitly defined font size will automatically adjust based on the available space.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-maxFontSize(value: number | string | Resource): TextAttribute--><!--Device-TextAttribute-maxFontSize(value: number | string | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## maxLineHeight

```TypeScript
maxLineHeight(value: LengthMetrics | undefined)
```

Sets the maximum line height of text. If the value is less than or equal to 0, the maximum line height is unrestricted. If **maxLineHeight** is less than **minLineHeight**, **maxLineHeight** takes effect using the value of **minLineHeight**.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-TextAttribute-maxLineHeight(value: LengthMetrics | undefined): TextAttribute--><!--Device-TextAttribute-maxLineHeight(value: LengthMetrics | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | LengthMetrics \| undefined | Yes |

## maxLines

```TypeScript
maxLines(value: number)
```

Sets the maximum number of lines for text. By default, text is automatically folded. If this attribute is specified, the text will not exceed the specified number of lines. If there is extra text, you can use [textOverflow](#textOverflow) to specify how it is displayed.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-maxLines(value: number): TextAttribute--><!--Device-TextAttribute-maxLines(value: number): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## minFontScale

```TypeScript
minFontScale(scale: number | Resource)
```

Sets the minimum font scale factor for text.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-minFontScale(scale: number | Resource): TextAttribute--><!--Device-TextAttribute-minFontScale(scale: number | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## minFontSize

```TypeScript
minFontSize(value: number | string | Resource)
```

Sets the minimum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported. For the setting to take effect, this attribute must be used together with [maxFontSize](#maxFontSize) and [maxLines](#maxLines), or layout constraint settings. When the adaptive font size is used, the **fontSize** settings do not take effect. If the value of **minFontSize** is less than or equal to 0, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontSize) attribute is used instead. If **fontSize** is not set, the default value will apply. Since API version 18, adaptive font sizing is supported on child components and styled strings, and text segments without an explicitly defined font size will automatically adjust based on the available space.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-minFontSize(value: number | string | Resource): TextAttribute--><!--Device-TextAttribute-minFontSize(value: number | string | Resource): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## minLineHeight

```TypeScript
minLineHeight(value: LengthMetrics | undefined)
```

Sets the minimum line height of text. If the value is less than or equal to 0, the default value **0** is used.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-TextAttribute-minLineHeight(value: LengthMetrics | undefined): TextAttribute--><!--Device-TextAttribute-minLineHeight(value: LengthMetrics | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | LengthMetrics \| undefined | Yes |

## minLines

```TypeScript
minLines(minLines: Optional<number>)
```

Sets the minimum number of lines for text. If the actual text height is less than the height for the minimum number of lines, the component uses the height corresponding to the minimum number of lines. When this API and [maxLines](#maxLines) are both set, the minimum line height cannot exceed the maximum line height. If constraintSize is set for the text, the component height is confined within the constraintSize bounds.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-TextAttribute-minLines(minLines: Optional<number>): TextAttribute--><!--Device-TextAttribute-minLines(minLines: Optional<number>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [minLines](#minLines) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

## onCopy

```TypeScript
onCopy(callback: (value: string) => void)
```

Called when data is copied to the pasteboard, which is displayed when the text box is long pressed. Currently, only text can be copied.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-onCopy(callback: (value: string) => void): TextAttribute--><!--Device-TextAttribute-onCopy(callback: (value: string) => void): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (value: string) = & gt; void | Yes |

## onMarqueeStateChange

```TypeScript
onMarqueeStateChange(callback: Callback<MarqueeState>)
```

Called when the marquee animation reaches the specified state.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TextAttribute-onMarqueeStateChange(callback: Callback<MarqueeState>): TextAttribute--><!--Device-TextAttribute-onMarqueeStateChange(callback: Callback<MarqueeState>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[MarqueeState](arkts-arkui-marqueestate-e.md)&gt; | Yes |

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void)
```

Called when the text selection position changes.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAttribute--><!--Device-TextAttribute-onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (selectionStart: number, selectionEnd: number) = & gt; void | Yes |

## onWillCopy

```TypeScript
onWillCopy(callback: Callback<string, boolean>)
```

Called before the copy operation is performed. **Since**: 26.0.0

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-onWillCopy(callback: Callback<string, boolean>): TextAttribute--><!--Device-TextAttribute-onWillCopy(callback: Callback<string, boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;string, boolean & gt; | Yes |

## optimizeTrailingSpace

```TypeScript
optimizeTrailingSpace(optimize: Optional<boolean>)
```

Sets whether to optimize trailing spaces at line endings during text layout, resolving alignment display issues caused by trailing spaces. When **Text.optimizeTrailingSpace** is set to **true**: * Trailing space optimization applies to multi-line text, single-line text, and text and image layouts ( particularly noticeable with **TextAlign.Center** or **TextAlign.End**). * For text containing only spaces, decoration lines, shadows, and background colors follow the space text display. * Leading spaces are not optimized. When text with trailing spaces wraps, trailing spaces on each line are optimized based on component width. When optimizing pure space text by setting [optimizeTrailingSpace](#optimizeTrailingSpace) to **true**, you cannot simultaneously set backgroundColor, [decoration](#decoration), and [textAlign](#textAlign) attributes.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-optimizeTrailingSpace(optimize: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-optimizeTrailingSpace(optimize: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optimize | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## orphanCharOptimization

```TypeScript
orphanCharOptimization(enabled: Optional<boolean>)
```

Sets whether to enable orphan character optimization during text typesetting. If this attribute is not set, orphan character optimization is disabled by default. Orphan character optimization improves the text layout by handling the orphan character (the first Chinese character of the last line of a paragraph) more efficiently. When enabled, it adjusts line breaks to avoid orphan characters as much as possible. This feature takes effect only when [wordBreak](#wordBreak) is not **BREAK_ALL** and [locale](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textstyle-i.md#TextStyle) of the first [TextStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textstyle-i.md#TextStyle) of the text to be typeset is either **"zh-Hans"** or **"zh-Hant"**. **Since**: 26.0.0

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-orphanCharOptimization(enabled: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-orphanCharOptimization(enabled: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## privacySensitive

```TypeScript
privacySensitive(supported: boolean)
```

Sets whether to enable privacy mode on widgets.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-TextAttribute-privacySensitive(supported: boolean): TextAttribute--><!--Device-TextAttribute-privacySensitive(supported: boolean): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| supported | boolean | Yes |

## punctuationOverflow

```TypeScript
punctuationOverflow(enabled: Optional<boolean>)
```

Whether to enable punctuation overflow at line ends.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-punctuationOverflow(enabled: Optional<boolean>): TextAttribute--><!--Device-TextAttribute-punctuationOverflow(enabled: Optional<boolean>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: ResourceColor)
```

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-TextAttribute-selectedBackgroundColor(color: ResourceColor): TextAttribute--><!--Device-TextAttribute-selectedBackgroundColor(color: ResourceColor): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedDragPreviewStyle

```TypeScript
selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)
```

Applies a transition animation to text content. Supports numeric flip animation via [NumericTextTransition](../arkts-apis/arkts-arkui-numerictexttransition-c.md#NumericTextTransition).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextAttribute-selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): TextAttribute--><!--Device-TextAttribute-selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SelectedDragPreviewStyle](../arkts-apis/arkts-arkui-selecteddragpreviewstyle-i.md) \| undefined | Yes |

## selection

```TypeScript
selection(selectionStart: number, selectionEnd: number)
```

Sets text selection. The selected text is highlighted, with selection handles and the text selection menu displayed. If [copyOption](#copyOption) is set to **CopyOptions.None**, the setting of the **selection** attribute does not take effect. If [textOverflow](#textOverflow) is set to **TextOverflow.MARQUEE**, the setting of the **selection** attribute does not take effect. If the value of **selectionStart** is greater than or equal to that of **selectionEnd**, no text will be selected. The value range is [0, textSize], where **textSize** indicates the maximum number of characters in the text content. If the value is less than 0, the value **0** will be used. If the value is greater than **textSize**, **textSize** will be used. If the selection range falls within a truncated or invisible area, selection is ignored. When clip is set to **false**, the text outside the parent component can be selected. You can obtain the selection range change result through the [onTextSelectionChange](#onTextSelectionChange) API.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-selection(selectionStart: number, selectionEnd: number): TextAttribute--><!--Device-TextAttribute-selection(selectionStart: number, selectionEnd: number): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | number | Yes |
| selectionEnd | number | Yes |

## shaderStyle

```TypeScript
shaderStyle(shader: ShaderStyle)
```

Applies gradient or solid color effects to text. Supports [RadialGradientStyle](../arkts-apis/arkts-arkui-radialgradientstyle-c.md#RadialGradientStyle), [LinearGradientStyle](../arkts-apis/arkts-arkui-lineargradientstyle-c.md#LinearGradientStyle), and [ColorShaderStyle](../arkts-apis/arkts-arkui-colorshaderstyle-c.md#ColorShaderStyle). **shaderStyle** takes precedence over fontColor and AI-based styling. For solid colors, prefer using fontColor.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-shaderStyle(shader: ShaderStyle): TextAttribute--><!--Device-TextAttribute-shaderStyle(shader: ShaderStyle): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shader | [ShaderStyle](../arkts-apis/arkts-arkui-shaderstyle-c.md) | Yes |

## tailIndents

```TypeScript
tailIndents(value: Optional<LengthMetrics | Array<LengthMetrics>>)
```

Specify the tail indentation for each line in a text block. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;When a single LengthMetrics value is provided, all lines share the same tail indent. &lt;br&gt;When an array is provided, the i-th element specifies the tail indent for the i-th line. If the number of text lines exceeds the array length, the last element in the array is used for the remaining lines. &lt;br&gt;Negative values are treated as 0. &lt;br&gt;If the value is set to undefined, the default value 0 is used. &lt;/p&gt;

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextAttribute-tailIndents(value: Optional<LengthMetrics | Array<LengthMetrics>>): TextAttribute--><!--Device-TextAttribute-tailIndents(value: Optional<LengthMetrics | Array<LengthMetrics>>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Optional](arkts-arkui-optional-t.md)&lt;LengthMetrics \| Array & lt;LengthMetrics & gt; & gt; | Yes |

## textAlign

```TypeScript
textAlign(value: TextAlign)
```

Sets the horizontal alignment of the text. The text takes up the full width of the **Text** component. The vertical position of the text paragraph can be controlled by the align attribute, but the horizontal position cannot be controlled by **align** in this component. The specific effects are as follows: - **Alignment.TopStart**, **Alignment.Top**, **Alignment.TopEnd**: Content aligns to the top. - **Alignment.Start**, **Alignment.Center**, **Alignment.End**: Content is centered vertically. - **Alignment.BottomStart**, **Alignment.Bottom**, **Alignment.BottomEnd:** Content aligns to the bottom. When **textAlign** is set to **TextAlign.JUSTIFY**, the [wordBreak](#wordBreak) property must be configured according to the text content. The last line of text aligns to the start horizontally and does not participate in justification. > **NOTE：**> > **textAlign** only adjusts the overall text layout and does not affect character display order. For character > display order adjustment, see > [Bidirectional Text Layout and Alignment](../../../ui/arkts-internationalization.md#bidirectional-text-layout-and-alignment).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-textAlign(value: TextAlign): TextAttribute--><!--Device-TextAttribute-textAlign(value: TextAlign): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextAlign](#textAlign) | Yes |

## textCase

```TypeScript
textCase(value: TextCase)
```

Sets the text case.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-textCase(value: TextCase): TextAttribute--><!--Device-TextAttribute-textCase(value: TextCase): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextCase](../arkts-apis/arkts-arkui-textcase-e.md) | Yes |

## textContentAlign

```TypeScript
textContentAlign(textContentAlign: Optional<TextContentAlign>)
```

Sets the vertical alignment of the text content area within the component. This API takes effect only when the height of the text content exceeds the component's height.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-TextAttribute-textContentAlign(textContentAlign: Optional<TextContentAlign>): TextAttribute--><!--Device-TextAttribute-textContentAlign(textContentAlign: Optional<TextContentAlign>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textContentAlign](#textContentAlign) | [Optional](arkts-arkui-optional-t.md)&lt;[TextContentAlign](../arkts-apis/arkts-arkui-textcontentalign-e.md)&gt; | Yes |

## textDirection

```TypeScript
textDirection(direction: TextDirection | undefined)
```

Specifies the text layout direction. If this attribute is not set, the default text layout direction follows the component layout direction.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextAttribute-textDirection(direction: TextDirection | undefined): TextAttribute--><!--Device-TextAttribute-textDirection(direction: TextDirection | undefined): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | TextDirection \| undefined | Yes |

## textIndent

```TypeScript
textIndent(value: Length)
```

Sets the indent of the first line text.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-textIndent(value: Length): TextAttribute--><!--Device-TextAttribute-textIndent(value: Length): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## textOverflow

```TypeScript
textOverflow(options: TextOverflowOptions)
```

Sets the display mode for overflowing text. When [TextOverflowOptions](arkts-arkui-textoverflowoptions-i.md#TextOverflowOptions) is set to **TextOverflow.None**, **TextOverflow.Clip**, or **TextOverflow.Ellipsis**: - **TextOverflow.None** or **TextOverflow.Clip**: Text is truncated when it exceeds the maximum number of lines. - **TextOverflow.Ellipsis**: Overflowing text is replaced with an ellipsis (...). - This must be used with [maxLines](#maxLines) for the settings to take effect. - Line breaking behavior is controlled by [wordBreak](#wordBreak). By default, it uses **WordBreak.BREAK_WORD**, which breaks text by word (for example, English text is broken at word boundaries). To break text by character, set **wordBreak** to **WordBreak.BREAK_ALL**. - Line wrapping behavior is governed by [lineBreakStrategy](#lineBreakStrategy) which takes effect only when [wordBreak](#wordBreak) is not **WordBreak.BREAK_ALL**. Hyphens are not supported. - Since API version 11, it is recommended that you configure both [textOverflow](#textOverflow) and [wordBreak](#wordBreak) to control truncation behavior. For details, see [Example 4](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#example-4-setting-text-wrapping-and-line-breaking) &lt;!--RP1--&gt;&lt;!--RP1End--&gt;. When **TextOverflowOptions** is set to **TextOverflow.MARQUEE**: - Text scrolls horizontally within a single line. - [maxLines](#maxLines) and[copyOption](#copyOption) are ignored. - The clip attribute of the **Text** component defaults to **true**. - [CustomSpan](../arkts-apis/arkts-arkui-customspan-c.md#CustomSpan) is not supported in marquee mode. - Behavior of [textAlign](#textAlign): If the text does not scroll, **textAlign** applies; if the text scrolls, **textAlign** is ignored. - Since API version 12, **TextOverflow.MARQUEE** is available for the **ImageSpan** component, where the text and images are allowed to scroll within a single line.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextAttribute-textOverflow(options: TextOverflowOptions): TextAttribute--><!--Device-TextAttribute-textOverflow(options: TextOverflowOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextOverflowOptions](arkts-arkui-textoverflowoptions-i.md) | Yes |

## textSelectable

```TypeScript
textSelectable(mode: TextSelectableMode)
```

Sets whether the text is selectable and focusable. This attribute must be used in conjunction with [copyOption](#copyOption).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextAttribute-textSelectable(mode: TextSelectableMode): TextAttribute--><!--Device-TextAttribute-textSelectable(mode: TextSelectableMode): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [TextSelectableMode](../arkts-apis/arkts-arkui-textselectablemode-e.md) | Yes |

## textShadow

```TypeScript
textShadow(value: ShadowOptions | Array<ShadowOptions>)
```

Sets the text shadow. Intelligent color extraction is not supported for the **type**, **fill**, and **color** fields of the **ShadowOptions** object. Since API version 11, this API supports input parameters in an array to implement multiple text shadows.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TextAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions>): TextAttribute--><!--Device-TextAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](arkts-arkui-shadowoptions-i.md)&gt; | Yes |

## textVerticalAlign

```TypeScript
textVerticalAlign(textVerticalAlign: Optional<TextVerticalAlign>)
```

Sets the vertical alignment of the text. > **NOTE：**> > - When this API and [halfLeading](#halfLeading) are both set, **halfLeading** does not take > effect. > > - The effect of this attribute is noticeable only when the same font size is used in a paragraph and > [lineHeight](#lineHeight) is set, or when different font sizes are mixed in a paragraph. > Otherwise, the effect is the same regardless of whether this attribute is set or which enum value is used. The > **SuperscriptStyle** in TextStyle takes effect only when the value of > TextVerticalAlign is set to **TextVerticalAlign.BASELINE**. In other vertical > alignment modes, the superscript and subscript texts are displayed in the same way as the normal text.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextAttribute-textVerticalAlign(textVerticalAlign: Optional<TextVerticalAlign>): TextAttribute--><!--Device-TextAttribute-textVerticalAlign(textVerticalAlign: Optional<TextVerticalAlign>): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textVerticalAlign](#textVerticalAlign) | [Optional](arkts-arkui-optional-t.md)&lt;TextVerticalAlign&gt; | Yes |

## wordBreak

```TypeScript
wordBreak(value: WordBreak)
```

Sets the word break rule. By default, when **wordBreak** is not called or is set to **WordBreak.BREAK_WORD**, text is broken by word. (for example, English text is broken at word boundaries). To break text by character, with the excess part displayed as an ellipsis (...), use **WordBreak.BREAK_ALL** in combination with **{overflow: TextOverflow.Ellipsis}** and **maxLines**.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAttribute-wordBreak(value: WordBreak): TextAttribute--><!--Device-TextAttribute-wordBreak(value: WordBreak): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [WordBreak](#wordBreak) | Yes |
