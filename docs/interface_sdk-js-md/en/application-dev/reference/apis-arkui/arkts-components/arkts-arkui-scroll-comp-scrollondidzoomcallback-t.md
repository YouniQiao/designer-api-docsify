# ScrollOnDidZoomCallback

```TypeScript
declare type ScrollOnDidZoomCallback = (scale: number) => void
```

Defines the callback triggered when the scroll scaling of each frame is complete.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | number | Yes | Current scale factor. |
