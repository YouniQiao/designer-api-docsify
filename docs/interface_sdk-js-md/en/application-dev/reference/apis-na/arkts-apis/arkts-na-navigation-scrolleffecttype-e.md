# ScrollEffectType

Declares the scroll blur effect type for the title bar.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum ScrollEffectType--><!--Device-unnamed-export declare enum ScrollEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COMMON_BLUR

```TypeScript
COMMON_BLUR = 0
```

Common blur style. It applies uniform blur to the background. The blurred background appear/disappear with transparent gradient.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollEffectType-COMMON_BLUR = 0--><!--Device-ScrollEffectType-COMMON_BLUR = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GRADUAL_BLUR

```TypeScript
GRADUAL_BLUR = 1
```

Gradual blur style. It applies uniform blur to the title background with clear boundaries. The title bar content changes color/state before and after scrolling. During scrolling, it changes linearly following the gesture.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollEffectType-GRADUAL_BLUR = 1--><!--Device-ScrollEffectType-GRADUAL_BLUR = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

