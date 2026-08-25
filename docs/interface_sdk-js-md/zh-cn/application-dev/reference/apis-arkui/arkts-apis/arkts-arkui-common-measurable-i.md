# Measurable

Sub component info passed from framework when measure happens.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getBorderWidth

```TypeScript
getBorderWidth(): DirectionalEdgesT<double> | undefined
```

Obtains the border width of the child component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DirectionalEdgesT](arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined |

## getMargin

```TypeScript
getMargin(): DirectionalEdgesT<double> | undefined
```

Obtains the margin of the child component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DirectionalEdgesT](arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined |

## getPadding

```TypeScript
getPadding(): DirectionalEdgesT<double> | undefined
```

Obtains the padding of the child component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DirectionalEdgesT](arkts-arkui-directionaledgest-i.md)&lt;double&gt; \| undefined |

## measure

```TypeScript
measure(constraint: ConstraintSizeOptions | undefined): MeasureResult | undefined
```

Applies the size constraint to the child component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constraint | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MeasureResult](arkts-arkui-common-measureresult-i.md) \| undefined |

## uniqueId

```TypeScript
uniqueId?: int
```

Unique ID that the system assigns to the child component.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
