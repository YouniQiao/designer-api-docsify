# WifiP2pGroupInfo

P2P group information.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-wifiManager-interface WifiP2pGroupInfo--><!--Device-wifiManager-interface WifiP2pGroupInfo-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## clientDevices

```TypeScript
clientDevices: WifiP2pDevice[]
```

Client list

**类型：** [WifiP2pDevice](arkts-connectivity-wifimanager-wifip2pdevice-i.md)[]

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-clientDevices: WifiP2pDevice[]--><!--Device-WifiP2pGroupInfo-clientDevices: WifiP2pDevice[]-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## frequency

```TypeScript
frequency: int
```

Frequency

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-frequency: int--><!--Device-WifiP2pGroupInfo-frequency: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## goIpAddress

```TypeScript
goIpAddress: string
```

Group owner IP address

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-goIpAddress: string--><!--Device-WifiP2pGroupInfo-goIpAddress: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## groupName

```TypeScript
groupName: string
```

Group name

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-groupName: string--><!--Device-WifiP2pGroupInfo-groupName: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## interface

```TypeScript
interface: string
```

Interface name

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-WifiP2pGroupInfo-interface: string--><!--Device-WifiP2pGroupInfo-interface: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## interfaceName

```TypeScript
interfaceName: string
```

Interface name

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WifiP2pGroupInfo-interfaceName: string--><!--Device-WifiP2pGroupInfo-interfaceName: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## isP2pGo

```TypeScript
isP2pGo: boolean
```

Indicates whether it is group owner

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-isP2pGo: boolean--><!--Device-WifiP2pGroupInfo-isP2pGo: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## networkId

```TypeScript
networkId: int
```

Network ID

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-networkId: int--><!--Device-WifiP2pGroupInfo-networkId: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## ownerInfo

```TypeScript
ownerInfo: WifiP2pDevice
```

Group owner information

**类型：** [WifiP2pDevice](arkts-connectivity-wifimanager-wifip2pdevice-i.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-ownerInfo: WifiP2pDevice--><!--Device-WifiP2pGroupInfo-ownerInfo: WifiP2pDevice-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

## passphrase

```TypeScript
passphrase: string
```

The group passphrase

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiP2pGroupInfo-passphrase: string--><!--Device-WifiP2pGroupInfo-passphrase: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

