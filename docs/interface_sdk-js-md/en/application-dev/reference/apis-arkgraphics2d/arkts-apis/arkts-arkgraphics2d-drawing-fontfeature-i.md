# FontFeature

表示字体特征。字体特征是字体内置的排版规则，用于控制字形的显示效果，具体包括连字、替代字形、上下标等功能。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-drawing-interface FontFeature--><!--Device-drawing-interface FontFeature-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## name

```TypeScript
name: string
```

字体特征的名称。通常为4个ASCII字符组成的标签（如liga、frac、case等），需对应的ttf文件支持才能生效。建议通过字体查看工具或查阅字体文档，确定有效名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontFeature-name: string--><!--Device-FontFeature-name: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## value

```TypeScript
value: double
```

字体特征的数值，浮点数。需要对应的ttf文件支持才能生效。建议通过字体查看工具或查阅字体文档，确定具体的有效取值范围。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontFeature-value: double--><!--Device-FontFeature-value: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

