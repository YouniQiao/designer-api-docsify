# ClipOp

画布裁剪方式的枚举。

> **说明：**
> 
> 示意图展示了以INTERSECT方式裁剪一个矩形后，使用不同枚举值继续裁剪一个圆形的结果，绿色区域为最终的裁剪区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-enum ClipOp--><!--Device-drawing-enum ClipOp-End-->

**System capability:** SystemCapability.Graphics.Drawing

## DIFFERENCE

```TypeScript
DIFFERENCE = 0
```

将指定区域裁剪（取差集）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ClipOp-DIFFERENCE = 0--><!--Device-ClipOp-DIFFERENCE = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## INTERSECT

```TypeScript
INTERSECT = 1
```

将指定区域保留（取交集）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ClipOp-INTERSECT = 1--><!--Device-ClipOp-INTERSECT = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

