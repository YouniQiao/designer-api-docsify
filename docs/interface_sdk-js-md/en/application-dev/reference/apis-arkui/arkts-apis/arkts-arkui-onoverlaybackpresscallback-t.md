# OnOverlayBackPressCallback

```TypeScript
export declare type OnOverlayBackPressCallback = () => boolean
```

Defines the callback type for intercepting the overlay swipe-back event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-export declare type OnOverlayBackPressCallback = () => boolean--><!--Device-unnamed-export declare type OnOverlayBackPressCallback = () => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether to intercept the back-press event. If **true** is returned, the event is intercepted and is prevented from reaching the lower-layer component. If **false** is returned, the event is transparently transmitted to the lower-layer component. |
