# SelectAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**继承/实现关系：** SelectAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## arrowModifier

```TypeScript
default arrowModifier(modifier: SymbolGlyphModifier | undefined): this
```

定制Select按钮下拉箭头图标样式的方法，在应用arrowModifier之后，Select按钮下拉箭头的图标样式将完全由开发者自定义。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default arrowModifier(modifier: SymbolGlyphModifier | undefined): this--><!--Device-SelectAttribute-default arrowModifier(modifier: SymbolGlyphModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | 是 | 在Select组件上，定制Select按钮下拉箭头图标样式的方法。取值为undefined时，则不使用箭头修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## arrowPosition

```TypeScript
default arrowPosition(value: ArrowPosition | undefined): this
```

设置下拉菜单项的文本与箭头之间的对齐方式。与[arrowPosition](../arkts-components/arkts-arkui-arrowposition-e.md/arkts-arkui-arrowposition-e.md)相比，position参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default arrowPosition(value: ArrowPosition | undefined): this--><!--Device-SelectAttribute-default arrowPosition(value: ArrowPosition | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ArrowPosition](../arkts-components/arkts-arkui-arrowposition-e.md) \| undefined | 是 | 下拉菜单项的文本与箭头之间的对齐方式。&lt;br/&gt;当value的值为undefined时，默认值：ArrowPosition.END |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Select组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default attributeModifier(        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SelectAttribute-default attributeModifier(        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SelectAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | Select组件的属 性修改器。&lt;br/&gt;当modifier的值为undefined时，不使用属性修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## avoidance

```TypeScript
default avoidance(mode: AvoidanceMode | undefined): this
```

设置下拉菜单的避让模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default avoidance(mode: AvoidanceMode | undefined): this--><!--Device-SelectAttribute-default avoidance(mode: AvoidanceMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AvoidanceMode](arkts-arkui-select-avoidancemode-e.md) \| undefined | 是 | 设置下拉菜单的避让模式。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：AvoidanceMode.COVER_TARGET |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the chained object of Select component attributes |

## controlSize

```TypeScript
default controlSize(value: ControlSize | undefined): this
```

设置Select组件的尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default controlSize(value: ControlSize | undefined): this--><!--Device-SelectAttribute-default controlSize(value: ControlSize | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ControlSize](../arkts-components/arkts-arkui-controlsize-e.md) \| undefined | 是 | Select组件的尺寸。&lt;br/&gt;当value的值为undefined时，默认值为ControlSize.NORMAL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## divider

```TypeScript
default divider(options: DividerOptions | null | undefined): this
```

设置分割线样式，不设置该属性则按"默认值"展示分割线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default divider(options: DividerOptions | null | undefined): this--><!--Device-SelectAttribute-default divider(options: DividerOptions | null | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerOptions](../arkts-components/arkts-arkui-divideroptions-i.md) \| null \| undefined | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。&lt;br/&gt;默认值：&lt;br/&gt;{&lt;br/&gt; strokeWidth: '1px' , &lt;br/&gt;color: '#33182431'&lt;br/&gt;}&lt;br/&gt;2.设置为null时，不显示分割线。&lt;br/&gt;3.取值为undefined时，按默认值处理。 &lt;br/&gt; 4 .strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。&lt;br/&gt;5.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。 startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## dividerStyle

```TypeScript
default dividerStyle(style: DividerStyleOptions | undefined): this
```

设置分割线样式，不设置该属性则按"默认值"展示分割线。该属性与divider互斥，按调用顺序生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default dividerStyle(style: DividerStyleOptions | undefined): this--><!--Device-SelectAttribute-default dividerStyle(style: DividerStyleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。&lt;br/&gt;默认值：&lt;br/&gt;{&lt;br/&gt; strokeWidth: '1px' , &lt;br/&gt;color: '#33182431'&lt;br/&gt;}&lt;br/&gt;2.设置为null或undefined时，展示默认分割线。&lt;br/&gt;3.当mode为 FLOAT_ABOVE_MENU时，strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。当mode为EMBEDDED_IN_MENU时，分割线在Menu中展开，独立占用 高度。&lt;br/&gt;4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## font

```TypeScript
default font(value: Font | undefined): this
```

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。与[font](arkts-arkui-select-selectattribute-i.md#font)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default font(value: Font | undefined): this--><!--Device-SelectAttribute-default font(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | 下拉按钮本身的文本样式。&lt;br/&gt;如果设置controlSize的值为：controlSize.SMALL，size默认值是 `\\$r('sys.float.ohos_id_text_size_button2')`，否则为`\\$r('sys.float.ohos_id_text_size_button1')`。&lt;br/&gt;当value的值为 undefined时，恢复为系统文本样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置下拉按钮本身的文本颜色。与[fontColor](arkts-arkui-select-selectattribute-i.md#fontcolor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default fontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default fontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉按钮本身的文本颜色。&lt;br/&gt;当resColor的值为undefined时，默认值： `\\$r('sys.color.ohos_id_color_text_primary')`混合`\\$r('sys.color.ohos_id_alpha_content_primary')`的透明度。&lt;br/&gt;当value 的值为undefined时，维持上次取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## keyboardAvoidMode

```TypeScript
default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this
```

设置Select菜单避让键盘的模式。默认不避让。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this--><!--Device-SelectAttribute-default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [MenuKeyboardAvoidMode](../arkts-components/arkts-arkui-menukeyboardavoidmode-e.md) \| undefined | 是 | Select菜单避让键盘的模式。&lt;br/&gt;当mode的值为undefined时，默认不避让键盘。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## menuAlign

```TypeScript
default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this
```

设置下拉按钮与下拉菜单间的对齐方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this--><!--Device-SelectAttribute-default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [MenuAlignType](arkts-arkui-select-menualigntype-e.md) \| undefined | 是 | 对齐方式类型。&lt;br/&gt;当alignType的值为undefined时，默认值：MenuAlignType.START |
| offset | [Offset](arkts-arkui-componentutils-offset-i.md) \| undefined | 否 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。&lt;br/&gt; 默认值：{dx: 0, dy: 0} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundBlurStyle

```TypeScript
default menuBackgroundBlurStyle(value: BlurStyle | undefined): this
```

设置下拉菜单的背景模糊材质。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuBackgroundBlurStyle(value: BlurStyle | undefined): this--><!--Device-SelectAttribute-default menuBackgroundBlurStyle(value: BlurStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 | 下拉菜单的背景模糊材质。&lt;br/&gt;当style的值为undefined时，默认值：BlurStyle.COMPONENT_ULTRA_THICK |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundBlurStyleOptions

```TypeScript
default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this
```

设置Select组件的背景模糊效果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this--><!--Device-SelectAttribute-default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurStyle | [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md) \| undefined | 是 | 设置Select组件的背景模糊效果。&lt;br/&gt;当blurStyle的值为undefined时，恢复默认 值，默认值请参考BackgroundBlurStyleOptions类型说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## menuBackgroundColor

```TypeScript
default menuBackgroundColor(value: ResourceColor | undefined): this
```

设置下拉菜单的背景色。与  
[menuBackgroundColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-select copy.md#menubackgroundcolor11)&lt;sup&gt;11+&lt;/sup&gt;相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuBackgroundColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default menuBackgroundColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉菜单的背景色。&lt;br/&gt;当resColor的值为undefined时，默认值为Color.Transparent。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuBackgroundEffect

```TypeScript
default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this
```

设置Select组件的背景属性。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this--><!--Device-SelectAttribute-default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | 是 | 设置Select组件的背景属性，包括：模糊半径、亮度、饱和度和颜色。&lt;br/&gt;当effect的值为 undefined时，恢复默认值，默认值请参考BackgroundEffectOptions类型说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## menuItemContentModifier

```TypeScript
default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this
```

定制Select下拉菜单项内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this--><!--Device-SelectAttribute-default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;MenuItemConfiguration&gt; \| undefined | 是 | 在Select组件上，定制下拉菜单项内容区的方法。&lt;br/&gt;modifier：内 容修改器，开发者需要自定义class实现ContentModifier接口。&lt;br/&gt;当modifier的值为undefined时，不使用内容修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuOutline

```TypeScript
default menuOutline(outline: MenuOutlineOptions | undefined): this
```

设置下拉菜单框的外描边样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuOutline(outline: MenuOutlineOptions | undefined): this--><!--Device-SelectAttribute-default menuOutline(outline: MenuOutlineOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outline | [MenuOutlineOptions](arkts-arkui-select-menuoutlineoptions-i.md) \| undefined | 是 | 下拉菜单框的外描边样式。取值为undefined时，按各属性的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## menuSystemMaterial

```TypeScript
default menuSystemMaterial(material: SystemUiMaterial | undefined): this
```

Set system-styled materials for select's menu. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of select's menu.

Device Behavior Differences:The effect of the same material may vary across different devices depending on their computing power.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default menuSystemMaterial(material: SystemUiMaterial | undefined): this--><!--Device-SelectAttribute-default menuSystemMaterial(material: SystemUiMaterial | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| material | [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md) \| undefined | 是 | The select's menu material, undefined means retaining the original visual style of the select's menu. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## minKeyboardAvoidDistance

```TypeScript
default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this
```

设置Select菜单与键盘之间的最小距离。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this--><!--Device-SelectAttribute-default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 | Select菜单与键盘之间的最小距离。&lt;br/&gt;当distance的值为undefined时，使用默认距离。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## onSelect

```TypeScript
default onSelect(callback: OnSelectCallback | undefined): this
```

下拉菜单选中某一项时，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default onSelect(callback: OnSelectCallback | undefined): this--><!--Device-SelectAttribute-default onSelect(callback: OnSelectCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSelectCallback](arkts-arkui-onselectcallback-t.md) \| undefined | 是 | 下拉菜单选中某一项的回调。&lt;br/&gt;当callback的值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## optionBgColor

```TypeScript
default optionBgColor(value: ResourceColor | undefined): this
```

设置下拉菜单项的背景色。与[optionBgColor](arkts-arkui-select-selectattribute-i.md#optionbgcolor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionBgColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default optionBgColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉菜单项的背景色。&lt;br/&gt;当resColor的值为undefined时，默认值为Color.Transparent。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## optionFont

```TypeScript
default optionFont(value: Font | undefined): this
```

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

与[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionFont(value: Font | undefined): this--><!--Device-SelectAttribute-default optionFont(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | 下拉菜单项的文本样式。&lt;br/&gt;当value的值为undefined时，默认值：&lt;br/&gt;{&lt;br/&gt;size: \\$r(' sys.float.ohos_id_text_size_body1'),&lt;br/&gt;weight: FontWeight.Regular&lt;br/&gt;} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## optionFontColor

```TypeScript
default optionFontColor(value: ResourceColor | undefined): this
```

设置下拉菜单项的文本颜色。与[optionFontColor](arkts-arkui-select-selectattribute-i.md#optionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionFontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default optionFontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉菜单项的文本颜色。&lt;br/&gt;当value的值为undefined时，默认值：\\$r(' sys.color.ohos_id_color_text_primary') |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## optionHeight

```TypeScript
default optionHeight(value: Dimension | undefined): this
```

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。与  
[optionHeight](../../../reference/apis-arkui/arkui-ts/ts-basic-components-select copy.md#optionheight11)&lt;sup&gt;11+&lt;/sup&gt;相比，height参数新增了对undefined类型的支持。

当设置为异常值或零时，属性不生效。

如果下拉菜单所有选项的实际高度小于设定的高度，下拉菜单的高度按实际高度显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionHeight(value: Dimension | undefined): this--><!--Device-SelectAttribute-default optionHeight(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | 下拉菜单显示的最大高度。&lt;br/&gt;当height的值为undefined时，属性不生效，下拉菜单最大高度设为默认值，即下拉菜单最大高度默认值为屏 幕可用高度的80%。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## optionTextModifier

```TypeScript
default optionTextModifier(modifier: TextModifier | undefined): this
```

定制Select下拉菜单未选中项文本样式的方法，在应用optionTextModifier之后，下拉菜单未选中项的文本样式将完全由开发者自定义。

如果[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)与optionTextModifier的Font属性同时设置，则优先使用[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)设置下拉菜单未选中项的文本样式；[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)中缺省的属性将设置为对应的默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionTextModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default optionTextModifier(modifier: TextModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | 是 | 在Select组件上，定制Select下拉菜单未选中项样式的方法。取值为undefined时，则不使用此选项修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## optionWidth

```TypeScript
default optionWidth(value: Dimension | OptionWidthMode | undefined): this
```

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。与  
[optionWidth](../../../reference/apis-arkui/arkui-ts/ts-basic-components-select copy.md#optionwidth11)&lt;sup&gt;11+&lt;/sup&gt;相比，width参数新增了对undefined类型的支持。

当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default optionWidth(value: Dimension | OptionWidthMode | undefined): this--><!--Device-SelectAttribute-default optionWidth(value: Dimension | OptionWidthMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| OptionWidthMode \| undefined | 是 | 下拉菜单项的宽度。&lt;br/&gt;当width的值为undefined时，属性无效，菜单项宽度设为默认值，即2栅 格。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## selected

```TypeScript
default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this
```

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，默认选择值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。

该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this--><!--Device-SelectAttribute-default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numCount | int \| Resource \| undefined \| Bindable&lt;int&gt; \| Bindable&lt;Resource&gt; | 是 | 下拉菜单初始选项的索引。&lt;br/&gt;当numCount的 值为undefined时，选中第一项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## selectedOptionBgColor

```TypeScript
default selectedOptionBgColor(value: ResourceColor | undefined): this
```

设置下拉菜单选中项的背景色。与[selectedOptionBgColor](arkts-arkui-select-selectattribute-i.md#selectedoptionbgcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default selectedOptionBgColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default selectedOptionBgColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉菜单选中项的背景色。&lt;br/&gt;当resColor的值为undefined时，默认值： `\\$r('sys.color.ohos_id_color_component_activated')`混合`\\$r('sys.color.ohos_id_alpha_highlight_bg')`的透明度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedOptionFont

```TypeScript
default selectedOptionFont(value: Font | undefined): this
```

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。与[selectedOptionFont](arkts-arkui-select-selectattribute-i.md#selectedoptionfont)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default selectedOptionFont(value: Font | undefined): this--><!--Device-SelectAttribute-default selectedOptionFont(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | 下拉菜单选中项的文本样式。&lt;br/&gt;当value的值为undefined时，默认值：&lt;br/&gt;{&lt;br/&gt;size: \\$r(' sys.float.ohos_id_text_size_body1'),&lt;br/&gt;weight: FontWeight.Regular&lt;br/&gt;} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedOptionFontColor

```TypeScript
default selectedOptionFontColor(value: ResourceColor | undefined): this
```

设置下拉菜单选中项的文本颜色。与[selectedOptionFontColor](arkts-arkui-select-selectattribute-i.md#selectedoptionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default selectedOptionFontColor(value: ResourceColor | undefined): this--><!--Device-SelectAttribute-default selectedOptionFontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 下拉菜单选中项的文本颜色。&lt;br/&gt;当resColor的值为undefined时，默认值为\\$r(' sys.color.ohos_id_color_text_primary_activated')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedOptionTextModifier

```TypeScript
default selectedOptionTextModifier(modifier: TextModifier | undefined): this
```

定制Select下拉菜单选中项文本样式的方法，在应用selectedOptionTextModifier之后，下拉菜单选中项的文本样式将完全由开发者自定义。

如果[selectedOptionFont](arkts-arkui-select-selectattribute-i.md#selectedoptionfont)与selectedOptionTextModifier的Font属性同时设置，则优先使用  
[selectedOptionFont](arkts-arkui-select-selectattribute-i.md#selectedoptionfont)设置下拉菜单选中项的文本样式；若未设置[selectedOptionFont](arkts-arkui-select-selectattribute-i.md#selectedoptionfont)，则优先使用[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)设置下拉菜单选中项的文本样式。其中[selectedOptionFont](arkts-arkui-select-selectattribute-i.md#selectedoptionfont)或者  
[optionFont](arkts-arkui-select-selectattribute-i.md#optionfont)缺省的属性将设置为对应的默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default selectedOptionTextModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default selectedOptionTextModifier(modifier: TextModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | 是 | 设置下拉菜单项选中项的文本样式。&lt;br/&gt;开发者可以根据需要管理和维护文本的样式进行设置。取值为undefined时，则不使用选中项 文本修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## showDefaultSelectedIcon

```TypeScript
default showDefaultSelectedIcon(show:boolean | undefined): this
```

设置是否显示默认选择的图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default showDefaultSelectedIcon(show:boolean | undefined): this--><!--Device-SelectAttribute-default showDefaultSelectedIcon(show:boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean \| undefined | 是 | 是否显示默认选定的图标。取值为undefined时，按默认值处理。&lt;br&gt;默认值为false，true代表显示默认选择的图标，false代表不显示默认 选择的图标。&lt;br&gt;当show为true，并且通过selectedOptionBgColor设置选中项的背景色时，同时显示所设置的选中项的背景色和默认选定的图标；当show为true，但未通过 selectedOptionBgColor设置选中项的背景色时，不突出显示背景色，只显示默认选定的图标。false代表不显示默认选定的图标，通过突出显示背景色来表示选中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## showInSubWindow

```TypeScript
default showInSubWindow(showInSubWindow: boolean | undefined): this
```

设置下拉菜单是否显示在子窗中。未通过该接口设置时，下拉菜单默认不显示在子窗中。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default showInSubWindow(showInSubWindow: boolean | undefined): this--><!--Device-SelectAttribute-default showInSubWindow(showInSubWindow: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showInSubWindow | boolean \| undefined | 是 | 设置下拉菜单是否显示在子窗中。&lt;br&gt;true代表下拉菜单显示在子窗中。&lt;br&gt;false代表下拉菜单不显示在子窗中。&lt;br&gt;默 认值：2in1设备为true，其他设备为false。取值为undefined时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | The attribute of the select. |

## space

```TypeScript
default space(value: Length | undefined): this
```

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。设置为null、undefined，或者小于等于8的值，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default space(value: Length | undefined): this--><!--Device-SelectAttribute-default space(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 下拉菜单项的文本与箭头之间的间距。&lt;br/&gt;当value的值为undefined时，默认值：8 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## textModifier

```TypeScript
default textModifier(modifier: TextModifier | undefined): this
```

定制Select按钮文本样式的方法，在应用了textModifier之后，Select按钮的文本样式将完全由开发者自定义。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default textModifier(modifier: TextModifier | undefined): this--><!--Device-SelectAttribute-default textModifier(modifier: TextModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | TextModifier \| undefined | 是 | 在Select组件上，定制按钮文本样式的方法。取值为undefined时，则不使用文本修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

## value

```TypeScript
default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this
```

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。string和resource类型支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectAttribute-default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this--><!--Device-SelectAttribute-default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resStr | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined \| Bindable&lt;string&gt; \| Bindable&lt;Resource&gt; | 是 | 下拉按钮本身的文本内容。&lt;br/&gt;当resStr的值为 undefined时维持上次取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | the attribute of the select. |

