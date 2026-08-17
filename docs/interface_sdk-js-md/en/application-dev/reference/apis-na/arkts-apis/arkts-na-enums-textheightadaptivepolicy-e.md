# TextHeightAdaptivePolicy

Enum of text height adaptation

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum TextHeightAdaptivePolicy--><!--Device-unnamed-export declare enum TextHeightAdaptivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MAX_LINES_FIRST

```TypeScript
MAX_LINES_FIRST = 0
```

Priority is given to using the maxLines attribute to adapt the text height. If the layout size using the maxLines attribute exceeds the layout constraint, try reducing the font size to display more text.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextHeightAdaptivePolicy-MAX_LINES_FIRST = 0--><!--Device-TextHeightAdaptivePolicy-MAX_LINES_FIRST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MIN_FONT_SIZE_FIRST

```TypeScript
MIN_FONT_SIZE_FIRST = 1
```

Priority is given to using the minFontSize attribute to adapt the text height. If the text can be layout in a single line using the minFontSize property, try increasing the font size and using the maximum possible font size.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextHeightAdaptivePolicy-MIN_FONT_SIZE_FIRST = 1--><!--Device-TextHeightAdaptivePolicy-MIN_FONT_SIZE_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LAYOUT_CONSTRAINT_FIRST

```TypeScript
LAYOUT_CONSTRAINT_FIRST = 2
```

Priority is given to using the layout constraint to adapt the text height. If the layout size exceeds the layout constraint, try reducing the font size. If the layout size still exceeds the layout constraint after reducing the font size to minFontSize, remove the lines that exceed the layout constraint.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextHeightAdaptivePolicy-LAYOUT_CONSTRAINT_FIRST = 2--><!--Device-TextHeightAdaptivePolicy-LAYOUT_CONSTRAINT_FIRST = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

