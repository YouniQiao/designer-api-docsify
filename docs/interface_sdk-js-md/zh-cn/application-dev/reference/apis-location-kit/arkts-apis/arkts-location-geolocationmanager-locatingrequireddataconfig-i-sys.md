# LocatingRequiredDataConfig（系统接口）

Describes the request parameters for obtaining the data required for locating.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface LocatingRequiredDataConfig--><!--Device-geoLocationManager-export interface LocatingRequiredDataConfig-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## arfcn

```TypeScript
arfcn?: int[]
```

Indicates absolute radio frequency channel number (ARFCN).Querying Cell Information by Specified ARFCN.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredDataConfig-arfcn?: int[]--><!--Device-LocatingRequiredDataConfig-arfcn?: int[]-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## needStartScan

```TypeScript
needStartScan: boolean
```

Indicates whether to start scanning.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredDataConfig-needStartScan: boolean--><!--Device-LocatingRequiredDataConfig-needStartScan: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## plmnId

```TypeScript
plmnId?: int[]
```

Indicates PLMN number of the SIM card.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredDataConfig-plmnId?: int[]--><!--Device-LocatingRequiredDataConfig-plmnId?: int[]-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## scanInterval

```TypeScript
scanInterval?: int
```

Indicates the interval between scans. The unit is millisecond.This parameter needs to be set only when scanning information is continuously monitored.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredDataConfig-scanInterval?: int--><!--Device-LocatingRequiredDataConfig-scanInterval?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## scanTimeout

```TypeScript
scanTimeout?: int
```

Indicates the timeout period of a single scan. The unit is millisecond. The default value is 10000.This parameter needs to be set only when getLocatingRequiredData is used.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredDataConfig-scanTimeout?: int--><!--Device-LocatingRequiredDataConfig-scanTimeout?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## slotId

```TypeScript
slotId?: int
```

Indicates SIM card slot number.The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredDataConfig-slotId?: int--><!--Device-LocatingRequiredDataConfig-slotId?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: LocatingRequiredDataType
```

Indicates the type of locating required data.

**类型：** [LocatingRequiredDataType](arkts-location-geolocationmanager-locatingrequireddatatype-e-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredDataConfig-type: LocatingRequiredDataType--><!--Device-LocatingRequiredDataConfig-type: LocatingRequiredDataType-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

