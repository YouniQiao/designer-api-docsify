# TextInputAttribute

除支持通用属性，还支持以下属性：

> **说明：**&gt;
> 默认情况下，通用属性padding的默认值为：
{&nbsp;top: '8vp',&nbsp;right: '16vp',&nbsp;bottom: '8vp',&nbsp;left: '16vp'}

> 输入框开启下划线模式时，通用属性padding的默认值为：
{&nbsp;top: '12vp',&nbsp;right: '0vp',&nbsp;bottom: '12vp',&nbsp;left: '0vp'}

> 当输入框设置padding为0时，可设置
> borderRadius为0避免光标被截断。当光标
> 在文本框边缘显示异常时，请检查是否是padding、borderRadius属性影响造成。&gt;
> 从API version 10开始，单行输入框可设置.width('auto')使组件宽度自适应文本宽度，自适应时组件宽度受constraintSize属性以及父容器传递的最大最小宽度限制，其余使用方式参考
> [尺寸设置](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md)。

**继承/实现关系：** TextInputAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextInputAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## barState

```TypeScript
default barState(value: BarState | undefined): this
```

设置内联输入风格编辑态时滚动条的显示模式。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(iconOptions: CancelButtonOptions | undefined): this
```

设置右侧清除按钮样式。不支持内联模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iconOptions | [CancelButtonOptions](../arkts-components/arkts-arkui-cancelbuttonoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## cancelButton

```TypeScript
default cancelButton(symbolOptions: CancelButtonSymbolOptions | undefined): this
```

设置右侧清除按钮样式，仅支持symbol图标。不支持 [TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)的内联 模式。示例请参考 [示例15（设置symbol类型清除按钮）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#示例15设置symbol类型清除按钮)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| symbolOptions | [CancelButtonSymbolOptions](../arkts-components/arkts-arkui-cancelbuttonsymboloptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretColor

```TypeScript
default caretColor(value: ResourceColor | undefined): this
```

设置输入框光标颜色。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretPosition

```TypeScript
default caretPosition(value: int | undefined): this
```

设置光标位置。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## caretStyle

```TypeScript
default caretStyle(value: CaretStyle | undefined): this
```

设置光标风格。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## contentType

```TypeScript
default contentType(value: ContentType | undefined): this
```

设置自动填充类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ContentType](arkts-arkui-textinput-contenttype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

设置输入的文本是否可复制。设置CopyOptions.None时，只支持粘贴和全选。设置CopyOptions.None时，不允许拖拽。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## customKeyboard

```TypeScript
default customKeyboard(value: CustomBuilder | ComponentContentBase | undefined, options?: KeyboardOptions): this
```

设置自定义键盘。当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景不会对应用原始界面产生压缩或者上提。自定义键盘无法获取焦点，但是会拦截手势事件。默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[TextInputController](arkts-arkui-textinput-textinputcontroller-c.md). [stopEditing](arkts-arkui-textinput-textinputcontroller-c.md#stopediting)方法控制键盘关闭。当设置自定义键盘时，可以通过绑定onKeyPreIme事件 规避物理键盘的输入。从API version 23开始，自定义键盘可以通过 [setCustomKeyboardContinueFeature](arkts-arkui-arkui-uicontext-uicontext-c.md#setcustomkeyboardcontinuefeature) 开启接续，在切换至其他自定义键盘时，会直接切换，不会触发键盘关闭和拉起动画。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## ellipsisMode

```TypeScript
default ellipsisMode(mode: EllipsisMode | undefined): this
```

设置省略位置。ellipsisMode属性仅在 [TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)的内联 模式下生效，需要配合overflow设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。非编辑态时正常生效，编辑态时EllipsisMode.START和EllipsisMode.CENTER仅在maxLines设置为1时生效，EllipsisMode.END、 EllipsisMode.MULTILINE_START和EllipsisMode.MULTILINE_CENTER正常生效。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableAutoFill

```TypeScript
default enableAutoFill(value: boolean | undefined): this
```

设置是否启用自动填充。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableAutoFillAnimation

```TypeScript
default enableAutoFillAnimation(enabled: boolean | undefined): this
```

设置是否启用自动填充动效。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## enableKeyboardOnFocus

```TypeScript
default enableKeyboardOnFocus(value: boolean | undefined): this
```

设置TextInput通过点击以外的方式获焦时，是否主动拉起软键盘。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置字体颜色。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: ResourceStr | undefined): this
```

设置字体列表。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

设置字体大小。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

设置字体样式。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## heightAdaptivePolicy

```TypeScript
default heightAdaptivePolicy(value: TextHeightAdaptivePolicy | undefined): this
```

组件设置为内联输入风格时，设置文本自适应高度的方式。当设置为TextHeightAdaptivePolicy.MAX_LINES_FIRST时，优先使用[maxLines](#maxlines)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束， 则尝试在[minFontSize](#minfontsize)和[maxFontSize](#maxfontsize)的范围内缩小字体以显示更多文本。当设置为TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST时，优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在 minFontSize和maxFontSize的范围内增大字体并使用最大限度的字体大小。当设置为TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST时，与TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST效果一样。组件设置为非内联输入风格时，设置文本自适应高度(TextHeightAdaptivePolicy)的三种方式效果一样，即在minFontSize和maxFontSize的范围内缩小字体以显示更多文本。

> **说明：**&gt;
> 组件设置为内联输入风格，编辑态与非编辑态存在字体大小不一致情况。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## inputFilter

```TypeScript
default inputFilter(value: ResourceStr | undefined, error?: Callback<string> | undefined): this
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。从API version 11开始，设置inputFilter且输入的字符不为空字符，会导致[type](#type)接口附带的文本过滤效果失效。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## lineBreakStrategy

```TypeScript
default lineBreakStrategy(strategy: LineBreakStrategy | undefined): this
```

设置折行规则。该属性在wordBreak不等于breakAll的时候生效，不支持连字符。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

设置文本的行高。设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

> **说明：**&gt;
> - 特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。&gt;
> - 设置[密码模式](../../../ui/arkts-common-components-text-input.md#密码模式)时，通过该接口设置行高[lineHeight](#lineheight)不生
> 效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| scale | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[minFontSize](#minfontsize)以及[maxLines](#maxlines)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[fontSize](#fontsize)属性的值生效，未设置时按照其默认值生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxLength

```TypeScript
default maxLength(value: int | undefined): this
```

设置文本的最大输入字符数。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## maxLines

```TypeScript
default maxLines(value: int | undefined): this
```

设置内联输入风格编辑态时文本可显示的最大行数。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| scale | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[maxFontSize](#maxfontsize)以及[maxLines](#maxlines)(组件设置为内联输入风格且编辑态时使用)或布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](#fontsize)属性的值生效，未设置时按照其默认值生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onEditChange

```TypeScript
default onEditChange(callback: Callback<boolean> | undefined): this
```

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。取值为undefined时，不使用回调函数。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onSecurityStateChange

```TypeScript
default onSecurityStateChange(callback: Callback<boolean> | undefined): this
```

密码显隐状态切换时，触发该回调。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onSubmit

```TypeScript
default onSubmit(callback: OnSubmitCallback | undefined): this
```

按下输入法回车键触发该回调。非TV设备按下回车键时输入框默认会失焦且收起键盘，可在OnSubmitCallback回调中配置是否收起键盘，参考 [示例2（设置下划线）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#示例2设置下划线)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnSubmitCallback](arkts-arkui-onsubmitcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## onWillAttachIME

```TypeScript
default onWillAttachIME(callback: Callback<IMEClient> | undefined): this
```

在输入框将要绑定输入法前触发该回调。<!--Del-->在输入框将要绑定输入法前，可以通过`UIContext`的系统接口 [setKeyboardAppearanceConfig](../../../reference/apis-arkui/js-apis-arkui-UIContext-sys.md#setkeyboardappearanceconfig20) 设置键盘的样式。<!--DelEnd-->从API version 22开始，调用[IMEClient](../../../reference/apis-arkui/arkui-ts/ts-text-common.md#imeclient20对象说明)的 setExtraConfig方法可以设置输入法扩展信息。在绑定输入法成 功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## orphanCharOptimization

```TypeScript
default orphanCharOptimization(enabled: boolean | undefined): this
```

设置文本排版时是否使能孤字优化。不通过该接口设置，默认不使能孤字优化。孤字优化通过更高效地处理孤立字符（段落尾行首字符）来改善文本布局。使能后，它会调整换行点以尽可能避免孤立字符。孤字优化特性需在[wordBreak](#wordbreak)为非BREAK_ALL并且待排版文本首个 [TextStyle](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#textstyle)的 [locale](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#textstyle)为“zh-Hans”或“zh-Hant”时生效。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## passwordIcon

```TypeScript
default passwordIcon(value: PasswordIcon | undefined): this
```

设置当密码输入模式时，输入框末尾的图标。支持jpg、png、bmp、heic和webp类型的图片格式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PasswordIcon](arkts-arkui-textinput-passwordicon-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## passwordRules

```TypeScript
default passwordRules(value: string | undefined): this
```

定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。<!--RP1--><!--RP1End-->

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## placeholderColor

```TypeScript
default placeholderColor(value: ResourceColor | undefined): this
```

设置placeholder文本颜色。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## punctuationOverflow

```TypeScript
default punctuationOverflow(enabled: boolean | undefined): this
```

设置是否启用行尾标点符号悬挂。不通过该接口设置，默认标点符号不悬挂。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectAll

```TypeScript
default selectAll(value: boolean | undefined): this
```

设置初始状态时，是否全选文本。不支持 [TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)的内联 模式。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

设置文本输入框内文本拖拽时的背板样式。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## selectionMenuHidden

```TypeScript
default selectionMenuHidden(value: boolean | undefined): this
```

设置是否隐藏系统文本选择菜单。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## setTextInputOptions

```TypeScript
default setTextInputOptions(value?: TextInputOptions): this
```

设置TextInput组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextInputOptions](arkts-arkui-textinput-textinputoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

设置文本着色器效果，如线性渐变、径向渐变效果等。

> **说明：**&gt;
> 当同时设置shaderStyle和[strokeWidth](#strokewidth)时，shaderStyle不生效。&gt;
> shaderStyle的优先级高于[fontColor](#fontcolor)。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showCounter

```TypeScript
default showCounter(value: boolean | undefined, options?: InputCounterOptions | undefined): this
```

设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。未调用showCounter接口时，默认不显示计数器。参数value为true时，才能设置options，文本框开启计数下标功能，需要配合[maxLength](#maxlength)（设置最大字符限制）一起使用。字符计数器显示的效果是当前输入字符数/最大可输入字符数。当输入字符数大于最大字符数乘百分比值时，显示字符计数器。如果用户设置计数器时不设置InputCounterOptions，那么当前输入字符数超过最大字符数时，边框和计数器下标将变为红色。用户同时设置参数value为true和 [InputCounterOptions](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#inputcounteroptions11对象说明)， 当thresholdPercentage数值在有效区间内，且输入字符数超过最大字符数时，边框和计数器下标将变为红色，框体抖动。highlightBorder设置为false，则不显示红色边框，计数器默认显示红色，框体抖动。  
[TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)的内联 模式、[密码模式](../../../ui/arkts-common-components-text-input.md#密码模式)下字符计数器不显示。  
[示例5（设置计数器）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#示例5设置计数器)展示了设置showCounter的效 果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| options | [InputCounterOptions](../arkts-components/arkts-arkui-inputcounteroptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showError

```TypeScript
default showError(value?: ResourceStr | undefined): this
```

设置错误状态下提示的错误文本或者不显示错误状态。当参数类型为ResourceStr并且输入内容不符合定义规范时，提示错误文本，当提示错误单行文本超长时，末尾以省略号显示。当参数类型为undefined时，不显示错误状态。请参考 [示例2](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#示例2设置下划线)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showPassword

```TypeScript
default showPassword(visible: boolean | undefined): this
```

设置密码的显隐状态。当[InputType](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#inputtype枚举说明)设置为Password、 NEW_PASSWORD和NUMBER_PASSWORD模式时，密码保护功能才能生效。非密码输入模式则不会触发该功能。  
[密码模式](../../../ui/arkts-common-components-text-input.md#密码模式)时，由于输入框后端的状态和前端应用侧的状态管理变量会不一致，可能导致末尾图标的状态异常。建议在 [onSecurityStateChange](#onsecuritystatechange)上增加状态同步。参考 [示例1（设置与获取光标位置）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#示例1设置与获取光标位置)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| visible | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showPasswordIcon

```TypeScript
default showPasswordIcon(value: boolean | undefined): this
```

设置当密码输入模式时，输入框末尾的图标是否显示。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showUnderline

```TypeScript
default showUnderline(value: boolean | undefined): this
```

设置是否开启下划线。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## showUnit

```TypeScript
default showUnit(value: CustomBuilder | undefined): this
```

设置控件作为文本框单位。需搭配[showUnderline](#showunderline)使用，当showUnderline为true时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## style

```TypeScript
default style(value: TextInputStyle | TextContentStyle | undefined): this
```

设置输入框为默认风格或内联输入风格，内联输入风格只支持InputType.Normal类型。输入框类型介绍请参考[type](#type)接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextInputStyle](arkts-arkui-textinput-textinputstyle-e.md) \| [TextContentStyle](arkts-arkui-textcontentstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

设置文本在输入框中的水平对齐方式。支持TextAlign.Start、TextAlign.Center和TextAlign.End。TextAlign.JUSTIFY的对齐方式按照TextAlign.Start处理。可通过align属性控制文本段落在垂直方向上的位置。此组 件中不可使用align属性控制文本段落在水平方向上的位置。  
- Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对齐。 - Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。 - Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## textOverflow

```TypeScript
default textOverflow(value: TextOverflow | undefined): this
```

设置文本超长时的显示方式。仅在 [TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)值为内 联模式的编辑态、非编辑态下支持。文本截断是按字进行。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可将wordBreak属性设置为WordBreak.BREAK_ALL。当overflow设置为TextOverflow.None时，效果与TextOverflow.Clip相同。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## type

```TypeScript
default type(value: InputType | undefined): this
```

设置输入框类型。不同的InputType会拉起对应类型的键盘，同时限制输入。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [InputType](arkts-arkui-textinput-inputtype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## underlineColor

```TypeScript
default underlineColor(value: ResourceColor | UnderlineColor | undefined): this
```

设置下划线颜色。开启输入框下划线[showUnderline](#showunderline)时，支持配置下划线颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [UnderlineColor](arkts-arkui-textinput-underlinecolor-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |

## wordBreak

```TypeScript
default wordBreak(value: WordBreak | undefined): this
```

设置文本断行规则。该属性在组件设置 [TextInputStyle](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textinput.md#textinputstyle9枚举说明)的内联 模式时样式生效，但对placeholder文本无效。

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
| [TextInputAttribute](arkts-arkui-textinput-textinputattribute-i.md) |
