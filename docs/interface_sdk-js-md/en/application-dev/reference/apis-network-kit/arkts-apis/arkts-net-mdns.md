# @ohos.net.mdns(MDNS Management)

Multicast DNS (MDNS) provides functions such as adding, removing, discovering, and resolving local services on a LAN.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.MDNS

## Modules to Import

```TypeScript
import mdns from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addLocalService(MDNS Management)](arkts-network-mdns-addlocalservice-f.md) | Adds an MDNS service. This API uses an asynchronous callback to return the result. |
| [addLocalService(MDNS Management)](arkts-network-mdns-addlocalservice-f.md) | Adds an MDNS service. This API uses a promise to return the result. |
| [createDiscoveryService(MDNS Management)](arkts-network-mdns-creatediscoveryservice-f.md) | Creates a **DiscoveryService** object, which is used to discover MDNS services of the specified type. |
| [removeLocalService(MDNS Management)](arkts-network-mdns-removelocalservice-f.md) | Removes an MDNS service. This API uses an asynchronous callback to return the result. |
| [removeLocalService(MDNS Management)](arkts-network-mdns-removelocalservice-f.md) | Removes an MDNS service. This API uses a promise to return the result. |
| [resolveLocalService(MDNS Management)](arkts-network-mdns-resolvelocalservice-f.md) | Resolves an MDNS service. This API uses an asynchronous callback to return the result. |
| [resolveLocalService(MDNS Management)](arkts-network-mdns-resolvelocalservice-f.md) | Resolves an MDNS service. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [DiscoveryEventInfo(MDNS Management)](arkts-network-mdns-discoveryeventinfo-i.md) | Defines the MDNS service event information. |
| [DiscoveryService(MDNS Management)](arkts-network-mdns-discoveryservice-i.md) | Defines a **DiscoveryService** object for discovering MDNS services of the specified type. |
| [LocalServiceInfo(MDNS Management)](arkts-network-mdns-localserviceinfo-i.md) | MDNS service information. |
| [ServiceAttribute(MDNS Management)](arkts-network-mdns-serviceattribute-i.md) | MDNS service attribute information. |

### Enums

| Name | Description |
| --- | --- |
| [MdnsError(MDNS Management)](arkts-network-mdns-mdnserror-e.md) | Defines the MDNS error information. |

### Types

| Name | Description |
| --- | --- |
| [NetAddress(MDNS Management)](arkts-network-mdns-netaddress-t.md) | Obtains the network address. |
