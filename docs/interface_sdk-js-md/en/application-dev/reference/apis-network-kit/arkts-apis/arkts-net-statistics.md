# @ohos.net.statistics

The Traffic Management module provides the capability to obtain device network traffic data. This module supports querying packet traffic usage from multiple dimensions, for example: - Obtaining the uplink/downlink traffic data of a specified NIC. - Obtaining the total traffic data of all NICs, facilitating the viewing of overall device network usage. - Obtaining the traffic data of a specified application based on the application UID, helping you monitor the network resource consumption of applications. - Obtaining traffic statistics for a specified socket, providing a data foundation for fine-grained network performance analysis. - Obtaining the historical traffic usage of an application within a specified time period, facilitating the analysis of long-term network usage trends of the application.

**Since:** 23

<!--Device-unnamed-declare namespace statistics--><!--Device-unnamed-declare namespace statistics-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllRxBytes](arkts-network-statistics-getallrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getAllRxBytes](arkts-network-statistics-getallrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getAllTxBytes](arkts-network-statistics-getalltxbytes-f.md) | Obtains the total uplink traffic of all NICs (in bytes) from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getAllTxBytes](arkts-network-statistics-getalltxbytes-f.md) | Obtains the total uplink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getCellularRxBytes](arkts-network-statistics-getcellularrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210 &gt; 3012 will be thrown. |
| [getCellularRxBytes](arkts-network-statistics-getcellularrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210 &gt; 3012 will be thrown. |
| [getCellularTxBytes](arkts-network-statistics-getcellulartxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210 &gt; 3012 will be thrown. |
| [getCellularTxBytes](arkts-network-statistics-getcellulartxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210 &gt; 3012 will be thrown. |
| [getIfaceRxBytes](arkts-network-statistics-getifacerxbytes-f.md) | Obtains the total downlink traffic of the specified NIC from the last startup to the time when this API is called ( in bytes). This API uses an asynchronous callback to return the result. |
| [getIfaceRxBytes](arkts-network-statistics-getifacerxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getIfaceTxBytes](arkts-network-statistics-getifacetxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getIfaceTxBytes](arkts-network-statistics-getifacetxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getSelfTrafficStats](arkts-network-statistics-getselftrafficstats-f.md) | Obtains the traffic statistics of the specified application on the specified network within the specified period. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; - Currently, only cellular and Wi-Fi traffic usage can be obtained. &gt; - Currently, only traffic usage within the last 31 days can be obtained. If the timestamp passed in the parameter &gt; is earlier than 31 days before the current system time, error code 2103019 will be returned. &gt; &gt; - This API may take some time to execute. Do not call it frequently. |
| [getSockfdRxBytes](arkts-network-statistics-getsockfdrxbytes-f.md) | Obtains the downlink traffic (in bytes) of the specified socket. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed. |
| [getSockfdRxBytes](arkts-network-statistics-getsockfdrxbytes-f.md) | Obtains the downlink traffic (in bytes) of the specified socket. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed. |
| [getSockfdTxBytes](arkts-network-statistics-getsockfdtxbytes-f.md) | Obtains the uplink traffic of the specified socket (in bytes). This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed. |
| [getSockfdTxBytes](arkts-network-statistics-getsockfdtxbytes-f.md) | Obtains the uplink traffic (in bytes) of the specified socket. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed. |
| [getUidRxBytes](arkts-network-statistics-getuidrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; If the application has not generated any traffic consumption after the restart, error code 2103005 will be &gt; thrown. |
| [getUidRxBytes](arkts-network-statistics-getuidrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; If the application has not generated any traffic consumption after the restart, error code 2103005 will be &gt; thrown. |
| [getUidTxBytes](arkts-network-statistics-getuidtxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; If the application has not generated any traffic consumption after the restart, error code 2103005 will be &gt; thrown. |
| [getUidTxBytes](arkts-network-statistics-getuidtxbytes-f.md) | Obtains the total uplink traffic of the specified application from the last startup to the time when this API is called (in bytes). This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; If the application has not generated any traffic consumption after the restart, error code 2103005 will be &gt; thrown. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getMonthTrafficStats](arkts-network-statistics-getmonthtrafficstats-f-sys.md) | Get this month traffic data of the cellular network. |
| [getTrafficPlanInfo](arkts-network-statistics-gettrafficplaninfo-f-sys.md) | Get traffic plan info. |
| [getTrafficStatsByIface](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | Obtains the historical data traffic of the specified NIC. This API uses an asynchronous callback to return the result. |
| [getTrafficStatsByIface](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | Obtains the historical data traffic of the specified NIC. This API uses a promise to return the result. \| Name \| Type \| Mandatory\| Description \| \| --------- \| ------------------------- \| ---- \| --------------------------------------------------- \| \| ifaceInfo \| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) \| Yes \| NIC information. For details, see [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md).\| |
| [getTrafficStatsByNetwork](arkts-network-statistics-gettrafficstatsbynetwork-f-sys.md) | Obtains the traffic statistics of all applications on the specified network within the specified period. This API uses a promise to return the result. |
| [getTrafficStatsByUid](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) | Obtains the historical data traffic of the specified application. This API uses an asynchronous callback to return the result. |
| [getTrafficStatsByUid](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) | Obtains the historical data traffic of the specified application. This API uses a promise to return the result. |
| [getTrafficStatsByUidNetwork](arkts-network-statistics-gettrafficstatsbyuidnetwork-f-sys.md) | Obtains the traffic statistics of the specified application on the specified network within the specified period. This method uses a promise to return the result. |
| [offNetStatsChange](arkts-network-statistics-offnetstatschange-f-sys.md) | Unregister notifications of network traffic updates. |
| [off_netStatsChange](arkts-network-statistics-offnetstatschange-f-sys.md) | Unsubscribes from traffic change events. This API uses an asynchronous callback to return the result. |
| [onNetStatsChange](arkts-network-statistics-onnetstatschange-f-sys.md) | Register notifications of network traffic updates. |
| [on_netStatsChange](arkts-network-statistics-onnetstatschange-f-sys.md) | Subscribes to traffic change events. This API uses an asynchronous callback to return the result. |
| [setCalibrationTraffic](arkts-network-statistics-setcalibrationtraffic-f-sys.md) | Sets traffic calibration data. You can use this API to set traffic data during traffic calibration. This API uses a promise to return the result. |
| [setTrafficPlanInfo](arkts-network-statistics-settrafficplaninfo-f-sys.md) | Set traffic plan info. |
| [updateIfacesStats](arkts-network-statistics-updateifacesstats-f-sys.md) | Updates network interface statistics data. |
| [updateStatsData](arkts-network-statistics-updatestatsdata-f-sys.md) | Updates network statistics data. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | Defines the parameters for querying historical traffic of an NIC. |
| [NetStatsChangeInfo](arkts-network-statistics-netstatschangeinfo-i-sys.md) | Defines the NIC status and usage of an application. |
| [NetStatsInfo](arkts-network-statistics-netstatsinfo-i-sys.md) | Defines the historical traffic information. |
| [NetStatsInfoSequenceItem](arkts-network-statistics-netstatsinfosequenceitem-i-sys.md) | Parameters for an [NetStatsInfo](arkts-network-statistics-netstatsinfo-i-sys.md) with start time and end time. |
| [NetworkInfo](arkts-network-statistics-networkinfo-i-sys.md) | Defines the network information. |
| [UidInfo](arkts-network-statistics-uidinfo-i-sys.md) | Defines the parameters for querying historical traffic of an application. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [TrafficPlanParam](arkts-network-statistics-trafficplanparam-e-sys.md) | Defines the fields related to the traffic plan. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [NetBearType](arkts-network-statistics-netbeartype-t.md) | Defines the network type. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [NetStatsInfoSequence](arkts-network-statistics-netstatsinfosequence-t-sys.md) | Array of [NetStatsInfoSequenceItem](arkts-network-statistics-netstatsinfosequenceitem-i-sys.md). |
| [UidNetStatsInfo](arkts-network-statistics-uidnetstatsinfo-t-sys.md) | [NetStatsInfo](arkts-network-statistics-netstatsinfo-i-sys.md) for every UID. Key is UID. |
<!--DelEnd-->

