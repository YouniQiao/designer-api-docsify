# LineHeightStyle

行高缩放基数枚举。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-text-enum LineHeightStyle--><!--Device-text-enum LineHeightStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## FONT_SIZE

```TypeScript
FONT_SIZE = 0
```

以字号大小作为缩放基数。最终行高为[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md).fontSize * [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md).heightScale。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineHeightStyle-FONT_SIZE = 0--><!--Device-LineHeightStyle-FONT_SIZE = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## FONT_HEIGHT

```TypeScript
FONT_HEIGHT = 1
```

以字形高度作为缩放基数。最终行高为塑形后字形高度 * [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md).heightScale。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineHeightStyle-FONT_HEIGHT = 1--><!--Device-LineHeightStyle-FONT_HEIGHT = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

