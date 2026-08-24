# OverlayOptions

Defines the OverlayOptions interface.&lt;strong&gt;NOTE&lt;/strong&gt;:<br> When both align and offset are set, the effects are combined. The overlay is first aligned relative to the component and then offset from its current upper left corner.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface OverlayOptions--><!--Device-unnamed-export declare interface OverlayOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## align

```TypeScript
align?: Alignment
```

Defines align type.

**Type:** [Alignment](../../apis-arkui/arkts-apis/arkts-arkui-alignment-e.md)

**Default:** TopStart

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayOptions-align?: Alignment--><!--Device-OverlayOptions-align?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: OverlayOffset
```

Defines offset type.

**Type:** [OverlayOffset](arkts-common-overlayoffset-i.md)

**Default:** - the overlay is in the upper left corner of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayOptions-offset?: OverlayOffset--><!--Device-OverlayOptions-offset?: OverlayOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

