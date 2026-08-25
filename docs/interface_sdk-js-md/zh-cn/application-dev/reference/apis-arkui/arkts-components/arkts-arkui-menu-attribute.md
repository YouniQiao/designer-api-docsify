# Menu属性/事件

除支持通用属性外，还支持以下属性：

**继承/实现关系：** MenuAttribute extends CommonMethod<MenuAttribute>

**起始版本：** 9

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## font

```TypeScript
font(value: Font)
```

统一设置Menu中所有文本的字体样式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](#font) | 是 |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

统一设置Menu中所有文本的颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## fontSize

```TypeScript
fontSize(value: Length)
```

统一设置Menu中所有文本的尺寸。

> **说明：**&gt;
> 从API version 9开始支持，从API version 10开始废弃，建议使用[font](#font)代替。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [font](#font)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## menuItemDivider

```TypeScript
menuItemDivider(options: DividerStyleOptions | undefined)
```

设置MenuItem分割线样式，不设置该属性则不展示分割线。startMargin + endMargin超过组件宽度后startMargin和endMargin会被置0。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DividerStyleOptions](../arkts-apis/arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 |

## menuItemGroupDivider

```TypeScript
menuItemGroupDivider(options: DividerStyleOptions | undefined)
```

设置MenuItemGroup顶部和底部分割线的样式，不设置该属性则默认展示分割线。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DividerStyleOptions](../arkts-apis/arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 |

## radius

```TypeScript
radius(value: Dimension | BorderRadiuses)
```

设置Menu边框圆角半径。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [BorderRadiuses](../arkts-apis/arkts-arkui-borderradiuses-t.md) | 是 |

## subMenuExpandingMode

```TypeScript
subMenuExpandingMode(mode: SubMenuExpandingMode)
```

设置Menu子菜单展开样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SubMenuExpandingMode](arkts-arkui-submenuexpandingmode-e.md) | 是 |

## subMenuExpandSymbol

```TypeScript
subMenuExpandSymbol(symbol: SymbolGlyphModifier)
```

设置Menu子菜单展开符号。仅在SubMenuExpandingMode.EMBEDDED_EXPAND或SubMenuExpandingMode.STACK_EXPAND模式下显示，SubMenuExpandingMode.SIDE_EXPAND模式下不显示。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| symbol | [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | 是 |
