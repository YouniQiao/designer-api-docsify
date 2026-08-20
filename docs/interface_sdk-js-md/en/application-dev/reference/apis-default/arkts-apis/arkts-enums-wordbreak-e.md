# WordBreak

Enum of word break

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum WordBreak--><!--Device-unnamed-export declare enum WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NORMAL

```TypeScript
NORMAL = 0
```

By default, CJK text can be wrapped between any 2 characters, and non-CJK text can only be wrapped in spaces.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WordBreak-NORMAL = 0--><!--Device-WordBreak-NORMAL = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BREAK_ALL

```TypeScript
BREAK_ALL = 1
```

Non-CJK text be wrapped at any character

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WordBreak-BREAK_ALL = 1--><!--Device-WordBreak-BREAK_ALL = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BREAK_WORD

```TypeScript
BREAK_WORD = 2
```

Non-CJK text can be wrapped at any character and if a complete word can be preserved in space breaks, the word must be kept on the line.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WordBreak-BREAK_WORD = 2--><!--Device-WordBreak-BREAK_WORD = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HYPHENATION

```TypeScript
HYPHENATION = 3
```

For supported languages, line breaks can be performed by syllables.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WordBreak-HYPHENATION = 3--><!--Device-WordBreak-HYPHENATION = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

