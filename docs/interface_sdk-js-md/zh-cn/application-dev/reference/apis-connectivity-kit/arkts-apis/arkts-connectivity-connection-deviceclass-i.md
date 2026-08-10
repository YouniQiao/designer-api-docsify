# DeviceClass

Describes the class of a bluetooth device.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-connection-interface DeviceClass--><!--Device-connection-interface DeviceClass-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## classOfDevice

```TypeScript
classOfDevice: int
```

Class of the device.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceClass-classOfDevice: int--><!--Device-DeviceClass-classOfDevice: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## majorClass

```TypeScript
majorClass: MajorClass
```

Major classes of Bluetooth devices.

**类型：** [MajorClass](arkts-connectivity-bluetoothmanager-majorclass-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceClass-majorClass: MajorClass--><!--Device-DeviceClass-majorClass: MajorClass-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## majorMinorClass

```TypeScript
majorMinorClass: MajorMinorClass
```

Major and minor classes of Bluetooth devices.

**类型：** [MajorMinorClass](arkts-connectivity-bluetooth-majorminorclass-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceClass-majorMinorClass: MajorMinorClass--><!--Device-DeviceClass-majorMinorClass: MajorMinorClass-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

