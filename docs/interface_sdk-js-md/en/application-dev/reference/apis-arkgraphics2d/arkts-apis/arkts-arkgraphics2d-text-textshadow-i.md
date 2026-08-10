# TextShadow

文本阴影。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface TextShadow--><!--Device-text-interface TextShadow-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## blurRadius

```TypeScript
blurRadius?: double
```

模糊半径，浮点数，单位为物理像素px，默认为0.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextShadow-blurRadius?: double--><!--Device-TextShadow-blurRadius?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## color

```TypeScript
color?: common2D.Color
```

文本阴影的颜色，默认为黑色Color(255, 0, 0, 0)。

**Type:** common2D.Color

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextShadow-color?: common2D.Color--><!--Device-TextShadow-color?: common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

## point

```TypeScript
point?: common2D.Point
```

文本阴影基于当前文本的偏移位置，横、纵坐标要大于等于零，单位为物理像素px，默认为common2D.Point(0, 0)。

**Type:** common2D.Point

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextShadow-point?: common2D.Point--><!--Device-TextShadow-point?: common2D.Point-End-->

**System capability:** SystemCapability.Graphics.Drawing

