# ScanReport

Describes the contents of the scan report.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-ble-interface ScanReport--><!--Device-ble-interface ScanReport-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## reportType

```TypeScript
reportType: ScanReportType
```

The type of scan report

**类型：** [ScanReportType](arkts-connectivity-ble-scanreporttype-e.md)

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ScanReport-reportType: ScanReportType--><!--Device-ScanReport-reportType: ScanReportType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## scanResult

```TypeScript
scanResult: Array<ScanResult>
```

Describes the contents of the scan results.

**类型：** Array&lt;ScanResult&gt;

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ScanReport-scanResult: Array<ScanResult>--><!--Device-ScanReport-scanResult: Array<ScanResult>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

