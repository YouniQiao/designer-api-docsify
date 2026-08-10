# AclStateResult

Acl state change result.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-connection-interface AclStateResult--><!--Device-connection-interface AclStateResult-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## deviceId

```TypeScript
deviceId: string
```

The virtual address of a Bluetooth device. For example, "11:22:33:AA:BB:FF".

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AclStateResult-deviceId: string--><!--Device-AclStateResult-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: AclState
```

Acl state of the device.

**类型：** [AclState](arkts-connectivity-connection-aclstate-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AclStateResult-state: AclState--><!--Device-AclStateResult-state: AclState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

