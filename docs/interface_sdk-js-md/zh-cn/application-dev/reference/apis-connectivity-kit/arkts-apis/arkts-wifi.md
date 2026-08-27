# @ohos.wifi

提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。@namespace wifi

**起始版本：** 6

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md) | 添加不可信网络配置，使用Promise异步回调。 |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md) | 添加不可信网络配置，使用callback异步回调。 |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md) | 创建P2P群组。 |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md) | 获取国家码信息。 |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md) | 获取当前群组信息。 |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md) | 获取当前群组信息。 |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md) | 获取IP信息。 |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md) | 获取WLAN连接信息。使用Promise异步回调。 |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md) | 获取WLAN连接信息。使用callback异步回调。 |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md) | 获取P2P连接信息。 |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md) | 获取P2P连接信息。 |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md) | 获取发现的设备信息。 |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md) | 获取发现的设备信息。 |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md) | 获取扫描结果，使用Promise异步回调。 |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md) | 获取扫描结果，使用callback异步回调。 |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md) | 查询WLAN信号强度。 |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md) | 查询WLAN是否已连接。 |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md) | 判断设备是否支持相关WLAN特性。 |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md) | 查询WLAN是否已使能。 |
| [off](arkts-connectivity-wifi-off-f.md#offwifistatechange) | 取消订阅WLAN状态改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offwificonnectionchange) | 取消订阅WLAN连接状态改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offwifiscanstatechange) | 取消订阅WLAN扫描状态改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offwifirssichange) | 取消订阅WLAN RSSI改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offhotspotstatechange) | 取消订阅WLAN热点状态改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2pstatechange) | 取消订阅P2P状态改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2pconnectionchange) | 取消订阅P2P连接改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2pdevicechange) | 取消订阅P2P本地设备改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2ppeerdevicechange) | 取消订阅P2P对端设备改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2ppersistentgroupchange) | 取消订阅P2P持久群组改变事件。 |
| [off](arkts-connectivity-wifi-off-f.md#offp2pdiscoverychange) | 取消订阅P2P发现事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onwifistatechange) | 订阅WLAN状态改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onwificonnectionchange) | 订阅WLAN连接状态改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onwifiscanstatechange) | 订阅WLAN扫描状态改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onwifirssichange) | 订阅WLAN RSSI改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onhotspotstatechange) | 订阅WLAN热点状态改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2pstatechange) | 订阅P2P状态改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2pconnectionchange) | 订阅P2P连接改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2pdevicechange) | 订阅P2P本地设备改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2ppeerdevicechange) | 订阅P2P对端设备改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2ppersistentgroupchange) | 订阅P2P持久群组改变事件。 |
| [on](arkts-connectivity-wifi-on-f.md#onp2pdiscoverychange) | 订阅P2P发现事件。 |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md) | 取消P2P连接。 |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md) | 使用指定配置发起与设备的P2P连接。 |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md) | 移除P2P群组。 |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md) | 移除不可信网络配置，使用Promise异步回调。 |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md) | 移除不可信网络配置，使用callback异步回调。 |
| [scan](arkts-connectivity-wifi-scan-f.md) | 启动WLAN扫描。 |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md) | 发现WLAN P2P设备。 |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md) | 停止发现WLAN P2P设备。 |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md) | 添加网络配置，使用Promise异步回调。 |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md) | 添加网络配置，使用callback异步回调。 |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md) | 连接到指定网络。 |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md) | 应用使用该接口连接到热点。 |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md) | 删除指定网络ID的持久P2P群组。 |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md) | 去使能热点。 |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md) | 去使能网络配置。 |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md) | 去使能WLAN。 |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md) | 断开连接的网络。 |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md) | 使能热点。 |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md) | 使能WLAN。 |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md) | 获取网络配置。 |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md) | 获取设备的MAC地址。WLAN必须已使能。 |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md) | 获取热点配置信息。 |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md) | 获取连接的设备。 |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md) | 查询设备支持的特性。 |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md) | 热点是否已使能。 |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md) | 热点是否支持双频。 |
| off | 取消订阅WLAN数据流改变事件。 |
| off | 取消订阅WLAN热点STA加入事件。 |
| off | 取消订阅WLAN热点STA离开事件。 |
| on | 订阅WLAN数据流改变事件。 |
| on | 订阅WLAN热点STA加入事件。 |
| on | 订阅WLAN热点STA离开事件。 |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md) | 重新关联网络。 |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md) | 重新连接网络。 |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md) | 移除所有网络配置。 |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md) | 移除指定的网络配置。 |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md) | 设置WLAN P2P设备名称。 |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md) | 设置热点配置信息。 |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md) | 更新网络配置。 |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [IpInfo](arkts-connectivity-wifi-ipinfo-i.md) | WLAN IP信息。 |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | WLAN设备配置信息。 |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i.md) | WLAN连接信息。 |
| [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) | P2P配置。@interface WifiP2PConfig |
| [WifiP2pDevice](arkts-connectivity-wifi-wifip2pdevice-i.md) | P2P设备信息。 |
| [WifiP2pGroupInfo](arkts-connectivity-wifi-wifip2pgroupinfo-i.md) | P2P群组信息。@interface WifiP2pGroupInfo |
| [WifiP2pLinkedInfo](arkts-connectivity-wifi-wifip2plinkedinfo-i.md) | P2P连接信息。 |
| [WifiScanInfo](arkts-connectivity-wifi-wifiscaninfo-i.md) | 描述扫描到的WLAN信息。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) | WLAN热点配置信息。 |
| [IpConfig](arkts-connectivity-wifi-ipconfig-i-sys.md) | WLAN IP配置信息。 |
| [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) | WLAN站点信息。 |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i-sys.md) | WLAN设备配置信息。 |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i-sys.md) | WLAN连接信息。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ConnState](arkts-connectivity-wifi-connstate-e.md) | WLAN连接状态枚举。 |
| [GroupOwnerBand](arkts-connectivity-wifi-groupownerband-e.md) | P2P群组所有者频段。 |
| [P2pConnectState](arkts-connectivity-wifi-p2pconnectstate-e.md) | P2P连接状态。 |
| [P2pDeviceStatus](arkts-connectivity-wifi-p2pdevicestatus-e.md) | P2P设备状态。 |
| [WifiSecurityType](arkts-connectivity-wifi-wifisecuritytype-e.md) | 描述WLAN加密类型。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [IpType](arkts-connectivity-wifi-iptype-e-sys.md) | WLAN IP类型枚举。 |
| [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md) | supplicant状态枚举。 |
<!--DelEnd-->
