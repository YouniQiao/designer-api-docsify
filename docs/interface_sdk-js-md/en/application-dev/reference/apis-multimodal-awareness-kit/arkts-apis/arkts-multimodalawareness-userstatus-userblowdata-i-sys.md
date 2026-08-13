# UserBlowData (System API)

Defines user blow data.

**Inheritance/Implementation:** UserBlowData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#UserStatusData-(System-API))

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-userStatus-export interface UserBlowData--><!--Device-userStatus-export interface UserBlowData-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## blowDirection

```TypeScript
blowDirection?: int
```

Blow direction. The value ranges from 0 to 2. 0: Not blowing, 1: Blowing from bottom mic, 2: Blowing from top mic.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-blowDirection?: int--><!--Device-UserBlowData-blowDirection?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## emotion

```TypeScript
emotion?: int
```

User emotion level. The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm, 3: A little unhappy, 4: Angry, 5: Crying.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-emotion?: int--><!--Device-UserBlowData-emotion?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## facePosition

```TypeScript
facePosition?: double[]
```

Face position relative to screen. The normalized coordinate system ranges from 0 to 640.

**Type:** double[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-facePosition?: double[]--><!--Device-UserBlowData-facePosition?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## gravityAcceleration

```TypeScript
gravityAcceleration?: double[]
```

Gravity acceleration of user motion status, in m/s².

**Type:** double[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-gravityAcceleration?: double[]--><!--Device-UserBlowData-gravityAcceleration?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## isGazeStatus

```TypeScript
isGazeStatus?: boolean
```

Whether user is gazing at screen.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-isGazeStatus?: boolean--><!--Device-UserBlowData-isGazeStatus?: boolean-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## linearAcceleration

```TypeScript
linearAcceleration?: double[][]
```

Linear acceleration of user motion status, in m/s²..

**Type:** double[][]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-linearAcceleration?: double[][]--><!--Device-UserBlowData-linearAcceleration?: double[][]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## strengthLevel

```TypeScript
strengthLevel?: int
```

Blow strength level. The value must be an integer within [1,12].

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserBlowData-strengthLevel?: int--><!--Device-UserBlowData-strengthLevel?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

