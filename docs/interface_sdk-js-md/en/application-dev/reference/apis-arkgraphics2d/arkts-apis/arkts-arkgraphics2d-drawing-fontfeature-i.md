# FontFeature

Defines font features, which are typesetting rules within a font that determine how glyphs look, such as ligatures, alternates, and superscripts/subscripts.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-drawing-interface FontFeature--><!--Device-drawing-interface FontFeature-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'drawing';
```

## name

```TypeScript
name: string
```

Name of a font feature. Common font feature names include **liga**, **frac**, and **case**. A font feature needs a TTF file to work.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontFeature-name: string--><!--Device-FontFeature-name: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## value

```TypeScript
value: double
```

Value of a font feature, which is a floating point number. You are advised to determine the valid value range by using a font viewing tool or referring to the font document.

**Type:** double

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontFeature-value: double--><!--Device-FontFeature-value: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

