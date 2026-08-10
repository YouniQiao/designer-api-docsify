# CircleAttribute

圆形绘制组件属性。

**Inheritance/Implementation:** CircleAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;CircleAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fill

```TypeScript
default fill(value: ResourceColor | ColorMetrics | undefined): this
```

设置填充区域的颜色，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this--><!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColorMetrics \| undefined | Yes | 填充区域颜色。&lt;br/&gt;默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black &lt;br/&gt;异常值undefined、null、NaN和Infinity按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setCircleOptions

```TypeScript
default setCircleOptions(options?: CircleOptions): this
```

设置Circle构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this--><!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CircleOptions](../arkts-components/arkts-arkui-circleoptions-i.md) | No | Circle构造参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回CircleAttribute实例。 |

## stroke

```TypeScript
default stroke(value: ResourceColor | ColorMetrics| undefined): this
```

设置边框颜色，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this--><!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColorMetrics \| undefined | Yes | 边框颜色。&lt;br/&gt;默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Transparent&lt;br/&gt;异常值undefined和null按照默认值处理， NaN和Infinity按照[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

