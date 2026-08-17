# RestoreStateCallback

```TypeScript
export type RestoreStateCallback = (savedState: Record<string, Object> | null) => void
```

Custom page state restore callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type RestoreStateCallback = (savedState: Record<string, Object> | null) => void--><!--Device-unnamed-export type RestoreStateCallback = (savedState: Record<string, Object> | null) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savedState | Record&lt;string, Object&gt; \| null | Yes | Custom page state saved by onSaveState. |

