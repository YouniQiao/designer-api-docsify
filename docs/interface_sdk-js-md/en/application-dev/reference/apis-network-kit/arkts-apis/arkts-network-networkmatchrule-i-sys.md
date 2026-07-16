# NetworkMatchRule (System API)

The matching rules of network quota policies.

**Since:** 10

<!--Device-policy-export interface NetworkMatchRule--><!--Device-policy-export interface NetworkMatchRule-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## identity

```TypeScript
identity: string
```

To specify the identity of network, such as different WLAN.

**Type:** string

**Since:** 10

<!--Device-NetworkMatchRule-identity: string--><!--Device-NetworkMatchRule-identity: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## netType

```TypeScript
netType: NetBearType
```

netType see {@link NetBearType}.

**Type:** NetBearType

**Since:** 10

<!--Device-NetworkMatchRule-netType: NetBearType--><!--Device-NetworkMatchRule-netType: NetBearType-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## simId

```TypeScript
simId: string
```

The ID of the target card, valid when netType is BEARER_CELLULAR.

**Type:** string

**Since:** 10

<!--Device-NetworkMatchRule-simId: string--><!--Device-NetworkMatchRule-simId: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

