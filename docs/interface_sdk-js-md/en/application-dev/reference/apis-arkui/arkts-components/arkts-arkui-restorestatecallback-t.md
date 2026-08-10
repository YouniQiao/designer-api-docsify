# RestoreStateCallback

```TypeScript
declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void
```

自定义页面状态恢复回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void--><!--Device-unnamed-declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savedState | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; \| null | Yes | onSaveState保存的自定义页面状态。 |

