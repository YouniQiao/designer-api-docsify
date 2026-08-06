# TextTab

Implements a paragraph-style text tab, which stores the alignment mode and position.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-text-interface TextTab--><!--Device-text-interface TextTab-End-->

**System capability:** SystemCapability.Graphics.Drawing

## alignment

```TypeScript
alignment: TextAlign
```

Text alignment method after the tab character in a paragraph. It supports the LEFT (left alignment), RIGHT (right alignment), and CENTER (center alignment) alignment methods of [TextAlign]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Unlisted enum values are treated as left alignment, with left alignment as the default.

**Type:** TextAlign

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextTab-alignment: TextAlign--><!--Device-TextTab-alignment: TextAlign-End-->

**System capability:** SystemCapability.Graphics.Drawing

## location

```TypeScript
location: double
```

Alignment position of the text following the tab character. The value is a floating point number, in px. The minimum value is 1.0. When the value is less than 1.0, the tab character is replaced with a space.

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextTab-location: double--><!--Device-TextTab-location: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

