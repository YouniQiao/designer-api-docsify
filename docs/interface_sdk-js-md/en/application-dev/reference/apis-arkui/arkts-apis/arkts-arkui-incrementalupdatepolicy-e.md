# IncrementalUpdatePolicy

Defines incremental update policies for text rendering.

**Since:** 26.0.0

<!--Device-unnamed-declare enum IncrementalUpdatePolicy--><!--Device-unnamed-declare enum IncrementalUpdatePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Disable incremental updates. Full layout rendering is used.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IncrementalUpdatePolicy-NONE = 0--><!--Device-IncrementalUpdatePolicy-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PARAGRAPH_CACHE

```TypeScript
PARAGRAPH_CACHE = 1
```

Enable incremental updates with paragraph-level cache.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1--><!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

