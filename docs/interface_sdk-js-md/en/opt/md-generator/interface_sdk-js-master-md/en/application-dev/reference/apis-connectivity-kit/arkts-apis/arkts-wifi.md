# @ohos.wifi

Provides methods to operate or manage Wi-Fi.

**Since:** 6

**Deprecated since:** -1

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
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#addUntrustedConfig) |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#addUntrustedConfig) |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md#createGroup) |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md#getCountryCode) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getCurrentGroup) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getCurrentGroup) |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md#getIpInfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getLinkedInfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getLinkedInfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getP2pLinkedInfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getP2pLinkedInfo) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getP2pPeerDevices) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getP2pPeerDevices) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getScanInfos) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getScanInfos) |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md#getSignalLevel) |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md#isConnected) |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md#isFeatureSupported) |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md#isWifiActive) |
| [off_hotspotStateChange](arkts-connectivity-wifi-offhotspotstatechange-f.md#off_hotspotStateChange) |
| [off_p2pConnectionChange](arkts-connectivity-wifi-offp2pconnectionchange-f.md#off_p2pConnectionChange) |
| [off_p2pDeviceChange](arkts-connectivity-wifi-offp2pdevicechange-f.md#off_p2pDeviceChange) |
| [off_p2pDiscoveryChange](arkts-connectivity-wifi-offp2pdiscoverychange-f.md#off_p2pDiscoveryChange) |
| [off_p2pPeerDeviceChange](arkts-connectivity-wifi-offp2ppeerdevicechange-f.md#off_p2pPeerDeviceChange) |
| [off_p2pPersistentGroupChange](arkts-connectivity-wifi-offp2ppersistentgroupchange-f.md#off_p2pPersistentGroupChange) |
| [off_p2pStateChange](arkts-connectivity-wifi-offp2pstatechange-f.md#off_p2pStateChange) |
| [off_wifiConnectionChange](arkts-connectivity-wifi-offwificonnectionchange-f.md#off_wifiConnectionChange) |
| [off_wifiRssiChange](arkts-connectivity-wifi-offwifirssichange-f.md#off_wifiRssiChange) |
| [off_wifiScanStateChange](arkts-connectivity-wifi-offwifiscanstatechange-f.md#off_wifiScanStateChange) |
| [off_wifiStateChange](arkts-connectivity-wifi-offwifistatechange-f.md#off_wifiStateChange) |
| [on_hotspotStateChange](arkts-connectivity-wifi-onhotspotstatechange-f.md#on_hotspotStateChange) |
| [on_p2pConnectionChange](arkts-connectivity-wifi-onp2pconnectionchange-f.md#on_p2pConnectionChange) |
| [on_p2pDeviceChange](arkts-connectivity-wifi-onp2pdevicechange-f.md#on_p2pDeviceChange) |
| [on_p2pDiscoveryChange](arkts-connectivity-wifi-onp2pdiscoverychange-f.md#on_p2pDiscoveryChange) |
| [on_p2pPeerDeviceChange](arkts-connectivity-wifi-onp2ppeerdevicechange-f.md#on_p2pPeerDeviceChange) |
| [on_p2pPersistentGroupChange](arkts-connectivity-wifi-onp2ppersistentgroupchange-f.md#on_p2pPersistentGroupChange) |
| [on_p2pStateChange](arkts-connectivity-wifi-onp2pstatechange-f.md#on_p2pStateChange) |
| [on_wifiConnectionChange](arkts-connectivity-wifi-onwificonnectionchange-f.md#on_wifiConnectionChange) |
| [on_wifiRssiChange](arkts-connectivity-wifi-onwifirssichange-f.md#on_wifiRssiChange) |
| [on_wifiScanStateChange](arkts-connectivity-wifi-onwifiscanstatechange-f.md#on_wifiScanStateChange) |
| [on_wifiStateChange](arkts-connectivity-wifi-onwifistatechange-f.md#on_wifiStateChange) |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md#p2pCancelConnect) |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md#p2pConnect) |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md#removeGroup) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeUntrustedConfig) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeUntrustedConfig) |
| [scan](arkts-connectivity-wifi-scan-f.md#scan) |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md#startDiscoverDevices) |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md#stopDiscoverDevices) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#addDeviceConfig-(System-API)) |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#addDeviceConfig-(System-API)) |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md#connectToDevice-(System-API)) |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md#connectToNetwork-(System-API)) |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md#deletePersistentGroup-(System-API)) |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md#disableHotspot-(System-API)) |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md#disableNetwork-(System-API)) |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md#disableWifi-(System-API)) |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md#disconnect-(System-API)) |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md#enableHotspot-(System-API)) |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md#enableWifi-(System-API)) |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md#getDeviceConfigs-(System-API)) |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md#getDeviceMacAddress-(System-API)) |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md#getHotspotConfig-(System-API)) |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md#getStations-(System-API)) |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md#getSupportedFeatures-(System-API)) |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md#isHotspotActive-(System-API)) |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md#isHotspotDualBandSupported-(System-API)) |
| [off_hotspotStaJoin](arkts-connectivity-wifi-offhotspotstajoin-f-sys.md#off_hotspotStaJoin) |
| [off_hotspotStaLeave](arkts-connectivity-wifi-offhotspotstaleave-f-sys.md#off_hotspotStaLeave) |
| [off_streamChange](arkts-connectivity-wifi-offstreamchange-f-sys.md#off_streamChange) |
| [on_hotspotStaJoin](arkts-connectivity-wifi-onhotspotstajoin-f-sys.md#on_hotspotStaJoin) |
| [on_hotspotStaLeave](arkts-connectivity-wifi-onhotspotstaleave-f-sys.md#on_hotspotStaLeave) |
| [on_streamChange](arkts-connectivity-wifi-onstreamchange-f-sys.md#on_streamChange) |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md#reassociate-(System-API)) |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md#reconnect-(System-API)) |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md#removeAllNetwork-(System-API)) |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md#removeDevice-(System-API)) |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md#setDeviceName-(System-API)) |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md#setHotspotConfig-(System-API)) |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md#updateNetwork-(System-API)) |
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
