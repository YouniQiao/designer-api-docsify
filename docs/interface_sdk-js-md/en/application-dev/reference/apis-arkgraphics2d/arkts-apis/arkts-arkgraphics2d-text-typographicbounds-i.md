# TypographicBounds

Describes the typographic boundaries of a text line. These boundaries depend on the typographic font and font size,but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, independent of the characters themselves.
    **NOTE**  
    
    The figure shows the text line typesetting parameters: width (the width of the text line including left and right  
    spaces), ascent (the highest point of the ascent), descent (the lowest point of the descent), leading (line  
    spacing), top (the highest point of the current line), baseline (the character baseline), bottom (the lowest  
    point of the current line), and next line top (the highest point of the next line).  
    
    !\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_  
    
    The figure shows the typesetting boundaries for the string " a b ".  
    
    !\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_  
    
    The figure shows the typesetting boundaries for the string "j" or "E".  
    
    !  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-text-interface TypographicBounds--><!--Device-text-interface TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

## ascent

```TypeScript
ascent: double
```

Ascent height of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-ascent: double--><!--Device-TypographicBounds-ascent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## descent

```TypeScript
descent: double
```

Descent height of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-descent: double--><!--Device-TypographicBounds-descent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## leading

```TypeScript
leading: double
```

Leading of a text line, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-leading: double--><!--Device-TypographicBounds-leading: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## width

```TypeScript
width: double
```

Total width of the layout boundary, which is a floating-point value in physical pixels (px).

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypographicBounds-width: double--><!--Device-TypographicBounds-width: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

