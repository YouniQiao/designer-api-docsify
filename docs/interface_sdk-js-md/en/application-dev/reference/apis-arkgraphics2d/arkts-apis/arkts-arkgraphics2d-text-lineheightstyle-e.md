# LineHeightStyle

Enumerates the line height scaling base.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-text-enum LineHeightStyle--><!--Device-text-enum LineHeightStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## FONT_SIZE

```TypeScript
FONT_SIZE = 0
```

Uses the font size as the scaling base. The line height is calculated as follows:  
[TextStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.fontSize * [TextStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.heightScale.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineHeightStyle-FONT_SIZE = 0--><!--Device-LineHeightStyle-FONT_SIZE = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## FONT_HEIGHT

```TypeScript
FONT_HEIGHT = 1
```

Uses the font height as the scaling base. The line height is calculated as follows: the height of the shaped glyph * [TextStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.heightScale.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineHeightStyle-FONT_HEIGHT = 1--><!--Device-LineHeightStyle-FONT_HEIGHT = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

