# CachedCountOptions

Defines the properties for controlling the cached count behavior.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface CachedCountOptions--><!--Device-unnamed-export declare interface CachedCountOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## independent

```TypeScript
independent?: boolean
```

Whether cachedCount is independent of group calculation. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_When set to true, cachedCount is calculated by actual child component count, independent of displayCount group calculation. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_When swipeByGroup is enabled and this is false, cachedCount is calculated by group. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CachedCountOptions-independent?: boolean--><!--Device-CachedCountOptions-independent?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShown

```TypeScript
isShown?: boolean
```

Whether the cached nodes within the range rendered without being added to the render tree.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CachedCountOptions-isShown?: boolean--><!--Device-CachedCountOptions-isShown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

