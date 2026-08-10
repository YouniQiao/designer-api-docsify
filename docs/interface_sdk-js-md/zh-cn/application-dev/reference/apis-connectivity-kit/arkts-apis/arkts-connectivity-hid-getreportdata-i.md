# GetReportData

Describe the GET_REPORT data is received from remote host.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-hid-interface GetReportData--><!--Device-hid-interface GetReportData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## bufferSize

```TypeScript
bufferSize: int
```

bufferSize of GET_REPORT data, maximum number of octets to transfer during data phase.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GetReportData-bufferSize: int--><!--Device-GetReportData-bufferSize: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## id

```TypeScript
id: int
```

id of GET_REPORT data.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GetReportData-id: int--><!--Device-GetReportData-id: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## type

```TypeScript
type: ReportType
```

reportType of GET_REPORT data.

**类型：** [ReportType](arkts-connectivity-hid-reporttype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GetReportData-type: ReportType--><!--Device-GetReportData-type: ReportType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

