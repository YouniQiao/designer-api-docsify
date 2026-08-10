# CircleAttribute

圆形绘制组件属性。

**继承/实现关系：** CircleAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;CircleAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fill

```TypeScript
default fill(value: ResourceColor | ColorMetrics | undefined): this
```

设置填充区域的颜色，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this--><!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColorMetrics \| undefined | 是 | 填充区域颜色。&lt;br/&gt;默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black &lt;br/&gt;异常值undefined、null、NaN和Infinity按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setCircleOptions

```TypeScript
default setCircleOptions(options?: CircleOptions): this
```

设置Circle构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this--><!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CircleOptions](../arkts-components/arkts-arkui-circleoptions-i.md) | 否 | Circle构造参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回CircleAttribute实例。 |

## stroke

```TypeScript
default stroke(value: ResourceColor | ColorMetrics| undefined): this
```

设置边框颜色，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this--><!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColorMetrics \| undefined | 是 | 边框颜色。&lt;br/&gt;默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Transparent&lt;br/&gt;异常值undefined和null按照默认值处理， NaN和Infinity按照[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

