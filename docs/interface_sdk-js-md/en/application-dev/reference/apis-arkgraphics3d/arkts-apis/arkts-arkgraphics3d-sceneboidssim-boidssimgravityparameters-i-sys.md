# BoidsSimGravityParameters (System API)

Attraction field parameters, used to configure the attraction field in the scene.

**Since:** 26.0.0

<!--Device-unnamed-export interface BoidsSimGravityParameters--><!--Device-unnamed-export interface BoidsSimGravityParameters-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## accelerationMag

```TypeScript
accelerationMag?: double
```

The magnitude of the attraction acceleration applied to the individual, with the direction pointing toward the attraction field entity. Value >= 0. Default value: 0.0.

**Type:** double

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimGravityParameters-accelerationMag?: double--><!--Device-BoidsSimGravityParameters-accelerationMag?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## radius

```TypeScript
radius?: double
```

The radius of the attraction field. Only individuals strictly within this distance are attracted (boundary force is 0). Value >= 0. Default value: 0.0.

**Type:** double

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimGravityParameters-radius?: double--><!--Device-BoidsSimGravityParameters-radius?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

