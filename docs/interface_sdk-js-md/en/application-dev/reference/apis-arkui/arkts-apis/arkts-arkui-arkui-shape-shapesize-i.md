# ShapeSize

形状的尺寸参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ShapeSize--><!--Device-unnamed-export interface ShapeSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## height

```TypeScript
height?: double | string
```

形状的高度。 

类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md)。 

单位：vp

取值为异常值时按照0vp处理。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeSize-height?: double | string--><!--Device-ShapeSize-height?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: double | string
```

形状的宽度。

类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md)。 

单位：vp

取值为异常值时按照0vp处理。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeSize-width?: double | string--><!--Device-ShapeSize-width?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

