# BondStateParam

Describes the class of a bluetooth device.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-connection-interface BondStateParam--><!--Device-connection-interface BondStateParam-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## cause

```TypeScript
cause: UnbondCause
```

Cause of unbond.

**类型：** [UnbondCause](arkts-connectivity-connection-unbondcause-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BondStateParam-cause: UnbondCause--><!--Device-BondStateParam-cause: UnbondCause-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## causeMessage

```TypeScript
causeMessage?: string
```

Cause message of unbond.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BondStateParam-causeMessage?: string--><!--Device-BondStateParam-causeMessage?: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Address of a Bluetooth device.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BondStateParam-deviceId: string--><!--Device-BondStateParam-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: BondState
```

Profile connection state of the device.

**类型：** [BondState](arkts-connectivity-connection-bondstate-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BondStateParam-state: BondState--><!--Device-BondStateParam-state: BondState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

