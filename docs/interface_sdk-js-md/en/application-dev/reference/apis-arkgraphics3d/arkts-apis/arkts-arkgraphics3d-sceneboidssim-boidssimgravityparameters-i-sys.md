# BoidsSimGravityParameters (System API)

Boids模拟引力场参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface BoidsSimGravityParameters--><!--Device-unnamed-export interface BoidsSimGravityParameters-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## accelerationMag

```TypeScript
accelerationMag?: double
```

施加于boid、方向指向实体的吸引加速度大小。取值范围：[0, +∞)。默认值：0.0

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimGravityParameters-accelerationMag?: double--><!--Device-BoidsSimGravityParameters-accelerationMag?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## radius

```TypeScript
radius?: double
```

作用半径。实体在此距离范围内的boid会受到吸引（边界处力为零）。取值范围：[0, +∞)。默认值：0.0

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimGravityParameters-radius?: double--><!--Device-BoidsSimGravityParameters-radius?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

