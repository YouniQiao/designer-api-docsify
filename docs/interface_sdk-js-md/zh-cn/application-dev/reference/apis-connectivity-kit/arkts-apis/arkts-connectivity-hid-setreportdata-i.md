# SetReportData

Describe the SET_REPORT data is received from remote host.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-hid-interface SetReportData--><!--Device-hid-interface SetReportData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## data

```TypeScript
data: Uint8Array
```

data of SET_REPORT data.

**类型：** Uint8Array

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SetReportData-data: Uint8Array--><!--Device-SetReportData-data: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## id

```TypeScript
id: int
```

id of SET_REPORT data.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SetReportData-id: int--><!--Device-SetReportData-id: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## type

```TypeScript
type: ReportType
```

reportType of SET_REPORT data.

**类型：** [ReportType](arkts-connectivity-hid-reporttype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SetReportData-type: ReportType--><!--Device-SetReportData-type: ReportType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

