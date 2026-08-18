# NetSpecifier

Provides an instance that bear data network capabilities.

**Since:** 23

<!--Device-connection-export interface NetSpecifier--><!--Device-connection-export interface NetSpecifier-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## bearerPrivateIdentifier

```TypeScript
bearerPrivateIdentifier?: string
```

Network identifier, the identifier for Wi Fi networks is "wifi", and the identifier for cellular networks is "simId1" (corresponding to SIM card 1).

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetSpecifier-bearerPrivateIdentifier?: string--><!--Device-NetSpecifier-bearerPrivateIdentifier?: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## netCapabilities

```TypeScript
netCapabilities: NetCapabilities
```

The transmission capacity and support of the network's global proxy storage data network.

**Type:** [NetCapabilities](arkts-network-connection-netcapabilities-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetSpecifier-netCapabilities: NetCapabilities--><!--Device-NetSpecifier-netCapabilities: NetCapabilities-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

