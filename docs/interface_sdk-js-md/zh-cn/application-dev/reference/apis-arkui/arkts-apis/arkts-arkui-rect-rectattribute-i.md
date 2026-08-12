# RectAttribute

矩形绘制组件。

**继承/实现关系：** RectAttribute extends [CommonShapeMethod](CommonShapeMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface RectAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface RectAttribute extends CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RectAttribute-default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RectAttribute-default attributeModifier(modifier: AttributeModifier<RectAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RectAttribute](arkts-arkui-rect-rectattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## radius

```TypeScript
default radius(value: Length | Array<RadiusItem> | undefined): this
```

设置圆角半径大小，取值范围≥0，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RectAttribute-default radius(value: Length | Array<RadiusItem> | undefined): this--><!--Device-RectAttribute-default radius(value: Length | Array<RadiusItem> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| Array&lt;[RadiusItem](arkts-arkui-radiusitem-t.md)&gt; \| undefined | 是 | 圆角半径大小。 默认值：0 默认单位：vp 异常值undefined和null按照[[0, 0], [0, 0], [0, 0], [0, 0]]处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## radiusHeight

```TypeScript
default radiusHeight(value: Length | undefined): this
```

设置圆角的高度，仅设置高时宽高一致，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RectAttribute-default radiusHeight(value: Length | undefined): this--><!--Device-RectAttribute-default radiusHeight(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 圆角的高度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## radiusWidth

```TypeScript
default radiusWidth(value: Length | undefined): this
```

设置圆角的宽度，仅设置宽时宽高一致，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RectAttribute-default radiusWidth(value: Length | undefined): this--><!--Device-RectAttribute-default radiusWidth(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 圆角的宽度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setRectOptions

```TypeScript
default setRectOptions(options?: RectOptions | RoundedRectOptions): this
```

Set Rect options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RectAttribute-default setRectOptions(options?: RectOptions | RoundedRectOptions): this--><!--Device-RectAttribute-default setRectOptions(options?: RectOptions | RoundedRectOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-rect-roundedrectoptions-i.md) | 否 | Rect constructor options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the RectAttribute. |

