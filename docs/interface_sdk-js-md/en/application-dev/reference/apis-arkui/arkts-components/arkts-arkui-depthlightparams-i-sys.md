# DepthLightParams (System API)

光照参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface DepthLightParams--><!--Device-unnamed-declare interface DepthLightParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## color

```TypeScript
color: DepthColorRGB
```

光照颜色。

**Type:** [DepthColorRGB](../arkts-apis/arkts-arkui-common-depthcolorrgb-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DepthLightParams-color: DepthColorRGB--><!--Device-DepthLightParams-color: DepthColorRGB-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## direction

```TypeScript
direction: DepthVector3
```

光照方向向量。无单位，其值表示3D空间中的坐标。

**Type:** [DepthVector3](../arkts-apis/arkts-arkui-common-depthvector3-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DepthLightParams-direction: DepthVector3--><!--Device-DepthLightParams-direction: DepthVector3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## intensity

```TypeScript
intensity: double
```

光照强度。无单位，取值范围[0, +∞)。

建议取值范围[0, 1]，当设置为0时，无光照。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DepthLightParams-intensity: double--><!--Device-DepthLightParams-intensity: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

