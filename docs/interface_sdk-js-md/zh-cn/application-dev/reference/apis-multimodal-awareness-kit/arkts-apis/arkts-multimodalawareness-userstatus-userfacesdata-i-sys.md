# UserFacesData（系统接口）

Defines user face data.

**继承/实现关系：** UserFacesData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface UserFacesData extends UserStatusData--><!--Device-userStatus-export interface UserFacesData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## angularVelocity

```TypeScript
angularVelocity?: double[]
```

Angular velocity of user motion status, in rad/s.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-angularVelocity?: double[]--><!--Device-UserFacesData-angularVelocity?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## azimuth

```TypeScript
azimuth?: double[]
```

Azimuth of user motion status.The value ranges from 0 to 360, in degrees.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-azimuth?: double[]--><!--Device-UserFacesData-azimuth?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## faceNum

```TypeScript
faceNum?: int
```

Number of faces detected.The value must be an integer within [0,3].

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-faceNum?: int--><!--Device-UserFacesData-faceNum?: int-End-->

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

<!--Device-UserFacesData-gravityAcceleration?: double[]--><!--Device-UserFacesData-gravityAcceleration?: double[]-End-->

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

<!--Device-UserFacesData-linearAcceleration?: double[][]--><!--Device-UserFacesData-linearAcceleration?: double[][]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## visualAngle

```TypeScript
visualAngle?: double[]
```

User visual angle.The value ranges from 0 to 90, in degrees.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFacesData-visualAngle?: double[]--><!--Device-UserFacesData-visualAngle?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

