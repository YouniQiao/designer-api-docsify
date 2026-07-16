# BoidsSimParameters (System API)

Boids simulation parameters bound per-boid.

**Since:** 26.0.0

<!--Device-unnamed-export interface BoidsSimParameters--><!--Device-unnamed-export interface BoidsSimParameters-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## alignmentDistance

```TypeScript
alignmentDistance?: number
```

Perception radius for the alignment rule. Boids within this distance (inclusive) contribute to alignment force. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-alignmentDistance?: double--><!--Device-BoidsSimParameters-alignmentDistance?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## alignmentWeight

```TypeScript
alignmentWeight?: number
```

How strongly the boid steers to match the average heading of neighbours within alignmentDistance.Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-alignmentWeight?: double--><!--Device-BoidsSimParameters-alignmentWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## boundaryDistance

```TypeScript
boundaryDistance?: number
```

Distance from boundary walls within which the boundary repulsion force takes effect. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-boundaryDistance?: double--><!--Device-BoidsSimParameters-boundaryDistance?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## boundaryMaxPos

```TypeScript
boundaryMaxPos?: Vec3
```

Upper corner of the axis-aligned bounding box constraining boid movement. Default: (0, 0, 0).

**Type:** Vec3

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-boundaryMaxPos?: Vec3--><!--Device-BoidsSimParameters-boundaryMaxPos?: Vec3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## boundaryMinPos

```TypeScript
boundaryMinPos?: Vec3
```

Lower corner of the axis-aligned bounding box constraining boid movement.When any component of boundaryMinPos is greater than or equal to the corresponding component of boundaryMaxPos, this boid is considered unbounded. Default: (0, 0, 0).

**Type:** Vec3

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-boundaryMinPos?: Vec3--><!--Device-BoidsSimParameters-boundaryMinPos?: Vec3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## boundaryWeight

```TypeScript
boundaryWeight?: number
```

How strongly the boid is pushed back when within boundaryDistance of the boundary box edges.Range: [0, +inf). Default: 0.0.If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-boundaryWeight?: double--><!--Device-BoidsSimParameters-boundaryWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## cohesionDistance

```TypeScript
cohesionDistance?: number
```

Perception radius for the cohesion rule. Boids within this distance (inclusive) contribute to cohesion force. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-cohesionDistance?: double--><!--Device-BoidsSimParameters-cohesionDistance?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## cohesionWeight

```TypeScript
cohesionWeight?: number
```

How strongly the boid steers toward the average position of neighbours within cohesionDistance.Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-cohesionWeight?: double--><!--Device-BoidsSimParameters-cohesionWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## gravityWeight

```TypeScript
gravityWeight?: number
```

How strongly gravity field entities attract this boid. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-gravityWeight?: double--><!--Device-BoidsSimParameters-gravityWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## initialPosition

```TypeScript
initialPosition?: Vec3
```

Initial position of the boid. When it's not set, the entity's current transform position is used.Default: (NaN, NaN, NaN).

**Type:** Vec3

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-initialPosition?: Vec3--><!--Device-BoidsSimParameters-initialPosition?: Vec3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## initialRotation

```TypeScript
initialRotation?: Quaternion
```

Initial rotation of the boid. When it's not set, the entity's current transform rotation is used.Default: (NaN, NaN, NaN, NaN).

**Type:** Quaternion

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-initialRotation?: Quaternion--><!--Device-BoidsSimParameters-initialRotation?: Quaternion-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## initialVelocity

```TypeScript
initialVelocity?: Vec3
```

Initial velocity of the boid. Default: (0, 0, 0).

**Type:** Vec3

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-initialVelocity?: Vec3--><!--Device-BoidsSimParameters-initialVelocity?: Vec3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## maxAccelerationMag

```TypeScript
maxAccelerationMag?: number
```

Maximum acceleration the boid can reach per simulation frame. Range: [0, +inf). Default: approximately 39.06.If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-maxAccelerationMag?: double--><!--Device-BoidsSimParameters-maxAccelerationMag?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## maxTurnRate

```TypeScript
maxTurnRate?: Vec3
```

Per-axis rotation limit in radians per simulation frame. Range: [0, +inf) per axis.Default: approximately 0.0377 per axis.If a value exceeding the valid range is assigned, it will be clamped.

**Type:** Vec3

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-maxTurnRate?: Vec3--><!--Device-BoidsSimParameters-maxTurnRate?: Vec3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## maxVelocityMag

```TypeScript
maxVelocityMag?: number
```

Maximum speed the boid can reach per simulation frame. Range: [0, +inf). Default: approximately 0.625.If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-maxVelocityMag?: double--><!--Device-BoidsSimParameters-maxVelocityMag?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## repulsionWeight

```TypeScript
repulsionWeight?: number
```

How strongly repulsion field entities push this boid away. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-repulsionWeight?: double--><!--Device-BoidsSimParameters-repulsionWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## separationDistance

```TypeScript
separationDistance?: number
```

Perception radius for the separation rule. Only boids strictly within this distance contribute to separation force (force is zero at the boundary). Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-separationDistance?: double--><!--Device-BoidsSimParameters-separationDistance?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## separationWeight

```TypeScript
separationWeight?: number
```

How strongly the boid steers away from nearby neighbours within separationDistance. Range: [0, +inf). Default: 0.0If a value exceeding the valid range is assigned, it will be clamped.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimParameters-separationWeight?: double--><!--Device-BoidsSimParameters-separationWeight?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

