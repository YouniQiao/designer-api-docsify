# AlphabetIndexer属性/事件

width属性设置"auto"时表示自适应宽度，宽度会随索引项最大宽度变化。  
padding属性默认为4vp。文本最大的字体缩放倍数maxFontScale和最小的字体缩放倍数minFontScale 皆为1，不跟随系统字体大小调节变化。除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：

**继承/实现关系：** AlphabetIndexerAttribute extends CommonMethod<AlphabetIndexerAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## alignStyle

```TypeScript
alignStyle(value: IndexerAlign, offset?: Length)
```

设置索引条提示弹窗的对齐样式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [IndexerAlign](arkts-arkui-indexeralign-e.md) | 是 |
| offset | [Length](../arkts-apis/arkts-arkui-length-t.md) | 否 |

## autoCollapse

```TypeScript
autoCollapse(value: boolean)
```

设置是否使用自适应折叠模式。如果索引项第一项为“#”，当除去第一项后剩余索引项数量 &lt;= 9时，选择全显示模式（所有索引项完整显示）；9 &lt; 剩余索引项数量 &lt;= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式； 剩余索引项数量 &gt; 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。如果索引项第一项不为“#”，当所有索引项数量 &lt;= 9时，选择全显示模式（所有索引项完整显示）；9 < 所有索引项数量 <= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式； 所有索引项数量 > 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。

> **说明：**

&gt; 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## color

```TypeScript
color(value: ResourceColor)
```

设置未选中项文本颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(value: boolean)
```

设置是否开启触控反馈。开启后，在手指触摸或滑动选中索引项时会触发振动反馈。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## font

```TypeScript
font(value: Font)
```

设置未选中项文本样式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](#font) | 是 |

## itemBorderRadius

```TypeScript
itemBorderRadius(value: number)
```

设置索引项背板圆角半径。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## itemSize

```TypeScript
itemSize(value: string | number)
```

设置索引项区域大小。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| number | 是 |

## onPopupSelect

```TypeScript
onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback)
```

提示弹窗二级索引选中事件，回调参数为当前选中二级索引项索引。仅在[usingPopup](#usingpopup)为true时触发。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](arkts-arkui-onalphabetindexerpopupselectcallback-t.md) | 是 |

## onRequestPopupData

```TypeScript
onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback)
```

设置提示弹窗二级索引项内容事件，回调参数为当前选中项索引，回调返回值为提示弹窗需显示的二级索引项内容。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](arkts-arkui-onalphabetindexerrequestpopupdatacallback-t.md) | 是 |

## onSelect

```TypeScript
onSelect(callback: OnAlphabetIndexerSelectCallback)
```

索引项选中事件，回调参数为当前选中项索引。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](arkts-arkui-onalphabetindexerselectcallback-t.md) | 是 |

## onSelected

```TypeScript
onSelected(callback: (index: number) => void)
```

注册索引项选中事件回调，回调参数为当前选中项索引。

> **说明：**

> 从API version 7开始支持，从API version 8开始废弃，建议使用[onSelect](#onselect)替代。

**起始版本：** 7

**废弃版本：** 8

**替代接口：** [onSelect](#onselect)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (index: number) = & gt; void | 是 |

## popupBackground

```TypeScript
popupBackground(value: ResourceColor)
```

设置提示弹窗背景颜色。该接口未被主动调用或参数value传入undefined时：API version 11及以前版本，提示弹窗背景颜色默认为0xFFFFFFFF，显示为白色。对于API version 12至API version 24版本，默认为#66808080，显示为半透明的灰色。从API版本26.0.0开始，如果[popupBackground](#popupbackground) [popupBackgroundBlurStyle](#popupbackgroundblurstyle)均未被主动调用或 参数value传入undefined，高档、中档算力设备默认显示为沉浸式材质 ImmersiveStyle的THIN样式，低档算力设备默认显示为白色背景。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(value: BlurStyle)
```

设置提示弹窗的背景模糊材质。API版本26.0.0之前版本，未通过该接口设置时，默认为组件普通材质模糊，对应取值为BlurStyle中的COMPONENT_REGULAR。从API版本26.0.0开始， [popupBackground](#popupbackground)和popupBackgroundBlurStyle均未被主动调用或者传入undefined时，在高档 、中档算力设备默认显示为沉浸式材质ImmersiveStyle的THIN样式，低档 算力设备默认显示为白色背景。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | 是 |

## popupColor

```TypeScript
popupColor(value: ResourceColor)
```

设置提示弹窗一级索引项文本颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## popupFont

```TypeScript
popupFont(value: Font)
```

设置提示弹窗一级索引文本样式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](#font) | 是 |

## popupItemBackgroundColor

```TypeScript
popupItemBackgroundColor(value: ResourceColor)
```

设置提示弹窗二级索引项背景颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## popupItemBorderRadius

```TypeScript
popupItemBorderRadius(value: number)
```

设置提示弹窗索引项背板圆角半径。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## popupItemFont

```TypeScript
popupItemFont(value: Font)
```

设置提示弹窗二级索引项文本样式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](#font) | 是 |

## popupPosition

```TypeScript
popupPosition(value: Position)
```

设置提示弹窗相对于索引条上边框中点的位置。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) | 是 |

## popupSelectedColor

```TypeScript
popupSelectedColor(value: ResourceColor)
```

设置提示弹窗二级索引选中项文本颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## popupTitleBackground

```TypeScript
popupTitleBackground(value: ResourceColor)
```

设置提示弹窗一级索引项背景颜色。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## popupUnselectedColor

```TypeScript
popupUnselectedColor(value: ResourceColor)
```

设置提示弹窗二级索引未选中项文本颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selected

```TypeScript
selected(index: number)
```

设置选中项索引值。与[AlphabetIndexerOptions](arkts-arkui-alphabetindexeroptions-i.md)中的selected同时设置时，该属性的优先级更高。从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(value: ResourceColor)
```

设置选中项背景颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

设置选中项文本颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selectedFont

```TypeScript
selectedFont(value: Font)
```

设置选中项文本样式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](#font) | 是 |

## usingPopup

```TypeScript
usingPopup(value: boolean)
```

设置是否显示提示弹窗。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |
