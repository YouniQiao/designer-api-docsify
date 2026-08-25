# MenuAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** MenuAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Menu组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuAttribute](arkts-arkui-menu-menuattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## font

```TypeScript
default font(value: Font | undefined): this
```

统一设置Menu中所有文本的尺寸。

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
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

统一设置Menu中所有文本的颜色。

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
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## menuItemDivider

```TypeScript
default menuItemDivider(options: DividerStyleOptions | undefined): this
```

设置menuItem分割线样式，不设置该属性则不展示分割线。startMargin + endMargin 超过组件宽度后startMargin和endMargin会被置0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## menuItemGroupDivider

```TypeScript
default menuItemGroupDivider(options: DividerStyleOptions | undefined): this
```

设置menuItemGroup上下分割线的样式，不设置该属性则默认展示分割线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## radius

```TypeScript
default radius(value: Dimension | BorderRadiuses | undefined): this
```

设置Menu边框圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## subMenuExpandingMode

```TypeScript
default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this
```

设置Menu子菜单展开样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SubMenuExpandingMode](arkts-arkui-menu-submenuexpandingmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

## subMenuExpandSymbol

```TypeScript
default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this
```

设置Menu子菜单展开符号。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| symbol | [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |
