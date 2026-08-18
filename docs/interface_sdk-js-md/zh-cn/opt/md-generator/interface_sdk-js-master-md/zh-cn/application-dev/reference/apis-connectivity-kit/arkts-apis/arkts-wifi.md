# @ohos.wifi

提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

**起始版本：** 6

<!--Device-unnamed-declare namespace wifi--><!--Device-unnamed-declare namespace wifi-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig) |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig) |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md#creategroup) |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md#getcountrycode) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup) |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup) |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md#getipinfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo) |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo) |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices) |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos) |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos) |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md#getsignallevel) |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md#isconnected) |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md#isfeaturesupported) |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md#iswifiactive) |
| [off_hotspotStateChange](arkts-connectivity-wifi-offhotspotstatechange-f.md#offhotspotstatechange) |
| [off_p2pConnectionChange](arkts-connectivity-wifi-offp2pconnectionchange-f.md#offp2pconnectionchange) |
| [off_p2pDeviceChange](arkts-connectivity-wifi-offp2pdevicechange-f.md#offp2pdevicechange) |
| [off_p2pDiscoveryChange](arkts-connectivity-wifi-offp2pdiscoverychange-f.md#offp2pdiscoverychange) |
| [off_p2pPeerDeviceChange](arkts-connectivity-wifi-offp2ppeerdevicechange-f.md#offp2ppeerdevicechange) |
| [off_p2pPersistentGroupChange](arkts-connectivity-wifi-offp2ppersistentgroupchange-f.md#offp2ppersistentgroupchange) |
| [off_p2pStateChange](arkts-connectivity-wifi-offp2pstatechange-f.md#offp2pstatechange) |
| [off_wifiConnectionChange](arkts-connectivity-wifi-offwificonnectionchange-f.md#offwificonnectionchange) |
| [off_wifiRssiChange](arkts-connectivity-wifi-offwifirssichange-f.md#offwifirssichange) |
| [off_wifiScanStateChange](arkts-connectivity-wifi-offwifiscanstatechange-f.md#offwifiscanstatechange) |
| [off_wifiStateChange](arkts-connectivity-wifi-offwifistatechange-f.md#offwifistatechange) |
| [on_hotspotStateChange](arkts-connectivity-wifi-onhotspotstatechange-f.md#onhotspotstatechange) |
| [on_p2pConnectionChange](arkts-connectivity-wifi-onp2pconnectionchange-f.md#onp2pconnectionchange) |
| [on_p2pDeviceChange](arkts-connectivity-wifi-onp2pdevicechange-f.md#onp2pdevicechange) |
| [on_p2pDiscoveryChange](arkts-connectivity-wifi-onp2pdiscoverychange-f.md#onp2pdiscoverychange) |
| [on_p2pPeerDeviceChange](arkts-connectivity-wifi-onp2ppeerdevicechange-f.md#onp2ppeerdevicechange) |
| [on_p2pPersistentGroupChange](arkts-connectivity-wifi-onp2ppersistentgroupchange-f.md#onp2ppersistentgroupchange) |
| [on_p2pStateChange](arkts-connectivity-wifi-onp2pstatechange-f.md#onp2pstatechange) |
| [on_wifiConnectionChange](arkts-connectivity-wifi-onwificonnectionchange-f.md#onwificonnectionchange) |
| [on_wifiRssiChange](arkts-connectivity-wifi-onwifirssichange-f.md#onwifirssichange) |
| [on_wifiScanStateChange](arkts-connectivity-wifi-onwifiscanstatechange-f.md#onwifiscanstatechange) |
| [on_wifiStateChange](arkts-connectivity-wifi-onwifistatechange-f.md#onwifistatechange) |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md#p2pcancelconnect) |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md#p2pconnect) |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md#removegroup) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig) |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig) |
| [scan](arkts-connectivity-wifi-scan-f.md#scan) |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md#startdiscoverdevices) |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md#stopdiscoverdevices) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig系统接口) |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig系统接口) |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md#connecttodevice系统接口) |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md#connecttonetwork系统接口) |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md#deletepersistentgroup系统接口) |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md#disablehotspot系统接口) |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md#disablenetwork系统接口) |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md#disablewifi系统接口) |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md#disconnect系统接口) |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md#enablehotspot系统接口) |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md#enablewifi系统接口) |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md#getdeviceconfigs系统接口) |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md#getdevicemacaddress系统接口) |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md#gethotspotconfig系统接口) |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md#getstations系统接口) |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md#getsupportedfeatures系统接口) |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md#ishotspotactive系统接口) |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md#ishotspotdualbandsupported系统接口) |
| [off_hotspotStaJoin](arkts-connectivity-wifi-offhotspotstajoin-f-sys.md#offhotspotstajoin) |
| [off_hotspotStaLeave](arkts-connectivity-wifi-offhotspotstaleave-f-sys.md#offhotspotstaleave) |
| [off_streamChange](arkts-connectivity-wifi-offstreamchange-f-sys.md#offstreamchange) |
| [on_hotspotStaJoin](arkts-connectivity-wifi-onhotspotstajoin-f-sys.md#onhotspotstajoin) |
| [on_hotspotStaLeave](arkts-connectivity-wifi-onhotspotstaleave-f-sys.md#onhotspotstaleave) |
| [on_streamChange](arkts-connectivity-wifi-onstreamchange-f-sys.md#onstreamchange) |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md#reassociate系统接口) |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md#reconnect系统接口) |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md#removeallnetwork系统接口) |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md#removedevice系统接口) |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md#setdevicename系统接口) |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md#sethotspotconfig系统接口) |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md#updatenetwork系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) |
| [IpConfig](arkts-connectivity-wifi-ipconfig-i-sys.md) |
| [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i-sys.md) |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ConnState](arkts-connectivity-wifi-connstate-e.md) |
| [GroupOwnerBand](arkts-connectivity-wifi-groupownerband-e.md) |
| [P2pConnectState](arkts-connectivity-wifi-p2pconnectstate-e.md) |
| [P2pDeviceStatus](arkts-connectivity-wifi-p2pdevicestatus-e.md) |
| [WifiSecurityType](arkts-connectivity-wifi-wifisecuritytype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [IpType](arkts-connectivity-wifi-iptype-e-sys.md) |
| [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md) |
<!--DelEnd-->
