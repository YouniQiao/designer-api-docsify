# ColumnAttribute

The ColumnAttribute.@extends CommonMethod @interface ColumnAttribute

**继承/实现关系：** ColumnAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
default alignItems(value: HorizontalAlign | undefined): this
```

设置子组件在水平方向上的对齐格式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [HorizontalAlign](arkts-arkui-horizontalalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ColumnAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ColumnAttribute](arkts-arkui-column-columnattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |

## justifyContent

```TypeScript
default justifyContent(value: FlexAlign | undefined): this
```

设置子组件在垂直方向上的对齐格式。

> **说明：**&gt;
> Column布局时若子组件不设置
> flexShrink
> 则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴，
> 此时FlexAlign.Center和FlexAlign.End会失效。

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
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |

## reverse

```TypeScript
default reverse(isReversed: boolean | undefined): this
```

设置子组件在垂直方向上的排列是否反转。

> **说明：**&gt;
> 若未设置reverse属性，主轴方向不反转；若设置了reverse属性，且参数值为undefined，
> 则视为默认值true，主轴方向反转。<br>
> 通用属性direction只能改变Column交叉轴方向，不改变Column主轴方向，
> 因此与reverse属性互不影响。

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
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |

## setColumnOptions

```TypeScript
default setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this
```

Set Column options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |
