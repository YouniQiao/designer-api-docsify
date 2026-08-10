# DiscoveryEventInfo

Defines the discovery events information of mDNS services.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-mdns-export interface DiscoveryEventInfo--><!--Device-mdns-export interface DiscoveryEventInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## errorCode

```TypeScript
errorCode?: MdnsError
```

The mDNS error information.

**类型：** [MdnsError](arkts-network-mdns-mdnserror-e.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-DiscoveryEventInfo-errorCode?: MdnsError--><!--Device-DiscoveryEventInfo-errorCode?: MdnsError-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## serviceInfo

```TypeScript
serviceInfo: LocalServiceInfo
```

Information about the mDNS service.

**类型：** [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-DiscoveryEventInfo-serviceInfo: LocalServiceInfo--><!--Device-DiscoveryEventInfo-serviceInfo: LocalServiceInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

