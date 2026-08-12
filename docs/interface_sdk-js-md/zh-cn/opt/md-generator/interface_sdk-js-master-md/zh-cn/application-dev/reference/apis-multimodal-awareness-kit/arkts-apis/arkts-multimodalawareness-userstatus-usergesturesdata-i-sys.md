# UserGesturesData（系统接口）

用户手势数据。

**继承/实现关系：** UserGesturesData extends [UserFacesData](arkts-multimodalawareness-userstatus-userfacesdata-i-sys.md#UserFacesData)

**起始版本：** 26.0.0

<!--Device-userStatus-export interface UserGesturesData extends UserFacesData--><!--Device-userStatus-export interface UserGesturesData extends UserFacesData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## directionAngle

```TypeScript
directionAngle?: number[]
```

用户手势与屏幕方向之间的角度。取值范围为0到90，单位：度。

**类型：** number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-directionAngle?: double[]--><!--Device-UserGesturesData-directionAngle?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## gestureSpeed

```TypeScript
gestureSpeed?: number[]
```

手势速度，单位：帧/秒（fps）。

**类型：** number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-gestureSpeed?: double[]--><!--Device-UserGesturesData-gestureSpeed?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## handPosition

```TypeScript
handPosition?: number[]
```

手部相对于屏幕的位置。归一化坐标系范围为0到640。

**类型：** number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-handPosition?: double[]--><!--Device-UserGesturesData-handPosition?: double[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## handType

```TypeScript
handType?: number
```

用户静态手势类型。取值范围为0到3。0：手掌，1：握拳，2：剪刀，3：比心。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-handType?: int--><!--Device-UserGesturesData-handType?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## isHandExist

```TypeScript
isHandExist?: boolean
```

用户手部是否存在。

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-isHandExist?: boolean--><!--Device-UserGesturesData-isHandExist?: boolean-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## motionGesture

```TypeScript
motionGesture?: number
```

用户动态手势类型。取值范围为0到3。0：上滑，1：下滑，2：截屏，3：释放。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserGesturesData-motionGesture?: int--><!--Device-UserGesturesData-motionGesture?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。
