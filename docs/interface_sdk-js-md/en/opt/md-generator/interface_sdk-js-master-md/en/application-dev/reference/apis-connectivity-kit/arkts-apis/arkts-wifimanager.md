# @ohos.wifiManager

Provides methods to operate or manage Wi-Fi.

**Since:** 12

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addcandidateconfig) |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addcandidateconfig-1) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#adddeviceconfig) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#adddeviceconfig-1) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connecttocandidateconfig) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connecttocandidateconfig-1) |
| [connectToCandidateConfigWithUserAction](arkts-connectivity-wifimanager-connecttocandidateconfigwithuseraction-f.md#connecttocandidateconfigwithuseraction) |
| [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md#connecttonetwork) |
| [createGroup](arkts-connectivity-wifimanager-creategroup-f.md#creategroup) |
| [disableWifi](arkts-connectivity-wifimanager-disablewifi-f.md#disablewifi) |
| [disconnect](arkts-connectivity-wifimanager-disconnect-f.md#disconnect) |
| [enableWifi](arkts-connectivity-wifimanager-enablewifi-f.md#enablewifi) |
| [getCandidateConfigs](arkts-connectivity-wifimanager-getcandidateconfigs-f.md#getcandidateconfigs) |
| [getCountryCode](arkts-connectivity-wifimanager-getcountrycode-f.md#getcountrycode) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getcurrentgroup) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getcurrentgroup-1) |
| [getDeviceConfigs](arkts-connectivity-wifimanager-getdeviceconfigs-f.md#getdeviceconfigs) |
| [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md#getdevicemacaddress) |
| [getIpInfo](arkts-connectivity-wifimanager-getipinfo-f.md#getipinfo) |
| [getIpv6Info](arkts-connectivity-wifimanager-getipv6info-f.md#getipv6info) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getlinkedinfo) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getlinkedinfo-1) |
| [getLinkedInfoSync](arkts-connectivity-wifimanager-getlinkedinfosync-f.md#getlinkedinfosync) |
| [getMultiLinkedInfo](arkts-connectivity-wifimanager-getmultilinkedinfo-f.md#getmultilinkedinfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getp2plinkedinfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getp2plinkedinfo-1) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getp2plocaldevice) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getp2plocaldevice-1) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getp2ppeerdevices) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getp2ppeerdevices-1) |
| [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md#getscaninfolist) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getscanresults) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getscanresults-1) |
| [getScanResultsSync](arkts-connectivity-wifimanager-getscanresultssync-f.md#getscanresultssync) |
| [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md#getsignallevel) |
| [isBandTypeSupported](arkts-connectivity-wifimanager-isbandtypesupported-f.md#isbandtypesupported) |
| [isConnected](arkts-connectivity-wifimanager-isconnected-f.md#isconnected) |
| [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md#isfeaturesupported) |
| [isHotspotActive](arkts-connectivity-wifimanager-ishotspotactive-f.md#ishotspotactive) |
| [isMeteredHotspot](arkts-connectivity-wifimanager-ismeteredhotspot-f.md#ismeteredhotspot) |
| [isWifiActive](arkts-connectivity-wifimanager-iswifiactive-f.md#iswifiactive) |
| [isWlanSupported](arkts-connectivity-wifimanager-iswlansupported-f.md#iswlansupported) |
| [off](arkts-connectivity-wifimanager-off-f.md#off) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-1) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-2) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-3) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-6) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-9) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-10) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-11) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-12) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-13) |
| [off](arkts-connectivity-wifimanager-off-f.md#off-14) |
| [on](arkts-connectivity-wifimanager-on-f.md#on) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-1) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-2) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-3) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-6) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-9) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-10) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-11) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-12) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-13) |
| [on](arkts-connectivity-wifimanager-on-f.md#on-14) |
| [p2pCancelConnect](arkts-connectivity-wifimanager-p2pcancelconnect-f.md#p2pcancelconnect) |
| [p2pConnect](arkts-connectivity-wifimanager-p2pconnect-f.md#p2pconnect) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removecandidateconfig) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removecandidateconfig-1) |
| [removeDevice](arkts-connectivity-wifimanager-removedevice-f.md#removedevice) |
| [removeGroup](arkts-connectivity-wifimanager-removegroup-f.md#removegroup) |
| [scan](arkts-connectivity-wifimanager-scan-f.md#scan) |
| [startDiscoverDevices](arkts-connectivity-wifimanager-startdiscoverdevices-f.md#startdiscoverdevices) |
| [startScan](arkts-connectivity-wifimanager-startscan-f.md#startscan) |
| [stopDiscoverDevices](arkts-connectivity-wifimanager-stopdiscoverdevices-f.md#stopdiscoverdevices) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHotspotBlockList](arkts-connectivity-wifimanager-addhotspotblocklist-f-sys.md#addhotspotblocklist) |
| [allowAutoConnect](arkts-connectivity-wifimanager-allowautoconnect-f-sys.md#allowautoconnect) |
| [connectToDevice](arkts-connectivity-wifimanager-connecttodevice-f-sys.md#connecttodevice) |
| [delHotspotBlockList](arkts-connectivity-wifimanager-delhotspotblocklist-f-sys.md#delhotspotblocklist) |
| [deletePersistentGroup](arkts-connectivity-wifimanager-deletepersistentgroup-f-sys.md#deletepersistentgroup) |
| [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md#disablehotspot) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disablenetwork) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disablenetwork-1) |
| [enableHiLinkHandshake](arkts-connectivity-wifimanager-enablehilinkhandshake-f-sys.md#enablehilinkhandshake) |
| [enableHotspot](arkts-connectivity-wifimanager-enablehotspot-f-sys.md#enablehotspot) |
| [enableSemiWifi](arkts-connectivity-wifimanager-enablesemiwifi-f-sys.md#enablesemiwifi) |
| [factoryReset](arkts-connectivity-wifimanager-factoryreset-f-sys.md#factoryreset) |
| [get5GChannelList](arkts-connectivity-wifimanager-get5gchannellist-f-sys.md#get5gchannellist) |
| [getDeviceConfig](arkts-connectivity-wifimanager-getdeviceconfig-f-sys.md#getdeviceconfig) |
| [getDisconnectedReason](arkts-connectivity-wifimanager-getdisconnectedreason-f-sys.md#getdisconnectedreason) |
| [getHotspotBlockList](arkts-connectivity-wifimanager-gethotspotblocklist-f-sys.md#gethotspotblocklist) |
| [getHotspotConfig](arkts-connectivity-wifimanager-gethotspotconfig-f-sys.md#gethotspotconfig) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getp2pgroups) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getp2pgroups-1) |
| [getScanAlwaysAllowed](arkts-connectivity-wifimanager-getscanalwaysallowed-f-sys.md#getscanalwaysallowed) |
| [getStations](arkts-connectivity-wifimanager-getstations-f-sys.md#getstations) |
| [getSupportedFeatures](arkts-connectivity-wifimanager-getsupportedfeatures-f-sys.md#getsupportedfeatures) |
| [getWifiCapability](arkts-connectivity-wifimanager-getwificapability-f-sys.md#getwificapability) |
| [getWifiDetailState](arkts-connectivity-wifimanager-getwifidetailstate-f-sys.md#getwifidetailstate) |
| [isHotspotDualBandSupported](arkts-connectivity-wifimanager-ishotspotdualbandsupported-f-sys.md#ishotspotdualbandsupported) |
| [isOpenSoftApAllowed](arkts-connectivity-wifimanager-isopensoftapallowed-f-sys.md#isopensoftapallowed) |
| [isRandomMacDisabled](arkts-connectivity-wifimanager-israndommacdisabled-f-sys.md#israndommacdisabled) |
| [off](arkts-connectivity-wifimanager-off-f-sys.md#off-4) |
| [off](arkts-connectivity-wifimanager-off-f-sys.md#off-5) |
| [off](arkts-connectivity-wifimanager-off-f-sys.md#off-7) |
| [off](arkts-connectivity-wifimanager-off-f-sys.md#off-8) |
| [on](arkts-connectivity-wifimanager-on-f-sys.md#on-4) |
| [on](arkts-connectivity-wifimanager-on-f-sys.md#on-5) |
| [on](arkts-connectivity-wifimanager-on-f-sys.md#on-7) |
| [on](arkts-connectivity-wifimanager-on-f-sys.md#on-8) |
| [reassociate](arkts-connectivity-wifimanager-reassociate-f-sys.md#reassociate) |
| [reconnect](arkts-connectivity-wifimanager-reconnect-f-sys.md#reconnect) |
| [removeAllNetwork](arkts-connectivity-wifimanager-removeallnetwork-f-sys.md#removeallnetwork) |
| [setDeviceName](arkts-connectivity-wifimanager-setdevicename-f-sys.md#setdevicename) |
| [setHotspotConfig](arkts-connectivity-wifimanager-sethotspotconfig-f-sys.md#sethotspotconfig) |
| [setScanAlwaysAllowed](arkts-connectivity-wifimanager-setscanalwaysallowed-f-sys.md#setscanalwaysallowed) |
| [setWifiCapability](arkts-connectivity-wifimanager-setwificapability-f-sys.md#setwificapability) |
| [startPortalCertification](arkts-connectivity-wifimanager-startportalcertification-f-sys.md#startportalcertification) |
| [startWifiDetection](arkts-connectivity-wifimanager-startwifidetection-f-sys.md#startwifidetection) |
| [updateNetwork](arkts-connectivity-wifimanager-updatenetwork-f-sys.md#updatenetwork) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectSettings](arkts-connectivity-wifimanager-connectsettings-i.md) |
| [IpInfo](arkts-connectivity-wifimanager-ipinfo-i.md) |
| [Ipv6Info](arkts-connectivity-wifimanager-ipv6info-i.md) |
| [WifiDeviceConfig](arkts-connectivity-wifimanager-wifideviceconfig-i.md) |
| [WifiEapConfig](arkts-connectivity-wifimanager-wifieapconfig-i.md) |
| [WifiInfoElem](arkts-connectivity-wifimanager-wifiinfoelem-i.md) |
| [WifiLinkedInfo](arkts-connectivity-wifimanager-wifilinkedinfo-i.md) |
| [WifiP2PConfig](arkts-connectivity-wifimanager-wifip2pconfig-i.md) |
| [WifiP2pDevice](arkts-connectivity-wifimanager-wifip2pdevice-i.md) |
| [WifiP2pGroupInfo](arkts-connectivity-wifimanager-wifip2pgroupinfo-i.md) |
| [WifiP2pLinkedInfo](arkts-connectivity-wifimanager-wifip2plinkedinfo-i.md) |
| [WifiScanInfo](arkts-connectivity-wifimanager-wifiscaninfo-i.md) |
| [WifiWapiConfig](arkts-connectivity-wifimanager-wifiwapiconfig-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HotspotConfig](arkts-connectivity-wifimanager-hotspotconfig-i-sys.md) |
| [IpConfig](arkts-connectivity-wifimanager-ipconfig-i-sys.md) |
| [Ipv6Config](arkts-connectivity-wifimanager-ipv6config-i-sys.md) |
| [StationInfo](arkts-connectivity-wifimanager-stationinfo-i-sys.md) |
| [WifiDeviceConfig](arkts-connectivity-wifimanager-wifideviceconfig-i-sys.md) |
| [WifiLinkedInfo](arkts-connectivity-wifimanager-wifilinkedinfo-i-sys.md) |
| [WifiProxyConfig](arkts-connectivity-wifimanager-wifiproxyconfig-i-sys.md) |
| [WifiScanInfo](arkts-connectivity-wifimanager-wifiscaninfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnState](arkts-connectivity-wifimanager-connstate-e.md) |
| [DeviceAddressType](arkts-connectivity-wifimanager-deviceaddresstype-e.md) |
| [EapMethod](arkts-connectivity-wifimanager-eapmethod-e.md) |
| [GroupOwnerBand](arkts-connectivity-wifimanager-groupownerband-e.md) |
| [P2pConnectState](arkts-connectivity-wifimanager-p2pconnectstate-e.md) |
| [P2pDeviceStatus](arkts-connectivity-wifimanager-p2pdevicestatus-e.md) |
| [Phase2Method](arkts-connectivity-wifimanager-phase2method-e.md) |
| [WapiPskType](arkts-connectivity-wifimanager-wapipsktype-e.md) |
| [WifiBandType](arkts-connectivity-wifimanager-wifibandtype-e.md) |
| [WifiCapability](arkts-connectivity-wifimanager-wificapability-e.md) |
| [WifiCategory](arkts-connectivity-wifimanager-wificategory-e.md) |
| [WifiChannelWidth](arkts-connectivity-wifimanager-wifichannelwidth-e.md) |
| [WifiLinkType](arkts-connectivity-wifimanager-wifilinktype-e.md) |
| [WifiSecurityType](arkts-connectivity-wifimanager-wifisecuritytype-e.md) |
| [WifiStandard](arkts-connectivity-wifimanager-wifistandard-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DisconnectedReason](arkts-connectivity-wifimanager-disconnectedreason-e-sys.md) |
| [IpType](arkts-connectivity-wifimanager-iptype-e-sys.md) |
| [ProxyMethod](arkts-connectivity-wifimanager-proxymethod-e-sys.md) |
| [SuppState](arkts-connectivity-wifimanager-suppstate-e-sys.md) |
| [WifiDetailState](arkts-connectivity-wifimanager-wifidetailstate-e-sys.md) |
<!--DelEnd-->
