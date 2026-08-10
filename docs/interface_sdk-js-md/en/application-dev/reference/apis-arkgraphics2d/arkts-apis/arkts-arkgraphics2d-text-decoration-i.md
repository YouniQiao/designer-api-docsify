# Decoration

文本装饰线。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface Decoration--><!--Device-text-interface Decoration-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## color

```TypeScript
color?: common2D.Color
```

装饰线颜色，默认为跟随文本颜色。

**Type:** common2D.Color

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Decoration-color?: common2D.Color--><!--Device-Decoration-color?: common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

## decorationStyle

```TypeScript
decorationStyle?: TextDecorationStyle
```

装饰线样式，默认为SOLID。

**Type:** [TextDecorationStyle](../../apis-arkui/arkts-apis/arkts-arkui-enums-textdecorationstyle-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Decoration-decorationStyle?: TextDecorationStyle--><!--Device-Decoration-decorationStyle?: TextDecorationStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## decorationThicknessScale

```TypeScript
decorationThicknessScale?: double
```

装饰线粗细系数，浮点数，默认为1.0。如果设置的值小于等于0，则不会绘制装饰线。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Decoration-decorationThicknessScale?: double--><!--Device-Decoration-decorationThicknessScale?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## textDecoration

```TypeScript
textDecoration?: TextDecorationType
```

装饰线类型，默认为NONE。

**Type:** [TextDecorationType](../../apis-arkui/arkts-apis/arkts-arkui-textdecorationtype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Decoration-textDecoration?: TextDecorationType--><!--Device-Decoration-textDecoration?: TextDecorationType-End-->

**System capability:** SystemCapability.Graphics.Drawing

