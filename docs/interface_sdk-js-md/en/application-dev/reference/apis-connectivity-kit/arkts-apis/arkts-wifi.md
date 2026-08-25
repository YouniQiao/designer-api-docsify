# @ohos.wifi

Provides methods to operate or manage Wi-Fi. @namespace wifi

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md) |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md) |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md) |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md) |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md) |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md) |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md) |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md) |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md) |
| [off](arkts-connectivity-wifi-off-f.md#offwifistatechange) |
| [off](arkts-connectivity-wifi-off-f.md#offwificonnectionchange) |
| [off](arkts-connectivity-wifi-off-f.md#offwifiscanstatechange) |
| [off](arkts-connectivity-wifi-off-f.md#offwifirssichange) |
| [off](arkts-connectivity-wifi-off-f.md#offhotspotstatechange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2pstatechange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2pconnectionchange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2pdevicechange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2ppeerdevicechange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2ppersistentgroupchange) |
| [off](arkts-connectivity-wifi-off-f.md#offp2pdiscoverychange) |
| [on](arkts-connectivity-wifi-on-f.md#onwifistatechange) |
| [on](arkts-connectivity-wifi-on-f.md#onwificonnectionchange) |
| [on](arkts-connectivity-wifi-on-f.md#onwifiscanstatechange) |
| [on](arkts-connectivity-wifi-on-f.md#onwifirssichange) |
| [on](arkts-connectivity-wifi-on-f.md#onhotspotstatechange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2pstatechange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2pconnectionchange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2pdevicechange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2ppeerdevicechange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2ppersistentgroupchange) |
| [on](arkts-connectivity-wifi-on-f.md#onp2pdiscoverychange) |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md) |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md) |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md) |
| [scan](arkts-connectivity-wifi-scan-f.md) |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md) |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md) |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md) |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md) |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md) |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md) |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md) |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md) |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md) |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md) |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md) |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md) |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md) |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md) |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md) |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md) |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md) |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md) |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md) |
| [off](arkts-connectivity-wifi-off-f-sys.md#offstreamchange) |
| [off](arkts-connectivity-wifi-off-f-sys.md#offhotspotstajoin) |
| [off](arkts-connectivity-wifi-off-f-sys.md#offhotspotstaleave) |
| [on](arkts-connectivity-wifi-on-f-sys.md#onstreamchange) |
| [on](arkts-connectivity-wifi-on-f-sys.md#onhotspotstajoin) |
| [on](arkts-connectivity-wifi-on-f-sys.md#onhotspotstaleave) |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md) |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md) |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md) |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md) |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md) |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md) |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md) |
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
### Interfaces(System API)

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
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IpType](arkts-connectivity-wifi-iptype-e-sys.md) |
| [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md) |
<!--DelEnd-->
