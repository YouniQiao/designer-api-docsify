# @ohos.wifi

Provides methods to operate or manage Wi-Fi.

**Since:** 6

<!--Device-unnamed-declare namespace wifi--><!--Device-unnamed-declare namespace wifi-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig) |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig-1) |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md#creategroup) |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md#getcountrycode) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup-1) |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md#getipinfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo-1) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo-1) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices-1) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos-1) |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md#getsignallevel) |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md#isconnected) |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md#isfeaturesupported) |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md#iswifiactive) |
| [off](arkts-connectivity-wifi-off-f.md#off) |
| [off](arkts-connectivity-wifi-off-f.md#off-1) |
| [off](arkts-connectivity-wifi-off-f.md#off-2) |
| [off](arkts-connectivity-wifi-off-f.md#off-3) |
| [off](arkts-connectivity-wifi-off-f.md#off-5) |
| [off](arkts-connectivity-wifi-off-f.md#off-8) |
| [off](arkts-connectivity-wifi-off-f.md#off-9) |
| [off](arkts-connectivity-wifi-off-f.md#off-10) |
| [off](arkts-connectivity-wifi-off-f.md#off-11) |
| [off](arkts-connectivity-wifi-off-f.md#off-12) |
| [off](arkts-connectivity-wifi-off-f.md#off-13) |
| [on](arkts-connectivity-wifi-on-f.md#on) |
| [on](arkts-connectivity-wifi-on-f.md#on-1) |
| [on](arkts-connectivity-wifi-on-f.md#on-2) |
| [on](arkts-connectivity-wifi-on-f.md#on-3) |
| [on](arkts-connectivity-wifi-on-f.md#on-5) |
| [on](arkts-connectivity-wifi-on-f.md#on-8) |
| [on](arkts-connectivity-wifi-on-f.md#on-9) |
| [on](arkts-connectivity-wifi-on-f.md#on-10) |
| [on](arkts-connectivity-wifi-on-f.md#on-11) |
| [on](arkts-connectivity-wifi-on-f.md#on-12) |
| [on](arkts-connectivity-wifi-on-f.md#on-13) |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md#p2pcancelconnect) |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md#p2pconnect) |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md#removegroup) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig-1) |
| [scan](arkts-connectivity-wifi-scan-f.md#scan) |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md#startdiscoverdevices) |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md#stopdiscoverdevices) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig) |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig-1) |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md#connecttodevice) |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md#connecttonetwork) |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md#deletepersistentgroup) |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md#disablehotspot) |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md#disablenetwork) |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md#disablewifi) |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md#disconnect) |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md#enablehotspot) |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md#enablewifi) |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md#getdeviceconfigs) |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md#getdevicemacaddress) |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md#gethotspotconfig) |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md#getstations) |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md#getsupportedfeatures) |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md#ishotspotactive) |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md#ishotspotdualbandsupported) |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-4) |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-6) |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-7) |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-4) |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-6) |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-7) |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md#reassociate) |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md#reconnect) |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md#removeallnetwork) |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md#removedevice) |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md#setdevicename) |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md#sethotspotconfig) |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md#updatenetwork) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IpInfo](arkts-connectivity-wifi-ipinfo-i.md) |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i.md) |
| [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) |
| [WifiP2pDevice](arkts-connectivity-wifi-wifip2pdevice-i.md) |
| [WifiP2pGroupInfo](arkts-connectivity-wifi-wifip2pgroupinfo-i.md) |
| [WifiP2pLinkedInfo](arkts-connectivity-wifi-wifip2plinkedinfo-i.md) |
| [WifiScanInfo](arkts-connectivity-wifi-wifiscaninfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) |
| [IpConfig](arkts-connectivity-wifi-ipconfig-i-sys.md) |
| [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i-sys.md) |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnState](arkts-connectivity-wifi-connstate-e.md) |
| [GroupOwnerBand](arkts-connectivity-wifi-groupownerband-e.md) |
| [P2pConnectState](arkts-connectivity-wifi-p2pconnectstate-e.md) |
| [P2pDeviceStatus](arkts-connectivity-wifi-p2pdevicestatus-e.md) |
| [WifiSecurityType](arkts-connectivity-wifi-wifisecuritytype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IpType](arkts-connectivity-wifi-iptype-e-sys.md) |
| [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md) |
<!--DelEnd-->
