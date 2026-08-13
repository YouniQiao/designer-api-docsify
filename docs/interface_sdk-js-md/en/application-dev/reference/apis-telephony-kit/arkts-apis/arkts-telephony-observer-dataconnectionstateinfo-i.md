# DataConnectionStateInfo

Defines information about the data connection status.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

Network type.

**Type:** [RatType](arkts-telephony-observer-rattype-t.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataConnectionStateInfo-network: RatType--><!--Device-DataConnectionStateInfo-network: RatType-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: DataConnectState
```

Data connection status.

**Type:** DataConnectState

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataConnectionStateInfo-state: DataConnectState--><!--Device-DataConnectionStateInfo-state: DataConnectState-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

