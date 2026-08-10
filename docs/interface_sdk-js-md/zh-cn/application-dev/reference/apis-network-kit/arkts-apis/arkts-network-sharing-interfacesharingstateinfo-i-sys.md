# InterfaceSharingStateInfo（系统接口）

The interface is used to notify listeners of changes in shared interface status.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-sharing-export interface InterfaceSharingStateInfo--><!--Device-sharing-export interface InterfaceSharingStateInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## iface

```TypeScript
iface: string
```

The specified network interface name.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-InterfaceSharingStateInfo-iface: string--><!--Device-InterfaceSharingStateInfo-iface: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

## state

```TypeScript
state: SharingIfaceState
```

Network card sharing status.

**类型：** [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-InterfaceSharingStateInfo-state: SharingIfaceState--><!--Device-InterfaceSharingStateInfo-state: SharingIfaceState-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: SharingIfaceType
```

Enumerates the network sharing types of an NIC.

**类型：** [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-InterfaceSharingStateInfo-type: SharingIfaceType--><!--Device-InterfaceSharingStateInfo-type: SharingIfaceType-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

**系统接口：** 此接口为系统接口。

