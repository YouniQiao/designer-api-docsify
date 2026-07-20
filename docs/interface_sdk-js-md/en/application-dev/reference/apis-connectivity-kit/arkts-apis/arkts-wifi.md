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

| Name | Description |
| --- | --- |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig) | Adds a specified untrusted hotspot configuration.  <p>This method adds one configuration at a time. After this configuration is added,your device will determine whether to connect to the hotspot. |
| [addUntrustedConfig](arkts-connectivity-wifi-adduntrustedconfig-f.md#adduntrustedconfig-1) | Adds a specified untrusted hotspot configuration.  <p>This method adds one configuration at a time. After this configuration is added,your device will determine whether to connect to the hotspot. |
| [createGroup](arkts-connectivity-wifi-creategroup-f.md#creategroup) | Creates a P2P group. |
| [getCountryCode](arkts-connectivity-wifi-getcountrycode-f.md#getcountrycode) | Obtains the country code of this device. |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup) | Obtains information about the current group. |
| [getCurrentGroup](arkts-connectivity-wifi-getcurrentgroup-f.md#getcurrentgroup-1) | Obtains information about the current group. |
| [getIpInfo](arkts-connectivity-wifi-getipinfo-f.md#getipinfo) | Obtains the IP information of a Wi-Fi connection.  <p>The IP information includes the host IP address, gateway address, and DNS information. |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo) | Obtains information about a Wi-Fi connection. |
| [getLinkedInfo](arkts-connectivity-wifi-getlinkedinfo-f.md#getlinkedinfo-1) | Obtains information about a Wi-Fi connection. |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo) | Obtains information about a P2P connection. |
| [getP2pLinkedInfo](arkts-connectivity-wifi-getp2plinkedinfo-f.md#getp2plinkedinfo-1) | Obtains information about a P2P connection. |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices) | Obtains the information about the found devices. |
| [getP2pPeerDevices](arkts-connectivity-wifi-getp2ppeerdevices-f.md#getp2ppeerdevices-1) | Obtains the information about the found devices. |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos) | Obtains the hotspot information that scanned. |
| [getScanInfos](arkts-connectivity-wifi-getscaninfos-f.md#getscaninfos-1) | Obtains the hotspot information that scanned. |
| [getSignalLevel](arkts-connectivity-wifi-getsignallevel-f.md#getsignallevel) | Calculates the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band. |
| [isConnected](arkts-connectivity-wifi-isconnected-f.md#isconnected) | Checks whether a Wi-Fi connection has been set up. |
| [isFeatureSupported](arkts-connectivity-wifi-isfeaturesupported-f.md#isfeaturesupported) | Checks whether this device supports a specified feature. |
| [isWifiActive](arkts-connectivity-wifi-iswifiactive-f.md#iswifiactive) | Queries the Wi-Fi status |
| [off](arkts-connectivity-wifi-off-f.md#off) | Unsubscribe Wi-Fi status change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f.md#off-1) | Unsubscribe Wi-Fi connection change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f.md#off-2) | Unsubscribe Wi-Fi scan status change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f.md#off-3) | Unsubscribe Wi-Fi rssi change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f.md#off-5) | Unsubscribe Wi-Fi hotspot state change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f.md#off-8) | Unsubscribe P2P status change events. |
| [off](arkts-connectivity-wifi-off-f.md#off-9) | Unsubscribe P2P connection change events. |
| [off](arkts-connectivity-wifi-off-f.md#off-10) | Unsubscribe P2P local device change events. |
| [off](arkts-connectivity-wifi-off-f.md#off-11) | Unsubscribe P2P peer device change events. |
| [off](arkts-connectivity-wifi-off-f.md#off-12) | Unsubscribe P2P persistent group change events. |
| [off](arkts-connectivity-wifi-off-f.md#off-13) | Unsubscribe P2P discovery events. |
| [on](arkts-connectivity-wifi-on-f.md#on) | Subscribe Wi-Fi status change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-1) | Subscribe Wi-Fi connection change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-2) | Subscribe Wi-Fi scan status change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-3) | Subscribe Wi-Fi rssi change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-5) | Subscribe Wi-Fi hotspot state change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-8) | Subscribe P2P status change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-9) | Subscribe P2P connection change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-10) | Subscribe P2P local device change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-11) | Subscribe P2P peer device change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-12) | Subscribe P2P persistent group change events. |
| [on](arkts-connectivity-wifi-on-f.md#on-13) | Subscribe P2P discovery events. |
| [p2pCancelConnect](arkts-connectivity-wifi-p2pcancelconnect-f.md#p2pcancelconnect) | Canceling a P2P connection. |
| [p2pConnect](arkts-connectivity-wifi-p2pconnect-f.md#p2pconnect) | Initiates a P2P connection to a device with the specified configuration. |
| [removeGroup](arkts-connectivity-wifi-removegroup-f.md#removegroup) | Removes a P2P group. |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig) | Removes a specified untrusted hotspot configuration.  <p>This method removes one configuration at a time. |
| [removeUntrustedConfig](arkts-connectivity-wifi-removeuntrustedconfig-f.md#removeuntrustedconfig-1) | Removes a specified untrusted hotspot configuration.  <p>This method removes one configuration at a time. |
| [scan](arkts-connectivity-wifi-scan-f.md#scan) | Scans Wi-Fi hotspot.  <p>This API works in asynchronous mode.</p> |
| [startDiscoverDevices](arkts-connectivity-wifi-startdiscoverdevices-f.md#startdiscoverdevices) | Discover Wi-Fi P2P devices. |
| [stopDiscoverDevices](arkts-connectivity-wifi-stopdiscoverdevices-f.md#stopdiscoverdevices) | Stops discovering Wi-Fi P2P devices. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig) | Adds Wi-Fi connection configuration to the device.  <p>The configuration will be updated when the configuration is added.</p> |
| [addDeviceConfig](arkts-connectivity-wifi-adddeviceconfig-f-sys.md#adddeviceconfig-1) | Adds Wi-Fi connection configuration to the device.  <p>The configuration will be updated when the configuration is added.</p> |
| [connectToDevice](arkts-connectivity-wifi-connecttodevice-f-sys.md#connecttodevice) | Connects to Wi-Fi network. |
| [connectToNetwork](arkts-connectivity-wifi-connecttonetwork-f-sys.md#connecttonetwork) | Connects to Wi-Fi network. |
| [deletePersistentGroup](arkts-connectivity-wifi-deletepersistentgroup-f-sys.md#deletepersistentgroup) | Deletes the persistent P2P group with the specified network ID. |
| [disableHotspot](arkts-connectivity-wifi-disablehotspot-f-sys.md#disablehotspot) | Disables a Wi-Fi hotspot.  <p>This method is asynchronous. If Wi-Fi is enabled after the Wi-Fi hotspot is disabled, Wi-Fi may be re-enabled. |
| [disableNetwork](arkts-connectivity-wifi-disablenetwork-f-sys.md#disablenetwork) | Disables a specified network.  <p>The disabled network will not be associated with again. |
| [disableWifi](arkts-connectivity-wifi-disablewifi-f-sys.md#disablewifi) | Disables Wi-Fi. |
| [disconnect](arkts-connectivity-wifi-disconnect-f-sys.md#disconnect) | Disconnect Wi-Fi network. |
| [enableHotspot](arkts-connectivity-wifi-enablehotspot-f-sys.md#enablehotspot) | Enables a Wi-Fi hotspot.  <p>This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled. |
| [enableWifi](arkts-connectivity-wifi-enablewifi-f-sys.md#enablewifi) | Enables Wi-Fi. |
| [getDeviceConfigs](arkts-connectivity-wifi-getdeviceconfigs-f-sys.md#getdeviceconfigs) | Obtains the list of all existing Wi-Fi configurations.  <p>You can obtain only the Wi-Fi configurations you created on your own application. |
| [getDeviceMacAddress](arkts-connectivity-wifi-getdevicemacaddress-f-sys.md#getdevicemacaddress) | Obtains the MAC address of a Wi-Fi device. Wi-Fi must be enabled.  <p>The MAC address is unique and cannot be changed. |
| [getHotspotConfig](arkts-connectivity-wifi-gethotspotconfig-f-sys.md#gethotspotconfig) | Obtains the Wi-Fi hotspot configuration. |
| [getStations](arkts-connectivity-wifi-getstations-f-sys.md#getstations) | Obtains the list of clients that are connected to a Wi-Fi hotspot.  <p>This method can only be used on a device that serves as a Wi-Fi hotspot. |
| [getSupportedFeatures](arkts-connectivity-wifi-getsupportedfeatures-f-sys.md#getsupportedfeatures) | Obtains the features supported by this device.  <p>To check whether this device supports a specified feature. |
| [isHotspotActive](arkts-connectivity-wifi-ishotspotactive-f-sys.md#ishotspotactive) | Checks whether Wi-Fi hotspot is active on a device. |
| [isHotspotDualBandSupported](arkts-connectivity-wifi-ishotspotdualbandsupported-f-sys.md#ishotspotdualbandsupported) | Checks whether a device serving as a Wi-Fi hotspot supports both the 2.4 GHz and 5 GHz Wi-Fi. |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-4) | Unsubscribe Wi-Fi stream change events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-6) | Unsubscribe Wi-Fi hotspot sta join events.  <p>All callback functions will be deregistered If there is no specific callback parameter.</p> |
| [off](arkts-connectivity-wifi-off-f-sys.md#off-7) | Unsubscribe Wi-Fi hotspot sta leave events. |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-4) | Subscribe Wi-Fi stream change events. |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-6) | Subscribe Wi-Fi hotspot sta join events. |
| [on](arkts-connectivity-wifi-on-f-sys.md#on-7) | Subscribe Wi-Fi hotspot sta leave events. |
| [reassociate](arkts-connectivity-wifi-reassociate-f-sys.md#reassociate) | Re-associate to current network. |
| [reconnect](arkts-connectivity-wifi-reconnect-f-sys.md#reconnect) | Re-connects to current network. |
| [removeAllNetwork](arkts-connectivity-wifi-removeallnetwork-f-sys.md#removeallnetwork) | Removes all the saved Wi-Fi configurations. |
| [removeDevice](arkts-connectivity-wifi-removedevice-f-sys.md#removedevice) | Deletes a Wi-Fi network with a specified ID.  <p>After a Wi-Fi network is deleted, its configuration will be deleted from the list of Wi-Fi configurations.If the Wi-Fi network is being connected, the connection will be interrupted.The application can only delete Wi-Fi networks it has created. |
| [setDeviceName](arkts-connectivity-wifi-setdevicename-f-sys.md#setdevicename) | Sets the name of the Wi-Fi P2P device. |
| [setHotspotConfig](arkts-connectivity-wifi-sethotspotconfig-f-sys.md#sethotspotconfig) | Sets the hotspot for a device.  <p>Only OPEN and WPA2 PSK hotspot can be configured. |
| [updateNetwork](arkts-connectivity-wifi-updatenetwork-f-sys.md#updatenetwork) | Updates the specified Wi-Fi configuration. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [IpInfo](arkts-connectivity-wifi-ipinfo-i.md) | Wi-Fi IP information. |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | Wi-Fi device configuration information. |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i.md) | Wi-Fi connection information. |
| [WifiP2PConfig](arkts-connectivity-wifi-wifip2pconfig-i.md) | P2P config. |
| [WifiP2pDevice](arkts-connectivity-wifi-wifip2pdevice-i.md) | P2P device information. |
| [WifiP2pGroupInfo](arkts-connectivity-wifi-wifip2pgroupinfo-i.md) | P2P group information. |
| [WifiP2pLinkedInfo](arkts-connectivity-wifi-wifip2plinkedinfo-i.md) | P2P linked information. |
| [WifiScanInfo](arkts-connectivity-wifi-wifiscaninfo-i.md) | Describes the scanned Wi-Fi information. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) | Wi-Fi hotspot configuration information. |
| [IpConfig](arkts-connectivity-wifi-ipconfig-i-sys.md) | Wi-Fi IP configuration information. |
| [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) | Wi-Fi station information. |
| [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i-sys.md) | Wi-Fi device configuration information. |
| [WifiLinkedInfo](arkts-connectivity-wifi-wifilinkedinfo-i-sys.md) | Wi-Fi connection information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ConnState](arkts-connectivity-wifi-connstate-e.md) | The state of Wi-Fi connection enumeration. |
| [GroupOwnerBand](arkts-connectivity-wifi-groupownerband-e.md) | P2P group owner band. |
| [P2pConnectState](arkts-connectivity-wifi-p2pconnectstate-e.md) | P2P connection status. |
| [P2pDeviceStatus](arkts-connectivity-wifi-p2pdevicestatus-e.md) | P2P device status. |
| [WifiSecurityType](arkts-connectivity-wifi-wifisecuritytype-e.md) | Describes the wifi security type. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [IpType](arkts-connectivity-wifi-iptype-e-sys.md) | Wi-Fi IP type enumeration. |
| [SuppState](arkts-connectivity-wifi-suppstate-e-sys.md) | The state of the supplicant enumeration. |
<!--DelEnd-->

