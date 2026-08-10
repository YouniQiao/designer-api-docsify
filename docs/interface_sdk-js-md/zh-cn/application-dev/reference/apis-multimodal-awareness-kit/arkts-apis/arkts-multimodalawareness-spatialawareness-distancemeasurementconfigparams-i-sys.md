# DistanceMeasurementConfigParams（系统接口）

Configuration parameters for the distance measurement interface

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-spatialAwareness-export interface DistanceMeasurementConfigParams--><!--Device-spatialAwareness-export interface DistanceMeasurementConfigParams-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## deviceList

```TypeScript
deviceList: string[]
```

distance measurement supported devices list

**类型：** string[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementConfigParams-deviceList: string[]--><!--Device-DistanceMeasurementConfigParams-deviceList: string[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## reportFrequency

```TypeScript
reportFrequency: int
```

distance measurement result reporting frequency

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementConfigParams-reportFrequency: int--><!--Device-DistanceMeasurementConfigParams-reportFrequency: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## reportMode

```TypeScript
reportMode: ReportingMode
```

distance measurement result reporting mode

**类型：** [ReportingMode](arkts-multimodalawareness-spatialawareness-reportingmode-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementConfigParams-reportMode: ReportingMode--><!--Device-DistanceMeasurementConfigParams-reportMode: ReportingMode-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## techType

```TypeScript
techType: TechnologyType
```

distance measurement technology type

**类型：** [TechnologyType](arkts-multimodalawareness-spatialawareness-technologytype-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DistanceMeasurementConfigParams-techType: TechnologyType--><!--Device-DistanceMeasurementConfigParams-techType: TechnologyType-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

