# RoundRectShapeOptions

Represents the parameter of the constructor used to create a **RectShape** object with rounded corners. This API inherits from [ShapeSize](../../apis-na/arkts-apis/arkts-na-arkui-shape-shapesize-i.md#ShapeSize).

**Inheritance/Implementation:** RoundRectShapeOptions extends [ShapeSize](../../apis-na/arkts-apis/arkts-na-arkui-shape-shapesize-i.md#ShapeSize)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-interface RoundRectShapeOptions--><!--Device-unnamed-interface RoundRectShapeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape } from 'RectShape';
import { CircleShape } from 'CircleShape';
import { EllipseShape } from 'EllipseShape';
import { PathShape } from 'PathShape';
```

## radiusHeight

```TypeScript
radiusHeight?: number | string
```

Radius height of the rectangle border corners. When the parameter type is number, the valid value range is 0, +∞). When the parameter type is string, the value must conform to the [Length type specification. Unit: vp. If the value is invalid, 0 vp is used.

**Type:** number \| string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RoundRectShapeOptions-radiusHeight?: number | string--><!--Device-RoundRectShapeOptions-radiusHeight?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radiusWidth

```TypeScript
radiusWidth?: number | string
```

Radius width of the rectangle border corners. When the parameter type is number, the valid value range is 0, +∞). When the parameter type is string, the value must conform to the [Length type specification. Unit: vp. If the value is invalid, 0 vp is used.

**Type:** number \| string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RoundRectShapeOptions-radiusWidth?: number | string--><!--Device-RoundRectShapeOptions-radiusWidth?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

