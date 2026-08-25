# CommonShapeMethod

CommonShapeMethod@extends CommonMethod

**继承/实现关系：** CommonShapeMethod extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## allowForceDark

```TypeScript
default allowForceDark(value: boolean): this
```

Set whether the component enables the ability to invert colors. This interface needs to be set as the first attribute of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## antiAlias

```TypeScript
default antiAlias(value: boolean | undefined): this
```

Specifies whether anti-aliasing is enabled.

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
| this |

## fill

```TypeScript
default fill(value: ResourceColor | undefined): this
```

Sets the color of the fill area. An invalid value is handled as the default value. If this attribute and the universal attribute foregroundColor are both set, whichever is set later takes effect.

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
| this |

## fillOpacity

```TypeScript
default fillOpacity(value: double | string | Resource | undefined): this
```

Sets the opacity of the fill area. The value range is [0.0, 1.0]. A value less than 0.0 evaluates to the value 0.0. A value greater than 1.0 evaluates to the value 1.0. Any other value evaluates to the value 1.0.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## stroke

```TypeScript
default stroke(value: ResourceColor | undefined): this
```

Sets the stroke color. If this attribute is not set, the component does not have any stroke. If the value is invalid, no stroke will be drawn.

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
| this |

## strokeDashArray

```TypeScript
default strokeDashArray(value: Array<Length> | undefined): this
```

Sets the gap for the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeDashOffset

```TypeScript
default strokeDashOffset(value: double | string | undefined): this
```

Sets the offset of the start point for drawing the stroke. An invalid value is handled as the default value.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeLineCap

```TypeScript
default strokeLineCap(value: LineCapStyle | undefined): this
```

Sets the cap style of the stroke.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineCapStyle](arkts-arkui-linecapstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeLineJoin

```TypeScript
default strokeLineJoin(value: LineJoinStyle | undefined): this
```

Sets the join style of the stroke. This attribute does not work for the Circle component, which does not have corners.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineJoinStyle](arkts-arkui-linejoinstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeMiterLimit

```TypeScript
default strokeMiterLimit(value: double | string | undefined): this
```

Limits for drawing acute angles as bevels

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeOpacity

```TypeScript
default strokeOpacity(value: double | string | Resource | undefined): this
```

Sets the stroke opacity. The value range is [0.0, 1.0]. A value less than 0.0 evaluates to the value 0.0. A value greater than 1.0 evaluates to the value 1.0. Any other value evaluates to the value 1.0.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## strokeWidth

```TypeScript
default strokeWidth(value: Length | undefined): this
```

Sets the stroke width. If this attribute is of the string type, percentage values are not supported and will be treated as 1 px.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
