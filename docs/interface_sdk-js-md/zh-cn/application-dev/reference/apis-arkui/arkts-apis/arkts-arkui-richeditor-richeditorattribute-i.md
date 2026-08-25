# RichEditorAttribute

除支持通用属性外，还支持以下属性：

> **说明：**&gt;
> - align属性只支持上方、中间和下方位置的对齐方式。&gt;
> - 不支持borderImage属性。&gt;
> - 组件水平方向默认padding为16vp，竖直方向默认padding为8vp。

**继承/实现关系：** RichEditorAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## aboutToDelete

```TypeScript
default aboutToDelete(callback: Callback<RichEditorDeleteValue, boolean> | undefined): this
```

输入法删除内容前，触发回调。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorDeleteValue](arkts-arkui-richeditor-richeditordeletevalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## aboutToIMEInput

```TypeScript
default aboutToIMEInput(callback: Callback<RichEditorInsertValue, boolean> | undefined): this
```

输入法输入内容前触发回调。可用于需要拦截输入内容的场景，如过滤敏感词、限制输入格式、实时校验输入合法性等。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorInsertValue](arkts-arkui-richeditor-richeditorinsertvalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RichEditorAttribute> | AttributeModifier<CommonMethod> |
        undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## barState

```TypeScript
default barState(state: BarState | undefined): this
```

RichEditor滚动条的显示模式。

> **说明：**&gt;
> 从API version 18开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [BarState](arkts-arkui-barstate-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## bindSelectionMenu

```TypeScript
default bindSelectionMenu(spanType: RichEditorSpanType | undefined, content: CustomBuilder | undefined,
        responseType: ResponseType | RichEditorResponseType | undefined,
        options?: SelectionMenuOptions | undefined): this
```

设置自定义选择菜单。支持自定义菜单风格和触发条件，适合需要深度自定义菜单的场景。自定义菜单超长时，建议内部嵌套 Scroll组件使用，避免键盘被遮挡。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanType | [RichEditorSpanType](arkts-arkui-richeditor-richeditorspantype-e.md) \| undefined | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| responseType | [ResponseType](arkts-arkui-responsetype-e.md) \| [RichEditorResponseType](arkts-arkui-richeditor-richeditorresponsetype-e.md) \| undefined | 是 |
| options | [SelectionMenuOptions](arkts-arkui-richeditor-selectionmenuoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## caretColor

```TypeScript
default caretColor(value: ResourceColor | undefined): this
```

设置输入框光标、手柄颜色。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## compressLeadingPunctuation

```TypeScript
default compressLeadingPunctuation(enabled: boolean | undefined): this
```

设置是否开启行首标点符号压缩。适用于行首标点符号需要与正文内容对齐的场景。

> **说明：**&gt;
> 行首标点符号默认不压缩。&gt;
> 支持压缩的标点符号，请参考[ParagraphStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraphstyle-i.md)的行首压缩的标点范围。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## copyOptions

```TypeScript
default copyOptions(value: CopyOptions | undefined): this
```

设置组件是否支持复制和粘贴文本内容。从API version 20开始，RichEditor组件在执行复制或剪切操作时，会将HTML格式的内容添加到剪贴板中。  
- 仅支持TextSpan和ImageSpan向剪贴板中添加HTML内容，其他Span类型（如BuilderSpan、SymbolSpan、CustomSpan）则不能添加。 - 设置RichEditor组件的属性字符串时，请参考属性字符串[toHtml](arkts-arkui-styledstring-c.md#tohtml) 接口文档，以了解支持转换为HTML的范围。  
copyOptions不为CopyOptions.None时，长按组件内容，会弹出文本选择菜单。如果通过bindSelectionMenu等方式自定义文本选择菜单，则会弹出自定义的菜单。设置copyOptions为CopyOptions.None时，禁用复制、剪切、翻译、分享、搜索、帮写功能，且不支持拖拽操作。 同时 [enableDataDetector](#enabledatadetector)的实体识别菜单和 [enableSelectedDataDetector](#enableselecteddatadetector)的AI菜单功能将受限。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(value: CustomBuilder | ComponentContentBase | undefined,
                           options?: KeyboardOptions | undefined): this
```

设置自定义键盘。当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认键盘宽度。自定义键盘无法获取焦点，但是会拦截手势事件。默认在输入控件失去焦点时，关闭自定义键盘。自定义键盘支持接续功能，使用 [setCustomKeyboardContinueFeature](arkts-arkui-arkui-uicontext-uicontext-c.md#setcustomkeyboardcontinuefeature) 接口，可以设置自定义键盘之间切换时是否接续。

> **说明：**&gt;
> 从API version 23开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) \| undefined | 是 |
| options | [KeyboardOptions](arkts-arkui-richeditor-keyboardoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## dataDetectorConfig

```TypeScript
default dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

设置文本特殊实体识别配置，可配置识别类型、实体显示样式，并可选择是否开启长按预览功能。需配合[enableDataDetector](#enabledatadetector)一起使用，设置enableDataDetector为true时， dataDetectorConfig的配置才能生效。当有两个实体A、B重叠时，按以下规则保留实体：
1.&nbsp;若A&nbsp;⊂&nbsp;B，则保留B，反之则保留A。
2.&nbsp;当A&nbsp;⊄&nbsp;B且B&nbsp;⊄&nbsp;A时，若A.start&nbsp;&lt;&nbsp;B.start，则保留A，反之则保留B。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [TextDataDetectorConfig](arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

设置系统默认菜单的扩展项，允许配置扩展项的文本内容、图标和回调方法。与[bindSelectionMenu](#bindselectionmenu)的区别：editMenuOptions在系统默认菜单风格基础上添加扩展项，触发条件不变， 适合仅需扩展菜单项的场景；bindSelectionMenu完全自定义菜单风格和触发条件，适合需要深度自定义菜单的场景。调用[disableMenuItems](arkts-arkui-arkui-uicontext-textmenucontroller-c.md#disablemenuitems)或 [disableSystemServiceMenuItems](arkts-arkui-arkui-uicontext-textmenucontroller-c.md#disablesystemservicemenuitems)接口屏蔽文本 选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法onCreateMenu的入参列表中不包含被屏蔽的菜单选项。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enableAutoSpacing

```TypeScript
default enableAutoSpacing(enable: boolean | undefined): this
```

设置是否开启中文与西文的自动间距。适用于混排中英文内容（如新闻文章、技术文档）等需要改善中西文之间阅读体验的场景。开启后，中文字符与西文字符之间将自动插入间距；关闭后不自动插入间距。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enableDataDetector

```TypeScript
default enableDataDetector(enable: boolean | undefined): this
```

设置是否进行文本特殊实体识别，识别的类型包括电话号码、邮箱地址、网址链接、日期、地址等。具体识别类型可通过 [dataDetectorConfig](#datadetectorconfig)属性配置。该接口依赖设备系统具备文本实体识别能力，否则设置不会生效。当enableDataDetector设置为true且未指定[dataDetectorConfig](#datadetectorconfig)属性时，系统将默认识别所有类型的实 体，并将这些实体的color和decoration更改为预设样式：触摸点击或鼠标右键点击实体时，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。对addBuilderSpan的节点文本，该功能不会生效。当copyOptions设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本和复制功能。<!--RP1--><!--RP1End-->

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

设置RichEditor是否支持触感反馈。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(isEnabled: boolean | undefined): this
```

设置RichEditor通过点击以外的方式获焦时，是否主动拉起软键盘。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enablePreviewText

```TypeScript
default enablePreviewText(enable: boolean | undefined): this
```

设置是否开启预上屏功能。开启后，组件内显示输入法输入过程中的拼音、笔画字符。

> **说明：**&gt;
> 从API version 18开始，该接口支持在
> attributeModifier
> 中调用。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enableSelectedDataDetector

```TypeScript
default enableSelectedDataDetector(enable: boolean | undefined): this
```

设置是否启用文本选择的AI菜单功能。启用后可识别选区中的邮件、电话、网址、日期、地址等，并在文本选择菜单中展示对应的AI菜单项。默认启用AI菜单功能。AI菜单功能启用时，在组件中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括 [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)中的url（打开链接）、email（新建邮件）、 phoneNumber（呼叫）、address（导航前往）、dateTime（新建日程）。AI菜单生效时，选中范围内需包括且仅包括一个完整的AI实体，才能展示对应的选项。该菜单项与 [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)中的askAI菜单项不同时出现。本功能仅在[copyOptions](#copyoptions)为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE时生效。该接口依赖设备底层具有文本识别能力，否则设置不会生效。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## enterKeyType

```TypeScript
default enterKeyType(value: EnterKeyType | undefined): this
```

设置软键盘输入法回车键类型。设置后，软键盘回车键的图标和触发行为将根据指定类型变化，不同EnterKeyType对应不同的回车键样式。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## fallbackLineSpacing

```TypeScript
default fallbackLineSpacing(enabled: boolean | undefined): this
```

在多行文字叠加场景下，设置行高是否基于文字实际高度自适应。适用于混排不同字号文字、聊天消息气泡等需要避免文字重叠的场景。不通过该接口设置，默认行高不基于文字实际高度自适应。该接口依赖[RichEditorTextStyle](arkts-arkui-richeditor-richeditortextstyleresult-i.md)的lineHeight属性。当lineHeight设置值小于当前字号下文本渲染出的实际高度时， fallbackLineSpacing属性将生效。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## horizontalScrolling

```TypeScript
default horizontalScrolling(enabled: boolean | undefined): this
```

设置当文本宽度超过内容区宽度时是否启用水平滚动。适用于需要显示长文本内容（如代码片段、长URL等）而不希望自动换行的场景。不通过该接口设置，默认禁用水平滚动。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## includeFontPadding

```TypeScript
default includeFontPadding(include: boolean | undefined): this
```

设置是否在首行和尾行增加间距以避免文字截断。适用于自定义字体行高较小导致文字被裁剪、紧凑排版等场景。不通过该接口设置，默认不增加间距。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## keyboardAppearance

```TypeScript
default keyboardAppearance(appearance: KeyboardAppearance | undefined): this
```

设置键盘外观。适用于需要根据应用主题或沉浸式场景调整键盘视觉风格的场景，如深色模式下使用DARK外观。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## maxLength

```TypeScript
default maxLength(maxLength: int | undefined): this
```

设置组件内容的最大长度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [maxLength](#maxlength) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## maxLines

```TypeScript
default maxLines(maxLines: int | undefined): this
```

设置组件可显示的最大行数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [maxLines](#maxlines) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: Callback<CopyEvent> | undefined): this
```

复制时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的复制。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件，默认支持图文的复制。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[CopyEvent](arkts-arkui-richeditor-copyevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onCut

```TypeScript
default onCut(callback: Callback<CutEvent> | undefined): this
```

剪切时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的剪切。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件，默认支持图文的剪切。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[CutEvent](arkts-arkui-richeditor-cutevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onDeleteComplete

```TypeScript
default onDeleteComplete(callback: VoidCallback | undefined): this
```

输入法删除内容后，触发回调。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onDidChange

```TypeScript
default onDidChange(callback: OnDidChangeCallback | undefined): this
```

在组件执行增删操作后，触发回调。如果文本实际未发生增删，则不触发该回调。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

> **说明：**&gt;
> 从API version 18开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnDidChangeCallback](arkts-arkui-ondidchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onDidIMEInput

```TypeScript
default onDidIMEInput(callback: Callback<TextRange> | undefined): this
```

输入法输入完成后，触发回调。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[TextRange](arkts-arkui-textcommon-textrange-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onEditingChange

```TypeScript
default onEditingChange(callback: Callback<boolean> | undefined): this
```

组件内容的编辑状态发生变化时触发该回调函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onIMEInputComplete

```TypeScript
default onIMEInputComplete(callback: Callback<RichEditorTextSpanResult> | undefined): this
```

输入法输入完成后，触发回调。该接口仅支持返回一个文本span的信息，当编辑操作涉及返回多个文本span信息时，建议使用[onDidIMEInput](#ondidimeinput)接口。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorTextSpanResult](arkts-arkui-richeditor-richeditortextspanresult-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onPaste

```TypeScript
default onPaste(callback: PasteEventCallback | undefined): this
```

粘贴完成前，触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PasteEventCallback](arkts-arkui-pasteeventcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onReady

```TypeScript
default onReady(callback: VoidCallback | undefined): this
```

富文本组件初始化完成后触发回调。初始化完成后组件可正常响应输入和交互。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onSelect

```TypeScript
default onSelect(callback: Callback<RichEditorSelection> | undefined): this
```

鼠标左键双击选中内容触发回调；松开鼠标左键再次触发回调。手指长按选中内容触发回调；松开手指再次触发回调。通过手指或鼠标连续修改选中区、三击选段场景，不回调onSelect。需要实时感知选中区变化的场景和使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件，请使用 onSelectionChange接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorSelection](arkts-arkui-richeditor-richeditorselection-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onSelectionChange

```TypeScript
default onSelectionChange(callback: Callback<RichEditorRange> | undefined): this
```

内容选择区域或编辑状态下的光标位置发生变化时，将触发该回调。光标位置变化时，回调中选择区域的起始和终止位置相等。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: SubmitCallback | undefined): this
```

按下软键盘输入法回车键时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SubmitCallback](arkts-arkui-submitcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

在组件绑定输入法前，触发回调。适用于需要定制输入法行为的场景，如设置输入法扩展配置以实现特定输入模式、自定义输入法功能等。调用IMEClient的setExtraConfig方法设置输入法扩展信息。在绑定输入法成功后， 输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。<!--Del-->从API版本26.0.0开始，在输入框将要绑定输入法前，可以通过`UIContext`的系统接口 [setKeyboardAppearanceConfig](arkts-arkui-arkui-uicontext-uicontext-c-sys.md#setkeyboardappearanceconfig)设置键盘的样式。<!--DelEnd-->

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## onWillChange

```TypeScript
default onWillChange(callback: Callback<RichEditorChangeValue, boolean> | undefined): this
```

在组件执行增删操作前，触发回调。与[onDidChange](#ondidchange)形成will/did时序模式：onWillChange在增删操作前触发，onDidChange在增删操作后触发； onWillChange返回false时，组件不执行增删操作，onDidChange不会触发。两者可同时使用。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建的RichEditor组件不支持该回调。

> **说明：**&gt;
> 从API version 18开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[RichEditorChangeValue](arkts-arkui-richeditor-richeditorchangevalue-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## orphanCharOptimization

```TypeScript
default orphanCharOptimization(enabled: boolean | undefined): this
```

设置文本排版时是否启用孤字优化。适用于长文排版、电子书阅读等需要避免段落末行仅剩一个字影响阅读体验的场景。不通过该接口设置，默认不启用孤字优化。孤字优化通过更高效地处理孤立字符（段落尾行首字符）来改善文本布局。启用后，它会调整换行点以尽可能避免孤立字符。孤字优化特性需在 [RichEditorParagraphStyle](arkts-arkui-richeditor-richeditorparagraphstyle-i.md)的wordBreak属性为非BREAK_ALL并且待排版文本首个 [TextStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textstyle-i.md)的 [locale](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textstyle-i.md)为“zh-Hans”或“zh-Hant”时生效。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## placeholder

```TypeScript
default placeholder(value: ResourceStr | undefined, style?: PlaceholderStyle | undefined): this
```

设置无输入时的提示文本。设置后，组件无内容时显示提示文本，用户开始输入内容后提示文本自动消失。

> **说明：**&gt;
> 从API version 18开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| style | [PlaceholderStyle](arkts-arkui-richeditor-placeholderstyle-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## punctuationOverflow

```TypeScript
default punctuationOverflow(enabled: boolean | undefined): this
```

设置是否启用行尾标点符号悬挂。启用后，允许行尾单个标点符号超出排版宽度而不换行，适用于需要避免行尾标点符号换行至下一行行首以提升排版美观度的场景。不通过该接口设置，默认标点符号不悬挂。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## scrollBarColor

```TypeScript
default scrollBarColor(color: ColorMetrics | undefined): this
```

设置组件滚动条颜色。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(value: ResourceColor | undefined): this
```

设置文本选中的底板颜色。如果未设置不透明度，默认为20%不透明度。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

设置拖动预览样式。适用于需要自定义拖拽内容外观的场景，如匹配应用主题风格的拖拽预览效果。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## setRichEditorOptions

```TypeScript
default setRichEditorOptions(options: RichEditorOptions | RichEditorStyledStringOptions): this
```

设置 RichEditor 选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RichEditorOptions](arkts-arkui-richeditor-richeditoroptions-i.md) \| [RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## singleLine

```TypeScript
default singleLine(isEnable: boolean | undefined): this
```

设置是否启用单行模式。未通过该接口设置时，默认不启用单行模式。

> **说明：**&gt;
> 单行模式不显示滚动条。&gt;
> 单行模式下换行符会显示为空格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## stopBackPress

```TypeScript
default stopBackPress(isStopped: boolean | undefined): this
```

设置是否阻止返回键传递。适用于编辑内容未保存时阻止返回避免数据丢失、弹窗编辑等需要防止用户误操作退出编辑的场景。

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
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |

## undoStyle

```TypeScript
default undoStyle(style: UndoStyle | undefined): this
```

设置撤销还原时是否保留原内容的样式。使用[RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md)构建RichEditor组件时，撤销还原时默认保留原内容样式，不受该接口设置的属性影响 。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [UndoStyle](arkts-arkui-richeditor-undostyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |
