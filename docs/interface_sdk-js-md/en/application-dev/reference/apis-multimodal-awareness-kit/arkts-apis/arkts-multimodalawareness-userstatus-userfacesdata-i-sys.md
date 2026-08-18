# UserFacesData (System API)

Defines user face data.

**Inheritance/Implementation:** UserFacesData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#userstatusdata-system-api)

**Since:** 26.0.0

<!--Device-userStatus-export interface UserFacesData--><!--Device-userStatus-export interface UserFacesData-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## angularVelocity

```TypeScript
angularVelocity?: double[]
```

Angular velocity of user motion status, in rad/s.

**Type:** double[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-angularVelocity?: double[]--><!--Device-UserFacesData-angularVelocity?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## azimuth

```TypeScript
azimuth?: double[]
```

Azimuth of user motion status. The value ranges from 0 to 360, in degrees.

**Type:** double[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-azimuth?: double[]--><!--Device-UserFacesData-azimuth?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## faceNum

```TypeScript
faceNum?: int
```

Number of faces detected. The value must be an integer within [0,3].

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-faceNum?: int--><!--Device-UserFacesData-faceNum?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## gravityAcceleration

```TypeScript
gravityAcceleration?: double[]
```

Gravity acceleration of user motion status, in m/s².

**Type:** double[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-gravityAcceleration?: double[]--><!--Device-UserFacesData-gravityAcceleration?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## linearAcceleration

```TypeScript
linearAcceleration?: double[][]
```

Linear acceleration of user motion status, in m/s².

**Type:** double[][]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-linearAcceleration?: double[][]--><!--Device-UserFacesData-linearAcceleration?: double[][]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## visualAngle

```TypeScript
visualAngle?: double[]
```

User visual angle. The value ranges from 0 to 90, in degrees.

**Type:** double[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserFacesData-visualAngle?: double[]--><!--Device-UserFacesData-visualAngle?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

