# DepthComponentOptions (System API)

Defines the options of DepthComponent.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface DepthComponentOptions--><!--Device-unnamed-export declare interface DepthComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## colorSpace

```TypeScript
colorSpace?: colorSpaceManager.ColorSpace
```

Color space of the background.

**Type:** colorSpaceManager.ColorSpace

**Default:** colorSpaceManager.ColorSpace.SRGB

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentOptions-colorSpace?: colorSpaceManager.ColorSpace--><!--Device-DepthComponentOptions-colorSpace?: colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## depthSpace

```TypeScript
depthSpace?: DepthSpaceType
```

Depth space type.

**Type:** [DepthSpaceType](arkts-depthcomponent-depthspacetype-e-sys.md)

**Default:** DepthSpaceType.INSTANCE

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentOptions-depthSpace?: DepthSpaceType--><!--Device-DepthComponentOptions-depthSpace?: DepthSpaceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## render3DScale

```TypeScript
render3DScale?: double
```

Scale factor for 3D rendering window, applied to both width and height. The value range is (0.0, 1.0]. Values outside this range are invalid and the default value is used.

**Type:** double

**Default:** 1.0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentOptions-render3DScale?: double--><!--Device-DepthComponentOptions-render3DScale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

