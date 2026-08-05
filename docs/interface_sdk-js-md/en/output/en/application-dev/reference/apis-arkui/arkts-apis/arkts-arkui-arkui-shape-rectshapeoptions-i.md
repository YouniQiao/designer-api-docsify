# RectShapeOptions

Represents the parameter of the constructor used to create a **RectShape** object. This API inherits from [ShapeSize]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** RectShapeOptions extends [ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface RectShapeOptions extends ShapeSize--><!--Device-unnamed-interface RectShapeOptions extends ShapeSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: number | string | Array<number | string>
```

Radius of the rectangle border corners. When the parameter type is number, the valid value range is [0, +∞). When the parameter type is string, the value must conform to the [Length]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type specification. Unit: vp. If the value is invalid, 0 vp is used.

**Type:** number \| string \| Array&lt;number \| string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RectShapeOptions-radius?: number | string | Array<number | string>--><!--Device-RectShapeOptions-radius?: number | string | Array<number | string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

