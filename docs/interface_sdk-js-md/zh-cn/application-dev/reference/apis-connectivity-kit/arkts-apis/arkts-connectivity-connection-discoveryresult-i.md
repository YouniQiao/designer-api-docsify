# DiscoveryResult

Describes the contents of the discovery results

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-connection-interface DiscoveryResult--><!--Device-connection-interface DiscoveryResult-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## deviceClass

```TypeScript
deviceClass: DeviceClass
```

The class of the device

**类型：** [DeviceClass](arkts-connectivity-connection-deviceclass-i.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DiscoveryResult-deviceClass: DeviceClass--><!--Device-DiscoveryResult-deviceClass: DeviceClass-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Identify of the discovery device

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DiscoveryResult-deviceId: string--><!--Device-DiscoveryResult-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceName

```TypeScript
deviceName: string
```

The local name of the device

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DiscoveryResult-deviceName: string--><!--Device-DiscoveryResult-deviceName: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rssi

```TypeScript
rssi: int
```

RSSI of the remote device

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DiscoveryResult-rssi: int--><!--Device-DiscoveryResult-rssi: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

