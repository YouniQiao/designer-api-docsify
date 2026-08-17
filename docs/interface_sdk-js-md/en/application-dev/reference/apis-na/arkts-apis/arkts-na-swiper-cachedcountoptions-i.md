# CachedCountOptions

Defines the properties for controlling the cached count behavior.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface CachedCountOptions--><!--Device-unnamed-export declare interface CachedCountOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## independent

```TypeScript
independent?: boolean
```

Whether cachedCount is independent of group calculation. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When set to true, cachedCount is calculated by actual child component count, independent of displayCount group calculation. <br>When swipeByGroup is enabled and this is false, cachedCount is calculated by group. &lt;/p&gt;

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CachedCountOptions-isShown?: boolean--><!--Device-CachedCountOptions-isShown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

