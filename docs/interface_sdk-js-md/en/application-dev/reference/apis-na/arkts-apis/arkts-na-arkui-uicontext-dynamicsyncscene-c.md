# DynamicSyncScene

Represents a dynamic synchronization scene.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class DynamicSyncScene--><!--Device-unnamed-export declare class DynamicSyncScene-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getFrameRateRange

```TypeScript
getFrameRateRange(): ExpectedFrameRateRange
```

Gets the FrameRateRange of the DynamicSyncScene.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicSyncScene-getFrameRateRange(): ExpectedFrameRateRange--><!--Device-DynamicSyncScene-getFrameRateRange(): ExpectedFrameRateRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| ExpectedFrameRateRange | The range of frameRate. |

## setFrameRateRange

```TypeScript
setFrameRateRange(range: ExpectedFrameRateRange): void
```

Sets the FrameRateRange of the DynamicSyncScene.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicSyncScene-setFrameRateRange(range: ExpectedFrameRateRange): void--><!--Device-DynamicSyncScene-setFrameRateRange(range: ExpectedFrameRateRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | ExpectedFrameRateRange | Yes | The range of frameRate. |

