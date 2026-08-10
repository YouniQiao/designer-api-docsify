# UserFaceAngleData（系统接口）

Defines user face angle data.

**继承/实现关系：** UserFaceAngleData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface UserFaceAngleData extends UserStatusData--><!--Device-userStatus-export interface UserFaceAngleData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## hpeNetworkId

```TypeScript
hpeNetworkId: string
```

Network ID of device that user head is facing.The maximum length is 128.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserFaceAngleData-hpeNetworkId: string--><!--Device-UserFaceAngleData-hpeNetworkId: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

