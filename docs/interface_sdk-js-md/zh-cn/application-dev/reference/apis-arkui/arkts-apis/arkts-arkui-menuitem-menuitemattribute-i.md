# MenuItemAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** MenuItemAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置MenuItem组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## contentFont

```TypeScript
default contentFont(value: Font | undefined): this
```

设置菜单项中内容信息的字体样式。

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
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## contentFontColor

```TypeScript
default contentFontColor(value: ResourceColor | undefined): this
```

设置菜单项中内容信息的字体颜色。

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
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## labelFont

```TypeScript
default labelFont(value: Font | undefined): this
```

设置菜单项中标签信息的字体样式。

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
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## labelFontColor

```TypeScript
default labelFontColor(value: ResourceColor | undefined): this
```

设置菜单项中标签信息的字体颜色。

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
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: ((selected: boolean) => void) | undefined): this
```

当选中状态发生变化时，触发该回调。只有手动触发且MenuItem状态改变时才会触发onChange回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((selected: boolean) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## selected

```TypeScript
default selected(value: boolean | undefined | Bindable<boolean>): this
```

设置菜单项是否选中。从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。从API version 18开始，该参数支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |

## selectIcon

```TypeScript
default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this
```

设置当菜单项被选中时，是否显示被选中的图标。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |
