# SearchAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** SearchAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SearchAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SearchAttribute](arkts-arkui-search-searchattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## autoCapitalizationMode

```TypeScript
default autoCapitalizationMode(mode: AutoCapitalizationMode | undefined): this
```

设置自动大小写模式的文本模式，只提供接口能力，具体实现以输入法应用为主。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions | undefined): this
```

设置右侧清除按钮样式。示例请参考 [示例2（设置搜索和删除图标）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#示例2设置搜索和删除图标)和 [示例11（设置symbol类型清除按钮）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-search.md#示例11设置symbol类型清除按钮)。Wearable设备上默认图标大小为18fp。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CancelButtonOptions](arkts-arkui-search-cancelbuttonoptions-i.md) \| [CancelButtonSymbolOptions](arkts-arkui-search-cancelbuttonsymboloptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## caretStyle

```TypeScript
default caretStyle(value: CaretStyle | undefined): this
```

设置光标样式。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## compressLeadingPunctuation

```TypeScript
default compressLeadingPunctuation(enabled: boolean | undefined): this
```

设置是否开启行首标点符号压缩。

> **说明：**&gt;
> - 行首标点符号默认不压缩。&gt;
> - 支持压缩的标点符号，请参考[ParagraphStyle](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#paragraphstyle)
> 的行首压缩的标点范围。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

设置输入的文本是否可复制。设置CopyOptions.None时，当前Search中的文字无法被复制、剪切、翻译、分享、搜索和帮写，支持粘贴和全选。设置CopyOptions.None时，不允许拖拽。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(
      value: CustomBuilder | ComponentContentBase | undefined, options?: KeyboardOptions): this
```

设置自定义键盘。当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景不会对应用原始界面产生压缩或者上提。自定义键盘无法获取焦点，但是会拦截手势事件。默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[stopEditing](arkts-arkui-search-searchcontroller-c.md#stopediting)方法控制键盘关闭。如果设备支持拍摄输入，设置自定义键盘后，该输入框会不支持拍摄输入。当设置自定义键盘时，可以通过绑定onKeyPreIme事件 规避物理键盘的输入。从API version 23开始，自定义键盘可以通过 [setCustomKeyboardContinueFeature](arkts-arkui-arkui-uicontext-uicontext-c.md#setcustomkeyboardcontinuefeature) 开启接续，在切换至其他自定义键盘时，会直接切换，不会触发键盘关闭和拉起动画。

> **说明：**&gt;
> 该接口不支持在
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
| options | [KeyboardOptions](arkts-arkui-richeditor-keyboardoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## decoration

```TypeScript
default decoration(value: TextDecorationOptions | undefined): this
```

设置文本装饰线类型样式及其颜色。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## dividerColor

```TypeScript
default dividerColor(color: ColorMetrics | undefined): this
```

设置输入框分割线颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。调用 [disableMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems)或 [disableSystemServiceMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems) 接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法 onCreateMenu的入参列表中不包含被屏蔽的菜单选项。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableAutoSpacing

```TypeScript
default enableAutoSpacing(enabled: boolean | undefined): this
```

设置是否开启中文与西文的自动间距。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

设置是否开启触控反馈。开启触控反馈时，需要在工程的[module.json5](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段以开启振动权限，配置 如下：

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(value: boolean | undefined): this
```

设置Search通过点击以外的方式获焦时，是否主动拉起软键盘。从API version 10开始，获焦默认绑定输入法。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enablePreviewText

```TypeScript
default enablePreviewText(enable: boolean | undefined): this
```

设置是否开启输入预上屏。预上屏内容定义为文字暂存态，目前不支持文字拦截功能。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enableSelectedDataDetector

```TypeScript
default enableSelectedDataDetector(enable: boolean | undefined): this
```

设置是否对选中文本进行实体识别。该接口依赖设备底层应具有文本识别能力，否则设置不会生效。当enableSelectedDataDetector设置为true时，默认识别所有类型的实体。启用后可识别选区中的邮件、电话、网址、日期、地址等，并在文本选择菜单中展示对应的AI菜单项。默认启用AI菜单功能。AI菜单功能启用时，在组件中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括 TextMenuItemId中的url（打开链接）、email（新建邮 件）、phoneNumber（呼叫）、address（导航前往）、dateTime（新建日程）。AI菜单生效时，选中范围内需包括且仅包括一个完整的AI实体，才能展示对应的选项。该菜单项与 TextMenuItemId中的askAI菜单项不同时出现。需要CopyOptions为 CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE时，本功能生效。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## enterKeyType

```TypeScript
default enterKeyType(value: EnterKeyType | undefined): this
```

设置输入法回车键类型。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## fallbackLineSpacing

```TypeScript
default fallbackLineSpacing(enabled: boolean | undefined): this
```

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。不通过该接口设置，默认行高不基于文字实际高度自适应。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置输入文本的字体颜色。fontSize、fontStyle、fontWeight和fontFamily在[textFont](#textfont)属性中设置。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

设置文字特性效果，比如数字等宽的特性。格式为：normal \| \&lt;feature-tag-value\&gt;\&lt;feature-tag-value\&gt;的格式为：\&lt;string\&gt; \[ \&lt;integer\&gt; \| on \| off ]\&lt;feature-tag-value\&gt;的个数可以有多个，中间用','隔开。例如，使用等宽数字的输入格式为："ss01" on。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## halfLeading

```TypeScript
default halfLeading(halfLeading: boolean | undefined): this
```

设置文本在行内垂直居中，将行间距平分至行的顶部与底部。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## includeFontPadding

```TypeScript
default includeFontPadding(include: boolean | undefined): this
```

设置是否在首行和尾行增加间距以避免文字截断。不通过该接口设置，默认不增加间距。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## inputFilter

```TypeScript
default inputFilter(value: ResourceStr | undefined, error?: Callback<string> | undefined): this
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。设置inputFilter且输入的字符不为空字符，会导致设置输入框类型(即type接口)附带的文本过滤效果失效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| error | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## keyboardAppearance

```TypeScript
default keyboardAppearance(appearance: KeyboardAppearance | undefined): this
```

设置输入框拉起的键盘样式，需要输入法适配后生效。具体参考[输入法应用沉浸模式](../../../inputmethod/inputmethod-immersive-mode-guide.md)。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## letterSpacing

```TypeScript
default letterSpacing(value: double | string | Resource | undefined): this
```

设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。对每个字符生效，包括行尾字符。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

设置文本的文本行高。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

设置文本最大的字体缩放倍数。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[minFontSize](#minfontsize)以及布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[textFont](#textfont)属性里面size的取值生效，未设置时按照其默认值生效。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## maxLength

```TypeScript
default maxLength(value: int | undefined): this
```

设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

设置文本最小的字体缩放倍数。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[maxFontSize](#maxfontsize)以及布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。minFontSize小于或等于0时，自适应字号不生效，此时按照[textFont](#textfont)属性里面size的取值生效，未设置时按照其默认值生效。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: EditableTextOnChangeCallback | undefined): this
```

输入内容发生变化时，触发该回调。在本回调中，若执行了光标操作，需要开发者在预上屏场景下依据previewText参数调整光标逻辑，以适应预上屏场景。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onContentScroll

```TypeScript
default onContentScroll(callback: OnContentScrollCallback | undefined): this
```

文本内容滚动时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnContentScrollCallback](arkts-arkui-oncontentscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: Callback<string> | undefined): this
```

进行复制操作时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onCut

```TypeScript
default onCut(callback: Callback<string> | undefined): this
```

进行剪切操作时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onDidDelete

```TypeScript
default onDidDelete(callback: Callback<DeleteValue> | undefined): this
```

在删除完成时，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onDidInsert

```TypeScript
default onDidInsert(callback: Callback<InsertValue> | undefined): this
```

在输入完成时，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onEditChange

```TypeScript
default onEditChange(callback: Callback<boolean> | undefined): this
```

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onPaste

```TypeScript
default onPaste(callback: OnPasteCallback | undefined): this
```

进行粘贴操作时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnPasteCallback](arkts-arkui-onpastecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: SearchSubmitCallback | undefined): this
```

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SearchSubmitCallback](arkts-arkui-searchsubmitcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: OnTextSelectionChangeCallback | undefined): this
```

文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnTextSelectionChangeCallback](arkts-arkui-ontextselectionchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

在搜索框将要绑定输入法前触发该回调。<!--Del-->在搜索框将要绑定输入法前，可以通过`UIContext`的系统接口 [setKeyboardAppearanceConfig](../../../reference/apis-arkui/js-apis-arkui-UIContext-sys.md#setkeyboardappearanceconfig20) 设置键盘的样式。<!--DelEnd-->从API version 22开始，调用IMEClient的 setExtraConfig方法可以设置输入法扩展信息。在绑定输入法成 功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

> **说明：**&gt;
> 该接口不支持在
> attributeModifier
> 中调用。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillChange

```TypeScript
default onWillChange(callback: Callback<EditableTextChangeValue, boolean> | undefined): this
```

在文本内容将要发生变化时，触发该回调。onWillChange的回调时序晚于onWillInsert、onWillDelete，早于onDidInsert、onDidDelete。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

在进行复制操作前，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillCut

```TypeScript
default onWillCut(callback: Callback<string, boolean> | undefined): this
```

在进行剪切操作前，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillDelete

```TypeScript
default onWillDelete(callback: Callback<DeleteValue, boolean> | undefined): this
```

在将要删除时，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## onWillInsert

```TypeScript
default onWillInsert(callback: Callback<InsertValue, boolean> | undefined): this
```

在将要输入时，触发该回调。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## placeholderColor

```TypeScript
default placeholderColor(value: ResourceColor | undefined): this
```

设置placeholder文本颜色，Wearable设备上默认值为'#99ffffff'。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## placeholderFont

```TypeScript
default placeholderFont(value?: Font | undefined): this
```

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## searchButton

```TypeScript
default searchButton(value: string | undefined, option?: SearchButtonOptions | undefined): this
```

设置搜索框末尾搜索按钮。点击搜索按钮，同时触发onSubmit与onClick回调。Wearable设备上默认字体大小为18fp。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |
| option | [SearchButtonOptions](arkts-arkui-search-searchbuttonoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## searchIcon

```TypeScript
default searchIcon(value: IconOptions | SymbolGlyphModifier | undefined): this
```

设置左侧搜索图标样式。Wearable设备上默认图标大小为16vp。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [IconOptions](arkts-arkui-search-iconoptions-i.md) \| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(value: ResourceColor | undefined): this
```

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

设置搜索框内文本拖拽时的背板样式。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## selectionMenuHidden

```TypeScript
default selectionMenuHidden(value: boolean | undefined): this
```

设置是否不弹出系统文本选择菜单。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## setSearchOptions

```TypeScript
default setSearchOptions(options?: SearchOptions): this
```

设置Search组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SearchOptions](arkts-arkui-search-searchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

设置文本着色器效果，如线性渐变、径向渐变效果等。

> **说明：**&gt;
> 当同时设置shaderStyle和[strokeWidth](#strokewidth)时，shaderStyle不生效。&gt;
> shaderStyle的优先级高于fontColor。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## stopBackPress

```TypeScript
default stopBackPress(isStopped: boolean | undefined): this
```

设置是否阻止返回键传递。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## strokeColor

```TypeScript
default strokeColor(color: ResourceColor | undefined): this
```

设置文本描边的颜色。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## strokeJoinStyle

```TypeScript
default strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): this
```

设置文本描边拐角样式。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(width: LengthMetrics | undefined): this
```

设置文本描边的宽度。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

设置文本在搜索框中的对齐方式。目前支持的对齐方式有：TextAlign.Start、TextAlign.Center、TextAlign.End、TextAlign.LEFT、TextAlign.RIGHT。 TextAlign.JUSTIFY的对齐方式按照TextAlign.Start处理。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textDirection

```TypeScript
default textDirection(direction: TextDirection | undefined): this
```

指定文本排版方向，未通过该接口设置时，默认文本排版方向遵循组件布局方向。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textFont

```TypeScript
default textFont(value?: Font | undefined): this
```

设置搜索框内输入文本样式，包括字体大小、字体粗细、字体族、字体风格。Wearable设备上默认字体大小为18fp。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## textIndent

```TypeScript
default textIndent(value: Dimension | undefined): this
```

设置首行文本缩进。

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
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |

## type

```TypeScript
default type(value: SearchType | undefined): this
```

设置输入框类型。不同的SearchType会拉起对应类型的键盘，同时限制输入。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SearchType](arkts-arkui-search-searchtype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SearchAttribute](arkts-arkui-search-searchattribute-i.md) |
