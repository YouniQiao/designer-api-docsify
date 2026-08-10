# StateChangeParam

Profile state change parameters.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-baseProfile-export interface StateChangeParam--><!--Device-baseProfile-export interface StateChangeParam-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { baseProfile } from 'kits/@kit.ConnectivityKit';
```

## cause

```TypeScript
cause: DisconnectCause
```

Cause of disconnect

**类型：** [DisconnectCause](arkts-connectivity-baseprofile-disconnectcause-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StateChangeParam-cause: DisconnectCause--><!--Device-StateChangeParam-cause: DisconnectCause-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

The address of device

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StateChangeParam-deviceId: string--><!--Device-StateChangeParam-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## role

```TypeScript
role?: PanRole
```

PAN role of the device

**类型：** [PanRole](arkts-connectivity-baseprofile-panrole-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StateChangeParam-role?: PanRole--><!--Device-StateChangeParam-role?: PanRole-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Profile state value

**类型：** [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StateChangeParam-state: ProfileConnectionState--><!--Device-StateChangeParam-state: ProfileConnectionState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

