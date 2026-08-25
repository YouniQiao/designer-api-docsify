# ListItemGroupAttribute

The ListItemGroupAttribute.

**继承/实现关系：** ListItemGroupAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ListItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置ListItemGroup组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ListItemGroupAttribute](arkts-arkui-listitemgroup-listitemgroupattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## childrenMainSize

```TypeScript
default childrenMainSize(value: ChildrenMainSize | undefined): this
```

设置ListItemGroup组件的子组件在主轴方向的大小信息。

> **说明：**&gt;
> - 必须同时给所在的List组件设置childrenMainSize属性才可以正常生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ChildrenMainSize](../arkts-components/arkts-arkui-childrenmainsize-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## divider

```TypeScript
default divider(value: ListDividerOptions | null | undefined): this
```

设置ListItem分割线样式，默认无分割线。strokeWidth，startMargin和endMargin不支持设置百分比。ListItem设置多态样式时，被按压的子组件上下的分割线不绘制。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ListDividerOptions](../arkts-components/arkts-arkui-listdivideroptions-i.md) \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setListItemGroupOptions

```TypeScript
default setListItemGroupOptions(options?: ListItemGroupOptions): this
```

设置ListItemGroup选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ListItemGroupOptions](arkts-arkui-listitemgroup-listitemgroupoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ListItemGroupAttribute](arkts-arkui-listitemgroup-listitemgroupattribute-i.md) |
