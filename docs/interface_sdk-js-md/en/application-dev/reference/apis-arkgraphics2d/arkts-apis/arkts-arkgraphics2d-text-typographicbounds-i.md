# TypographicBounds

文本行的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版边界相同，即与字符本身无关。

> **说明：**
> 
> 示意图展示文本行排版参数：width（包含左右空格的文本行宽度）、ascent（上升高度最高点）、descent（下降高度最低点）、leading（行间距）、top（当前行最高点）、baseline（字符基线）、bottom（
> 当前行最低点）、next line top（下一行最高点）。
> 
> ![Typographic.png](../../../reference/apis-arkgraphics2d/figures/Typographic.png)
> 
> 示意图展示了字符串为" a b "的排版边界。
> 
> ![TypographicBounds.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds.png)
> 
> 示意图展示了字符串为"j"或"E"的排版边界。
> 
> !
> [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-text-interface TypographicBounds--><!--Device-text-interface TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## ascent

```TypeScript
ascent: double
```

文本行的上升高度，浮点数，单位为物理像素px。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-ascent: double--><!--Device-TypographicBounds-ascent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## descent

```TypeScript
descent: double
```

文本行的下降高度，浮点数，单位为物理像素px。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-descent: double--><!--Device-TypographicBounds-descent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## leading

```TypeScript
leading: double
```

文本行的行间距，浮点数，单位为物理像素px。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-leading: double--><!--Device-TypographicBounds-leading: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## width

```TypeScript
width: double
```

排版边界的总宽度，浮点数，单位为物理像素px。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-width: double--><!--Device-TypographicBounds-width: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

