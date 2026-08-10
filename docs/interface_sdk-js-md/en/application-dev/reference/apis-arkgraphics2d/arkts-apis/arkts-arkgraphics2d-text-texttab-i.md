# TextTab

段落风格的文本制表符，储存了对齐方式和位置。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-text-interface TextTab--><!--Device-text-interface TextTab-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## alignment

```TypeScript
alignment: TextAlign
```

段落中制表符之后的文本对齐方式，支持设置[TextAlign](arkts-arkgraphics2d-text-textalign-e.md)的LEFT左对齐、RIGHT右对齐和CENTER居中对齐方式，未列出的枚举值将视为左对齐，默认为左对齐。

**Type:** [TextAlign](arkts-arkgraphics2d-text-textalign-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextTab-alignment: TextAlign--><!--Device-TextTab-alignment: TextAlign-End-->

**System capability:** SystemCapability.Graphics.Drawing

## location

```TypeScript
location: double
```

制表符之后的文本对齐位置，浮点数，单位为物理像素px，最小值为1.0，当该值小于1.0时，该制表符会被替换为一个空格。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextTab-location: double--><!--Device-TextTab-location: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

