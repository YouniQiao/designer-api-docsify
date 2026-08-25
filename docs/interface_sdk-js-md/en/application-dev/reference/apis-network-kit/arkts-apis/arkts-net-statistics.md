# @ohos.net.statistics(Traffic Management)

The Traffic Management module provides the capability to obtain device network traffic data. This module supports querying packet traffic usage from multiple dimensions, for example:  
- Obtaining the uplink/downlink traffic data of a specified NIC.  
- Obtaining the total traffic data of all NICs, facilitating the viewing of overall device network usage.  
- Obtaining the traffic data of a specified application based on the application UID, helping you monitor the network  
resource consumption of applications.  
- Obtaining traffic statistics for a specified socket, providing a data foundation for fine-grained network  
performance analysis.  
- Obtaining the historical traffic usage of an application within a specified time period, facilitating the analysis  
of number-term network usage trends of the application.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAllRxBytes(Traffic Management)](arkts-network-statistics-getallrxbytes-f.md) |
| [getAllRxBytes(Traffic Management)](arkts-network-statistics-getallrxbytes-f.md) |
| [getAllTxBytes(Traffic Management)](arkts-network-statistics-getalltxbytes-f.md) |
| [getAllTxBytes(Traffic Management)](arkts-network-statistics-getalltxbytes-f.md) |
| [getCellularRxBytes(Traffic Management)](arkts-network-statistics-getcellularrxbytes-f.md) |
| [getCellularRxBytes(Traffic Management)](arkts-network-statistics-getcellularrxbytes-f.md) |
| [getCellularTxBytes(Traffic Management)](arkts-network-statistics-getcellulartxbytes-f.md) |
| [getCellularTxBytes(Traffic Management)](arkts-network-statistics-getcellulartxbytes-f.md) |
| [getIfaceRxBytes(Traffic Management)](arkts-network-statistics-getifacerxbytes-f.md) |
| [getIfaceRxBytes(Traffic Management)](arkts-network-statistics-getifacerxbytes-f.md) |
| [getIfaceTxBytes(Traffic Management)](arkts-network-statistics-getifacetxbytes-f.md) |
| [getIfaceTxBytes(Traffic Management)](arkts-network-statistics-getifacetxbytes-f.md) |
| [getSelfTrafficStats(Traffic Management)](arkts-network-statistics-getselftrafficstats-f.md) |
| [getSockfdRxBytes(Traffic Management)](arkts-network-statistics-getsockfdrxbytes-f.md) |
| [getSockfdRxBytes(Traffic Management)](arkts-network-statistics-getsockfdrxbytes-f.md) |
| [getSockfdTxBytes(Traffic Management)](arkts-network-statistics-getsockfdtxbytes-f.md) |
| [getSockfdTxBytes(Traffic Management)](arkts-network-statistics-getsockfdtxbytes-f.md) |
| [getUidRxBytes(Traffic Management)](arkts-network-statistics-getuidrxbytes-f.md) |
| [getUidRxBytes(Traffic Management)](arkts-network-statistics-getuidrxbytes-f.md) |
| [getUidTxBytes(Traffic Management)](arkts-network-statistics-getuidtxbytes-f.md) |
| [getUidTxBytes(Traffic Management)](arkts-network-statistics-getuidtxbytes-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getMonthTrafficStats(Traffic Management)](arkts-network-statistics-getmonthtrafficstats-f-sys.md) |
| [getTrafficPlanInfo(Traffic Management)](arkts-network-statistics-gettrafficplaninfo-f-sys.md) |
| [getTrafficStatsByIface(Traffic Management)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) |
| [getTrafficStatsByIface(Traffic Management)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | Obtains the historical data traffic of the specified NIC. This API uses a promise to return the result.  \| Name \| Type \| Mandatory\| Description \| \| --------- \| ------------------------- \| ---- \| --------------------------------------------------- \| \| ifaceInfo \| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) \| Yes \| NIC information. For details, see [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md).\|
| [getTrafficStatsByNetwork(Traffic Management)](arkts-network-statistics-gettrafficstatsbynetwork-f-sys.md) |
| [getTrafficStatsByUid(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) |
| [getTrafficStatsByUid(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) |
| [getTrafficStatsByUidNetwork(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuidnetwork-f-sys.md) |
| off(Traffic Management) |
| on(Traffic Management) |
| [setCalibrationTraffic(Traffic Management)](arkts-network-statistics-setcalibrationtraffic-f-sys.md) |
| [setTrafficPlanInfo(Traffic Management)](arkts-network-statistics-settrafficplaninfo-f-sys.md) |
| [updateIfacesStats(Traffic Management)](arkts-network-statistics-updateifacesstats-f-sys.md) |
| [updateStatsData(Traffic Management)](arkts-network-statistics-updatestatsdata-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetStatsInfo(Traffic Management)](arkts-network-statistics-netstatsinfo-i.md) |
| [NetworkInfo(Traffic Management)](arkts-network-statistics-networkinfo-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IfaceInfo(Traffic Management)](arkts-network-statistics-ifaceinfo-i-sys.md) |
| [NetStatsChangeInfo(Traffic Management)](arkts-network-statistics-netstatschangeinfo-i-sys.md) |
| [UidInfo(Traffic Management)](arkts-network-statistics-uidinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TrafficPlanParam(Traffic Management)](arkts-network-statistics-trafficplanparam-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetBearType(Traffic Management)](arkts-network-statistics-netbeartype-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UidNetStatsInfo(Traffic Management)](arkts-network-statistics-uidnetstatsinfo-t-sys.md) |
<!--DelEnd-->
