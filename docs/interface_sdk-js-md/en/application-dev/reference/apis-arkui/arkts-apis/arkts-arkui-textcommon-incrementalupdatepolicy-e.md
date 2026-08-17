# IncrementalUpdatePolicy

Defines incremental update policies for text rendering.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare enum IncrementalUpdatePolicy--><!--Device-unnamed-export declare enum IncrementalUpdatePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Disable incremental updates. Full layout rendering is used.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalUpdatePolicy-NONE = 0--><!--Device-IncrementalUpdatePolicy-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PARAGRAPH_CACHE

```TypeScript
PARAGRAPH_CACHE = 1
```

Enable incremental updates with paragraph-level cache.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1--><!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

