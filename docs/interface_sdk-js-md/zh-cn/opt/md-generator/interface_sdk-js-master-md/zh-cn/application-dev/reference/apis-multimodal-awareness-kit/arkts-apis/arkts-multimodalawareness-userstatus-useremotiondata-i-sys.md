# UserEmotionData（系统接口）

用户情绪数据。

**继承/实现关系：** UserEmotionData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#UserStatusData)

**起始版本：** 26.0.0

<!--Device-userStatus-export interface UserEmotionData extends UserStatusData--><!--Device-userStatus-export interface UserEmotionData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## confidence

```TypeScript
confidence?: number
```

用户情绪置信度。取值范围为0到100，值越大表示置信度越高。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-confidence?: int--><!--Device-UserEmotionData-confidence?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## emotionNonRealTime

```TypeScript
emotionNonRealTime ?: number[]
```

用户非实时情绪级别。取值范围为0到5。0：非常开心，1：有些开心，2：平静，3：有些不开心，4：生气，5：哭泣。

**类型：** number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-emotionNonRealTime ?: int[]--><!--Device-UserEmotionData-emotionNonRealTime ?: int[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## emotionRealTime

```TypeScript
emotionRealTime ?: number
```

用户实时情绪级别。取值范围为0到5。0：非常开心，1：有些开心，2：平静，3：有些不开心，4：生气，5：哭泣。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-emotionRealTime ?: int--><!--Device-UserEmotionData-emotionRealTime ?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## gravityAcceleration

```TypeScript
gravityAcceleration?: number[]
```

用户运动状态的重力加速度，单位：m/s²。

**类型：** number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-gravityAcceleration?: double[]--><!--Device-UserEmotionData-gravityAcceleration?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## isRealTime

```TypeScript
isRealTime?: boolean
```

情绪数据是否为实时数据。

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-isRealTime?: boolean--><!--Device-UserEmotionData-isRealTime?: boolean-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## linearAcceleration

```TypeScript
linearAcceleration?: number[][]
```

用户运动状态的线性加速度，单位：m/s²。

**类型：** number[][]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserEmotionData-linearAcceleration?: double[][]--><!--Device-UserEmotionData-linearAcceleration?: double[][]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。
