# OverlayManagerOptions

the property of OverlayManager.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface OverlayManagerOptions--><!--Device-unnamed-export interface OverlayManagerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## enableBackPressedEvent

```TypeScript
enableBackPressedEvent?: boolean
```

Set whether support backPressed event or not.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManagerOptions-enableBackPressedEvent?: boolean--><!--Device-OverlayManagerOptions-enableBackPressedEvent?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onBackPress

```TypeScript
onBackPress?: OnOverlayBackPressCallback
```

Callback for intercepting back-press events on an overlay. **NOTE：**1. When this callback is registered and **enableBackPressedEvent** is set to **true**, the back-press event will not close the overlay automatically. Instead, the overlay invokes this callback to decide whether the event should be propagated to the underlying components. 2. Return **true** to intercept the event (the event is consumed and will not be passed to lower layers), or **false** to allow the event to propagate through to the components below the overlay.

**Type:** [OnOverlayBackPressCallback](arkts-na-onoverlaybackpresscallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManagerOptions-onBackPress?: OnOverlayBackPressCallback--><!--Device-OverlayManagerOptions-onBackPress?: OnOverlayBackPressCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderRootOverlay

```TypeScript
renderRootOverlay?: boolean
```

the render property of overlay node.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManagerOptions-renderRootOverlay?: boolean--><!--Device-OverlayManagerOptions-renderRootOverlay?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

