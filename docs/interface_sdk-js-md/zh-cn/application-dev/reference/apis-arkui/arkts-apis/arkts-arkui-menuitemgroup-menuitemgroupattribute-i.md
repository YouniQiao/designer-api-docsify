# MenuItemGroupAttribute

不支持[通用属性](common)。

**继承/实现关系：** MenuItemGroupAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface MenuItemGroupAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuItemGroupAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置MenuItemGroup组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MenuItemGroupAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemGroupAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuItemGroupAttribute](arkts-arkui-menuitemgroup-menuitemgroupattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | MenuItemGroup组件的属性修改器。&lt;br/&gt;CommonMethod：[通用属性](common) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

