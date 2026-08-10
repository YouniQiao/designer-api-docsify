# MotionPathOptions

设置组件的运动路径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MotionPathOptions--><!--Device-unnamed-export declare interface MotionPathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from?: double
```

运动路径的起点。

默认值：0.0

取值范围：[0.0, 1.0]

设置小于0.0或大于1.0的值时，按默认值0.0处理。

**Type:** double

**Default:** 0.0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-from?: double--><!--Device-MotionPathOptions-from?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

位移动画的运动路径，使用[SVG路径描述规范](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-path.md#svg路径描述规范)。path中支持使用start和end进行起点和终点的替代，如：'Mstart.x start.y L50 50 Lend.x end.y Z'，更多说明请参考  
[绘制路径](../../../ui/ui-js-components-svg-path.md)。

设置为空字符串时相当于不设置路径动画。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-path: string--><!--Device-MotionPathOptions-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotatable

```TypeScript
rotatable?: boolean
```

是否跟随路径进行旋转。true代表跟随路径进行旋转，false代表不跟随路径进行旋转。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-rotatable?: boolean--><!--Device-MotionPathOptions-rotatable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to?: double
```

运动路径的终点。

默认值：1.0

取值范围：[0.0, 1.0]

设置小于0.0或大于1.0的值时，按默认值1.0处理，且满足to值 >= 异常值处理后的from值。

**Type:** double

**Default:** 1.0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-to?: double--><!--Device-MotionPathOptions-to?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

