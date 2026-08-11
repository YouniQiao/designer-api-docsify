# DataConnectionStateInfo

Indicates cellular data connect state and technology type.

**Since:** 11

<!--Device-observer-export interface DataConnectionStateInfo--><!--Device-observer-export interface DataConnectionStateInfo-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## network

```TypeScript
network: RatType
```

Indicates technology type.

**Type:** [RatType](arkts-telephony-observer-rattype-t.md)

**Since:** 11

<!--Device-DataConnectionStateInfo-network: RatType--><!--Device-DataConnectionStateInfo-network: RatType-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: DataConnectState
```

Indicates cellular data connect state.

**Type:** [DataConnectState](arkts-telephony-data-dataconnectstate-e.md)

**Since:** 11

<!--Device-DataConnectionStateInfo-state: DataConnectState--><!--Device-DataConnectionStateInfo-state: DataConnectState-End-->

**System capability:** SystemCapability.Telephony.StateRegistry
