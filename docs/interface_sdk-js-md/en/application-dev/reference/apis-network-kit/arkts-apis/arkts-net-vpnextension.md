# @ohos.net.vpnExtension(Enhanced VPN Management)

This module implements virtual private network (VPN) management, such as starting and stopping a third-party VPN. Third-party VPNs refer to VPN services provided by third parties. They usually support more security and privacy functions and more comprehensive customization options. Currently, the VPN capabilities provided to third-party applications are primarily used for creating virtual NICs and configuring VPN routing information. The connection tunnel process and internal connection protocols need to be implemented by the applications themselves.

> **NOTE：**&gt;
> The following modules cannot be referenced in the VpnExtensionAbility, as doing so may cause the program to exit
> abnormally:

> - [@ohos.contact (Contacts)](../../apis-contacts-kit/arkts-apis/arkts-contact.md)

> - [@ohos.geolocation](../../apis-location-kit/arkts-apis/arkts-geolocation.md),
> [@ohos.geoLocationManager (Geolocation Manager)](../../apis-location-kit/arkts-apis/arkts-geolocationmanager.md)

> - [@ohos.multimedia.audio (Audio Management)](../../apis-audio-kit/arkts-apis/arkts-multimedia-audio.md)

> - [@ohos.multimedia.camera (Camera Management)](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md)

> - [@ohos.telephony.call (Call)](../../apis-telephony-kit/arkts-apis/arkts-telephony-call.md)

> - [@ohos.telephony.sim (SIM Management)](../../apis-telephony-kit/arkts-apis/arkts-telephony-sim.md)

> - [@ohos.telephony.sms (SMS)](../../apis-telephony-kit/arkts-apis/arkts-telephony-sms.md)

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createVpnConnection(Enhanced VPN Management)](arkts-network-vpnextension-createvpnconnection-f.md) |
| [createVpnObserver(Enhanced VPN Management)](arkts-network-vpnextension-createvpnobserver-f.md) |
| [startVpnExtensionAbility(Enhanced VPN Management)](arkts-network-vpnextension-startvpnextensionability-f.md) |
| [stopVpnExtensionAbility(Enhanced VPN Management)](arkts-network-vpnextension-stopvpnextensionability-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isAlwaysOnVpnEnabled(Enhanced VPN Management)](arkts-network-vpnextension-isalwaysonvpnenabled-f-sys.md) |
| [setAlwaysOnVpnEnabled(Enhanced VPN Management)](arkts-network-vpnextension-setalwaysonvpnenabled-f-sys.md) |
| [updateVpnAuthorizedState(Enhanced VPN Management)](arkts-network-vpnextension-updatevpnauthorizedstate-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [VpnConfig(Enhanced VPN Management)](arkts-network-vpnextension-vpnconfig-i.md) |
| [VpnConnection(Enhanced VPN Management)](arkts-network-vpnextension-vpnconnection-i.md) |
| [VpnObserver(Enhanced VPN Management)](arkts-network-vpnextension-vpnobserver-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LinkAddress(Enhanced VPN Management)](arkts-network-vpnextension-linkaddress-t.md) |
| [RouteInfo(Enhanced VPN Management)](arkts-network-vpnextension-routeinfo-t.md) |
| [VpnExtensionContext(Enhanced VPN Management)](arkts-network-vpnextension-vpnextensioncontext-t.md) |
