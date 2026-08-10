# CanvasLineJoin

```TypeScript
declare type CanvasLineJoin = "bevel" | "miter" | "round"
```

定义长度不为0的两个连接部分（线段、圆弧和曲线）的类型。取值类型为下表类型中的并集。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-declare type CanvasLineJoin = "bevel" | "miter" | "round"--><!--Device-unnamed-declare type CanvasLineJoin = "bevel" | "miter" | "round"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| "bevel" | 在线段相连处使用三角形为底填充，每个部分矩形拐角独立。 |
| "miter" | 在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域， 该属性可以通过设置miterLimit属性展现效果。 |
| "round" | 在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。 |

