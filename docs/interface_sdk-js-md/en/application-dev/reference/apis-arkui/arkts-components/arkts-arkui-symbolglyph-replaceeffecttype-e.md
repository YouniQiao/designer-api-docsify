# ReplaceEffectType

The replace effect type of symbol.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare enum ReplaceEffectType--><!--Device-unnamed-export declare enum ReplaceEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEQUENTIAL

```TypeScript
SEQUENTIAL = 0
```

The default replace effect of symbol, the current symbol fully disappears before the new symbol fades in.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReplaceEffectType-SEQUENTIAL = 0--><!--Device-ReplaceEffectType-SEQUENTIAL = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CROSS_FADE

```TypeScript
CROSS_FADE = 1
```

The current symbol fades out while the new symbol fades in at the same time, producing a smoother and faster transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReplaceEffectType-CROSS_FADE = 1--><!--Device-ReplaceEffectType-CROSS_FADE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLASH_OVERLAY

```TypeScript
SLASH_OVERLAY = 2
```

Replaces the current symbol with a symbol that includes a diagonal slash overlay, typically used to indicate a disabled or inactive state. If a corresponding slashed symbol variant is not available, the symbol is replaced without animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReplaceEffectType-SLASH_OVERLAY = 2--><!--Device-ReplaceEffectType-SLASH_OVERLAY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

