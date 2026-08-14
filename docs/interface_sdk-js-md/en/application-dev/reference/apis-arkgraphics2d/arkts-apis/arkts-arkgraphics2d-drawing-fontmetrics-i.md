# FontMetrics

Describes the attributes that describe the font size and layout. A typeface has similar font metrics.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-drawing-interface FontMetrics--><!--Device-drawing-interface FontMetrics-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'drawing';
```

## ascent

```TypeScript
ascent: double
```

Distance from the baseline to the highest coordinate of the text. The value is a floating point number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-ascent: double--><!--Device-FontMetrics-ascent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## avgCharWidth

```TypeScript
avgCharWidth?: double
```

Average character width.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-avgCharWidth?: double--><!--Device-FontMetrics-avgCharWidth?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## bottom

```TypeScript
bottom: double
```

Maximum distance from the baseline to the lowest coordinate of the text. The value is a floating point number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-bottom: double--><!--Device-FontMetrics-bottom: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## capHeight

```TypeScript
capHeight?: double
```

Height of a capital letter. The value is usually a negative value.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-capHeight?: double--><!--Device-FontMetrics-capHeight?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## descent

```TypeScript
descent: double
```

Distance from the baseline to the lowest coordinate of the text. The value is a floating point number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-descent: double--><!--Device-FontMetrics-descent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## flags

```TypeScript
flags?: int
```

Font measurement flags that are valid.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-FontMetrics-flags?: int--><!--Device-FontMetrics-flags?: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## leading

```TypeScript
leading: double
```

Interline spacing, that is, the distance from the descent of one line of text to the ascent of the next line. The value is a floating point number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-leading: double--><!--Device-FontMetrics-leading: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## maxCharWidth

```TypeScript
maxCharWidth?: double
```

Maximum character width.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-maxCharWidth?: double--><!--Device-FontMetrics-maxCharWidth?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## strikethroughPosition

```TypeScript
strikethroughPosition?: double
```

Vertical distance from the baseline to the bottom of the strikethrough. The value is usually a negative value.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-strikethroughPosition?: double--><!--Device-FontMetrics-strikethroughPosition?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## strikethroughThickness

```TypeScript
strikethroughThickness?: double
```

Thickness of the strikethrough.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-strikethroughThickness?: double--><!--Device-FontMetrics-strikethroughThickness?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## top

```TypeScript
top: double
```

Maximum distance from the baseline to the highest coordinate of the text. The value is a floating point number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-top: double--><!--Device-FontMetrics-top: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## underlinePosition

```TypeScript
underlinePosition?: double
```

Vertical distance from the baseline to the top of the underline. The value is usually a positive number.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-underlinePosition?: double--><!--Device-FontMetrics-underlinePosition?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## underlineThickness

```TypeScript
underlineThickness?: double
```

Thickness of the underline.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-underlineThickness?: double--><!--Device-FontMetrics-underlineThickness?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## xHeight

```TypeScript
xHeight?: double
```

Height of the lowercase letter x. The value is usually a negative value.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-xHeight?: double--><!--Device-FontMetrics-xHeight?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## xMax

```TypeScript
xMax?: double
```

Horizontal distance from the rightmost edge of any glyph bounding box to the origin. The value is a positive number, indicating the maximum horizontal coordinate across all glyph bounding boxes.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-xMax?: double--><!--Device-FontMetrics-xMax?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## xMin

```TypeScript
xMin?: double
```

Horizontal distance from the leftmost edge of any glyph bounding box to the origin. This value is usually less than 0, indicating the minimum horizontal coordinate across all glyph bounding boxes.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontMetrics-xMin?: double--><!--Device-FontMetrics-xMin?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

