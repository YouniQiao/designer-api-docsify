# MenuItemAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**Inheritance/Implementation:** MenuItemAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置MenuItem组件的属性修改器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | MenuItem 组件的属性修改器。取值为undefined时，则不使用属性修改器。&lt;br/&gt;CommonMethod：[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentFont

```TypeScript
default contentFont(value: Font | undefined): this
```

设置菜单项中内容信息的字体样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes | 菜单项中内容信息的字体样式。取值为undefined时，按各属性的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentFontColor

```TypeScript
default contentFontColor(value: ResourceColor | undefined): this
```

设置菜单项中内容信息的字体颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 菜单项中内容信息的字体颜色。取值为undefined时，按默认值处理。&lt;br /&gt;默认值：'#E5000000' |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## labelFont

```TypeScript
default labelFont(value: Font | undefined): this
```

设置菜单项中标签信息的字体样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes | 菜单项中标签信息的字体样式。取值为undefined时，按各属性的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## labelFontColor

```TypeScript
default labelFontColor(value: ResourceColor | undefined): this
```

设置菜单项中标签信息的字体颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 菜单项中标签信息的字体颜色。取值为undefined时，按默认值处理。&lt;br /&gt;默认值：'#99000000' |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((selected: boolean) => void) | undefined): this
```

当选中状态发生变化时，触发该回调。只有手动触发且MenuItem状态改变时才会触发onChange回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this--><!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((selected: boolean) =&gt; void) \| undefined | Yes | 选中状态发生变化时，触发该回调。&lt;br /&gt;true：未选中切换为选中；false：选中切换为未选 中。&lt;br/&gt;ArkTS-Sta：当callback的值为undefined时，不使用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectIcon

```TypeScript
default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this
```

设置当菜单项被选中时，是否显示被选中的图标。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this--><!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| ResourceStr \| SymbolGlyphModifier \| undefined | Yes | 菜单项被选中时，是否显示被选中的图标。取值为undefined时，按默认值处 理。&lt;br/&gt;true：显示默认的对勾图标；false：不显示图标。&lt;br/&gt;ResourceStr：显示指定的图标。&lt;br/&gt;SymbolGlyphModifier：显示指定的HMSymbol图标。&lt;br/&gt;默认值： false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selected

```TypeScript
default selected(value: boolean | undefined | Bindable<boolean>): this
```

设置菜单项是否选中。

从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该参数支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this--><!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined \| Bindable&lt;boolean&gt; | Yes | 菜单项是否选中。取值为undefined时，按默认值处理。&lt;br/&gt;true：菜单项被选中；false：菜单 项不被选中。&lt;br /&gt;默认值：false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

