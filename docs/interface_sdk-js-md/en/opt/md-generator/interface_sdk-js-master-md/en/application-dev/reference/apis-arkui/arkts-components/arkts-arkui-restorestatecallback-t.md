# RestoreStateCallback

```TypeScript
declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void
```

Custom page state restore callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void--><!--Device-unnamed-declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savedState | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; \| null | Yes |
