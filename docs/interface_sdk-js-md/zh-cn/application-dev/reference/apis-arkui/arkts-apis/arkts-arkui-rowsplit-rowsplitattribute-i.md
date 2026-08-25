# RowSplitAttribute

将子组件横向布局，并在每个子组件之间插入纵向分割线。RowSplit通过分割线限制子组件的宽度。初始化时，分割线位置根据子组件的宽度来计算。 初始化后，动态修改子组件的宽度不生效，分割线位置保持不变，可以通过拖动相邻分割线改变子组件宽度。初始化后，动态修改 margin、 border、 padding 通用属性导致子组件宽度大于相邻分割线间距的异常情况下，不支持拖动分割线改变子组件的宽度。RowSplit组件形状裁剪的默认值为true。@extends CommonMethod @interface RowSplitAttribute

**继承/实现关系：** RowSplitAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RowSplitAttribute> | AttributeModifier<CommonMethod>
        | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RowSplitAttribute](arkts-arkui-rowsplit-rowsplitattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowSplitAttribute](arkts-arkui-rowsplit-rowsplitattribute-i.md) |

## resizeable

```TypeScript
default resizeable(value: boolean | undefined): this
```

设置分割线是否可拖拽。

> 说明：&gt;
> RowSplit的分割线可以改变左右两边子组件的宽度，子组件可改变宽度的范围取决于子组件的最大最小宽度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowSplitAttribute](arkts-arkui-rowsplit-rowsplitattribute-i.md) |

## setRowSplitOptions

```TypeScript
default setRowSplitOptions(): this
```

Set RowSplit options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RowSplitAttribute](arkts-arkui-rowsplit-rowsplitattribute-i.md) |
