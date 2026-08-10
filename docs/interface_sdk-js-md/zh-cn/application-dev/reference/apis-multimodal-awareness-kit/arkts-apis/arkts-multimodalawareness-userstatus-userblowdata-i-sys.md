# UserBlowData（系统接口）

Defines user blow data.

**继承/实现关系：** UserBlowData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface UserBlowData extends UserStatusData--><!--Device-userStatus-export interface UserBlowData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## blowDirection

```TypeScript
blowDirection?: int
```

Blow direction.The value ranges from 0 to 2. 0: Not blowing, 1: Blowing from bottom mic, 2: Blowing from top mic.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-blowDirection?: int--><!--Device-UserBlowData-blowDirection?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## emotion

```TypeScript
emotion?: int
```

User emotion level.The value ranges from 0 to 5. 0: Very happy, 1: A little happy, 2: Calm,3: A little unhappy, 4: Angry, 5: Crying.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-emotion?: int--><!--Device-UserBlowData-emotion?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## facePosition

```TypeScript
facePosition?: double[]
```

Face position relative to screen.The normalized coordinate system ranges from 0 to 640.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：double[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-facePosition?: double[]--><!--Device-UserBlowData-facePosition?: double[]-End-->

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

<!--Device-UserBlowData-gravityAcceleration?: double[]--><!--Device-UserBlowData-gravityAcceleration?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## isGazeStatus

```TypeScript
isGazeStatus?: boolean
```

Whether user is gazing at screen.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-isGazeStatus?: boolean--><!--Device-UserBlowData-isGazeStatus?: boolean-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## linearAcceleration

```TypeScript
linearAcceleration?: double[][]
```

Linear acceleration of user motion status, in m/s²..

**类型：** ArkTS-Dyn: number[][]  <br>ArkTS-Sta：double[][]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-linearAcceleration?: double[][]--><!--Device-UserBlowData-linearAcceleration?: double[][]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## strengthLevel

```TypeScript
strengthLevel?: int
```

Blow strength level.The value must be an integer within [1,12].

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserBlowData-strengthLevel?: int--><!--Device-UserBlowData-strengthLevel?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

