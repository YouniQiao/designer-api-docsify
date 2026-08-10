# ScanOptions

Describes the parameters for scan.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.ScanOptions

<!--Device-bluetooth-interface ScanOptions--><!--Device-bluetooth-interface ScanOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## dutyMode

```TypeScript
dutyMode?: ScanDuty
```

Bluetooth LE scan mode

**类型：** [ScanDuty](arkts-connectivity-ble-scanduty-e.md)

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.ScanOptions.dutyMode

<!--Device-ScanOptions-dutyMode?: ScanDuty--><!--Device-ScanOptions-dutyMode?: ScanDuty-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Time of delay for reporting the scan result

**类型：** number

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.ScanOptions.interval

<!--Device-ScanOptions-interval?: number--><!--Device-ScanOptions-interval?: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## matchMode

```TypeScript
matchMode?: MatchMode
```

Match mode for Bluetooth LE scan filters hardware match

**类型：** [MatchMode](arkts-connectivity-ble-matchmode-e.md)

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.ScanOptions.matchMode

<!--Device-ScanOptions-matchMode?: MatchMode--><!--Device-ScanOptions-matchMode?: MatchMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

