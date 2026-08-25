# TextAttribute

除支持通用属性，还支持以下属性：

**继承/实现关系：** TextAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextAttribute](arkts-arkui-text-textattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## baselineOffset

```TypeScript
default baselineOffset(value: double | string | undefined): this
```

设置文本基线的偏移量。设置该值为百分比时，按默认值显示。正数内容向上偏移，负数向下偏移。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## bindSelectionMenu

```TypeScript
default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined, responseType: TextResponseType | undefined, options?: SelectionMenuOptions | undefined): this
```

设置自定义选择菜单。bindSelectionMenu的长按响应时长为600ms， bindContextMenu的长按响应时 长为800ms，当两者同时绑定且触发方式均为长按时，优先响应bindSelectionMenu。自定义菜单超长时，建议内部嵌套使用Scroll组件，避免键盘被遮挡。从API版本26.0.0开始，文本组件调用该接口时，options中的menuType属性传入MenuType.PREVIEW_MENU，设置图片预览菜单的能力生效。如果要使用图片预览菜单，需要同时把spanType设置为TextSpanType.IMAGE，responseType设置为TextResponseType.LONG_PRESS，options中的menuType设置为 MenuType.PREVIEW_MENU才会生效。当[copyOption](#copyoption)为CopyOptions.None时，设置图片预览菜单将不会生效。

> **说明：**&gt;
> 该接口不支持在
> attributeModifier
> 中调用。&gt;
> 通过[editMenuOptions](#editmenuoptions)设置文本选择菜单时，保留系统默认的风格，触发菜单弹出的条件不变。&gt;
> 通过[bindSelectionMenu](#bindselectionmenu)设置文本选择菜单时，风格由开发者定义，触发菜单弹出的条件由开发者定义。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanType | [TextSpanType](arkts-arkui-text-textspantype-e.md) \| undefined | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| responseType | [TextResponseType](arkts-arkui-text-textresponsetype-e.md) \| undefined | 是 |
| options | [SelectionMenuOptions](arkts-arkui-richeditor-selectionmenuoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## caretColor

```TypeScript
default caretColor(color: ResourceColor | undefined): this
```

设置文本框选中区域手柄颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## contentTransition

```TypeScript
default contentTransition(transition: ContentTransition | undefined): this
```

可以设置为数字翻牌动效 NumericTextTransition。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transition | [ContentTransition](arkts-arkui-textcommon-contenttransition-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

设置组件是否支持文本可复制粘贴。从API version 20开始，当Text组件执行复制操作时，会将HTML格式的内容添加到剪贴板中。  
- 当Text组件包含子组件时，仅支持Span和 ImageSpan子组件向剪贴板中添加HTML格式的内容。 - 设置Text组件的属性字符串时，请参考属性字符串 toHtml接口文档，以了解支持转换为HTML的范围。  
设置copyOption为CopyOptions.InApp或者CopyOptions.LocalDevice时：  
- 长按文本，会弹出文本选择菜单，可选中文本并进行复制、全选操作。 - 默认情况下，长按选中文本可拖拽。若要取消此功能，可将 `draggable` 设置为 `false`。 - 若需要支持Ctrl+C复制，需同时设置[textSelectable](#textselectable)为TextSelectableMode.SELECTABLE_FOCUSABLE。  
此时Text会监听onClick事件，手势事件为非冒泡事件，若需要点击Text组件区域响应父组件的点击手势事件，建议在父组件上使用 parallelGesture绑定手势识别，也可参考 示例7（设置文本识别）。由于卡片没有长按事件，此场景下长按文本，不会弹出文本选择菜单。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## dataDetectorConfig

```TypeScript
default dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

设置文本识别配置，可配置识别类型、实体显示样式，以及是否开启长按预览等。需配合[enableDataDetector](#enabledatadetector)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## decoration

```TypeScript
default decoration(value: DecorationStyleInterface | undefined): this
```

设置文本装饰线样式及其颜色。

> **说明：**&gt;
> 当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见"gjyqp"等英文字符。&gt;
> 当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值"#00FFFFFF"时，装饰线颜色设置为透明色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DecorationStyleInterface](arkts-arkui-styledstring-decorationstyleinterface-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

设置选中文本拖拽效果。不能和onDragStart事件同时使用。当draggable设置为true时，需配合CopyOptions使用， 设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice，支持对选中文本的拖拽及复制到输入框。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。调用 [disableMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablemenuitems)或 [disableSystemServiceMenuItems](../../../reference/apis-arkui/arkts-apis-uicontext-textmenucontroller.md#disablesystemservicemenuitems) 接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法 onCreateMenu的入参列表中不包含被屏蔽的菜单选项。

> **说明：**&gt;
> 通过[editMenuOptions](#editmenuoptions)设置文本选择菜单时，保留系统默认的风格，触发菜单弹出的条件不变。&gt;
> 通过[bindSelectionMenu](#bindselectionmenu)设置文本选择菜单时，风格由开发者定义，触发菜单弹出的条件由开发者定义。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## ellipsisMode

```TypeScript
default ellipsisMode(value: EllipsisMode | undefined): this
```

设置省略位置。ellipsisMode属性需要与overflow设置为TextOverflow.Ellipsis以及maxLines使用，单独设置ellipsisMode属性不生效。EllipsisMode.START和EllipsisMode.CENTER仅在单行超长文本生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [EllipsisMode](arkts-arkui-ellipsismode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## enableDataDetector

```TypeScript
default enableDataDetector(enable: boolean | undefined): this
```

设置是否进行文本特殊实体识别。当enableDataDetector设置为true时，识别特殊实体。所识别实体的样式如下，即字体颜色改为蓝色、并添加蓝色下划线。

> **说明：**&gt;
> - 设备底层需要具备文本识别能力，该接口才能生效。&gt;
> - 当[textOverflow](#textoverflow)设置为TextOverflow.MARQUEE时，不进行文本特殊实体识别。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

设置是否开启触控反馈。开启触控反馈时，需要在工程的[module.json5配置文件](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段开启振动权 限，配置如下：

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## font

```TypeScript
default font(fontValue: Font | undefined, options?: FontSettingOptions | undefined): this
```

设置文本样式，支持设置字体配置项。仅Text组件生效，其子组件不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fontValue | [Font](arkts-arkui-font-i.md) \| undefined | 是 |
| options | [FontSettingOptions](arkts-arkui-textcommon-fontsettingoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

设置字体族。

> **说明：**&gt;
> 可以使用[loadFontSync](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#loadfontsync)注册自定义字体。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

设置文字特性效果，比如数字等宽的特性。格式为：normal \| \&lt;feature-tag-value\&gt;\&lt;feature-tag-value\&gt;的格式为：\&lt;string\&gt; \[ \&lt;integer\&gt; \| on \| off ]\&lt;feature-tag-value\&gt;的个数可以有多个，中间用','隔开。例如，使用等宽数字的输入格式为："ss01" on。

> **说明：**&gt;
> 不支持Text内同时存在文本内容和Span或ImageSpan子组件。如果同时存在，只显示Span或ImageSpan内的内容。&gt;
> 字体排版引擎会对开发者传入的宽度width进行向下取整，保证
> 是整型像素后进行排版。如果向上取整，可能会出现文字右侧被截断。&gt;
> 当多个Text组件在Row容器内布局且没有设置具体的布局分配信息时，Text会以Row的最大尺寸
> 进行布局。如果需要子组件主轴累加的尺寸不超过Row容器主轴的尺寸，可以设置
> layoutWeight或者是以
> Flex布局来约束子组件的主轴尺寸。&gt;
> 系统默认字体支持的liga连字：Th fb ff fb ffb ffh ffi ffk ffl fh fi fk fl rf rt rv rx ry。常导致Span、属性字符串的效果不符合预期，关闭liga连字特性可以规
> 避。&gt;
> 文字特性效果与使用的字体文件密切相关。例如，8标点挤压功能需要字体文件中字符支持"ss08"特性，否则无法压缩，在当前系统默认字体中右侧标点符号及感叹号、顿号、问号均不生效。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: double | string | Resource | undefined): this
```

设置字体大小。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontVariations

```TypeScript
default fontVariations(fontVariations: Array<FontVariation> | undefined): this
```

设置可变字体的属性。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fontVariations](#fontvariations) | Array&lt;[FontVariation](arkts-arkui-fontvariation-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(weight: int | FontWeight | ResourceStr | undefined, options?: FontSettingOptions | undefined): this
```

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| weight | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| options | [FontSettingOptions](arkts-arkui-textcommon-fontsettingoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## halfLeading

```TypeScript
default halfLeading(halfLeading: boolean | undefined): this
```

设置文本是否垂直居中。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## heightAdaptivePolicy

```TypeScript
default heightAdaptivePolicy(value: TextHeightAdaptivePolicy | undefined): this
```

设置文本自适应布局调整字号的方式。规则如下：  
- MAX_LINES_FIRST模式：优先使用[maxLines](#maxlines)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在 [minFontSize](#minfontsize)和[maxFontSize](#maxfontsize)的范围内缩小字体以显示更多文本。 - MIN_FONT_SIZE_FIRST模式：优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和maxFontSize的范围内增大字体 并使用最大限度的字体大小在一行内显示，否则按minFontSize显示。 - LAYOUT_CONSTRAINT_FIRST模式：优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在minFontSize和maxFontSize的范围内缩小字体以满足布局约束。如果将字体大小缩小到 minFontSize后，布局大小仍然超过布局约束，则删除超过布局约束的行。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## incrementalUpdatePolicy

```TypeScript
default incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): this
```

设置文本渲染的增量更新策略。未通过该接口设置时，默认为IncrementalUpdatePolicy.NONE。该接口仅在Text内容包含属性字符串（StyledString）时生效。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [IncrementalUpdatePolicy](arkts-arkui-textcommon-incrementalupdatepolicy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## letterSpacing

```TypeScript
default letterSpacing(value: double | string | undefined): this
```

设置文本字符间距。设置该值为百分比时，按默认值显示。设置该值为0时，按默认值显示。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。当取值为负值时，文字会被压缩。负值过小时会将组件内容区大小压缩为0，导致内容无法显示。对每个字符生效，包括行尾字符。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineBreakStrategy

```TypeScript
default lineBreakStrategy(strategy: LineBreakStrategy | undefined): this
```

设置折行规则。该属性在[wordBreak](#wordbreak)不等于WordBreak.BREAK_ALL的时候生效，且不支持连词符。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineHeight

```TypeScript
default lineHeight(value: double | string | Resource | undefined): this
```

设置文本的行高。设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

> **说明：**&gt;
> 特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineHeightMultiple

```TypeScript
default lineHeightMultiple(value: double | undefined): this
```

使用倍数模式设置文本的行高。设置行高为入参（value）与字高（fontHeight）的乘积。

> **说明：**&gt;
> 当lineHeightMultiple使用有效值和
> [lineHeight](#lineheight)或
> [lineSpacing](#linespacing)同时设置时，仅
> lineHeightMultiple生效。lineHeightMultiple小于0时，lineHeightMultiple不生效，使用
> [lineHeight](#lineheight)和
> [lineSpacing](#linespacing)设置行高和行间距。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## lineSpacing

```TypeScript
default lineSpacing(value: LengthMetrics | undefined, options?: LineSpacingOptions): this
```

设置文本的行间距。当不配置LineSpacingOptions时，首行上方和尾行下方默认会有行间距。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## marqueeOptions

```TypeScript
default marqueeOptions(options: TextMarqueeOptions | undefined): this
```

设置文本跑马灯模式的配置项。当textOverflow设置为TextOverflow.MARQUEE时，marqueeOptions的设置才能生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextMarqueeOptions](arkts-arkui-text-textmarqueeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxFontSize

```TypeScript
default maxFontSize(value: double | string | Resource | undefined): this
```

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[minFontSize](#minfontsize)以及[maxLines](#maxlines)或布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[fontSize](#fontsize)属性的值生效，未设置时按照其默认值生效。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxLineHeight

```TypeScript
default maxLineHeight(value: LengthMetrics | undefined): this
```

设置文本的最大行高，设置值不大于0时，最大行高不受限制。maxLineHeight小于minLineHeight时，maxLineHeight按照minLineHeight属性的值生效。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## maxLines

```TypeScript
default maxLines(value: int | undefined): this
```

设置文本的最大行数。默认情况下，文本是自动折行的，如果指定此属性，则文本最多不会超过指定的行数。如果有多余的文本，可以通过[textOverflow](#textoverflow)来指定截断方式。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minFontSize

```TypeScript
default minFontSize(value: double | string | Resource | undefined): this
```

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。需配合[maxFontSize](#maxfontsize)以及[maxLines](#maxlines)或布局大小限制使用，单独设置不生效。自适应字号生效时，fontSize设置不生效。minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](#fontsize)属性的值生效，未设置时按照其默认值生效。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minLineHeight

```TypeScript
default minLineHeight(value: LengthMetrics | undefined): this
```

设置文本的最小行高，设置值不大于0时，取默认值0。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## minLines

```TypeScript
default minLines(minLines: int | undefined): this
```

设置文本显示的最小行数。如果实际文本高度小于最小行数对应的高度，最后显示高度为最小行数对应的高度。与[maxLines](#maxlines)同时配置时，最小行数对应的显示高度不会超过最大行数对应的高度限制。如果文本设置了constraintSize，那 么组件最后显示高度会在 constraintSize约束内。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [minLines](#minlines) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onCopy

```TypeScript
default onCopy(callback: ((value: string) => void) | undefined): this
```

长按文本内部区域弹出剪贴板后，点击剪贴板复制按钮，触发该回调。目前只有文本可以复制。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onMarqueeStateChange

```TypeScript
default onMarqueeStateChange(callback: Callback<MarqueeState> | undefined): this
```

跑马灯动画进行到特定的阶段时，触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[MarqueeState](arkts-arkui-text-marqueestate-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: ((selectionStart: int, selectionEnd: int) => void) | undefined): this
```

文本选择的位置发生变化时，触发该回调。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## optimizeTrailingSpace

```TypeScript
default optimizeTrailingSpace(optimize: boolean | undefined): this
```

设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。设置Text.optimizeTrailingSpace为true时：  
* 多行、单行、图文混排等多种情况下均会优化行尾空格（TextAlign.Center或TextAlign.End时，优化效果明显）； * 纯空格文本时，修饰线、阴影、背景色跟随空格文本显示； * 行首空格不在优化范围内，行尾文本强制换行，每行行尾空格根据组件宽度优化行尾空格。当纯空格文本设置优化行尾空格[optimizeTrailingSpace](#optimizetrailingspace)为true时，不允许同时设置文本背景色 backgroundColor、 空格装饰线[decoration](#decoration)和对齐[textAlign](#textalign)三个属性。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| optimize | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## privacySensitive

```TypeScript
default privacySensitive(supported: boolean | undefined): this
```

设置是否支持卡片敏感隐私信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| supported | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(color: ResourceColor | undefined): this
```

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## selectedDragPreviewStyle

```TypeScript
default selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined): this
```

设置文本拖拽时的背板样式。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## selection

```TypeScript
default selection(selectionStart: int | undefined, selectionEnd: int | undefined): this
```

设置选中区域。选中区域高亮且显示手柄和文本选择菜单。当[copyOption](#copyoption)设置为CopyOptions.None时，设置selection属性不生效。当[textOverflow](#textoverflow)设置为TextOverflow.MARQUEE时，设置selection属性不生效。当selectionStart大于等于selectionEnd时不选中。可选范围为[0, textSize]，其中textSize为文本内容最大字符数，入参小于0时处理为0，大于textSize时处理为textSize。当selectionStart或selectionEnd位于截断的不可见区域时，文本不选中。当 clip设置为false时，超出父组件的文 本可以被选中。可通过[onTextSelectionChange](#ontextselectionchange)接口获取选中区域位置变化结果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectionStart | int \| undefined | 是 |
| selectionEnd | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## setTextOptions

```TypeScript
default setTextOptions(content?: string | Resource, value?: TextOptions): this
```

设置Text选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string \| [Resource](arkts-arkui-resource-t.md) | 否 |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: ShaderStyle | undefined): this
```

可以显示为径向渐变RadialGradientStyle或线 性渐变LinearGradientStyle或纯色 ColorShaderStyle的效果，shaderStyle的优 先级高于[fontColor](#fontcolor)和AI识别，纯色建议使用 [fontColor](#fontcolor)。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shader | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## tailIndents

```TypeScript
default tailIndents(value: LengthMetrics | Array<LengthMetrics> | undefined): this
```

设置文本尾部缩进。未通过该接口设置时，文本尾部缩进为0fp。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| Array&lt;[LengthMetrics](arkts-arkui-lengthmetrics-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textAlign

```TypeScript
default textAlign(value: TextAlign | undefined): this
```

设置文本段落在水平方向的对齐方式。文本段落宽度占满Text组件宽度。可通过align属性控制文本段落在垂直方向上的位置，此组 件中不可通过align属性控制文本段落在水平方向上的位置，具体效果如下：  
- Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对齐。 - Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。 - Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。  
当textAlign属性设置为TextAlign.JUSTIFY时，需要根据文本内容设置[wordBreak](#wordbreak)属性，且最后一行文本水平对齐首部，不参与两端对齐。

> **说明：**&gt;
> textAlign只能调整文本整体的布局，不影响字符的显示顺序。若需要调整字符的显示顺序，请参考
> [镜像状态字符对齐](../../../ui/arkts-internationalization.md#镜像状态字符对齐)。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textCase

```TypeScript
default textCase(value: TextCase | undefined): this
```

设置文本大小写。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TextCase](arkts-arkui-textcase-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textContentAlign

```TypeScript
default textContentAlign(textContentAlign: TextContentAlign | undefined): this
```

设置文本内容区在组件内的垂直对齐方式。此接口可以在文本内容区高度大于组件高度时生效，确保文本内容区的对齐方式正确显示。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [textContentAlign](#textcontentalign) | [TextContentAlign](arkts-arkui-textcommon-textcontentalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textIndent

```TypeScript
default textIndent(value: Length | undefined): this
```

设置首行文本缩进。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textOverflow

```TypeScript
default textOverflow(options: TextOverflowOptions | undefined): this
```

设置文本超长时的显示方式。当 TextOverflowOptions 设置为TextOverflow.None、TextOverflow.Clip或TextOverflow.Ellipsis时：  
- 设置为TextOverflow.None、TextOverflow.Clip，文本超长时按最大行截断显示。 - 设置为TextOverflow.Ellipsis，文本超长时显示不下的文本用省略号代替。 - 需配合[maxLines](#maxlines)使用，单独设置不生效。 - 断行规则参考[wordBreak](#wordbreak)。默认情况下参考WordBreak.BREAK_WORD的截断方式，文本截断按字进行。例如，英文以单词为最小单位进行截断。若需要以字母为单位进行截断，可设 置wordBreak属性为WordBreak.BREAK_ALL。 - 折行规则参考[lineBreakStrategy](#linebreakstrategy)。该属性在[wordBreak](#wordbreak)不等于WordBreak.BREAK_ALL的时候生效， 不支持连词符。 - 从API version 11开始，建议优先组合[textOverflow](#textoverflow)和[wordBreak](#wordbreak)属性来设置截断方式，具体详见 示例4（设置文本断行及折行）<!--RP1--><!-- RP1End-->。  
当TextOverflowOptions设置为TextOverflow.MARQUEE时：  
- 文本在一行内滚动显示。 - 设置[maxLines](#maxlines)及[copyOption](#copyoption)属性均不生效。 - Text组件clip属性默认为 true。 - 属性字符串的CustomSpan不支持跑马灯模式。 - [textAlign](#textalign)属性的生效规则：当文本不可滚动时，textAlign属性生效；当文本可滚动时，textAlign属性不生效。 - 从API version 12开始，当TextOverflowOptions设置为TextOverflow.MARQUEE时，支持ImageSpan组件，文本和图片可在一行内滚动显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextOverflowOptions](arkts-arkui-text-textoverflowoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textSelectable

```TypeScript
default textSelectable(mode: TextSelectableMode | undefined): this
```

设置是否支持文本可选择、可获焦。需配合[copyOption](#copyoption)使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [TextSelectableMode](arkts-arkui-textselectablemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textShadow

```TypeScript
default textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

设置文字阴影效果。不支持ShadowOptions对象中的type、fill字段和color字段的智能取色模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## textVerticalAlign

```TypeScript
default textVerticalAlign(textVerticalAlign: TextVerticalAlign | undefined): this
```

设置文本段落在垂直方向的对齐方式。

> **说明：**&gt;
> - 与[halfLeading](#halfleading)同时配置时，halfLeading不生效。&gt;
> - 一个段落下使用同一字号必须同时设置行高[lineHeight](#lineheight)或者同一个段落不同字号文本混排时才有效果差异，否则设置了该属性任意枚举值和未设置该属性都是一样的排版效果。属性字符串
> TextStyle中的SuperscriptStyle上
> 下角标样式仅在TextVerticalAlign属性值为
> TextVerticalAlign.BASELINE时生效，其余垂直对齐方式下上下角标文本和普通文本表现一致，无上下角标效果。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [textVerticalAlign](#textverticalalign) | [TextVerticalAlign](arkts-arkui-textcommon-textverticalalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |

## wordBreak

```TypeScript
default wordBreak(value: WordBreak | undefined): this
```

设置断行规则。默认情况下，不调用wordBreak或者设置WordBreak.BREAK_WORD时，文本截断按字进行。例如，英文以单词为最小单位进行截断。WordBreak.BREAK_ALL与{overflow:&nbsp;TextOverflow.Ellipsis}、maxLines组合使用，可实现英文单词按字母截断，超出部分以省略号显示。

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
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |
