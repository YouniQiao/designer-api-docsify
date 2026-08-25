# TextAttribute

TextAttribute.

**Inheritance/Implementation:** TextAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextAttribute](arkts-arkui-text-textattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## baselineOffset

```TypeScript
default baselineOffset(value: double | string | undefined): this
```

Called when the baseline offset is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## bindSelectionMenu

```TypeScript
default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined, responseType: TextResponseType | undefined, options?: SelectionMenuOptions | undefined): this
```

Bind to the selection menu.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The duration required for a long-press gesture is 600 ms for bindSelectionMenu and 800 ms for bindContextMenu. <br>When both bindSelectionMenu and bindContextMenu are set and both are configured to be triggered by a long-press gesture, bindSelectionMenu is triggered first. <br>If the custom menu is too long, embed a Scroll component to prevent the keyboard from being blocked. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spanType | [TextSpanType](arkts-arkui-text-textspantype-e.md) \| undefined | Yes |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | Yes |
| responseType | [TextResponseType](arkts-arkui-text-textresponsetype-e.md) \| undefined | Yes |
| options | [SelectionMenuOptions](arkts-arkui-richeditor-selectionmenuoptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## caretColor

```TypeScript
default caretColor(color: ResourceColor | undefined): this
```

Set the caret color for the selected text.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## contentTransition

```TypeScript
default contentTransition(transition: ContentTransition | undefined): this
```

Set text transition.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | [ContentTransition](arkts-arkui-textcommon-contenttransition-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

Allow replication.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this attribute is set to CopyOptions.InApp or CopyOptions.LocalDevice, a long press on the text will display a context menu that offers the copy and select-all options. <br>Because widgets do not have the long press event, the context menu will not be displayed when users long press text. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## dataDetectorConfig

```TypeScript
default dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

Data detector with config.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API must be used together with enableDataDetector. <br>It takes effect only when enableDataDetector is set to true. <br>When entities A and B overlap, the following rules are followed: &lt;ol&gt; &lt;li&gt;If A is a subset of B (A ⊂ B), then B is retained; otherwise, A is retained.&lt;/li&gt; &lt;li&gt;If A is not a subset of B (A ⊄ B) and B is not a subset of A (B ⊄ A), and if the starting point of A is earlier than that of B (A.start &lt; B.start), then A is retained; otherwise, B is retained.&lt;/li&gt; &lt;/ol&gt; </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [TextDataDetectorConfig](arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## decoration

```TypeScript
default decoration(value: DecorationStyleInterface | undefined): this
```

Called when the text decoration of the text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The style parameter cannot be used in widgets. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DecorationStyleInterface](arkts-arkui-styledstring-decorationstyleinterface-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

Enable the selectable area can be dragged.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute cannot be used together with the onDragStart event. <br>It must be used together with CopyOptions. <br>When it is set to true and copyOptions is set to CopyOptions.InApp or CopyOptions.LocalDevice, the selected text can be dragged and copied to the text box. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## ellipsisMode

```TypeScript
default ellipsisMode(value: EllipsisMode | undefined): this
```

Set the ellipsis mode.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the settings to work, overflow must be set to TextOverflow.Ellipsis and maxLines must be specified. <br>Setting ellipsisMode alone does not take effect. <br>EllipsisMode.START and EllipsisMode.CENTER take effect only when text overflows in a single line. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [EllipsisMode](arkts-arkui-ellipsismode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## enableDataDetector

```TypeScript
default enableDataDetector(enable: boolean | undefined): this
```

Enable data detector.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API only works on devices that provide text recognition. <br>When enableDataDetector is set to true, and the dataDetectorConfig attribute is not set, all types of entities are recognized by default, and the color and decoration of the recognized entities will be changed to the following styles: &lt;code&gt; color: '#ff007dff', decoration:{type: TextDecorationType.Underline, color: '#ff007dff', style: TextDecorationStyle.SOLID} &lt;/code&gt; <br>Touching and right-clicking an entity with the mouse will pop up the corresponding entity operation menu based on the type of entity, while left-clicking an entity with the mouse will directly respond to the first option of the menu. <br>This API does not work when overflow is set to TextOverflow.MARQUEE. <br>When copyOption is set to CopyOptions.None, the menu displayed after an entity is clicked does not provide the text selection, copy, translation, or sharing functionality. <br>When copyOption is not set to CopyOptions.None, and textSelectable is set to TextSelectableMode.UNSELECTABLE, the entity still has the copy functionality but does not have the text selection feature. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## font

```TypeScript
default font(fontValue: Font | undefined, options?: FontSettingOptions | undefined): this
```

Called when the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is only effective for the Text component, not for its child components. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontValue | [Font](arkts-arkui-font-i.md) \| undefined | Yes |
| options | [FontSettingOptions](arkts-arkui-textcommon-fontsettingoptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

Called when the font list of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Default font: 'HarmonyOS Sans'<br>The 'HarmonyOS Sans' font and registered custom fonts are supported for applications. <br>Only the 'HarmonyOS Sans' font is supported for widgets. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](arkts-arkui-resource-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: double | string | Resource | undefined): this
```

Called when the font size is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If fontSize is of the number type, the unit fp is used. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontVariations

```TypeScript
default fontVariations(fontVariations: Array<FontVariation> | undefined): this
```

Set the font variation.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fontVariations](#fontvariations) | Array&lt;[FontVariation](arkts-arkui-fontvariation-t.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(weight: int | FontWeight | ResourceStr | undefined, options?: FontSettingOptions | undefined): this
```

Called when the font weight is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| weight | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |
| options | [FontSettingOptions](arkts-arkui-textcommon-fontsettingoptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## halfLeading

```TypeScript
default halfLeading(halfLeading: boolean | undefined): this
```

Set the text with half leading.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The halfLeading settings configured within the component take precedence over those in module.json5. <br>The value true means that half leading is enabled, and false means the opposite. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## heightAdaptivePolicy

```TypeScript
default heightAdaptivePolicy(value: TextHeightAdaptivePolicy | undefined): this
```

Called when the height adaptive policy is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;ul&gt; &lt;li&gt;When this attribute is set to TextHeightAdaptivePolicy.MAX_LINES_FIRST, the maxLines attribute takes precedence for adjusting the text height. <br>If the maxLines setting results in a layout beyond the layout constraints, the text will shrink to a font size between minFontSize and maxFontSize to allow for more content to be shown.&lt;/li&gt; &lt;li&gt;If this attribute is set to TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST, the minFontSize attribute takes precedence for adjusting the text height. <br>If the text fits on one line at minFontSize,the system attempts to increase the font size within the range of minFontSize and maxFontSize to display the text as large as possible on one line. <br>If the text cannot fit into a single line even at minFontSize, it sticks with minFontSize.&lt;/li&gt; &lt;li&gt;If this attribute is set to TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST, the layout constraints take precedence for adjusting the text height. <br>If the resultant layout is beyond the layout constraints, the text will shrink to a font size between minFontSize and maxFontSize to respect the layout constraints. <br>If the text still extends beyond the layout constraints after shrinking to minFontSize, the lines that exceed the constraints are deleted.&lt;/li&gt; &lt;/ul&gt; </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## incrementalUpdatePolicy

```TypeScript
default incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): this
```

Sets the incremental update policy for text rendering.This API takes effect only when Text content contains a StyledString. Default value is IncrementalUpdatePolicy.NONE.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [IncrementalUpdatePolicy](arkts-arkui-textcommon-incrementalupdatepolicy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## letterSpacing

```TypeScript
default letterSpacing(value: double | string | undefined): this
```

Called when the distance between text fonts is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineBreakStrategy

```TypeScript
default lineBreakStrategy(strategy: LineBreakStrategy | undefined): this
```

Set the text line break strategy type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute takes effect when wordBreak is not set to breakAll. <br>Hyphens are not supported. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

Called when the vertical center mode of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than or equal to 0, the line height is not limited and the font size is adaptive. <br>If the value is of the number type, the unit fp is used. <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineHeightMultiple

```TypeScript
default lineHeightMultiple(value: double | undefined): this
```

Set the line height multiple value of text.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is set to undefined, this property is set to 0 and has no effect. </p>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineSpacing

```TypeScript
default lineSpacing(value: LengthMetrics | undefined, options?: LineSpacingOptions): this
```

Set font line spacing with options.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value specified is less than or equal to 0, the default value 0 is used. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes |
| options | [LineSpacingOptions](arkts-arkui-textcommon-linespacingoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## marqueeOptions

```TypeScript
default marqueeOptions(options: TextMarqueeOptions | undefined): this
```

Set the marquee options.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextMarqueeOptions](arkts-arkui-text-textmarqueeoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

Called when the maximum font scale of the font is set. Value range: [1, +∞)<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>A value less than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with minFontSize and maxLines, or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. <br>If the value of maxFontSize is less than or equal to 0, font size adaptation does not take effect. <br>In this case, the actual font size is determined by the value of fontSize. <br>If fontSize is not specified, the default value is used. <br>Since API version 18, this attribute takes effect on child components and styled strings, and the adaptive font size is applied to parts where the font size is not set. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxLineHeight

```TypeScript
default maxLineHeight(value: LengthMetrics | undefined): this
```

Set the maximum line height<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is set to undefined, this property does not limit the text line height. </p>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxLines

```TypeScript
default maxLines(value: int | undefined): this
```

Called when the maximum number of lines of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>By default, text is automatically folded. <br>If this attribute is specified, the text will not exceed the specified number of lines. <br>If there is extra text, you can use textOverflow to specify how it is displayed. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

Called when the minimum font scale of the font is set. Value range: [0, 1]<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>A value less than 0 is handled as 0. <br>A value greater than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with maxFontSize and maxLines, or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. <br>If the value of minFontSize is less than or equal to 0, font size adaptation does not take effect. <br>In this case, the actual font size is determined by the value of fontSize. <br>If fontSize is not specified, the default value is used. <br>Since API version 18, this attribute takes effect on child components and styled strings, and the adaptive font size is applied to parts where the font size is not set. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minLineHeight

```TypeScript
default minLineHeight(value: LengthMetrics | undefined): this
```

Set the minimum line height<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is set to undefined, this property does not limit the text line height. </p>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minLines

```TypeScript
default minLines(minLines: int | undefined): this
```

Called when the minimum number of lines of text is set.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [minLines](#minlines) | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: ((value: string) => void) | undefined): this
```

Called when using the Clipboard menu Currently, only text can be copied.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | ((value: string) = & gt; void) \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onMarqueeStateChange

```TypeScript
default onMarqueeStateChange(callback: Callback<MarqueeState> | undefined): this
```

Called when the text marquee state changes.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[MarqueeState](arkts-arkui-text-marqueestate-e.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: ((selectionStart: int, selectionEnd: int) => void) | undefined): this
```

Called when the text selection changes.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | ((selectionStart: int, selectionEnd: int) = & gt; void) \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

Called before using the Clipboard copy menu. Currently, only text can be copied.

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## optimizeTrailingSpace

```TypeScript
default optimizeTrailingSpace(optimize: boolean | undefined): this
```

Set whether to optimize the trailing spaces at the end of each line during text layout.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optimize | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## privacySensitive

```TypeScript
default privacySensitive(supported: boolean | undefined): this
```

Whether to support sensitive privacy information<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The value true means to enable privacy mode, in which case text is obscured as hyphens (-). <br>If this parameter is set to null, privacy mode is disabled. <br>Enabling privacy mode requires widget framework support. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| supported | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(color: ResourceColor | undefined): this
```

Set the selected background color of the text.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## selection

```TypeScript
default selection(selectionStart: int | undefined, selectionEnd: int | undefined): this
```

Text selection is achieved by specifying the start and end positions of the text.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The selected text is highlighted, and a selection handle is displayed together with a menu of available actions. <br>When copyOption is set to CopyOptions.None, the selection attribute is not effective. <br>When overflow is set to TextOverflow.MARQUEE, the selection attribute is not effective. <br>If the value of selectionStart is greater than or equal to that of selectionEnd, no text will be selected. <br>The value range is [0, textSize], where textSize indicates the maximum number of characters in the text content. <br>If the value is less than 0, the value 0 will be used. <br>If the value is greater than textSize, textSize will be used. <br>If the value of selectionStart or selectionEnd falls within the invisible area, no text will be selected. <br>If clipping is disabled, the text selection outside of the parent component takes effect. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | int \| undefined | Yes |
| selectionEnd | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## setTextOptions

```TypeScript
default setTextOptions(content?: string | Resource, value?: TextOptions): this
```

Set Text options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | string \| [Resource](arkts-arkui-resource-t.md) | No |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

Set the shader style of the text, such as lineargradient or radialgradient.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shader | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## tailIndents

```TypeScript
default tailIndents(value: LengthMetrics | Array<LengthMetrics> | undefined): this
```

Specify the tail indentation for each line in a text block.<p>&lt;strong&gt;Description&lt;/strong&gt;: <br>When a single LengthMetrics value is provided, all rows share the same tail indentation. <br>When an array is provided, the i-th element specifies the trailing indentation of the i-th line. If the number of lines of text exceeds the length of the array, the last element in the array is used. for the remaining lines. <br>A negative value is treated as 0. <br>If this parameter is set to undefined, the default value 0 is used. </p>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| Array&lt;[LengthMetrics](arkts-arkui-lengthmetrics-t.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

Called when the horizontal center mode of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The text takes up the full width of the Text component. <br>To set vertical alignment for the text, use the align attribute. <br>The align attribute alone does not control the horizontal position of the text. <br>In other words, Alignment.TopStart, Alignment.Top, and Alignment.TopEnd produce the same effect, top-aligning the text; Alignment.Start, Alignment.Center, and Alignment.End produce the same effect, centered-aligning the text vertically; Alignment.BottomStart, Alignment.Bottom, and Alignment.BottomEnd produce the same effect, bottom-aligning the text. <br>When textAlign is set to TextAlign.JUSTIFY, you must set the wordBreak attribute, and the text in the last line is horizontally aligned with the start edge. </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textCase

```TypeScript
default textCase(value: TextCase | undefined): this
```

Called when the type of letter in the text font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextCase](arkts-arkui-textcase-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textContentAlign

```TypeScript
default textContentAlign(textContentAlign: TextContentAlign | undefined): this
```

Set the vertical align of the whole text content.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textContentAlign](#textcontentalign) | [TextContentAlign](arkts-arkui-textcommon-textcontentalign-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textIndent

```TypeScript
default textIndent(value: Length | undefined): this
```

Specify the indentation of the first line in a text-block.

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textOverflow

```TypeScript
default textOverflow(options: TextOverflowOptions | undefined): this
```

Called when the overflow mode of the font is set.Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Text is clipped at the transition between words. <br>To clip text in the middle of a word, add \u200B between characters. <br>Since API version 11, preferably set the wordBreak attribute to WordBreak.BREAK_ALL to achieve the same purpose. <br>If overflow is set to TextOverflow.None, TextOverflow.Clip, or TextOverflow.Ellipsis, this attribute must be used with maxLines for the settings to take effect. <br>TextOverflow.None produces the same effect as TextOverflow.Clip. <br>If overflow is set to TextOverflow.MARQUEE, the text scrolls in a line, and neither maxLines nor copyOption takes effect. <br>The textAlign attribute takes effect only when the text is not scrollable. <br>With overflow set to TextOverflow.MARQUEE, the clip attribute is set to true by default. <br>TextOverflow.MARQUEE is not available for CustomSpan of the styled string. <br>Since API version 12, TextOverflow.MARQUEE is available for the ImageSpan component, where the text and images are displayed in scrolling mode in a line. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextOverflowOptions](arkts-arkui-text-textoverflowoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textSelectable

```TypeScript
default textSelectable(mode: TextSelectableMode | undefined): this
```

set text selectable and focusable

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [TextSelectableMode](arkts-arkui-textselectablemode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textShadow

```TypeScript
default textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

Called when the text shadow is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API does not work with the fill attribute or coloring strategy. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textVerticalAlign

```TypeScript
default textVerticalAlign(textVerticalAlign: TextVerticalAlign | undefined): this
```

Set the vertical align of the text.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textVerticalAlign](#textverticalalign) | [TextVerticalAlign](arkts-arkui-textcommon-textverticalalign-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## wordBreak

```TypeScript
default wordBreak(value: WordBreak | undefined): this
```

Set the word break type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When used with {overflow: TextOverflow.Ellipsis} and maxLines, WordBreak.BREAK_ALL can insert line breaks between letters when overflow occurs and display excess content with an ellipsis (...). </p>

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |
