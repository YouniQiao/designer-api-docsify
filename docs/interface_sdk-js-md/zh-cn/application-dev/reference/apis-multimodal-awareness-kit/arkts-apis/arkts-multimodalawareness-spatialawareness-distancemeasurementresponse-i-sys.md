# DistanceMeasurementResponse（系统接口）

Interface for distance measurement result

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-spatialAwareness-export interface DistanceMeasurementResponse--><!--Device-spatialAwareness-export interface DistanceMeasurementResponse-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## confidence

```TypeScript
confidence: float
```

indicates confidence of distance measurement

**类型：** float

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementResponse-confidence: float--><!--Device-DistanceMeasurementResponse-confidence: float-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## deviceId

```TypeScript
deviceId: string
```

indicates the ID of the remote ranging device

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementResponse-deviceId: string--><!--Device-DistanceMeasurementResponse-deviceId: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## distance

```TypeScript
distance: float
```

indicates distance result

**类型：** float

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementResponse-distance: float--><!--Device-DistanceMeasurementResponse-distance: float-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## rank

```TypeScript
rank: DistanceRank
```

indicates distance rank

**类型：** [DistanceRank](arkts-multimodalawareness-spatialawareness-distancerank-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementResponse-rank: DistanceRank--><!--Device-DistanceMeasurementResponse-rank: DistanceRank-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

