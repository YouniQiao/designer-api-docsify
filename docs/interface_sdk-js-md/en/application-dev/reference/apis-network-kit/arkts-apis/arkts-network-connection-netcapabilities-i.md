# NetCapabilities

Defines the network capability set.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-connection-export interface NetCapabilities--><!--Device-connection-export interface NetCapabilities-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## bearerTypes

```TypeScript
bearerTypes: Array<NetBearType>
```

Network type.

**Type:** Array&lt;NetBearType&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetCapabilities-bearerTypes: Array<NetBearType>--><!--Device-NetCapabilities-bearerTypes: Array<NetBearType>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## linkDownBandwidthKbps

```TypeScript
linkDownBandwidthKbps?: int
```

Downstream (network-to-device) bandwidth.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NetCapabilities-linkDownBandwidthKbps?: int--><!--Device-NetCapabilities-linkDownBandwidthKbps?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## linkUpBandwidthKbps

```TypeScript
linkUpBandwidthKbps?: int
```

Uplink (device-to-network) bandwidth.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NetCapabilities-linkUpBandwidthKbps?: int--><!--Device-NetCapabilities-linkUpBandwidthKbps?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## networkCap

```TypeScript
networkCap?: Array<NetCap>
```

Network-specific capabilities.

**Type:** Array&lt;[NetCap](arkts-network-connection-netcap-e.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetCapabilities-networkCap?: Array<NetCap>--><!--Device-NetCapabilities-networkCap?: Array<NetCap>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

