# TypographicBounds

Describes the typographic boundaries of a text line. These boundaries depend on the typographic font and font size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, independent of the characters themselves. &gt; **NOTE：**&gt; &gt; The figure shows the text line typesetting parameters: width (the width of the text line including left and right &gt; spaces), ascent (the highest point of the ascent), descent (the lowest point of the descent), leading (line &gt; spacing), top (the highest point of the current line), baseline (the character baseline), bottom (the lowest &gt; point of the current line), and next line top (the highest point of the next line). &gt; &gt;  &gt; &gt; The figure shows the typesetting boundaries for the string " a b ". &gt; &gt;  &gt; &gt; The figure shows the typesetting boundaries for the string "j" or "E". &gt; &gt; ! &gt; [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 23

<!--Device-text-interface TypographicBounds--><!--Device-text-interface TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## ascent

```TypeScript
ascent: double
```

Ascent height of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-ascent: double--><!--Device-TypographicBounds-ascent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## descent

```TypeScript
descent: double
```

Descent height of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-descent: double--><!--Device-TypographicBounds-descent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## leading

```TypeScript
leading: double
```

Leading of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-leading: double--><!--Device-TypographicBounds-leading: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## width

```TypeScript
width: double
```

Total width of the layout boundary, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-width: double--><!--Device-TypographicBounds-width: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

