# DataConnectionStateInfo

Indicates cellular data connect state and technology type.

**Since:** 11

<!--Device-observer-export interface DataConnectionStateInfo--><!--Device-observer-export interface DataConnectionStateInfo-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## network

```TypeScript
network: RatType
```

Indicates technology type.

**Type:** RatType

**Since:** 11

<!--Device-DataConnectionStateInfo-network: RatType--><!--Device-DataConnectionStateInfo-network: RatType-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: DataConnectState
```

Indicates cellular data connect state.

**Type:** DataConnectState

**Since:** 11

<!--Device-DataConnectionStateInfo-state: DataConnectState--><!--Device-DataConnectionStateInfo-state: DataConnectState-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

