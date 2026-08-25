# @ohos.wifiManager

Provides methods to operate or manage Wi-Fi. @namespace wifiManager

**Since:** 12

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md) |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md) |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md) |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md) |
| [connectToCandidateConfigWithUserAction](arkts-connectivity-wifimanager-connecttocandidateconfigwithuseraction-f.md) |
| [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md) |
| [createGroup](arkts-connectivity-wifimanager-creategroup-f.md) |
| [disableWifi](arkts-connectivity-wifimanager-disablewifi-f.md) |
| [disconnect](arkts-connectivity-wifimanager-disconnect-f.md) |
| [enableWifi](arkts-connectivity-wifimanager-enablewifi-f.md) |
| [getCandidateConfigs](arkts-connectivity-wifimanager-getcandidateconfigs-f.md) |
| [getCountryCode](arkts-connectivity-wifimanager-getcountrycode-f.md) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md) |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md) |
| [getDeviceConfigs](arkts-connectivity-wifimanager-getdeviceconfigs-f.md) |
| [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md) |
| [getIpInfo](arkts-connectivity-wifimanager-getipinfo-f.md) |
| [getIpv6Info](arkts-connectivity-wifimanager-getipv6info-f.md) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md) |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md) |
| [getLinkedInfoSync](arkts-connectivity-wifimanager-getlinkedinfosync-f.md) |
| [getMultiLinkedInfo](arkts-connectivity-wifimanager-getmultilinkedinfo-f.md) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md) |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md) |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md) |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md) |
| [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md) |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md) |
| [getScanResultsSync](arkts-connectivity-wifimanager-getscanresultssync-f.md) |
| [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md) |
| [isBandTypeSupported](arkts-connectivity-wifimanager-isbandtypesupported-f.md) |
| [isConnected](arkts-connectivity-wifimanager-isconnected-f.md) |
| [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md) |
| [isMeteredHotspot](arkts-connectivity-wifimanager-ismeteredhotspot-f.md) |
| [isWifiActive](arkts-connectivity-wifimanager-iswifiactive-f.md) |
| [isWlanSupported](arkts-connectivity-wifimanager-iswlansupported-f.md) |
| [off](arkts-connectivity-wifimanager-off-f.md#offwifistatechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offwificonnectionchange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offwifiscanstatechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offwifirssichange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offhotspotstatechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2pstatechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2pconnectionchange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2pdevicechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2ppeerdevicechange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2ppersistentgroupchange) |
| [off](arkts-connectivity-wifimanager-off-f.md#offp2pdiscoverychange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onwifistatechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onwificonnectionchange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onwifiscanstatechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onwifirssichange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onhotspotstatechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2pstatechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2pconnectionchange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2pdevicechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2ppeerdevicechange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2ppersistentgroupchange) |
| [on](arkts-connectivity-wifimanager-on-f.md#onp2pdiscoverychange) |
| [p2pCancelConnect](arkts-connectivity-wifimanager-p2pcancelconnect-f.md) |
| [p2pConnect](arkts-connectivity-wifimanager-p2pconnect-f.md) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md) |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md) |
| [removeDevice](arkts-connectivity-wifimanager-removedevice-f.md) |
| [removeGroup](arkts-connectivity-wifimanager-removegroup-f.md) |
| [scan](arkts-connectivity-wifimanager-scan-f.md) |
| [startDiscoverDevices](arkts-connectivity-wifimanager-startdiscoverdevices-f.md) |
| [startScan](arkts-connectivity-wifimanager-startscan-f.md) |
| [stopDiscoverDevices](arkts-connectivity-wifimanager-stopdiscoverdevices-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHotspotBlockList](arkts-connectivity-wifimanager-addhotspotblocklist-f-sys.md) |
| [allowAutoConnect](arkts-connectivity-wifimanager-allowautoconnect-f-sys.md) |
| [connectToDevice](arkts-connectivity-wifimanager-connecttodevice-f-sys.md) |
| [deletePersistentGroup](arkts-connectivity-wifimanager-deletepersistentgroup-f-sys.md) |
| [delHotspotBlockList](arkts-connectivity-wifimanager-delhotspotblocklist-f-sys.md) |
| [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md) |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md) |
| [enableHiLinkHandshake](arkts-connectivity-wifimanager-enablehilinkhandshake-f-sys.md) |
| [enableHotspot](arkts-connectivity-wifimanager-enablehotspot-f-sys.md) |
| [enableSemiWifi](arkts-connectivity-wifimanager-enablesemiwifi-f-sys.md) |
| [factoryReset](arkts-connectivity-wifimanager-factoryreset-f-sys.md) |
| [get5GChannelList](arkts-connectivity-wifimanager-get5gchannellist-f-sys.md) |
| [getDeviceConfig](arkts-connectivity-wifimanager-getdeviceconfig-f-sys.md) |
| [getDisconnectedReason](arkts-connectivity-wifimanager-getdisconnectedreason-f-sys.md) |
| [getHotspotBlockList](arkts-connectivity-wifimanager-gethotspotblocklist-f-sys.md) |
| [getHotspotConfig](arkts-connectivity-wifimanager-gethotspotconfig-f-sys.md) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md) |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md) |
| [getScanAlwaysAllowed](arkts-connectivity-wifimanager-getscanalwaysallowed-f-sys.md) |
| [getStations](arkts-connectivity-wifimanager-getstations-f-sys.md) |
| [getSupportedFeatures](arkts-connectivity-wifimanager-getsupportedfeatures-f-sys.md) |
| [getWifiCapability](arkts-connectivity-wifimanager-getwificapability-f-sys.md) |
| [getWifiDetailState](arkts-connectivity-wifimanager-getwifidetailstate-f-sys.md) |
| [isHotspotActive](arkts-connectivity-wifimanager-ishotspotactive-f-sys.md) |
| [isHotspotDualBandSupported](arkts-connectivity-wifimanager-ishotspotdualbandsupported-f-sys.md) |
| [isOpenSoftApAllowed](arkts-connectivity-wifimanager-isopensoftapallowed-f-sys.md) |
| [isRandomMacDisabled](arkts-connectivity-wifimanager-israndommacdisabled-f-sys.md) |
| off |
| off |
| off |
| off |
| on |
| on |
| on |
| on |
| [reassociate](arkts-connectivity-wifimanager-reassociate-f-sys.md) |
| [reconnect](arkts-connectivity-wifimanager-reconnect-f-sys.md) |
| [removeAllNetwork](arkts-connectivity-wifimanager-removeallnetwork-f-sys.md) |
| [setDeviceName](arkts-connectivity-wifimanager-setdevicename-f-sys.md) |
| [setHotspotConfig](arkts-connectivity-wifimanager-sethotspotconfig-f-sys.md) |
| [setScanAlwaysAllowed](arkts-connectivity-wifimanager-setscanalwaysallowed-f-sys.md) |
| [setWifiCapability](arkts-connectivity-wifimanager-setwificapability-f-sys.md) |
| [startPortalCertification](arkts-connectivity-wifimanager-startportalcertification-f-sys.md) |
| [startWifiDetection](arkts-connectivity-wifimanager-startwifidetection-f-sys.md) |
| [updateNetwork](arkts-connectivity-wifimanager-updatenetwork-f-sys.md) |
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
### Interfaces(System API)

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
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DisconnectedReason](arkts-connectivity-wifimanager-disconnectedreason-e-sys.md) |
| [IpType](arkts-connectivity-wifimanager-iptype-e-sys.md) |
| [ProxyMethod](arkts-connectivity-wifimanager-proxymethod-e-sys.md) |
| [SuppState](arkts-connectivity-wifimanager-suppstate-e-sys.md) |
| [WifiDetailState](arkts-connectivity-wifimanager-wifidetailstate-e-sys.md) |
<!--DelEnd-->
