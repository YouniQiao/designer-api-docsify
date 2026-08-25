# AlphabetIndexerAttribute

width属性设置"auto"时表示自适应宽度，宽度会随索引项最大宽度变 化。  
padding属性默认为4vp。文本最大的字体缩放倍数maxFontScale和最小的字体缩放 倍数minFontScale皆为1，不跟随系统字体大小调节变化 。除支持通用属性外，还支持以下属性：

**继承/实现关系：** AlphabetIndexerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignStyle

```TypeScript
default alignStyle(value: IndexerAlign | undefined, offset?: Length | undefined): this
```

设置索引条提示弹窗的对齐样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [IndexerAlign](arkts-arkui-alphabetindexer-indexeralign-e.md) \| undefined | 是 |
| offset | [Length](arkts-arkui-length-t.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<AlphabetIndexerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置AlphabetIndexer组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## autoCollapse

```TypeScript
default autoCollapse(value: boolean | undefined): this
```

设置是否使用自适应折叠模式。如果索引项第一项为“#”，当除去第一项后剩余索引项数量 &lt;= 9时，选择全显示模式；9 < 剩余索引项数量 <= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式；剩余索引项数量 > 13时，根据索引条高度自适应选择短 折叠模式或者长折叠模式。如果索引项第一项不为“#”，当所有索引项数量 <= 9时，选择全显示模式；9 < 所有索引项数量 <= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式；所有索引项数量 > 13时，根据索引条高度自适应选择短折叠模式或 者长折叠模式。

> **说明：**>
> 从API version 12开始，该接口支持在
&gt; attributeModifier
> 中调用。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## color

```TypeScript
default color(value: ResourceColor | undefined): this
```

设置未选中项文本颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(value: boolean | undefined): this
```

设置是否开启触控反馈。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## font

```TypeScript
default font(value: Font | undefined): this
```

设置未选中项文本样式。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## itemBorderRadius

```TypeScript
default itemBorderRadius(value: double | undefined): this
```

设置索引项背板圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## itemSize

```TypeScript
default itemSize(value: string | double | undefined): this
```

设置索引项区域大小。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## onPopupSelect

```TypeScript
default onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback | undefined): this
```

提示弹窗二级索引选中事件，回调参数为当前选中二级索引项索引。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](arkts-arkui-onalphabetindexerpopupselectcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## onRequestPopupData

```TypeScript
default onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback | undefined): this
```

设置提示弹窗二级索引项内容事件，回调参数为当前选中项索引，回调返回值为提示弹窗需显示的二级索引项内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](arkts-arkui-onalphabetindexerrequestpopupdatacallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## onSelect

```TypeScript
default onSelect(callback: OnAlphabetIndexerSelectCallback | undefined): this
```

索引项选中事件，回调参数为当前选中项索引。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](arkts-arkui-onalphabetindexerselectcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupBackground

```TypeScript
default popupBackground(value: ResourceColor | undefined): this
```

设置提示弹窗背景颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupBackgroundBlurStyle

```TypeScript
default popupBackgroundBlurStyle(value: BlurStyle | undefined): this
```

设置提示弹窗的背景模糊材质。未通过该接口设置时，默认为组件普通材质模糊，对应取值为BlurStyle中的COMPONENT_REGULAR。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupColor

```TypeScript
default popupColor(value: ResourceColor | undefined): this
```

设置提示弹窗一级索引项文本颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupFont

```TypeScript
default popupFont(value: Font | undefined): this
```

设置提示弹窗一级索引文本样式。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupItemBackgroundColor

```TypeScript
default popupItemBackgroundColor(value: ResourceColor | undefined): this
```

设置提示弹窗二级索引项背景颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupItemBorderRadius

```TypeScript
default popupItemBorderRadius(value: double | undefined): this
```

设置提示弹窗索引项背板圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupItemFont

```TypeScript
default popupItemFont(value: Font | undefined): this
```

设置提示弹窗二级索引项文本样式。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupPosition

```TypeScript
default popupPosition(value: Position | undefined): this
```

设置弹出窗口相对于索引条上边框中点的位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupSelectedColor

```TypeScript
default popupSelectedColor(value: ResourceColor | undefined): this
```

设置提示弹窗二级索引选中项文本颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupTitleBackground

```TypeScript
default popupTitleBackground(value: ResourceColor | undefined): this
```

设置提示弹窗一级索引项背景颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## popupUnselectedColor

```TypeScript
default popupUnselectedColor(value: ResourceColor | undefined): this
```

设置提示弹窗二级索引未选中项文本颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## selected

```TypeScript
default selected(index: int | Bindable<int> | undefined): this
```

设置选中项索引值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(value: ResourceColor | undefined): this
```

设置选中项背景颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置选中项文本颜色。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## selectedFont

```TypeScript
default selectedFont(value: Font | undefined): this
```

设置选中项文本样式。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## setAlphabetIndexerOptions

```TypeScript
default setAlphabetIndexerOptions(info: AlphabetIndexerOptions): this
```

设置字母索引器选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AlphabetIndexerOptions](arkts-arkui-alphabetindexer-alphabetindexeroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |

## usingPopup

```TypeScript
default usingPopup(value: boolean | undefined): this
```

设置是否显示提示弹窗。

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
| [AlphabetIndexerAttribute](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md) |
