# MenuItemAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**继承/实现关系：** MenuItemAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置MenuItem组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;MenuItemAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | MenuItem 组件的属性修改器。取值为undefined时，则不使用属性修改器。&lt;br/&gt;CommonMethod：[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentFont

```TypeScript
default contentFont(value: Font | undefined): this
```

设置菜单项中内容信息的字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | 菜单项中内容信息的字体样式。取值为undefined时，按各属性的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentFontColor

```TypeScript
default contentFontColor(value: ResourceColor | undefined): this
```

设置菜单项中内容信息的字体颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 菜单项中内容信息的字体颜色。取值为undefined时，按默认值处理。&lt;br /&gt;默认值：'#E5000000' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## labelFont

```TypeScript
default labelFont(value: Font | undefined): this
```

设置菜单项中标签信息的字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 | 菜单项中标签信息的字体样式。取值为undefined时，按各属性的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## labelFontColor

```TypeScript
default labelFontColor(value: ResourceColor | undefined): this
```

设置菜单项中标签信息的字体颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 菜单项中标签信息的字体颜色。取值为undefined时，按默认值处理。&lt;br /&gt;默认值：'#99000000' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((selected: boolean) => void) | undefined): this
```

当选中状态发生变化时，触发该回调。只有手动触发且MenuItem状态改变时才会触发onChange回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this--><!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((selected: boolean) =&gt; void) \| undefined | 是 | 选中状态发生变化时，触发该回调。&lt;br /&gt;true：未选中切换为选中；false：选中切换为未选 中。&lt;br/&gt;ArkTS-Sta：当callback的值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectIcon

```TypeScript
default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this
```

设置当菜单项被选中时，是否显示被选中的图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this--><!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| ResourceStr \| SymbolGlyphModifier \| undefined | 是 | 菜单项被选中时，是否显示被选中的图标。取值为undefined时，按默认值处 理。&lt;br/&gt;true：显示默认的对勾图标；false：不显示图标。&lt;br/&gt;ResourceStr：显示指定的图标。&lt;br/&gt;SymbolGlyphModifier：显示指定的HMSymbol图标。&lt;br/&gt;默认值： false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selected

```TypeScript
default selected(value: boolean | undefined | Bindable<boolean>): this
```

设置菜单项是否选中。

从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该参数支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this--><!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined \| Bindable&lt;boolean&gt; | 是 | 菜单项是否选中。取值为undefined时，按默认值处理。&lt;br/&gt;true：菜单项被选中；false：菜单 项不被选中。&lt;br /&gt;默认值：false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

