# EllipseAttribute

Provides attribute for Ellipse.

**Inheritance/Implementation:** EllipseAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EllipseAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface EllipseAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<EllipseAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EllipseAttribute-default attributeModifier(modifier: AttributeModifier<EllipseAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-EllipseAttribute-default attributeModifier(modifier: AttributeModifier<EllipseAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;EllipseAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setEllipseOptions

```TypeScript
default setEllipseOptions(options?: EllipseOptions): this
```

Set Ellipse options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EllipseAttribute-default setEllipseOptions(options?: EllipseOptions): this--><!--Device-EllipseAttribute-default setEllipseOptions(options?: EllipseOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](../arkts-components/arkts-arkui-ellipseoptions-i.md) | No | Ellipse constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the EllipseAttribute. |

