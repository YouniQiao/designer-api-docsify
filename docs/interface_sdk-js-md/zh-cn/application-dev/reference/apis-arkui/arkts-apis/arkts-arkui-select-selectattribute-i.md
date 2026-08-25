# SelectAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** SelectAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## arrowModifier

```TypeScript
default arrowModifier(modifier: SymbolGlyphModifier | undefined): this
```

定制Select按钮下拉箭头图标样式的方法，在应用arrowModifier之后，Select按钮下拉箭头的图标样式将完全由开发者自定义。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## arrowPosition

```TypeScript
default arrowPosition(value: ArrowPosition | undefined): this
```

设置下拉菜单项的文本与箭头之间的对齐方式。与[arrowPosition](arkts-arkui-select-arrowposition-e.md)相比，position参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ArrowPosition](arkts-arkui-select-arrowposition-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<SelectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Select组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SelectAttribute](arkts-arkui-select-selectattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## avoidance

```TypeScript
default avoidance(mode: AvoidanceMode | undefined): this
```

设置下拉菜单的避让模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AvoidanceMode](arkts-arkui-select-avoidancemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## controlSize

```TypeScript
default controlSize(value: ControlSize | undefined): this
```

设置Select组件的尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ControlSize](../arkts-components/arkts-arkui-controlsize-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## divider

```TypeScript
default divider(options: DividerOptions | null | undefined): this
```

设置分割线样式，不设置该属性则按"默认值"展示分割线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DividerOptions](arkts-arkui-textpicker-divideroptions-i.md) \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## dividerStyle

```TypeScript
default dividerStyle(style: DividerStyleOptions | undefined): this
```

设置分割线样式，不设置该属性则按"默认值"展示分割线。该属性与divider互斥，按调用顺序生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## font

```TypeScript
default font(value: Font | undefined): this
```

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。与[font](#font)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置下拉按钮本身的文本颜色。与[fontColor](#fontcolor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## keyboardAvoidMode

```TypeScript
default keyboardAvoidMode(mode: MenuKeyboardAvoidMode | undefined): this
```

设置Select菜单避让键盘的模式。默认不避让。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [MenuKeyboardAvoidMode](../arkts-components/arkts-arkui-menukeyboardavoidmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuAlign

```TypeScript
default menuAlign(alignType: MenuAlignType | undefined, offset?: Offset | undefined): this
```

设置下拉按钮与下拉菜单间的对齐方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [alignType](arkts-arkui-atomicservice-atomicservicesearch-menualignparams-i.md) | [MenuAlignType](arkts-arkui-select-menualigntype-e.md) \| undefined | 是 |
| offset | Offset \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuBackgroundBlurStyle

```TypeScript
default menuBackgroundBlurStyle(value: BlurStyle | undefined): this
```

设置下拉菜单的背景模糊材质。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuBackgroundBlurStyleOptions

```TypeScript
default menuBackgroundBlurStyleOptions(blurStyle: BackgroundBlurStyleOptions | undefined): this
```

设置Select组件的背景模糊效果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurStyle | [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuBackgroundColor

```TypeScript
default menuBackgroundColor(value: ResourceColor | undefined): this
```

设置下拉菜单的背景色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuBackgroundEffect

```TypeScript
default menuBackgroundEffect(effect: BackgroundEffectOptions | undefined): this
```

设置Select组件的背景属性。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuItemContentModifier

```TypeScript
default menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration> | undefined): this
```

定制Select下拉菜单项内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[MenuItemConfiguration](arkts-arkui-select-menuitemconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## menuOutline

```TypeScript
default menuOutline(outline: MenuOutlineOptions | undefined): this
```

设置下拉菜单框的外描边样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outline | [MenuOutlineOptions](arkts-arkui-select-menuoutlineoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## minKeyboardAvoidDistance

```TypeScript
default minKeyboardAvoidDistance(distance: LengthMetrics | undefined): this
```

设置Select菜单与键盘之间的最小距离。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distance | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## onSelect

```TypeScript
default onSelect(callback: OnSelectCallback | undefined): this
```

下拉菜单选中某一项时，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnSelectCallback](arkts-arkui-onselectcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionBgColor

```TypeScript
default optionBgColor(value: ResourceColor | undefined): this
```

设置下拉菜单项的背景色。与[optionBgColor](#optionbgcolor)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionFont

```TypeScript
default optionFont(value: Font | undefined): this
```

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。与[optionFont](#optionfont)相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionFontColor

```TypeScript
default optionFontColor(value: ResourceColor | undefined): this
```

设置下拉菜单项的文本颜色。与[optionFontColor](#optionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionHeight

```TypeScript
default optionHeight(value: Dimension | undefined): this
```

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。当设置为异常值或零时，属性不生效。如果下拉菜单所有选项的实际高度小于设定的高度，下拉菜单的高度按实际高度显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionTextModifier

```TypeScript
default optionTextModifier(modifier: TextModifier | undefined): this
```

定制Select下拉菜单未选中项文本样式的方法，在应用optionTextModifier之后，下拉菜单未选中项的文本样式将完全由开发者自定义。如果[optionFont](#optionfont)与optionTextModifier的Font属性同时设置，则优先使用[optionFont](#optionfont)设置下拉菜单未选中项的文本样 式；[optionFont](#optionfont)中缺省的属性将设置为对应的默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [TextModifier](arkts-arkui-textmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## optionWidth

```TypeScript
default optionWidth(value: Dimension | OptionWidthMode | undefined): this
```

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Dimension](arkts-arkui-dimension-t.md) \| [OptionWidthMode](arkts-arkui-optionwidthmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## selected

```TypeScript
default selected(numCount: int | Resource | undefined | Bindable<int> | Bindable<Resource>): this
```

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，默认选择值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。该属性支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numCount | int \| [Resource](arkts-arkui-resource-t.md) \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;int&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Resource](arkts-arkui-resource-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## selectedOptionBgColor

```TypeScript
default selectedOptionBgColor(value: ResourceColor | undefined): this
```

设置下拉菜单选中项的背景色。与[selectedOptionBgColor](#selectedoptionbgcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## selectedOptionFont

```TypeScript
default selectedOptionFont(value: Font | undefined): this
```

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。与[selectedOptionFont](#selectedoptionfont)相比， value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## selectedOptionFontColor

```TypeScript
default selectedOptionFontColor(value: ResourceColor | undefined): this
```

设置下拉菜单选中项的文本颜色。与[selectedOptionFontColor](#selectedoptionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## selectedOptionTextModifier

```TypeScript
default selectedOptionTextModifier(modifier: TextModifier | undefined): this
```

定制Select下拉菜单选中项文本样式的方法，在应用selectedOptionTextModifier之后，下拉菜单选中项的文本样式将完全由开发者自定义。如果[selectedOptionFont](#selectedoptionfont)与selectedOptionTextModifier的Font属性同时设置，则优先使用 [selectedOptionFont](#selectedoptionfont)设置下拉菜单选中项的文本样式；若未设置[selectedOptionFont](#selectedoptionfont)，则 优先使用[optionFont](#optionfont)设置下拉菜单选中项的文本样式。其中[selectedOptionFont](#selectedoptionfont)或者 [optionFont](#optionfont)缺省的属性将设置为对应的默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [TextModifier](arkts-arkui-textmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## showDefaultSelectedIcon

```TypeScript
default showDefaultSelectedIcon(show:boolean | undefined): this
```

设置是否显示默认选择的图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| show | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## showInSubWindow

```TypeScript
default showInSubWindow(showInSubWindow: boolean | undefined): this
```

设置下拉菜单是否显示在子窗中。未通过该接口设置时，下拉菜单默认不显示在子窗中。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [showInSubWindow](#showinsubwindow) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## space

```TypeScript
default space(value: Length | undefined): this
```

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。设置为null、undefined，或者小于等于8的值，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## textModifier

```TypeScript
default textModifier(modifier: TextModifier | undefined): this
```

定制Select按钮文本样式的方法，在应用了textModifier之后，Select按钮的文本样式将完全由开发者自定义。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [TextModifier](arkts-arkui-textmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |

## value

```TypeScript
default value(resStr: ResourceStr | undefined | Bindable<string> | Bindable<Resource>): this
```

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。string和resource类型支持Bindable双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resStr | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;string&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Resource](arkts-arkui-resource-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SelectAttribute](arkts-arkui-select-selectattribute-i.md) |
