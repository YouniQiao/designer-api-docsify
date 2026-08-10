# @ohos.net.mdns

Provides interfaces to discover DNS based services on a local network over Multicast DNS.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-unnamed-declare namespace mdns--><!--Device-unnamed-declare namespace mdns-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [addLocalService](arkts-network-mdns-addlocalservice-f.md#addlocalservice) | Adds an mDNS service. |
| [addLocalService](arkts-network-mdns-addlocalservice-f.md#addlocalservice-1) | Adds an mDNS service. |
| [createDiscoveryService](arkts-network-mdns-creatediscoveryservice-f.md#creatediscoveryservice) | Create an mDNS based discovery service with context and serviceType. |
| [removeLocalService](arkts-network-mdns-removelocalservice-f.md#removelocalservice) | Removes an mDNS service. |
| [removeLocalService](arkts-network-mdns-removelocalservice-f.md#removelocalservice-1) | Removes an mDNS service. |
| [resolveLocalService](arkts-network-mdns-resolvelocalservice-f.md#resolvelocalservice) | Resolves an mDNS service. |
| [resolveLocalService](arkts-network-mdns-resolvelocalservice-f.md#resolvelocalservice-1) | Resolves an mDNS service. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [DiscoveryEventInfo](arkts-network-mdns-discoveryeventinfo-i.md) | Defines the discovery events information of mDNS services. |
| [DiscoveryService](arkts-network-mdns-discoveryservice-i.md) | Defines a DiscoveryService object for discovering mDNS services of the specified type. |
| [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | Defines the mDNS service information. |
| [ServiceAttribute](arkts-network-mdns-serviceattribute-i.md) | Defines the mDNS service attribute information. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [MdnsError](arkts-network-mdns-mdnserror-e.md) | Defines the mDNS error information. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [NetAddress](arkts-network-mdns-netaddress-t.md) | Get a network address. |

