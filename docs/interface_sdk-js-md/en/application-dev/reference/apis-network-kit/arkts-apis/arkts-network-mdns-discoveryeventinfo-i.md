# DiscoveryEventInfo

Defines the discovery events information of mDNS services.

**Since:** 11

<!--Device-mdns-export interface DiscoveryEventInfo--><!--Device-mdns-export interface DiscoveryEventInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.MDNS

## Modules to Import

```TypeScript
import { mdns } from '@kit.NetworkKit';
```

## errorCode

```TypeScript
errorCode?: MdnsError
```

The mDNS error information.

**Type:** MdnsError

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DiscoveryEventInfo-errorCode?: MdnsError--><!--Device-DiscoveryEventInfo-errorCode?: MdnsError-End-->

**System capability:** SystemCapability.Communication.NetManager.MDNS

## serviceInfo

```TypeScript
serviceInfo: LocalServiceInfo
```

Information about the mDNS service.

**Type:** LocalServiceInfo

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DiscoveryEventInfo-serviceInfo: LocalServiceInfo--><!--Device-DiscoveryEventInfo-serviceInfo: LocalServiceInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.MDNS

