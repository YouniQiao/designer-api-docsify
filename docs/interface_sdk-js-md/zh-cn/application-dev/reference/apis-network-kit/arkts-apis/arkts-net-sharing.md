# @ohos.net.sharing

Provides network sharing related interfaces.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace sharing--><!--Device-unnamed-declare namespace sharing-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetSharing

## 导入模块

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getSharableRegexes](arkts-network-sharing-getsharableregexes-f-sys.md#getsharableregexes) | Get a list regular expression that defines any interface that can support network sharing. |
| [getSharableRegexes](arkts-network-sharing-getsharableregexes-f-sys.md#getsharableregexes-1) | Get a list regular expression that defines any interface that can support network sharing. |
| [getSharingIfaces](arkts-network-sharing-getsharingifaces-f-sys.md#getsharingifaces) | Obtains the names of interfaces in each sharing state. |
| [getSharingIfaces](arkts-network-sharing-getsharingifaces-f-sys.md#getsharingifaces-1) | Obtains the names of interfaces in each sharing state. |
| [getSharingState](arkts-network-sharing-getsharingstate-f-sys.md#getsharingstate) | Obtains the network sharing state for given type. |
| [getSharingState](arkts-network-sharing-getsharingstate-f-sys.md#getsharingstate-1) | Obtains the network sharing state for given type. |
| [getStatsRxBytes](arkts-network-sharing-getstatsrxbytes-f-sys.md#getstatsrxbytes) | Obtains the number of downlink data bytes of the sharing network interfaces. |
| [getStatsRxBytes](arkts-network-sharing-getstatsrxbytes-f-sys.md#getstatsrxbytes-1) | Obtains the number of downlink data bytes of the sharing network interfaces. |
| [getStatsTotalBytes](arkts-network-sharing-getstatstotalbytes-f-sys.md#getstatstotalbytes) | Obtains the number of total data bytes of the sharing network interfaces. |
| [getStatsTotalBytes](arkts-network-sharing-getstatstotalbytes-f-sys.md#getstatstotalbytes-1) | Obtains the number of total data bytes of the sharing network interfaces. |
| [getStatsTxBytes](arkts-network-sharing-getstatstxbytes-f-sys.md#getstatstxbytes) | Obtains the number of uplink data bytes of the sharing network interfaces. |
| [getStatsTxBytes](arkts-network-sharing-getstatstxbytes-f-sys.md#getstatstxbytes-1) | Obtains the number of uplink data bytes of the sharing network interfaces. |
| [isSharing](arkts-network-sharing-issharing-f-sys.md#issharing) | Return the global network sharing state. |
| [isSharing](arkts-network-sharing-issharing-f-sys.md#issharing-1) | Return the global network sharing state. |
| [isSharingSupported](arkts-network-sharing-issharingsupported-f-sys.md#issharingsupported) | Checks whether this device allows for network sharing. |
| [isSharingSupported](arkts-network-sharing-issharingsupported-f-sys.md#issharingsupported-1) | Checks whether this device allows for network sharing. |
| [off](arkts-network-sharing-off-f-sys.md#off) | Unregister a callback for the global network sharing state change. |
| [off](arkts-network-sharing-off-f-sys.md#off-1) | Unregister a callback for the interface network sharing state change. |
| [off](arkts-network-sharing-off-f-sys.md#off-2) | Unregister a callback for the sharing upstream network change. |
| [on](arkts-network-sharing-on-f-sys.md#on) | Register a callback for the global network sharing state change. |
| [on](arkts-network-sharing-on-f-sys.md#on-1) | Register a callback for the interface network sharing state change. |
| [on](arkts-network-sharing-on-f-sys.md#on-2) | Register a callback for the sharing upstream network change. |
| [startSharing](arkts-network-sharing-startsharing-f-sys.md#startsharing) | Start network sharing for given type. |
| [startSharing](arkts-network-sharing-startsharing-f-sys.md#startsharing-1) | Start network sharing for given type. |
| [stopSharing](arkts-network-sharing-stopsharing-f-sys.md#stopsharing) | Stop network sharing for given type. |
| [stopSharing](arkts-network-sharing-stopsharing-f-sys.md#stopsharing-1) | Stop network sharing for given type. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [InterfaceSharingStateInfo](arkts-network-sharing-interfacesharingstateinfo-i-sys.md) | The interface is used to notify listeners of changes in shared interface status. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | Enumerates the network sharing states of an NIC. |
| [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Enumerates the network sharing types of an NIC. |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [NetHandle](arkts-network-sharing-nethandle-t.md) | Get the handle of the data network. |

