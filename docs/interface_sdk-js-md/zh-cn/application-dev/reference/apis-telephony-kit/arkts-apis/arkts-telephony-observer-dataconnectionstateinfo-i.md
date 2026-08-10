# DataConnectionStateInfo

Indicates cellular data connect state and technology type.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-observer-export interface DataConnectionStateInfo--><!--Device-observer-export interface DataConnectionStateInfo-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## network

```TypeScript
network: RatType
```

Indicates technology type.

**类型：** [RatType](arkts-telephony-observer-rattype-t.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-DataConnectionStateInfo-network: RatType--><!--Device-DataConnectionStateInfo-network: RatType-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: DataConnectState
```

Indicates cellular data connect state.

**类型：** [DataConnectState](arkts-telephony-data-dataconnectstate-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-DataConnectionStateInfo-state: DataConnectState--><!--Device-DataConnectionStateInfo-state: DataConnectState-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

