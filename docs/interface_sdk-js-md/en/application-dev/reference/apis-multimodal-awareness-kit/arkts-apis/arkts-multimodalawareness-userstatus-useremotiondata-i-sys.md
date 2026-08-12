# UserEmotionData (System API)

Defines user emotion data.

**Inheritance/Implementation:** UserEmotionData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#UserStatusData)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-userStatus-export interface UserEmotionData extends UserStatusData--><!--Device-userStatus-export interface UserEmotionData extends UserStatusData-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## confidence

```TypeScript
confidence?: int
```

User emotion confidence.The value ranges from 0 to 100. A larger value indicates a higher confidence.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-confidence?: int--><!--Device-UserEmotionData-confidence?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## emotionNonRealTime

```TypeScript
emotionNonRealTime ?: int[]
```

User non-real-time emotion level.The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm,3: A little unhappy, 4: Angry, 5: Crying.

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-emotionNonRealTime ?: int[]--><!--Device-UserEmotionData-emotionNonRealTime ?: int[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## emotionRealTime

```TypeScript
emotionRealTime ?: int
```

User real-time emotion level.The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm,3: A little unhappy, 4: Angry, 5: Crying.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-emotionRealTime ?: int--><!--Device-UserEmotionData-emotionRealTime ?: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## gravityAcceleration

```TypeScript
gravityAcceleration?: double[]
```

Gravity acceleration of user motion status, in m/s².

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-gravityAcceleration?: double[]--><!--Device-UserEmotionData-gravityAcceleration?: double[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## isRealTime

```TypeScript
isRealTime?: boolean
```

Whether emotion data is real-time.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-isRealTime?: boolean--><!--Device-UserEmotionData-isRealTime?: boolean-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## linearAcceleration

```TypeScript
linearAcceleration?: double[][]
```

Linear acceleration of user motion status, in m/s².

**Type:** ArkTS-Dyn: number[][]  <br>ArkTS-Sta：double[][]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserEmotionData-linearAcceleration?: double[][]--><!--Device-UserEmotionData-linearAcceleration?: double[][]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

