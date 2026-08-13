# @ohos.wifiManager

Provides methods to operate or manage Wi-Fi.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig) |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#addDeviceConfig) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#addDeviceConfig) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connectToCandidateConfig) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connectToCandidateConfig) |
| [connectToCandidateConfigWithUserAction](arkts-connectivity-wifimanager-connecttocandidateconfigwithuseraction-f.md#connectToCandidateConfigWithUserAction) |
| [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md#connectToNetwork) |
| [createGroup](arkts-connectivity-wifimanager-creategroup-f.md#createGroup) |
| [disableWifi](arkts-connectivity-wifimanager-disablewifi-f.md#disableWifi) |
| [disconnect](arkts-connectivity-wifimanager-disconnect-f.md#disconnect) |
| [enableWifi](arkts-connectivity-wifimanager-enablewifi-f.md#enableWifi) |
| [getCandidateConfigs](arkts-connectivity-wifimanager-getcandidateconfigs-f.md#getCandidateConfigs) |
| [getCountryCode](arkts-connectivity-wifimanager-getcountrycode-f.md#getCountryCode) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getCurrentGroup) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getCurrentGroup) |
| [getDeviceConfigs](arkts-connectivity-wifimanager-getdeviceconfigs-f.md#getDeviceConfigs) |
| [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md#getDeviceMacAddress) |
| [getIpInfo](arkts-connectivity-wifimanager-getipinfo-f.md#getIpInfo) |
| [getIpv6Info](arkts-connectivity-wifimanager-getipv6info-f.md#getIpv6Info) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getLinkedInfo) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getLinkedInfo) |
| [getLinkedInfoSync](arkts-connectivity-wifimanager-getlinkedinfosync-f.md#getLinkedInfoSync) |
| [getMultiLinkedInfo](arkts-connectivity-wifimanager-getmultilinkedinfo-f.md#getMultiLinkedInfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getP2pLinkedInfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getP2pLinkedInfo) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getP2pLocalDevice) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getP2pLocalDevice) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getP2pPeerDevices) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getP2pPeerDevices) |
| [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md#getScanInfoList) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getScanResults) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getScanResults) |
| [getScanResultsSync](arkts-connectivity-wifimanager-getscanresultssync-f.md#getScanResultsSync) |
| [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md#getSignalLevel) |
| [isBandTypeSupported](arkts-connectivity-wifimanager-isbandtypesupported-f.md#isBandTypeSupported) |
| [isConnected](arkts-connectivity-wifimanager-isconnected-f.md#isConnected) |
| [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md#isFeatureSupported) |
| [isHotspotActive](arkts-connectivity-wifimanager-ishotspotactive-f.md#isHotspotActive) |
| [isMeteredHotspot](arkts-connectivity-wifimanager-ismeteredhotspot-f.md#isMeteredHotspot) |
| [isWifiActive](arkts-connectivity-wifimanager-iswifiactive-f.md#isWifiActive) |
| [isWlanSupported](arkts-connectivity-wifimanager-iswlansupported-f.md#isWlanSupported) |
| [offHotspotStateChange](arkts-connectivity-wifimanager-offhotspotstatechange-f.md#offHotspotStateChange) |
| [offP2pConnectionChange](arkts-connectivity-wifimanager-offp2pconnectionchange-f.md#offP2pConnectionChange) |
| [offP2pDeviceChange](arkts-connectivity-wifimanager-offp2pdevicechange-f.md#offP2pDeviceChange) |
| [offP2pDiscoveryChange](arkts-connectivity-wifimanager-offp2pdiscoverychange-f.md#offP2pDiscoveryChange) |
| [offP2pPeerDeviceChange](arkts-connectivity-wifimanager-offp2ppeerdevicechange-f.md#offP2pPeerDeviceChange) |
| [offP2pPersistentGroupChange](arkts-connectivity-wifimanager-offp2ppersistentgroupchange-f.md#offP2pPersistentGroupChange) |
| [offP2pStateChange](arkts-connectivity-wifimanager-offp2pstatechange-f.md#offP2pStateChange) |
| [offWifiConnectionChange](arkts-connectivity-wifimanager-offwificonnectionchange-f.md#offWifiConnectionChange) |
| [offWifiRssiChange](arkts-connectivity-wifimanager-offwifirssichange-f.md#offWifiRssiChange) |
| [offWifiScanStateChange](arkts-connectivity-wifimanager-offwifiscanstatechange-f.md#offWifiScanStateChange) |
| [offWifiStateChange](arkts-connectivity-wifimanager-offwifistatechange-f.md#offWifiStateChange) |
| off_hotspotStateChange |
| off_p2pConnectionChange |
| off_p2pDeviceChange |
| off_p2pDiscoveryChange |
| off_p2pPeerDeviceChange |
| off_p2pPersistentGroupChange |
| off_p2pStateChange |
| off_wifiConnectionChange |
| off_wifiRssiChange |
| off_wifiScanStateChange |
| off_wifiStateChange |
| [onHotspotStateChange](arkts-connectivity-wifimanager-onhotspotstatechange-f.md#onHotspotStateChange) |
| [onP2pConnectionChange](arkts-connectivity-wifimanager-onp2pconnectionchange-f.md#onP2pConnectionChange) |
| [onP2pDeviceChange](arkts-connectivity-wifimanager-onp2pdevicechange-f.md#onP2pDeviceChange) |
| [onP2pDiscoveryChange](arkts-connectivity-wifimanager-onp2pdiscoverychange-f.md#onP2pDiscoveryChange) |
| [onP2pPeerDeviceChange](arkts-connectivity-wifimanager-onp2ppeerdevicechange-f.md#onP2pPeerDeviceChange) |
| [onP2pPersistentGroupChange](arkts-connectivity-wifimanager-onp2ppersistentgroupchange-f.md#onP2pPersistentGroupChange) |
| [onP2pStateChange](arkts-connectivity-wifimanager-onp2pstatechange-f.md#onP2pStateChange) |
| [onWifiConnectionChange](arkts-connectivity-wifimanager-onwificonnectionchange-f.md#onWifiConnectionChange) |
| [onWifiRssiChange](arkts-connectivity-wifimanager-onwifirssichange-f.md#onWifiRssiChange) |
| [onWifiScanStateChange](arkts-connectivity-wifimanager-onwifiscanstatechange-f.md#onWifiScanStateChange) |
| [onWifiStateChange](arkts-connectivity-wifimanager-onwifistatechange-f.md#onWifiStateChange) |
| on_hotspotStateChange |
| on_p2pConnectionChange |
| on_p2pDeviceChange |
| on_p2pDiscoveryChange |
| on_p2pPeerDeviceChange |
| on_p2pPersistentGroupChange |
| on_p2pStateChange |
| on_wifiConnectionChange |
| on_wifiRssiChange |
| on_wifiScanStateChange |
| on_wifiStateChange |
| [p2pCancelConnect](arkts-connectivity-wifimanager-p2pcancelconnect-f.md#p2pCancelConnect) |
| [p2pConnect](arkts-connectivity-wifimanager-p2pconnect-f.md#p2pConnect) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removeCandidateConfig) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removeCandidateConfig) |
| [removeDevice](arkts-connectivity-wifimanager-removedevice-f.md#removeDevice) |
| [removeGroup](arkts-connectivity-wifimanager-removegroup-f.md#removeGroup) |
| [scan](arkts-connectivity-wifimanager-scan-f.md#scan) |
| [startDiscoverDevices](arkts-connectivity-wifimanager-startdiscoverdevices-f.md#startDiscoverDevices) |
| [startScan](arkts-connectivity-wifimanager-startscan-f.md#startScan) |
| [stopDiscoverDevices](arkts-connectivity-wifimanager-stopdiscoverdevices-f.md#stopDiscoverDevices) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHotspotBlockList](arkts-connectivity-wifimanager-addhotspotblocklist-f-sys.md#addHotspotBlockList-(System-API)) |
| [allowAutoConnect](arkts-connectivity-wifimanager-allowautoconnect-f-sys.md#allowAutoConnect-(System-API)) |
| [connectToDevice](arkts-connectivity-wifimanager-connecttodevice-f-sys.md#connectToDevice-(System-API)) |
| [delHotspotBlockList](arkts-connectivity-wifimanager-delhotspotblocklist-f-sys.md#delHotspotBlockList-(System-API)) |
| [deletePersistentGroup](arkts-connectivity-wifimanager-deletepersistentgroup-f-sys.md#deletePersistentGroup-(System-API)) |
| [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md#disableHotspot-(System-API)) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disableNetwork-(System-API)) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disableNetwork-(System-API)) |
| [enableHiLinkHandshake](arkts-connectivity-wifimanager-enablehilinkhandshake-f-sys.md#enableHiLinkHandshake-(System-API)) |
| [enableHotspot](arkts-connectivity-wifimanager-enablehotspot-f-sys.md#enableHotspot-(System-API)) |
| [enableSemiWifi](arkts-connectivity-wifimanager-enablesemiwifi-f-sys.md#enableSemiWifi-(System-API)) |
| [factoryReset](arkts-connectivity-wifimanager-factoryreset-f-sys.md#factoryReset-(System-API)) |
| [get5GChannelList](arkts-connectivity-wifimanager-get5gchannellist-f-sys.md#get5GChannelList-(System-API)) |
| [getDeviceConfig](arkts-connectivity-wifimanager-getdeviceconfig-f-sys.md#getDeviceConfig-(System-API)) |
| [getDisconnectedReason](arkts-connectivity-wifimanager-getdisconnectedreason-f-sys.md#getDisconnectedReason-(System-API)) |
| [getHotspotBlockList](arkts-connectivity-wifimanager-gethotspotblocklist-f-sys.md#getHotspotBlockList-(System-API)) |
| [getHotspotConfig](arkts-connectivity-wifimanager-gethotspotconfig-f-sys.md#getHotspotConfig-(System-API)) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getP2pGroups-(System-API)) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getP2pGroups-(System-API)) |
| [getScanAlwaysAllowed](arkts-connectivity-wifimanager-getscanalwaysallowed-f-sys.md#getScanAlwaysAllowed-(System-API)) |
| [getStations](arkts-connectivity-wifimanager-getstations-f-sys.md#getStations-(System-API)) |
| [getSupportedFeatures](arkts-connectivity-wifimanager-getsupportedfeatures-f-sys.md#getSupportedFeatures-(System-API)) |
| [getWifiCapability](arkts-connectivity-wifimanager-getwificapability-f-sys.md#getWifiCapability-(System-API)) |
| [getWifiDetailState](arkts-connectivity-wifimanager-getwifidetailstate-f-sys.md#getWifiDetailState-(System-API)) |
| [isHotspotDualBandSupported](arkts-connectivity-wifimanager-ishotspotdualbandsupported-f-sys.md#isHotspotDualBandSupported-(System-API)) |
| [isOpenSoftApAllowed](arkts-connectivity-wifimanager-isopensoftapallowed-f-sys.md#isOpenSoftApAllowed-(System-API)) |
| [isRandomMacDisabled](arkts-connectivity-wifimanager-israndommacdisabled-f-sys.md#isRandomMacDisabled-(System-API)) |
| [offDeviceConfigChange](arkts-connectivity-wifimanager-offdeviceconfigchange-f-sys.md#offDeviceConfigChange-(System-API)) |
| [offHotspotStaJoin](arkts-connectivity-wifimanager-offhotspotstajoin-f-sys.md#offHotspotStaJoin-(System-API)) |
| [offHotspotStaLeave](arkts-connectivity-wifimanager-offhotspotstaleave-f-sys.md#offHotspotStaLeave-(System-API)) |
| [offStreamChange](arkts-connectivity-wifimanager-offstreamchange-f-sys.md#offStreamChange-(System-API)) |
| [off_deviceConfigChange](arkts-connectivity-wifimanager-offdeviceconfigchange-f-sys.md) |
| off_hotspotStaJoin |
| off_hotspotStaLeave |
| off_streamChange |
| [onDeviceConfigChange](arkts-connectivity-wifimanager-ondeviceconfigchange-f-sys.md#onDeviceConfigChange-(System-API)) |
| [onHotspotStaJoin](arkts-connectivity-wifimanager-onhotspotstajoin-f-sys.md#onHotspotStaJoin-(System-API)) |
| [onHotspotStaLeave](arkts-connectivity-wifimanager-onhotspotstaleave-f-sys.md#onHotspotStaLeave-(System-API)) |
| [onStreamChange](arkts-connectivity-wifimanager-onstreamchange-f-sys.md#onStreamChange-(System-API)) |
| [on_deviceConfigChange](arkts-connectivity-wifimanager-ondeviceconfigchange-f-sys.md) |
| on_hotspotStaJoin |
| on_hotspotStaLeave |
| on_streamChange |
| [reassociate](arkts-connectivity-wifimanager-reassociate-f-sys.md#reassociate-(System-API)) |
| [reconnect](arkts-connectivity-wifimanager-reconnect-f-sys.md#reconnect-(System-API)) |
| [removeAllNetwork](arkts-connectivity-wifimanager-removeallnetwork-f-sys.md#removeAllNetwork-(System-API)) |
| [setDeviceName](arkts-connectivity-wifimanager-setdevicename-f-sys.md#setDeviceName-(System-API)) |
| [setHotspotConfig](arkts-connectivity-wifimanager-sethotspotconfig-f-sys.md#setHotspotConfig-(System-API)) |
| [setScanAlwaysAllowed](arkts-connectivity-wifimanager-setscanalwaysallowed-f-sys.md#setScanAlwaysAllowed-(System-API)) |
| [setWifiCapability](arkts-connectivity-wifimanager-setwificapability-f-sys.md#setWifiCapability-(System-API)) |
| [startPortalCertification](arkts-connectivity-wifimanager-startportalcertification-f-sys.md#startPortalCertification-(System-API)) |
| [startWifiDetection](arkts-connectivity-wifimanager-startwifidetection-f-sys.md#startWifiDetection-(System-API)) |
| [updateNetwork](arkts-connectivity-wifimanager-updatenetwork-f-sys.md#updateNetwork-(System-API)) |
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
