# CircleAttribute

Circle drawing component attribute functions.

**Inheritance/Implementation:** CircleAttribute extends [CommonShapeMethod](CommonShapeMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface CircleAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CircleAttribute-default attributeModifier(modifier: AttributeModifier<CircleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CircleAttribute](arkts-arkui-circle-circleattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fill

```TypeScript
default fill(value: ResourceColor | ColorMetrics | undefined): this
```

Sets the color of the fill area.An invalid value is handled as the default value.If this attribute and the universal attribute foregroundColor are both set, whichever is set later takes effect.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this--><!--Device-CircleAttribute-default fill(value: ResourceColor | ColorMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes | Color of the fill area. Default value: Color.Black. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setCircleOptions

```TypeScript
default setCircleOptions(options?: CircleOptions): this
```

Set Circle options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this--><!--Device-CircleAttribute-default setCircleOptions(options?: CircleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CircleOptions](arkts-arkui-circle-circleoptions-i.md) | No | Circle constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the CircleAttribute. |

## stroke

```TypeScript
default stroke(value: ResourceColor | ColorMetrics| undefined): this
```

Sets the stroke color.If this attribute is not set, the component does not have any stroke.If the value is invalid, no stroke will be drawn.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this--><!--Device-CircleAttribute-default stroke(value: ResourceColor | ColorMetrics| undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes | Stroke color. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

