# LineAttribute

直线绘制组件属性。

**Inheritance/Implementation:** LineAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;LineAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## endPoint

```TypeScript
default endPoint(value: ShapePoint | undefined): this
```

设置直线终点坐标点（相对坐标），支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | Yes | 直线终点坐标点（相对坐标），单位vp。&lt;br/&gt;默认值：[0,&nbsp;0] &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setLineOptions

```TypeScript
default setLineOptions(options?: LineOptions): this
```

设置Line构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this--><!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-line-lineoptions-i.md) | No | Line绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回LineAttribute实例。 |

## startPoint

```TypeScript
default startPoint(value: ShapePoint | undefined): this
```

设置直线起点坐标点（相对坐标），支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | Yes | 直线起点坐标点（相对坐标），单位vp。&lt;br/&gt;默认值：[0,&nbsp;0] &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

