# ScanOptions

Describes the parameters for scan.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface ScanOptions--><!--Device-ble-interface ScanOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## dutyMode

```TypeScript
dutyMode?: ScanDuty
```

Bluetooth LE scan mode

**类型：** [ScanDuty](arkts-connectivity-ble-scanduty-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-dutyMode?: ScanDuty--><!--Device-ScanOptions-dutyMode?: ScanDuty-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: int
```

Time of delay for reporting the scan result

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-interval?: int--><!--Device-ScanOptions-interval?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## isExtended

```TypeScript
isExtended?: boolean
```

Indicates whether the scan is extended, default is {@code false}

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-isExtended?: boolean--><!--Device-ScanOptions-isExtended?: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## matchMode

```TypeScript
matchMode?: MatchMode
```

Match mode for Bluetooth LE scan filters hardware match

**类型：** [MatchMode](arkts-connectivity-ble-matchmode-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-matchMode?: MatchMode--><!--Device-ScanOptions-matchMode?: MatchMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## phyType

```TypeScript
phyType?: PhyType
```

Physical Layer used during scan.

**类型：** [PhyType](arkts-connectivity-ble-phytype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-phyType?: PhyType--><!--Device-ScanOptions-phyType?: PhyType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## reportMode

```TypeScript
reportMode?: ScanReportMode
```

Report mode used during scan.

**类型：** [ScanReportMode](arkts-connectivity-ble-scanreportmode-e.md)

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ScanOptions-reportMode?: ScanReportMode--><!--Device-ScanOptions-reportMode?: ScanReportMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

