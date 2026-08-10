# DoorPositionResponse（系统接口）

Interface for indoor or outdoor identify result

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-spatialAwareness-export interface DoorPositionResponse--><!--Device-spatialAwareness-export interface DoorPositionResponse-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## deviceId

```TypeScript
deviceId: string
```

indicates the ID of the remote ranging device

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DoorPositionResponse-deviceId: string--><!--Device-DoorPositionResponse-deviceId: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## doorLockCode

```TypeScript
doorLockCode: int
```

indicates random code for unlocking the door

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DoorPositionResponse-doorLockCode: int--><!--Device-DoorPositionResponse-doorLockCode: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## position

```TypeScript
position: PositionRelativeToDoor
```

indicates result inside and outside the door

**类型：** [PositionRelativeToDoor](arkts-multimodalawareness-spatialawareness-positionrelativetodoor-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DoorPositionResponse-position: PositionRelativeToDoor--><!--Device-DoorPositionResponse-position: PositionRelativeToDoor-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

