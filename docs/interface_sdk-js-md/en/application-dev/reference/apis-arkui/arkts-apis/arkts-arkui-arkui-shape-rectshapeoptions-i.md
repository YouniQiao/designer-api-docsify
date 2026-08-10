# RectShapeOptions

RectShape 的构造函数参数。

继承自[ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md)。

**Inheritance/Implementation:** RectShapeOptions extends [ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RectShapeOptions extends ShapeSize--><!--Device-unnamed-export interface RectShapeOptions extends ShapeSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## radius

```TypeScript
radius?: double | string | Array<double | string>
```

矩形形状的圆角半径。

类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md)。

单位：vp

取值为异常值时按照0vp处理。

**Type:** double \| string \| Array&lt;double \| string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShapeOptions-radius?: double | string | Array<double | string>--><!--Device-RectShapeOptions-radius?: double | string | Array<double | string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

