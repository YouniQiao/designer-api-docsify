# MenuAttribute

除支持[通用属性](common)外，还支持以下属性：

**继承/实现关系：** MenuAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface MenuAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Menu组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default attributeModifier(        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuAttribute-default attributeModifier(        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuAttribute](arkts-arkui-menu-menuattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | Menu组件的属性修改 器。取值为undefined时，则不使用属性修改器。&lt;br/&gt;MenuAttribute：当前组件的[属性](#MenuAttribute)&lt;br/&gt;CommonMethod： [通用属性](common) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## font

```TypeScript
default font(value: Font | undefined): this
```

统一设置Menu中所有文本的尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default font(value: Font | undefined): this--><!--Device-MenuAttribute-default font(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | Menu中所有文本的尺寸。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：&lt;br/&gt;{&lt;br/&gt; size: 16,&lt;br/&gt; family: 'HarmonyOS Sans',&lt;br/&gt; weight: FontWeight.Medium,&lt;br/&gt; style: FontStyle.Normal&lt;br/&gt;} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

统一设置Menu中所有文本的颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default fontColor(value: ResourceColor | undefined): this--><!--Device-MenuAttribute-default fontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | Menu中所有文本的颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：'#E5000000' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## menuItemDivider

```TypeScript
default menuItemDivider(options: DividerStyleOptions | undefined): this
```

设置menuItem分割线样式，不设置该属性则不展示分割线。

startMargin + endMargin 超过组件宽度后startMargin和endMargin会被置0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default menuItemDivider(options: DividerStyleOptions | undefined): this--><!--Device-MenuAttribute-default menuItemDivider(options: DividerStyleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 | 设置menuItem分割线样式。取值为undefined时，则不展示分割线。&lt;br /&gt;-strokeWidth：分割线 的线宽。&lt;br /&gt;-color：分割线的颜色。&lt;br /&gt;-startMargin：分割线与menuItem侧边起始端的距离。&lt;br /&gt;-endMargin：分割线与menuItem侧边结束端的距离。&lt;br /&gt;- mode：分割线的模式，默认值为FLOATING_ABOVE_MENU。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## menuItemGroupDivider

```TypeScript
default menuItemGroupDivider(options: DividerStyleOptions | undefined): this
```

设置menuItemGroup上下分割线的样式，不设置该属性则默认展示分割线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default menuItemGroupDivider(options: DividerStyleOptions | undefined): this--><!--Device-MenuAttribute-default menuItemGroupDivider(options: DividerStyleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 | 设置menuItemGroup顶部和底部分割线样式。取值为undefined时，按各属性的默认值处理。&lt;br /&gt;- strokeWidth：分割线的线宽，默认值是1px。&lt;br /&gt;-color：分割线的颜色，默认值是 #33000000。&lt;br /&gt;-startMargin：分割线与menuItemGroup侧边起始端的距离，默认 为16vp，单位为vp。&lt;br /&gt;-endMargin：分割线与menuItemGroup侧边结束端的距离，默认为16vp，单位为vp。&lt;br /&gt;-mode：分割线的模式，默认值为 FLOATING_ABOVE_MENU。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## radius

```TypeScript
default radius(value: Dimension | BorderRadiuses | undefined): this
```

设置Menu边框圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default radius(value: Dimension | BorderRadiuses | undefined): this--><!--Device-MenuAttribute-default radius(value: Dimension | BorderRadiuses | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| undefined | 是 | Menu边框圆角半径。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：2in1设备上默认值为8 vp，其他设备上默认值为20vp。&lt;br/&gt; 从API version 12开始，当水平方向两个圆角半径之和的最大值大于菜单宽度，或垂直方向两个圆角半径之和的最大值大于菜单高度时，菜单四个圆角均采用菜单默认圆角半径值。 &lt;br/&gt;当设置Dimension类型且传参为异常值时，菜单圆角取默认值。&lt;br/&gt;当设置BorderRadiuses类型且传参为异常值时，菜单默认没有圆角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## subMenuExpandSymbol

```TypeScript
default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this
```

设置Menu子菜单展开符号。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this--><!--Device-MenuAttribute-default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | 是 | Menu子菜单展开符号。&lt;br/&gt;1、子菜单的展开样式为SubMenuExpandingMode.SIDE_EXPAND 时，不显示展开符号。&lt;br/&gt;2、子菜单的展开样式为SubMenuExpandingMode.EMBEDDED_EXPAND时，展开时展开符号会顺时针旋转180°。展开符号默认使用 `new SymbolGlyphModifier(\\$r('sys.symbol.chevron_down')).fontSize('24vp')`。&lt;br/&gt;3、子菜单的展开样式为 SubMenuExpandingMode.STACK_EXPAND时，展开时展开符号会顺时针旋转90°。展开符号默认使用 `new SymbolGlyphModifier(\\$r('sys.symbol.chevron_forward')).fontSize('20vp').padding(2)`。 &lt;br/&gt;4、取值为undefined 时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## subMenuExpandingMode

```TypeScript
default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this
```

设置Menu子菜单展开样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuAttribute-default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this--><!--Device-MenuAttribute-default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SubMenuExpandingMode](arkts-arkui-menu-submenuexpandingmode-e.md) \| undefined | 是 | Menu子菜单展开样式。取值为undefined时，按默认值处理。&lt;br/&gt;默认值： SubMenuExpandingMode.SIDE_EXPAND |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

