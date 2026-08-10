# setTextUndefinedGlyphDisplay

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## setTextUndefinedGlyphDisplay

```TypeScript
function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void
```

设置字符映射到.notdef（未定义）字形时要使用的字形类型。

调用此接口后，后续渲染的文本若包含未定义字形，均按此设置显示。

此配置会影响显示字体中未定义字符的方式：

- 默认使用字体的.notdef字形设计。  
- 开启后，缺失字形的字符将以豆腐块形式显示。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-text-function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void--><!--Device-text-function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| noGlyphShow | [TextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-textundefinedglyphdisplay-e.md) | Yes | 无法塑形字符的显示方式。 |

## Examples

```TypeScript
text.setTextUndefinedGlyphDisplay(text.TextUndefinedGlyphDisplay.USE_TOFU)
```

