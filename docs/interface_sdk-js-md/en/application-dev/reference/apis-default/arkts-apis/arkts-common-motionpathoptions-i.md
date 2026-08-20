# MotionPathOptions

Defines the motion path options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface MotionPathOptions--><!--Device-unnamed-export declare interface MotionPathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from?: double
```

Start point of the motion path. Value range: [0, 1]. A value less than 0 or greater than 1 evaluates to the default value **0**.

**Type:** double

**Default:** 0.0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-from?: double--><!--Device-MotionPathOptions-from?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

Motion path of the translation animation. The **svg** path string is used. In the value, **start** and **end** can be used in place of the start point and end point, for example, **'Mstart.x start.y L50 50 Lend.x end.y Z'**. If this parameter is set to an empty string, the path animation is not set.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-path: string--><!--Device-MotionPathOptions-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotatable

```TypeScript
rotatable?: boolean
```

Whether to rotate along the path.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-rotatable?: boolean--><!--Device-MotionPathOptions-rotatable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to?: double
```

End point of the motion path. Value range: [0, 1]. A value less than 0 or greater than 1 evaluates to the default value **1**, provided that the value of **to** is greater than or equal to the value of **from**.

**Type:** double

**Default:** 1.0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MotionPathOptions-to?: double--><!--Device-MotionPathOptions-to?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

