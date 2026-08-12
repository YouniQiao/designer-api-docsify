# PolylineAttribute

Defines Polyline attribute

**Inheritance/Implementation:** PolylineAttribute extends [CommonShapeMethod](CommonShapeMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PolylineAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PolylineAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PolylineAttribute-default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PolylineAttribute](arkts-arkui-polyline-polylineattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## points

```TypeScript
default points(value: Array<ShapePoint> | undefined): this
```

Called when the polyline is set to pass through the coordinate point list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default points(value: Array<ShapePoint> | undefined): this--><!--Device-PolylineAttribute-default points(value: Array<ShapePoint> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ShapePoint](arkts-arkui-shapepoint-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setPolylineOptions

```TypeScript
default setPolylineOptions(options?: PolylineOptions): this
```

Set Polyline options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default setPolylineOptions(options?: PolylineOptions): this--><!--Device-PolylineAttribute-default setPolylineOptions(options?: PolylineOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polyline-polylineoptions-i.md) | No | Polyline constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the PolylineAttribute. |

