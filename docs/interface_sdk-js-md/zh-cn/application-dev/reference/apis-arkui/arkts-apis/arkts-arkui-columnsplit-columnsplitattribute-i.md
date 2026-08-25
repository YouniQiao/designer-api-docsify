# ColumnSplitAttribute

The ColumnSplitAttribute.@extends CommonMethod @interface ColumnSplitAttribute

**继承/实现关系：** ColumnSplitAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ColumnSplitAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ColumnSplitAttribute](arkts-arkui-columnsplit-columnsplitattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ColumnSplitAttribute](arkts-arkui-columnsplit-columnsplitattribute-i.md) |

## divider

```TypeScript
default divider(value: ColumnSplitDividerStyle | null | undefined): this
```

设置分割线的margin。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ColumnSplitDividerStyle](arkts-arkui-columnsplit-columnsplitdividerstyle-i.md) \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ColumnSplitAttribute](arkts-arkui-columnsplit-columnsplitattribute-i.md) |

## resizeable

```TypeScript
default resizeable(value: boolean | undefined): this
```

设置分割线是否可拖拽。

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
| [ColumnSplitAttribute](arkts-arkui-columnsplit-columnsplitattribute-i.md) |

## setColumnSplitOptions

```TypeScript
default setColumnSplitOptions(): this
```

Set ColumnSplit options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ColumnSplitAttribute](arkts-arkui-columnsplit-columnsplitattribute-i.md) |
