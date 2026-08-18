# NetCapabilities

Defines the network capability set.

**Since:** 23

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

Network type. The array contains only one network type.

**Type:** Array&lt;NetBearType&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetCapabilities-bearerTypes: Array<NetBearType>--><!--Device-NetCapabilities-bearerTypes: Array<NetBearType>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## linkDownBandwidthKbps

```TypeScript
linkDownBandwidthKbps?: int
```

Downlink (network-to-device) bandwidth, in kbit/s. The value **0** indicates that the current network bandwidth cannot be evaluated.

**Type:** int

**Since:** 23

<!--Device-NetCapabilities-linkDownBandwidthKbps?: int--><!--Device-NetCapabilities-linkDownBandwidthKbps?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## linkUpBandwidthKbps

```TypeScript
linkUpBandwidthKbps?: int
```

Uplink (device-to-network) bandwidth, in kbit/s. The value **0** indicates that the current network bandwidth cannot be evaluated.

**Type:** int

**Since:** 23

<!--Device-NetCapabilities-linkUpBandwidthKbps?: int--><!--Device-NetCapabilities-linkUpBandwidthKbps?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## networkCap

```TypeScript
networkCap?: Array<NetCap>
```

Network capability.

**Type:** Array&lt;[NetCap](arkts-network-connection-netcap-e.md)&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetCapabilities-networkCap?: Array<NetCap>--><!--Device-NetCapabilities-networkCap?: Array<NetCap>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

