# GetReportData

Describe the GET_REPORT data is received from remote host.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

<!--Device-hid-interface GetReportData--><!--Device-hid-interface GetReportData-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { hid } from '@kit.ConnectivityKit';
```

## bufferSize

```TypeScript
bufferSize: int
```

bufferSize of GET_REPORT data, maximum number of octets to transfer during data phase.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetReportData-bufferSize: int--><!--Device-GetReportData-bufferSize: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## id

```TypeScript
id: int
```

id of GET_REPORT data.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetReportData-id: int--><!--Device-GetReportData-id: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## type

```TypeScript
type: ReportType
```

reportType of GET_REPORT data.

**Type:** ReportType

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetReportData-type: ReportType--><!--Device-GetReportData-type: ReportType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

