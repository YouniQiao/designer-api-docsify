# @ohos.net.sharing

Provides network sharing related interfaces.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sharing--><!--Device-unnamed-declare namespace sharing-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getSharableRegexes](arkts-network-sharing-getsharableregexes-f-sys.md#getSharableRegexes) | Get a list regular expression that defines any interface that can support network sharing. |
| [getSharableRegexes](arkts-network-sharing-getsharableregexes-f-sys.md#getSharableRegexes-(System-API)) | Get a list regular expression that defines any interface that can support network sharing. |
| [getSharingIfaces](arkts-network-sharing-getsharingifaces-f-sys.md#getSharingIfaces) | Obtains the names of interfaces in each sharing state. |
| [getSharingIfaces](arkts-network-sharing-getsharingifaces-f-sys.md#getSharingIfaces-(System-API)) | Obtains the names of interfaces in each sharing state. |
| [getSharingState](arkts-network-sharing-getsharingstate-f-sys.md#getSharingState) | Obtains the network sharing state for given type. |
| [getSharingState](arkts-network-sharing-getsharingstate-f-sys.md#getSharingState-(System-API)) | Obtains the network sharing state for given type. |
| [getStatsRxBytes](arkts-network-sharing-getstatsrxbytes-f-sys.md#getStatsRxBytes) | Obtains the number of downlink data bytes of the sharing network interfaces. |
| [getStatsRxBytes](arkts-network-sharing-getstatsrxbytes-f-sys.md#getStatsRxBytes-(System-API)) | Obtains the number of downlink data bytes of the sharing network interfaces. |
| [getStatsTotalBytes](arkts-network-sharing-getstatstotalbytes-f-sys.md#getStatsTotalBytes) | Obtains the number of total data bytes of the sharing network interfaces. |
| [getStatsTotalBytes](arkts-network-sharing-getstatstotalbytes-f-sys.md#getStatsTotalBytes-(System-API)) | Obtains the number of total data bytes of the sharing network interfaces. |
| [getStatsTxBytes](arkts-network-sharing-getstatstxbytes-f-sys.md#getStatsTxBytes) | Obtains the number of uplink data bytes of the sharing network interfaces. |
| [getStatsTxBytes](arkts-network-sharing-getstatstxbytes-f-sys.md#getStatsTxBytes-(System-API)) | Obtains the number of uplink data bytes of the sharing network interfaces. |
| [isSharing](arkts-network-sharing-issharing-f-sys.md#isSharing) | Return the global network sharing state. |
| [isSharing](arkts-network-sharing-issharing-f-sys.md#isSharing-(System-API)) | Return the global network sharing state. |
| [isSharingSupported](arkts-network-sharing-issharingsupported-f-sys.md#isSharingSupported) | Checks whether this device allows for network sharing. |
| [isSharingSupported](arkts-network-sharing-issharingsupported-f-sys.md#isSharingSupported-(System-API)) | Checks whether this device allows for network sharing. |
| [off_interfaceSharingStateChange](arkts-network-sharing-offinterfacesharingstatechange-f-sys.md#off_interfaceSharingStateChange) | Unregister a callback for the interface network sharing state change. |
| [off_sharingStateChange](arkts-network-sharing-offsharingstatechange-f-sys.md#off_sharingStateChange) | Unregister a callback for the global network sharing state change. |
| [off_sharingUpstreamChange](arkts-network-sharing-offsharingupstreamchange-f-sys.md#off_sharingUpstreamChange) | Unregister a callback for the sharing upstream network change. |
| [on_interfaceSharingStateChange](arkts-network-sharing-oninterfacesharingstatechange-f-sys.md#on_interfaceSharingStateChange) | Register a callback for the interface network sharing state change. |
| [on_sharingStateChange](arkts-network-sharing-onsharingstatechange-f-sys.md#on_sharingStateChange) | Register a callback for the global network sharing state change. |
| [on_sharingUpstreamChange](arkts-network-sharing-onsharingupstreamchange-f-sys.md#on_sharingUpstreamChange) | Register a callback for the sharing upstream network change. |
| [startSharing](arkts-network-sharing-startsharing-f-sys.md#startSharing) | Start network sharing for given type. |
| [startSharing](arkts-network-sharing-startsharing-f-sys.md#startSharing-(System-API)) | Start network sharing for given type. |
| [stopSharing](arkts-network-sharing-stopsharing-f-sys.md#stopSharing) | Stop network sharing for given type. |
| [stopSharing](arkts-network-sharing-stopsharing-f-sys.md#stopSharing-(System-API)) | Stop network sharing for given type. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [InterfaceSharingStateInfo](arkts-network-sharing-interfacesharingstateinfo-i-sys.md) | The interface is used to notify listeners of changes in shared interface status. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | Enumerates the network sharing states of an NIC. |
| [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Enumerates the network sharing types of an NIC. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [NetHandle](arkts-network-sharing-nethandle-t.md) | Get the handle of the data network. |

