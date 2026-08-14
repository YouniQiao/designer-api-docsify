# @ohos.wifiManager

Provides methods to operate or manage Wi-Fi.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from 'wifiManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig) | Add a specified candidate hotspot configuration and returns the networkId. This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot. The app must be in the foreground. |
| [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig) | Add a specified candidate hotspot configuration and returns the networkId. This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot. The app must be in the foreground. |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#addDeviceConfig) | Add Wi-Fi connection configuration to the device. The configuration will be updated when the configuration is added. |
| [addDeviceConfig](arkts-connectivity-wifimanager-adddeviceconfig-f.md#addDeviceConfig) | Add Wi-Fi connection configuration to the device. The configuration will be updated when the configuration is added. |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connectToCandidateConfig) | Connect to a specified candidate hotspot by networkId, only the configuration which is added by ourself is allowed to be connected. This method connect to a configuration at a time. The app must be in the foreground. |
| [connectToCandidateConfig](arkts-connectivity-wifimanager-connecttocandidateconfig-f.md#connectToCandidateConfig) | Connect to the specified candidate hotspot using connect settings. |
| [connectToCandidateConfigWithUserAction](arkts-connectivity-wifimanager-connecttocandidateconfigwithuseraction-f.md#connectToCandidateConfigWithUserAction) | Connect to a specified candidate hotspot by networkId, and wait for user respond result. Only the configuration which is added by ourself is allowed to be connected. This method connect to a configuration at a time. The app must be in the foreground. |
| [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md#connectToNetwork) | Connect to Wi-Fi hotspot by networkId. |
| [createGroup](arkts-connectivity-wifimanager-creategroup-f.md#createGroup) | Create a P2P group. |
| [disableWifi](arkts-connectivity-wifimanager-disablewifi-f.md#disableWifi) | Disable Wi-Fi. |
| [disconnect](arkts-connectivity-wifimanager-disconnect-f.md#disconnect) | Disconnect connection between sta and Wi-Fi hotspot. |
| [enableWifi](arkts-connectivity-wifimanager-enablewifi-f.md#enableWifi) | Enable Wi-Fi. |
| [getCandidateConfigs](arkts-connectivity-wifimanager-getcandidateconfigs-f.md#getCandidateConfigs) | Obtain the list of all existed candidate Wi-Fi configurations which added by ourself. You can obtain only the Wi-Fi configurations you created on your own application. |
| [getCountryCode](arkts-connectivity-wifimanager-getcountrycode-f.md#getCountryCode) | Obtain the country code of the device. |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getCurrentGroup) | Obtain information about the current p2p group. |
| [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md#getCurrentGroup) | Obtain information about the current p2p group. |
| [getDeviceConfigs](arkts-connectivity-wifimanager-getdeviceconfigs-f.md#getDeviceConfigs) | Obtain the list of all existed Wi-Fi configurations. |
| [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md#getDeviceMacAddress) | Obtain the MAC address of a Wi-Fi device. Wi-Fi must be enabled. The MAC address is unique and cannot be changed. |
| [getIpInfo](arkts-connectivity-wifimanager-getipinfo-f.md#getIpInfo) | Obtain the IPv4 information of the Wi-Fi connection. The IP information includes the host IP address, gateway address, and DNS information. |
| [getIpv6Info](arkts-connectivity-wifimanager-getipv6info-f.md#getIpv6Info) | Obtain the IPv6 information of the Wi-Fi connection. The IPv6 information includes the host IP address, gateway address, and DNS information. |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getLinkedInfo) | Obtain connection information about the Wi-Fi connection. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid. |
| [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md#getLinkedInfo) | Obtain connection information about the Wi-Fi connection. |
| [getLinkedInfoSync](arkts-connectivity-wifimanager-getlinkedinfosync-f.md#getLinkedInfoSync) | Obtain connection information about the Wi-Fi connection.this apireturns the result syncchronously. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid. |
| [getMultiLinkedInfo](arkts-connectivity-wifimanager-getmultilinkedinfo-f.md#getMultiLinkedInfo) | Obtain multiple Wi-Fi connection information when Wi-Fi linked in MLO(Muti-Link Operation) state. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid. |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getP2pLinkedInfo) | Obtain information about the P2P connection. |
| [getP2pLinkedInfo](arkts-connectivity-wifimanager-getp2plinkedinfo-f.md#getP2pLinkedInfo) | Obtain information about the P2P connection. |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getP2pLocalDevice) | Obtain the information about own device information. DeviceAddress in the returned WifiP2pDevice will be set "00:00:00:00:00:00", if ohos.permission.GET_WIFI_LOCAL_MAC is not granted. |
| [getP2pLocalDevice](arkts-connectivity-wifimanager-getp2plocaldevice-f.md#getP2pLocalDevice) | Obtain the information about own device information. DeviceAddress in the returned WifiP2pDevice will be set "00:00:00:00:00:00", if ohos.permission.GET_WIFI_LOCAL_MAC is not granted. |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getP2pPeerDevices) | Obtain the information about the found devices. |
| [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getP2pPeerDevices) | Obtain the information about the found devices. |
| [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md#getScanInfoList) | Obtain the scanned station list. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid. |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getScanResults) | Obtain the scanned sta list. |
| [getScanResults](arkts-connectivity-wifimanager-getscanresults-f.md#getScanResults) | Obtain the scanned sta list. |
| [getScanResultsSync](arkts-connectivity-wifimanager-getscanresultssync-f.md#getScanResultsSync) | Obtain the scanned sta list. |
| [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md#getSignalLevel) | Calculate the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band. |
| [isBandTypeSupported](arkts-connectivity-wifimanager-isbandtypesupported-f.md#isBandTypeSupported) | Check whether the current device supports the specified band. |
| [isConnected](arkts-connectivity-wifimanager-isconnected-f.md#isConnected) | Check whether the Wi-Fi connection has been set up. |
| [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md#isFeatureSupported) | Check whether the device supports a specified feature. |
| [isHotspotActive](arkts-connectivity-wifimanager-ishotspotactive-f.md#isHotspotActive) | Check whether Wi-Fi hotspot is active on a device. |
| [isMeteredHotspot](arkts-connectivity-wifimanager-ismeteredhotspot-f.md#isMeteredHotspot) | Whether the hotspot is metered hotspot or not. |
| [isWifiActive](arkts-connectivity-wifimanager-iswifiactive-f.md#isWifiActive) | Query the Wi-Fi status |
| [isWlanSupported](arkts-connectivity-wifimanager-iswlansupported-f.md#isWlanSupported) | Query whether Wi-Fi is available |
| [offHotspotStateChange](arkts-connectivity-wifimanager-offhotspotstatechange-f.md#offHotspotStateChange) | Unsubscribe Wi-Fi hotspot state change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [offP2pConnectionChange](arkts-connectivity-wifimanager-offp2pconnectionchange-f.md#offP2pConnectionChange) | Unsubscribe P2P connection change events. |
| [offP2pDeviceChange](arkts-connectivity-wifimanager-offp2pdevicechange-f.md#offP2pDeviceChange) | Unsubscribe P2P local device change events. |
| [offP2pDiscoveryChange](arkts-connectivity-wifimanager-offp2pdiscoverychange-f.md#offP2pDiscoveryChange) | Unsubscribe P2P discovery events. |
| [offP2pPeerDeviceChange](arkts-connectivity-wifimanager-offp2ppeerdevicechange-f.md#offP2pPeerDeviceChange) | Unsubscribe P2P peer device change events. |
| [offP2pPersistentGroupChange](arkts-connectivity-wifimanager-offp2ppersistentgroupchange-f.md#offP2pPersistentGroupChange) | Unsubscribe P2P persistent group change events. |
| [offP2pStateChange](arkts-connectivity-wifimanager-offp2pstatechange-f.md#offP2pStateChange) | Unsubscribe P2P status change events. |
| [offWifiConnectionChange](arkts-connectivity-wifimanager-offwificonnectionchange-f.md#offWifiConnectionChange) | Unsubscribe Wi-Fi connection change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [offWifiRssiChange](arkts-connectivity-wifimanager-offwifirssichange-f.md#offWifiRssiChange) | Unsubscribe Wi-Fi rssi change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [offWifiScanStateChange](arkts-connectivity-wifimanager-offwifiscanstatechange-f.md#offWifiScanStateChange) | Unsubscribe Wi-Fi scan status change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [offWifiStateChange](arkts-connectivity-wifimanager-offwifistatechange-f.md#offWifiStateChange) | Unsubscribe Wi-Fi status change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_hotspotStateChange | Unsubscribe Wi-Fi hotspot state change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_p2pConnectionChange | Unsubscribe P2P connection change events. |
| off_p2pDeviceChange | Unsubscribe P2P local device change events. |
| off_p2pDiscoveryChange | Unsubscribe P2P discovery events. |
| off_p2pPeerDeviceChange | Unsubscribe P2P peer device change events. |
| off_p2pPersistentGroupChange | Unsubscribe P2P persistent group change events. |
| off_p2pStateChange | Unsubscribe P2P status change events. |
| off_wifiConnectionChange | Unsubscribe Wi-Fi connection change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_wifiRssiChange | Unsubscribe Wi-Fi rssi change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_wifiScanStateChange | Unsubscribe Wi-Fi scan status change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_wifiStateChange | Unsubscribe Wi-Fi status change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [onHotspotStateChange](arkts-connectivity-wifimanager-onhotspotstatechange-f.md#onHotspotStateChange) | Subscribe Wi-Fi hotspot state change events. |
| [onP2pConnectionChange](arkts-connectivity-wifimanager-onp2pconnectionchange-f.md#onP2pConnectionChange) | Subscribe P2P connection change events. |
| [onP2pDeviceChange](arkts-connectivity-wifimanager-onp2pdevicechange-f.md#onP2pDeviceChange) | Subscribe P2P local device change events. |
| [onP2pDiscoveryChange](arkts-connectivity-wifimanager-onp2pdiscoverychange-f.md#onP2pDiscoveryChange) | Subscribe P2P discovery events. |
| [onP2pPeerDeviceChange](arkts-connectivity-wifimanager-onp2ppeerdevicechange-f.md#onP2pPeerDeviceChange) | Subscribe P2P peer device change events. |
| [onP2pPersistentGroupChange](arkts-connectivity-wifimanager-onp2ppersistentgroupchange-f.md#onP2pPersistentGroupChange) | Subscribe P2P persistent group change events. |
| [onP2pStateChange](arkts-connectivity-wifimanager-onp2pstatechange-f.md#onP2pStateChange) | Subscribe P2P status change events. |
| [onWifiConnectionChange](arkts-connectivity-wifimanager-onwificonnectionchange-f.md#onWifiConnectionChange) | Subscribe Wi-Fi connection change events. |
| [onWifiRssiChange](arkts-connectivity-wifimanager-onwifirssichange-f.md#onWifiRssiChange) | Subscribe Wi-Fi rssi change events. |
| [onWifiScanStateChange](arkts-connectivity-wifimanager-onwifiscanstatechange-f.md#onWifiScanStateChange) | Subscribe Wi-Fi scan status change events. |
| [onWifiStateChange](arkts-connectivity-wifimanager-onwifistatechange-f.md#onWifiStateChange) | Subscribe Wi-Fi status change events. |
| on_hotspotStateChange | Subscribe Wi-Fi hotspot state change events. |
| on_p2pConnectionChange | Subscribe P2P connection change events. |
| on_p2pDeviceChange | Subscribe P2P local device change events. |
| on_p2pDiscoveryChange | Subscribe P2P discovery events. |
| on_p2pPeerDeviceChange | Subscribe P2P peer device change events. |
| on_p2pPersistentGroupChange | Subscribe P2P persistent group change events. |
| on_p2pStateChange | Subscribe P2P status change events. |
| on_wifiConnectionChange | Subscribe Wi-Fi connection change events. |
| on_wifiRssiChange | Subscribe Wi-Fi rssi change events. |
| on_wifiScanStateChange | Subscribe Wi-Fi scan status change events. |
| on_wifiStateChange | Subscribe Wi-Fi status change events. |
| [p2pCancelConnect](arkts-connectivity-wifimanager-p2pcancelconnect-f.md#p2pCancelConnect) | Stop an ongoing p2p connection that is being established. |
| [p2pConnect](arkts-connectivity-wifimanager-p2pconnect-f.md#p2pConnect) | Initiate a P2P connection to a device with the specified configuration. |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removeCandidateConfig) | Remove a specified candidate hotspot configuration, only the configuration which is added by ourself is allowed to be removed. The app must be in the foreground. |
| [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md#removeCandidateConfig) | Remove a specified candidate hotspot configuration, only the configuration which is added by ourself is allowed to be removed. The app must be in the foreground. |
| [removeDevice](arkts-connectivity-wifimanager-removedevice-f.md#removeDevice) | Remove a Wi-Fi DeviceConfig with networkId. After a Wi-Fi DeviceConfig is removed, its configuration will be deleted from the list of Wi-Fi configurations. If the Wi-Fi DeviceConfig is being connected, the connection will be interrupted. The application can only delete Wi-Fi DeviceConfig it has created. |
| [removeGroup](arkts-connectivity-wifimanager-removegroup-f.md#removeGroup) | Remove a P2P group. |
| [scan](arkts-connectivity-wifimanager-scan-f.md#scan) | Scan Wi-Fi hotspot. |
| [startDiscoverDevices](arkts-connectivity-wifimanager-startdiscoverdevices-f.md#startDiscoverDevices) | Start discover Wi-Fi P2P devices. |
| [startScan](arkts-connectivity-wifimanager-startscan-f.md#startScan) | Scan Wi-Fi hotspot. |
| [stopDiscoverDevices](arkts-connectivity-wifimanager-stopdiscoverdevices-f.md#stopDiscoverDevices) | Stop discover Wi-Fi P2P devices. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addHotspotBlockList](arkts-connectivity-wifimanager-addhotspotblocklist-f-sys.md#addHotspotBlockList) | Add the station into the block list, the station can NOT access the hotspot. |
| [allowAutoConnect](arkts-connectivity-wifimanager-allowautoconnect-f-sys.md#allowAutoConnect) | Set whther to allow automatic connnect by networkId. The network can be associated with again if isAllowed is true, else not. |
| [connectToDevice](arkts-connectivity-wifimanager-connecttodevice-f-sys.md#connectToDevice) | Connect to Wi-Fi hotspot by WifiDeviceConfig. |
| [delHotspotBlockList](arkts-connectivity-wifimanager-delhotspotblocklist-f-sys.md#delHotspotBlockList) | Delete the station from block list, the station can access the hotspot. |
| [deletePersistentGroup](arkts-connectivity-wifimanager-deletepersistentgroup-f-sys.md#deletePersistentGroup) | Delete the persistent P2P group with the specified network ID. |
| [disableHotspot](arkts-connectivity-wifimanager-disablehotspot-f-sys.md#disableHotspot) | Disable Wi-Fi hotspot function. This method is asynchronous. If Wi-Fi is enabled after the Wi-Fi hotspot is disabled, Wi-Fi may be re-enabled. |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disableNetwork) | Disable the specified DeviceConfig by networkId. The disabled DeviceConfig will not be associated with again. |
| [disableNetwork](arkts-connectivity-wifimanager-disablenetwork-f-sys.md#disableNetwork-(System-API)) | Disable the specified DeviceConfig by networkId for a period of time. The disabled DeviceConfig will not be associated with again. |
| [enableHiLinkHandshake](arkts-connectivity-wifimanager-enablehilinkhandshake-f-sys.md#enableHiLinkHandshake) | Enable hiLink handshake. |
| [enableHotspot](arkts-connectivity-wifimanager-enablehotspot-f-sys.md#enableHotspot) | Enable Wi-Fi hotspot function. This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled. |
| [enableSemiWifi](arkts-connectivity-wifimanager-enablesemiwifi-f-sys.md#enableSemiWifi) | Enable semi - Wifi. |
| [factoryReset](arkts-connectivity-wifimanager-factoryreset-f-sys.md#factoryReset) | Reset all saved device configure. |
| [get5GChannelList](arkts-connectivity-wifimanager-get5gchannellist-f-sys.md#get5GChannelList) | Obtain the supported 5G channel list of the device. |
| [getDeviceConfig](arkts-connectivity-wifimanager-getdeviceconfig-f-sys.md#getDeviceConfig) | Obtain the single Wi-Fi configuration with Network ID. |
| [getDisconnectedReason](arkts-connectivity-wifimanager-getdisconnectedreason-f-sys.md#getDisconnectedReason) | Obtain the latest disconnected reason. |
| [getHotspotBlockList](arkts-connectivity-wifimanager-gethotspotblocklist-f-sys.md#getHotspotBlockList) | Get all the stations in the block list. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid. |
| [getHotspotConfig](arkts-connectivity-wifimanager-gethotspotconfig-f-sys.md#getHotspotConfig) | Obtain the Wi-Fi hotspot configuration. |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getP2pGroups) | Obtain information about the groups. |
| [getP2pGroups](arkts-connectivity-wifimanager-getp2pgroups-f-sys.md#getP2pGroups-(System-API)) | Obtain information about the groups. |
| [getScanAlwaysAllowed](arkts-connectivity-wifimanager-getscanalwaysallowed-f-sys.md#getScanAlwaysAllowed) | Get scan always allowed flag. |
| [getStations](arkts-connectivity-wifimanager-getstations-f-sys.md#getStations) | Obtain the list of stations that are connected to the Wi-Fi hotspot. This method can only be used on a device that serves as a Wi-Fi hotspot. |
| [getSupportedFeatures](arkts-connectivity-wifimanager-getsupportedfeatures-f-sys.md#getSupportedFeatures) | Obtain the features supported by the device. To check whether this device supports a specified feature. |
| [getWifiCapability](arkts-connectivity-wifimanager-getwificapability-f-sys.md#getWifiCapability) | Get Wi-Fi capability |
| [getWifiDetailState](arkts-connectivity-wifimanager-getwifidetailstate-f-sys.md#getWifiDetailState) | Obtains information about a Wi-Fi detail state. |
| [isHotspotDualBandSupported](arkts-connectivity-wifimanager-ishotspotdualbandsupported-f-sys.md#isHotspotDualBandSupported) | Check whether a device serving as a Wi-Fi hotspot supports both the 2.4 GHz and 5 GHz Wi-Fi. |
| [isOpenSoftApAllowed](arkts-connectivity-wifimanager-isopensoftapallowed-f-sys.md#isOpenSoftApAllowed) | Check whether Wi-Fi hotspot is can be operated under some situation. When the airplane mode is turned on and does not support the coexistence of softap and sta, nor does it support signal bridge, the hotspot switch cannot be operated. |
| [isRandomMacDisabled](arkts-connectivity-wifimanager-israndommacdisabled-f-sys.md#isRandomMacDisabled) | is random mac disabled |
| [offDeviceConfigChange](arkts-connectivity-wifimanager-offdeviceconfigchange-f-sys.md#offDeviceConfigChange) | Subscribe Wi-Fi device config change events. |
| [offHotspotStaJoin](arkts-connectivity-wifimanager-offhotspotstajoin-f-sys.md#offHotspotStaJoin) | Unsubscribe Wi-Fi hotspot sta join events. All callback functions will be deregistered If there is no specific callback parameter. |
| [offHotspotStaLeave](arkts-connectivity-wifimanager-offhotspotstaleave-f-sys.md#offHotspotStaLeave) | Unsubscribe Wi-Fi hotspot sta leave events. |
| [offStreamChange](arkts-connectivity-wifimanager-offstreamchange-f-sys.md#offStreamChange) | Unsubscribe Wi-Fi stream change events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_deviceConfigChange | Subscribe Wi-Fi device config change events. |
| off_hotspotStaJoin | Unsubscribe Wi-Fi hotspot sta join events. All callback functions will be deregistered If there is no specific callback parameter. |
| off_hotspotStaLeave | Unsubscribe Wi-Fi hotspot sta leave events. |
| off_streamChange | Unsubscribe Wi-Fi stream change events. All callback functions will be deregistered If there is no specific callback parameter. |
| [onDeviceConfigChange](arkts-connectivity-wifimanager-ondeviceconfigchange-f-sys.md#onDeviceConfigChange) | Subscribe Wi-Fi device config change events. |
| [onHotspotStaJoin](arkts-connectivity-wifimanager-onhotspotstajoin-f-sys.md#onHotspotStaJoin) | Subscribe Wi-Fi hotspot sta join events. |
| [onHotspotStaLeave](arkts-connectivity-wifimanager-onhotspotstaleave-f-sys.md#onHotspotStaLeave) | Subscribe Wi-Fi hotspot sta leave events. |
| [onStreamChange](arkts-connectivity-wifimanager-onstreamchange-f-sys.md#onStreamChange) | Subscribe Wi-Fi stream change events. |
| on_deviceConfigChange | Subscribe Wi-Fi device config change events. |
| on_hotspotStaJoin | Subscribe Wi-Fi hotspot sta join events. |
| on_hotspotStaLeave | Subscribe Wi-Fi hotspot sta leave events. |
| on_streamChange | Subscribe Wi-Fi stream change events. |
| [reassociate](arkts-connectivity-wifimanager-reassociate-f-sys.md#reassociate) | Re-associate to current network. |
| [reconnect](arkts-connectivity-wifimanager-reconnect-f-sys.md#reconnect) | Re-connect to current network. |
| [removeAllNetwork](arkts-connectivity-wifimanager-removeallnetwork-f-sys.md#removeAllNetwork) | Remove all the saved Wi-Fi configurations. |
| [setDeviceName](arkts-connectivity-wifimanager-setdevicename-f-sys.md#setDeviceName) | Set the name of the Wi-Fi P2P device. |
| [setHotspotConfig](arkts-connectivity-wifimanager-sethotspotconfig-f-sys.md#setHotspotConfig) | Set the hotspot configuration for the device. |
| [setScanAlwaysAllowed](arkts-connectivity-wifimanager-setscanalwaysallowed-f-sys.md#setScanAlwaysAllowed) | User can trigger scan even Wi-Fi is disabled. |
| [setWifiCapability](arkts-connectivity-wifimanager-setwificapability-f-sys.md#setWifiCapability) | Set Wi-Fi capability |
| [startPortalCertification](arkts-connectivity-wifimanager-startportalcertification-f-sys.md#startPortalCertification) | Start Portal certification. |
| [startWifiDetection](arkts-connectivity-wifimanager-startwifidetection-f-sys.md#startWifiDetection) | Start Wi-Fi network detection |
| [updateNetwork](arkts-connectivity-wifimanager-updatenetwork-f-sys.md#updateNetwork) | Update the specified Wi-Fi configuration. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ConnectSettings](arkts-connectivity-wifimanager-connectsettings-i.md) | Describes the settings for Wi-Fi connection. |
| [IpInfo](arkts-connectivity-wifimanager-ipinfo-i.md) | Wi-Fi IP information. |
| [Ipv6Info](arkts-connectivity-wifimanager-ipv6info-i.md) | Wi-Fi IPv6 information. |
| [WifiDeviceConfig](arkts-connectivity-wifimanager-wifideviceconfig-i.md) | Wi-Fi device configuration information. |
| [WifiEapConfig](arkts-connectivity-wifimanager-wifieapconfig-i.md) | Wi-Fi EAP config. |
| [WifiInfoElem](arkts-connectivity-wifimanager-wifiinfoelem-i.md) | Wi-Fi information elements. |
| [WifiLinkedInfo](arkts-connectivity-wifimanager-wifilinkedinfo-i.md) | Wi-Fi connection information. |
| [WifiP2PConfig](arkts-connectivity-wifimanager-wifip2pconfig-i.md) | P2P config. |
| [WifiP2pDevice](arkts-connectivity-wifimanager-wifip2pdevice-i.md) | P2P device information. |
| [WifiP2pGroupInfo](arkts-connectivity-wifimanager-wifip2pgroupinfo-i.md) | P2P group information. |
| [WifiP2pLinkedInfo](arkts-connectivity-wifimanager-wifip2plinkedinfo-i.md) | P2P linked information. |
| [WifiScanInfo](arkts-connectivity-wifimanager-wifiscaninfo-i.md) | Describes the scanned Wi-Fi information. |
| [WifiWapiConfig](arkts-connectivity-wifimanager-wifiwapiconfig-i.md) | Wi-Fi WAPI config. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [HotspotConfig](arkts-connectivity-wifimanager-hotspotconfig-i-sys.md) | Wi-Fi hotspot configuration information. |
| [IpConfig](arkts-connectivity-wifimanager-ipconfig-i-sys.md) | Wi-Fi IP configuration information. |
| [Ipv6Config](arkts-connectivity-wifimanager-ipv6config-i-sys.md) | Wi-Fi Ipv6 configuration information. |
| [StationInfo](arkts-connectivity-wifimanager-stationinfo-i-sys.md) | Wi-Fi station information. |
| [WifiDeviceConfig](arkts-connectivity-wifimanager-wifideviceconfig-i-sys.md) | Wi-Fi device configuration information. |
| [WifiLinkedInfo](arkts-connectivity-wifimanager-wifilinkedinfo-i-sys.md) | Wi-Fi connection information. |
| [WifiProxyConfig](arkts-connectivity-wifimanager-wifiproxyconfig-i-sys.md) | Wi-Fi Proxy config. |
| [WifiScanInfo](arkts-connectivity-wifimanager-wifiscaninfo-i-sys.md) | Describes the scanned Wi-Fi information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ConnState](arkts-connectivity-wifimanager-connstate-e.md) | The state of Wi-Fi connection enumeration. |
| [DeviceAddressType](arkts-connectivity-wifimanager-deviceaddresstype-e.md) | Wi-Fi device address( mac / bssid ) type. |
| [EapMethod](arkts-connectivity-wifimanager-eapmethod-e.md) | Wi-Fi EAP method. |
| [GroupOwnerBand](arkts-connectivity-wifimanager-groupownerband-e.md) | P2P group owner band. |
| [P2pConnectState](arkts-connectivity-wifimanager-p2pconnectstate-e.md) | P2P connection status. |
| [P2pDeviceStatus](arkts-connectivity-wifimanager-p2pdevicestatus-e.md) | P2P device status. |
| [Phase2Method](arkts-connectivity-wifimanager-phase2method-e.md) | Wi-Fi phase 2 method. |
| [WapiPskType](arkts-connectivity-wifimanager-wapipsktype-e.md) | Describes the WAPI pre-shared key Type. |
| [WifiBandType](arkts-connectivity-wifimanager-wifibandtype-e.md) | Wi-Fi band type. |
| [WifiCapability](arkts-connectivity-wifimanager-wificapability-e.md) | Wi-Fi Capability |
| [WifiCategory](arkts-connectivity-wifimanager-wificategory-e.md) | Wi-Fi Category. |
| [WifiChannelWidth](arkts-connectivity-wifimanager-wifichannelwidth-e.md) | Describes the wifi channel width. |
| [WifiLinkType](arkts-connectivity-wifimanager-wifilinktype-e.md) | Wi-Fi link type. |
| [WifiSecurityType](arkts-connectivity-wifimanager-wifisecuritytype-e.md) | Describes the wifi security type. |
| [WifiStandard](arkts-connectivity-wifimanager-wifistandard-e.md) | Wi-Fi standard. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DisconnectedReason](arkts-connectivity-wifimanager-disconnectedreason-e-sys.md) | Wi-Fi disconnected reason. |
| [IpType](arkts-connectivity-wifimanager-iptype-e-sys.md) | Wi-Fi IP type enumeration. |
| [ProxyMethod](arkts-connectivity-wifimanager-proxymethod-e-sys.md) | Wi-Fi Proxy method. |
| [SuppState](arkts-connectivity-wifimanager-suppstate-e-sys.md) | The state of the supplicant enumeration. |
| [WifiDetailState](arkts-connectivity-wifimanager-wifidetailstate-e-sys.md) | Wi-Fi detail state. |
<!--DelEnd-->

