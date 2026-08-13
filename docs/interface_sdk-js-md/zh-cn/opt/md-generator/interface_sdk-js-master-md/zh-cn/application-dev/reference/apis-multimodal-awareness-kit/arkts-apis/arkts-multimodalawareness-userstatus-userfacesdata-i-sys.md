# UserFacesData（系统接口）

用户面部数据。

**继承/实现关系：** UserFacesData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#UserStatusData（系统接口）)

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-userStatus-export interface UserFacesData--><!--Device-userStatus-export interface UserFacesData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## angularVelocity

```TypeScript
angularVelocity?: number[]
```

用户运动状态的角速度，单位：rad/s。

**类型：** number[]

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-angularVelocity?: double[]--><!--Device-UserFacesData-angularVelocity?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## azimuth

```TypeScript
azimuth?: number[]
```

用户运动状态的方位角。取值范围为0到360，单位：度。

**类型：** number[]

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-azimuth?: double[]--><!--Device-UserFacesData-azimuth?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## faceNum

```TypeScript
faceNum?: number
```

检测到的面部数量。取值范围为[0,3]的整数。

**类型：** number

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-faceNum?: int--><!--Device-UserFacesData-faceNum?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## gravityAcceleration

```TypeScript
gravityAcceleration?: number[]
```

用户运动状态的重力加速度，单位：m/s²。

**类型：** number[]

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-gravityAcceleration?: double[]--><!--Device-UserFacesData-gravityAcceleration?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## linearAcceleration

```TypeScript
linearAcceleration?: number[][]
```

用户运动状态的线性加速度，单位：m/s²。

**类型：** number[][]

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-linearAcceleration?: double[][]--><!--Device-UserFacesData-linearAcceleration?: double[][]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## visualAngle

```TypeScript
visualAngle?: number[]
```

用户视角。取值范围为0到90，单位：度。

**类型：** number[]

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-visualAngle?: double[]--><!--Device-UserFacesData-visualAngle?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。
