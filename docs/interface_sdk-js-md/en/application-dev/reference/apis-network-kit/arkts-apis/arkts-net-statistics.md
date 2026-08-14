# @ohos.net.statistics

Obtains traffic statistics.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace statistics--><!--Device-unnamed-declare namespace statistics-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { statistics } from 'statistics';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllRxBytes](arkts-network-statistics-getallrxbytes-f.md#getAllRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through all NICs. |
| [getAllRxBytes](arkts-network-statistics-getallrxbytes-f.md#getAllRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through all NICs. |
| [getAllTxBytes](arkts-network-statistics-getalltxbytes-f.md#getAllTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through all NICs. |
| [getAllTxBytes](arkts-network-statistics-getalltxbytes-f.md#getAllTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through all NICs. |
| [getCellularRxBytes](arkts-network-statistics-getcellularrxbytes-f.md#getCellularRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through the cellular network. |
| [getCellularRxBytes](arkts-network-statistics-getcellularrxbytes-f.md#getCellularRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through the cellular network. |
| [getCellularTxBytes](arkts-network-statistics-getcellulartxbytes-f.md#getCellularTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through the cellular network. |
| [getCellularTxBytes](arkts-network-statistics-getcellulartxbytes-f.md#getCellularTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through the cellular network. |
| [getIfaceRxBytes](arkts-network-statistics-getifacerxbytes-f.md#getIfaceRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through a specified NIC. |
| [getIfaceRxBytes](arkts-network-statistics-getifacerxbytes-f.md#getIfaceRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through a specified NIC. |
| [getIfaceTxBytes](arkts-network-statistics-getifacetxbytes-f.md#getIfaceTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through a specified NIC. |
| [getIfaceTxBytes](arkts-network-statistics-getifacetxbytes-f.md#getIfaceTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through a specified NIC. |
| [getSelfTrafficStats](arkts-network-statistics-getselftrafficstats-f.md#getSelfTrafficStats) | Get the traffic usage details of the specified network of the calling application in the specified time period and the specified networktype. |
| [getSockfdRxBytes](arkts-network-statistics-getsockfdrxbytes-f.md#getSockfdRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through a specified sockfd. |
| [getSockfdRxBytes](arkts-network-statistics-getsockfdrxbytes-f.md#getSockfdRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received through a specified sockfd. |
| [getSockfdTxBytes](arkts-network-statistics-getsockfdtxbytes-f.md#getSockfdTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through a specified sockfd. |
| [getSockfdTxBytes](arkts-network-statistics-getsockfdtxbytes-f.md#getSockfdTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent through a specified sockfd. |
| [getUidRxBytes](arkts-network-statistics-getuidrxbytes-f.md#getUidRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received by a specified application. |
| [getUidRxBytes](arkts-network-statistics-getuidrxbytes-f.md#getUidRxBytes) | Queries the data traffic (including all TCP and UDP data packets) received by a specified application. |
| [getUidTxBytes](arkts-network-statistics-getuidtxbytes-f.md#getUidTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent by a specified application. |
| [getUidTxBytes](arkts-network-statistics-getuidtxbytes-f.md#getUidTxBytes) | Queries the data traffic (including all TCP and UDP data packets) sent by a specified application. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getMonthTrafficStats](arkts-network-statistics-getmonthtrafficstats-f-sys.md#getMonthTrafficStats) | Get this month traffic data of the cellular network. |
| [getTrafficStatsByIface](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md#getTrafficStatsByIface) | Get the traffic usage details of the network interface in the specified time period. |
| [getTrafficStatsByIface](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md#getTrafficStatsByIface-(System-API)) | Get the traffic usage details of the network interface in the specified time period. |
| [getTrafficStatsByNetwork](arkts-network-statistics-gettrafficstatsbynetwork-f-sys.md#getTrafficStatsByNetwork) | Get the traffic usage details of the specified network of all applications in the specified time period. |
| [getTrafficStatsByUid](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md#getTrafficStatsByUid) | Get the traffic usage details of the specified time period of the application. |
| [getTrafficStatsByUid](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md#getTrafficStatsByUid-(System-API)) | Get the traffic usage details of the specified time period of the application. |
| [getTrafficStatsByUidNetwork](arkts-network-statistics-gettrafficstatsbyuidnetwork-f-sys.md#getTrafficStatsByUidNetwork) | Get the traffic usage sequence of the specified network of the application in the specified time period. |
| [offNetStatsChange](arkts-network-statistics-offnetstatschange-f-sys.md#offNetStatsChange) | Unregister notifications of network traffic updates. |
| off_netStatsChange | Unregister notifications of network traffic updates. |
| [onNetStatsChange](arkts-network-statistics-onnetstatschange-f-sys.md#onNetStatsChange) | Register notifications of network traffic updates. |
| on_netStatsChange | Register notifications of network traffic updates. |
| [setCalibrationTraffic](arkts-network-statistics-setcalibrationtraffic-f-sys.md#setCalibrationTraffic) | Set calibration traffic data. |
| [updateIfacesStats](arkts-network-statistics-updateifacesstats-f-sys.md#updateIfacesStats) | Updates network interface statistics data. |
| [updateStatsData](arkts-network-statistics-updatestatsdata-f-sys.md#updateStatsData) | Updates network statistics data. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md) | Detailed information of statistics. |
| [NetworkInfo](arkts-network-statistics-networkinfo-i.md) | Parameters for obtaining detailed information on specified network traffic usage. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | Parameters for obtaining detailed information on network interface traffic usage. |
| [NetStatsChangeInfo](arkts-network-statistics-netstatschangeinfo-i-sys.md) | Used to monitor and manage the status and usage of network interfaces. |
| [NetStatsInfoSequenceItem](arkts-network-statistics-netstatsinfosequenceitem-i-sys.md) | Parameters for an [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md#NetStatsInfo) with start time and end time. |
| [UidInfo](arkts-network-statistics-uidinfo-i-sys.md) | Parameters for obtaining detailed information on application traffic usage. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [NetBearType](arkts-network-statistics-netbeartype-t.md) |  |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [NetStatsInfoSequence](arkts-network-statistics-netstatsinfosequence-t-sys.md) | Array of [NetStatsInfoSequenceItem](arkts-network-statistics-netstatsinfosequenceitem-i-sys.md#NetStatsInfoSequenceItem-(System-API)). |
| [UidNetStatsInfo](arkts-network-statistics-uidnetstatsinfo-t-sys.md) | [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md#NetStatsInfo) for every UID. Key is UID. |
<!--DelEnd-->

