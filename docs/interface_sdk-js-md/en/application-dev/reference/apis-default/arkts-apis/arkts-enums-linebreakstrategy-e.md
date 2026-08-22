# LineBreakStrategy

Enum of line break strategy

@enum { number }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare enum LineBreakStrategy--><!--Device-unnamed-export declare enum LineBreakStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GREEDY

```TypeScript
GREEDY = 0
```

By default. Display as many characters as possible on each line until no more characters can be displayed on that line, and do not automatically add hyphens under this strategy

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineBreakStrategy-GREEDY = 0--><!--Device-LineBreakStrategy-GREEDY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HIGH_QUALITY

```TypeScript
HIGH_QUALITY = 1
```

High quality folding. Optimize the layout of the entire text's line breaks and automatically add hyphens if necessary.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineBreakStrategy-HIGH_QUALITY = 1--><!--Device-LineBreakStrategy-HIGH_QUALITY = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BALANCED

```TypeScript
BALANCED = 2
```

Balanced folding. We will try our best to ensure that the width of each line in a paragraph is the same, and if necessary, we will add conjunction

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineBreakStrategy-BALANCED = 2--><!--Device-LineBreakStrategy-BALANCED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

