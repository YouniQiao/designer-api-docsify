# TextAreaAttribute

Defines the attribute functions of TextArea.

**继承/实现关系：** TextAreaAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextAreaAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## autoCapitalizationMode

```TypeScript
default autoCapitalizationMode(mode: AutoCapitalizationMode | undefined): this
```

Set text mode of automatic case mode switching.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AutoCapitalizationMode](arkts-arkui-textcommon-autocapitalizationmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## barState

```TypeScript
default barState(value: BarState | undefined): this
```

Define bar state of the text area.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BarState](arkts-arkui-barstate-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## caretColor

```TypeScript
default caretColor(value: ResourceColor | undefined): this
```

Called when the insertion cursor color is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Since API version 12, this API can be used to set the text handle color, which is the same as the caret color. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## caretStyle

```TypeScript
default caretStyle(value: CaretStyle | undefined): this
```

Define the caret style of the text input.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CaretStyle](arkts-arkui-textcommon-caretstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## compressLeadingPunctuation

```TypeScript
default compressLeadingPunctuation(enabled: boolean | undefined): this
```

是否压缩行首的标点符号。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## contentType

```TypeScript
default contentType(contentType: ContentType | undefined): this
```

Called when the auto fill type is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [contentType](#contenttype) | [ContentType](arkts-arkui-textinput-contenttype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

Called when the copy option is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this attribute is set to CopyOptions.None, the text can only be pasted; all other actions, such as copying, cutting, and sharing, are disabled. <br>Dragging is not allowed when CopyOptions.None is set. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CopyOptions](arkts-arkui-copyoptions-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(value: CustomBuilder | ComponentContentBase | undefined, options?: KeyboardOptions): this
```

定义多行文本输入框的自定义键盘。<p>&lt;strong&gt;注意&lt;/strong&gt;: <br>设置自定义键盘时，激活文本框将打开指定的自定义组件，而不是系统输入法。 <br>自定义键盘的高度可以通过自定义组件的根节点的height属性设置， 其宽度固定为默认值。 <br>自定义键盘通过覆盖原屏幕的方式呈现，如果未启用回避模式或文本框不需要回避，则不会压缩或提升该键盘。 <br>自定义键盘无法获取焦点，但会阻止手势事件。 <br>默认情况下，当输入组件失去焦点时，自定义键盘将关闭。 <br>您也可以使用TextAreaController.stopEditing API来关闭键盘。 <br>设置自定义键盘时，文本框不支持相机输入，即使设备支持。 <br>设置自定义键盘时，可以绑定onKeyPrelme事件，防止物理键盘输入。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) \| undefined | 是 |
| options | [KeyboardOptions](arkts-arkui-richeditor-keyboardoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## decoration

```TypeScript
default decoration(value: TextDecorationOptions | undefined): this
```

Called when the text decoration of the text is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextDecorationOptions](../arkts-components/arkts-arkui-textdecorationoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

Set the custom text menu. Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editMenu | [EditMenuOptions](arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## ellipsisMode

```TypeScript
default ellipsisMode(mode: EllipsisMode | undefined): this
```

Set the ellipsis mode.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the settings to work, overflow must be set to TextOverflow.Ellipsis and maxLines must be specified. <br>Setting ellipsisMode alone does not take effect. <br>EllipsisMode.START and EllipsisMode.CENTER take effect only when maxLines is set to 1. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [EllipsisMode](arkts-arkui-ellipsismode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enableAutoFill

```TypeScript
default enableAutoFill(value: boolean | undefined): this
```

Sets whether enable auto fill or not.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enableAutoSpacing

```TypeScript
default enableAutoSpacing(enabled: boolean | undefined): this
```

是否启用中文和拉丁字符之间的自动间隔。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

Enable or disable haptic feedback.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>To enable haptic feedback, <br>you must declare the ohos.permission.VIBRATE permission under requestPermissions in the module.json5 file of the project. &lt;code&gt;"requestPermissions": [{"name": "ohos.permission.VIBRATE",}] &lt;/code&gt; </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(value: boolean | undefined): this
```

Sets whether request keyboard or not when on focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enablePreviewText

```TypeScript
default enablePreviewText(enable: boolean | undefined): this
```

Define the preview text mode of the text input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Preview text is in a temporary state and does not support text interception. <br>As such, it does not trigger onWillInsert, onDidInsert, onWillDelete, or onDidDelete callbacks. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enableSelectedDataDetector

```TypeScript
default enableSelectedDataDetector(enable: boolean | undefined): this
```

启用选中数据AI识别。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## enterKeyType

```TypeScript
default enterKeyType(value: EnterKeyType | undefined): this
```

Called when the type of soft keyboard input button is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fallbackLineSpacing

```TypeScript
default fallbackLineSpacing(enabled: boolean | undefined): this
```

是否包含回退字体的上升/下降，以防止重叠行。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Called when the font color is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: ResourceStr | undefined): this
```

Called when the font list of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The 'HarmonyOS Sans' font and registered custom fonts are supported for applications. <br>Only the 'HarmonyOS Sans' font is supported for widgets. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

Set font feature.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 | The fontFeature. normal \|  & lt;feature-tag-value & gt;, where & lt;feature-tag-value & gt; = & lt;string & gt; [ & lt;integer & gt; \ | on \|

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

Called when the font size is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

Called when the font style of a font is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

设置字体粗细时调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## halfLeading

```TypeScript
default halfLeading(halfLeading: boolean | undefined): this
```

设置文本是否使用半行距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [halfLeading](#halfleading) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## heightAdaptivePolicy

```TypeScript
default heightAdaptivePolicy(value: TextHeightAdaptivePolicy | undefined): this
```

Called when the height adaptive policy is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;ul&gt; &lt;li&gt;When this attribute is set to TextHeightAdaptivePolicy.MAX_LINES_FIRST, the maxLines attribute takes precedence for adjusting the text height. <br>If the maxLines setting results in a layout beyond the layout constraints, the text will shrink to a font size between minFontSize and maxFontSize to allow for more content to be shown. <br>If the text box is in inline input style, the font size in the editing state is different from that in the non-editing state.&lt;/li&gt; &lt;li&gt;If this attribute is set to TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST, the minFontSize attribute takes precedence for adjusting the text height. <br>If the text can fit in one line with the minFontSize setting, the text will enlarge to the largest possible font size between minFontSize and maxFontSize.&lt;/li&gt; &lt;li&gt;If this attribute is set to TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST, the layout constraints take precedence for adjusting the text height. <br>If the resultant layout is beyond the layout constraints, the text will shrink to a font size between minFontSize and maxFontSize to respect the layout constraints.&lt;/li&gt; &lt;/ul&gt; </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## horizontalScrolling

```TypeScript
default horizontalScrolling(enabled: boolean | undefined): this
```

当文本宽度大于视图时，是否启用水平滚动。 默认值为false，文本达到控件宽度自动换行。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## includeFontPadding

```TypeScript
default includeFontPadding(include: boolean | undefined): this
```

确定布局是否在顶部和底部添加额外的填充，以便为字符腾出空间。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| include | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## inputFilter

```TypeScript
default inputFilter(value: ResourceStr | undefined, error?: ((value: string) => void) | undefined): this
```

Called when the inputFilter of text is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Only inputs that comply with the regular expression can be displayed. <br>Other inputs are filtered out. <br>The specified regular expression can match single characters, but not strings. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| error | ((value: string) = & gt; void) \ | undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## keyboardAppearance

```TypeScript
default keyboardAppearance(appearance: KeyboardAppearance | undefined): this
```

设置键盘外观样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appearance | [KeyboardAppearance](arkts-arkui-textcommon-keyboardappearance-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## letterSpacing

```TypeScript
default letterSpacing(value: double | string | Resource | undefined): this
```

Called when the distance between text fonts is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value specified is a percentage or 0, the default value is used. <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>If the value specified is a negative value, the text is compressed. <br>A negative value too small may result in the text being compressed to 0 and no content being displayed. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## lineBreakStrategy

```TypeScript
default lineBreakStrategy(strategy: LineBreakStrategy | undefined): this
```

Set the text line break strategy type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute takes effect when wordBreak is not set to breakAll. Hyphens are not supported. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [LineBreakStrategy](arkts-arkui-linebreakstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

Called when the line height of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than or equal to 0, the line height is not limited and the font size is adaptive. <br>If the value is of the number type, the unit fp is used. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## lineSpacing

```TypeScript
default lineSpacing(value: LengthMetrics | undefined, options?: LineSpacingOptions): this
```

设置字体行间距。<p>&lt;strong&gt;注意&lt;/strong&gt;： <br>如果指定的值小于或等于0，则使用默认值0。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | 是 |
| options | [LineSpacingOptions](arkts-arkui-textcommon-linespacingoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

Called when the maximum font scale of the font is set. Value range: [1, +∞)<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>A value less than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

Called when the maximum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with minFontSize and maxLines, or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## maxLength

```TypeScript
default maxLength(value: int | undefined): this
```

Define the max length content of the text area.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>By default, there is no maximum number of characters. <br>When the maximum number of characters is reached, no more characters can be entered, and the border turns red. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## maxLines

```TypeScript
default maxLines(value: int | undefined, options?: MaxLinesOptions): this
```

定义文本区域的最大行数。 取值范围：(0, +∞)<p>&lt;strong&gt;注意&lt;/strong&gt;： <br>设置可以显示的最大行数。 <br>设置textOverflow时，如果内容超过此限制，文本将被截断。 <br>当textOverflow未设置时，在内联样式中 当文本框处于焦点状态时，如果内容超出限制，则文本是可滚动的； 当文本框没有焦点时，maxLines不适用。 <br>在非内联样式中，文本会根据行数进行截断。 <br>默认值：内联样式为3，非内联样式为+∞， 表示没有最大行数。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |
| options | [MaxLinesOptions](arkts-arkui-textcommon-maxlinesoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

Called when the minimum font scale of the font is set. Value range: [0, 1]<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The undefined type is supported. <br>A value less than 0 is handled as 0. <br>A value greater than 1 is handled as 1. <br>Abnormal values are ineffective by default. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

Called when the minimum font size of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>For the string type, numeric string values with optional units, for example, "10" or "10fp", are supported. <br>For the setting to take effect, this attribute must be used together with maxFontSize and maxLines, or layout constraint settings. <br>When the adaptive font size is used, the fontSize settings do not take effect. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## minLines

```TypeScript
default minLines(lines: int | undefined): this
```

定义多行输入框的最小行数。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lines](../../apis-notification-kit/arkts-apis/arkts-notification-notificationcontent-notificationmultilinecontent-i.md) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: EditableTextOnChangeCallback | undefined): this
```

Called when the input changes.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In this callback, if cursor operations are performed, you need to adjust the cursor logic based on the previewText parameter to make sure it works seamlessly under the preview display scenario. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [EditableTextOnChangeCallback](arkts-arkui-editabletextonchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onContentScroll

```TypeScript
default onContentScroll(callback: ((totalOffsetX: double, totalOffsetY: double) => void) | undefined): this
```

Called when the content scrolls.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((totalOffsetX: double, totalOffsetY: double) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: ((value: string) => void) | undefined): this
```

Called when using the Clipboard menu

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((value: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onCut

```TypeScript
default onCut(callback: ((value: string) => void) | undefined): this
```

Called when using the Clipboard menu

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((value: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onDidDelete

```TypeScript
default onDidDelete(callback: Callback<DeleteValue> | undefined): this
```

Get text value information when the deletion has been completed<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is available only for system input methods. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DeleteValue](arkts-arkui-textcommon-deletevalue-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onDidInsert

```TypeScript
default onDidInsert(callback: Callback<InsertValue> | undefined): this
```

Get text value information when completed input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is available only for system input methods. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[InsertValue](arkts-arkui-textcommon-insertvalue-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onEditChange

```TypeScript
default onEditChange(callback: ((isEditing: boolean) => void) | undefined): this
```

Called when judging whether the text editing change finished. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((isEditing: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onPaste

```TypeScript
default onPaste(callback: ((value: string, event: PasteEvent) => void) | undefined): this
```

Called when using the Clipboard menu

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((value: string, event: PasteEvent) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: TextAreaSubmitCallback | undefined): this
```

Called when submitted.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TextAreaSubmitCallback](arkts-arkui-textareasubmitcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: ((selectionStart: int, selectionEnd: int) => void) | undefined): this
```

Called when the text selection changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((selectionStart: int, selectionEnd: int) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

该方法在输入框组件绑定输入法前被调用。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[IMEClient](arkts-arkui-textcommon-imeclient-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillChange

```TypeScript
default onWillChange(callback: Callback<EditableTextChangeValue, boolean> | undefined): this
```

Get text value information when about to change.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This callback is triggered after onWillInsert and onWillDelete, but before onDidInsert and onDidDelete. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[EditableTextChangeValue](arkts-arkui-textcommon-editabletextchangevalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

在使用剪贴板复制菜单之前调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string, boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillCut

```TypeScript
default onWillCut(callback: Callback<string, boolean> | undefined): this
```

在使用剪贴板剪切菜单之前调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string, boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillDelete

```TypeScript
default onWillDelete(callback: Callback<DeleteValue, boolean> | undefined): this
```

Get text value information when about to delete.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It returns true if the text is deleted; returns false otherwise. <br>This callback is not called for text preview. <br>It is available only for system input methods. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DeleteValue](arkts-arkui-textcommon-deletevalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## onWillInsert

```TypeScript
default onWillInsert(callback: Callback<InsertValue, boolean> | undefined): this
```

Get text value information when about to input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It returns true if the text is inserted; returns false otherwise. <br>This callback is not triggered for pre-edit or candidate word operations. <br>It is available only for system input methods. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[InsertValue](arkts-arkui-textcommon-insertvalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## orphanCharOptimization

```TypeScript
default orphanCharOptimization(enabled: boolean | undefined): this
```

是否避免在段落的最后一行出现孤词。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## placeholderColor

```TypeScript
default placeholderColor(value: ResourceColor | undefined): this
```

Called when the color of the placeholder is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## placeholderFont

```TypeScript
default placeholderFont(value: Font | undefined): this
```

Called when the font property of the placeholder is set. The 'HarmonyOS Sans' font and registered custom fonts are supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## punctuationOverflow

```TypeScript
default punctuationOverflow(enabled: boolean | undefined): this
```

是否启用行尾标点溢出。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## scrollBarColor

```TypeScript
default scrollBarColor(thumbColor: ColorMetrics | undefined): this
```

滚动条的颜色。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| thumbColor | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(value: ResourceColor | undefined): this
```

Define the text selected background color of the text input. If the opacity is not set, a 20% opacity will be used.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

用于设置拖拽后的背板样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SelectedDragPreviewStyle](arkts-arkui-textcommon-selecteddragpreviewstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## selectionMenuHidden

```TypeScript
default selectionMenuHidden(value: boolean | undefined): this
```

Controls whether the selection menu pops up.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>&lt;em&gt;true&lt;/em&gt;: <br>The system text selection menu does not appear under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. <br>&lt;em&gt;false&lt;/em&gt;: <br>The system text selection menu appears under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## setTextAreaOptions

```TypeScript
default setTextAreaOptions(value?: TextAreaOptions): this
```

设置TextArea组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextAreaOptions](arkts-arkui-textarea-textareaoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

设置文本的着色器样式，如线性渐变或径向渐变。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shader | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## showCounter

```TypeScript
default showCounter(value: boolean | undefined, options?: InputCounterOptions): this
```

Define show counter of the text area.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>options can be set only when value is set to true, in which case a character counter is displayed below the text box. <br>This attribute must be used together with maxlength. <br>The character counter is displayed in this format: Number of characters entered/Character limit. <br>It is visible when the number of characters entered is greater than the character limit multiplied by the threshold percentage value. <br>If options is not set, the text box border and character counter subscript turn red when the number of characters entered reaches the limit. <br>If value is set to true and options is set, the text box border and character counter subscript turn red and the text box shakes when the number of characters entered reaches the limit, provided that the value of thresholdPercentage is valid. <br>If highlightBorder is set to false, the text box border does not turn red. <br>By default, highlightBorder is set to true. <br>The character counter is not displayed for text boxes in inline input style. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| options | [InputCounterOptions](../arkts-components/arkts-arkui-inputcounteroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## stopBackPress

```TypeScript
default stopBackPress(isStopped: boolean | undefined): this
```

设置是否阻止返回按键的回调事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isStopped | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## strokeColor

```TypeScript
default strokeColor(color: ResourceColor | undefined): this
```

设置描边颜色。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## strokeJoinStyle

```TypeScript
default strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): this
```

设置描边的连接样式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [strokeJoinStyle](#strokejoinstyle) | [StrokeJoinStyle](arkts-arkui-textcommon-strokejoinstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(width: LengthMetrics | undefined): this
```

设置描边宽度。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## style

```TypeScript
default style(value: TextContentStyle | undefined): this
```

Define style of the text area.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The inline input style is only available for the TextAreaType.Normal type. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextContentStyle](arkts-arkui-textcontentstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

Called when the alignment of the contents of a multiline text box is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>To set vertical alignment for the text, use the align attribute. <br>The align attribute alone does not control the horizontal position of the text. <br>In other words, Alignment.TopStart, Alignment.Top, and Alignment.TopEnd produce the same effect, top-aligning the text; Alignment.Start, Alignment.Center, and Alignment.End produce the same effect, centered-aligning the text vertically; Alignment.BottomStart, Alignment.Bottom, and Alignment.BottomEnd produce the same effect, bottom-aligning the text. <br>When textAlign is set to TextAlign.JUSTIFY, the text in the last line is horizontally aligned with the start edge. <br>Since API version 11, textAlign can be set to TextAlign.JUSTIFY. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextAlign](arkts-arkui-textalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## textDirection

```TypeScript
default textDirection(direction: TextDirection | undefined): this
```

设置文本方向。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | [TextDirection](arkts-arkui-textcommon-textdirection-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## textIndent

```TypeScript
default textIndent(value: Dimension | undefined): this
```

Specify the indentation of the first line in a text-block.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## textOverflow

```TypeScript
default textOverflow(value: TextOverflow | undefined): this
```

Called when the overflow mode of the font is set.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In inline style, the effect of truncating text according to maxLines only applies when textOverflow is set. <br>Text is clipped at the transition between words. <br>To clip text in the middle of a word, set wordBreak to WordBreak.BREAK_ALL. <br>If overflow is set to TextOverflow.None, TextOverflow.Clip, or TextOverflow.Ellipsis, this attribute must be used with maxLines for the settings to take effect. <br>TextOverflow.None produces the same effect as TextOverflow.Clip. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextOverflow](arkts-arkui-textoverflow-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## type

```TypeScript
default type(value: TextAreaType | undefined): this
```

Called when the input type is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextAreaType](arkts-arkui-textarea-textareatype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |

## wordBreak

```TypeScript
default wordBreak(value: WordBreak | undefined): this
```

Set the word break type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect for the placeholder text. <br>The component does not support the clip attribute. <br>Therefore, setting this attribute does not affect text clipping. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [WordBreak](arkts-arkui-wordbreak-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAreaAttribute](arkts-arkui-textarea-textareaattribute-i.md) |
