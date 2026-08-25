# RowAttribute

沿水平方向布局的容器。@extends CommonMethod @interface RowAttribute

**继承/实现关系：** RowAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
default alignItems(value: VerticalAlign | undefined): this
```

设置子组件在垂直方向上的对齐格式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [VerticalAlign](arkts-arkui-verticalalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](arkts-arkui-row-rowattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RowAttribute> | AttributeModifier<CommonMethod>
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
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RowAttribute](arkts-arkui-row-rowattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](arkts-arkui-row-rowattribute-i.md) |

## justifyContent

```TypeScript
default justifyContent(value: FlexAlign | undefined): this
```

设置子组件在水平方向上的对齐格式。

> 说明：&gt;
> Row布局时若子组件不设置
> flexShrink
> 则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴，此时FlexAlign.Center和FlexAlign.End会失效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FlexAlign](arkts-arkui-flexalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](arkts-arkui-row-rowattribute-i.md) |

## reverse

```TypeScript
default reverse(isReversed: boolean | undefined): this
```

设置子组件在水平方向上的排列是否反转。

> 说明：&gt;
> 若未设置reverse属性，主轴方向不反转；若设置了reverse属性，且参数值为undefined，
> 则视为默认值true，主轴方向反转。
> 由于主轴排列方向受通用属性direction影响，若设置了direction属性，
> 则当reverse属性设置为true时，总在direction属性生效的结果上再做一次反转。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isReversed | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](arkts-arkui-row-rowattribute-i.md) |

## setRowOptions

```TypeScript
default setRowOptions(options?: RowOptions | RowOptionsV2): this
```

Set Row options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](arkts-arkui-row-rowattribute-i.md) |
