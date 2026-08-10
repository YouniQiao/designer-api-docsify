# PolylineAttribute

折线绘制组件属性。

**Inheritance/Implementation:** PolylineAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PolylineAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PolylineAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PolylineAttribute-default attributeModifier(modifier: AttributeModifier<PolylineAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;PolylineAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## points

```TypeScript
default points(value: Array<ShapePoint> | undefined): this
```

设置折线经过坐标点列表，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default points(value: Array<ShapePoint> | undefined): this--><!--Device-PolylineAttribute-default points(value: Array<ShapePoint> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;ShapePoint&gt; \| undefined | Yes | 折线经过坐标点列表。使用时传入一个二维数组，每个子数组表示一个顶点的[x, y]坐标。 &lt;br/&gt;默认值：[]（空数组）&lt;br/&gt;默认单位：vp &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setPolylineOptions

```TypeScript
default setPolylineOptions(options?: PolylineOptions): this
```

设置Polyline构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolylineAttribute-default setPolylineOptions(options?: PolylineOptions): this--><!--Device-PolylineAttribute-default setPolylineOptions(options?: PolylineOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](../arkts-components/arkts-arkui-polylineoptions-i.md) | No | Polyline绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回PolylineAttribute实例。 |

