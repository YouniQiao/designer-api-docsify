# ScanFilter

Describes the criteria for filtering scanning results can be set.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface ScanFilter--><!--Device-ble-interface ScanFilter-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## irk

```TypeScript
irk?: Uint8Array
```

Identity Resolving Key of BLE peripheral device.{@link ScanFilter#irk} needs to be used with {@link ScanFilter#address}.

**类型：** Uint8Array

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScanFilter-irk?: Uint8Array--><!--Device-ScanFilter-irk?: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

