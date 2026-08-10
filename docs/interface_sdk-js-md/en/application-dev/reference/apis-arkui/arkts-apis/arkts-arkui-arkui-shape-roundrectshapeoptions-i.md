# RoundRectShapeOptions

RectShape 带有半径的构造函数参数。

继承自[ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md)。

**Inheritance/Implementation:** RoundRectShapeOptions extends [ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RoundRectShapeOptions extends ShapeSize--><!--Device-unnamed-export interface RoundRectShapeOptions extends ShapeSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## radiusHeight

```TypeScript
radiusHeight?: double | string
```

矩形形状圆角半径的高度。

类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md)。

单位：vp

取值为异常值时按照0vp处理。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RoundRectShapeOptions-radiusHeight?: double | string--><!--Device-RoundRectShapeOptions-radiusHeight?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radiusWidth

```TypeScript
radiusWidth?: double | string
```

矩形形状圆角半径的宽度。

类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md)。

单位：vp

取值为异常值时按照0vp处理。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RoundRectShapeOptions-radiusWidth?: double | string--><!--Device-RoundRectShapeOptions-radiusWidth?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

