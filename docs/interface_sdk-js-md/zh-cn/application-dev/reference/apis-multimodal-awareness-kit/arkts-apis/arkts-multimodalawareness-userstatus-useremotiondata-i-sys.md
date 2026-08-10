# UserEmotionData（系统接口）

Defines user emotion data.

**继承/实现关系：** UserEmotionData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface UserEmotionData extends UserStatusData--><!--Device-userStatus-export interface UserEmotionData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## confidence

```TypeScript
confidence?: int
```

User emotion confidence.The value ranges from 0 to 100. A larger value indicates a higher confidence.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-confidence?: int--><!--Device-UserEmotionData-confidence?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## emotionNonRealTime

```TypeScript
emotionNonRealTime ?: int[]
```

User non-real-time emotion level.The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm,3: A little unhappy, 4: Angry, 5: Crying.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-emotionNonRealTime ?: int[]--><!--Device-UserEmotionData-emotionNonRealTime ?: int[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## emotionRealTime

```TypeScript
emotionRealTime ?: int
```

User real-time emotion level.The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm,3: A little unhappy, 4: Angry, 5: Crying.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-emotionRealTime ?: int--><!--Device-UserEmotionData-emotionRealTime ?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## gravityAcceleration

```TypeScript
gravityAcceleration?: double[]
```

Gravity acceleration of user motion status, in m/s².

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-gravityAcceleration?: double[]--><!--Device-UserEmotionData-gravityAcceleration?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## isRealTime

```TypeScript
isRealTime?: boolean
```

Whether emotion data is real-time.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-isRealTime?: boolean--><!--Device-UserEmotionData-isRealTime?: boolean-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## linearAcceleration

```TypeScript
linearAcceleration?: double[][]
```

Linear acceleration of user motion status, in m/s².

**类型：** ArkTS-Dyn: number[][]  <br>ArkTS-Sta：double[][]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-linearAcceleration?: double[][]--><!--Device-UserEmotionData-linearAcceleration?: double[][]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

