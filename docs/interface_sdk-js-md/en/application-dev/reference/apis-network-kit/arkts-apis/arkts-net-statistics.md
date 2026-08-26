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
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllRxBytes(Traffic Management)](arkts-network-statistics-getallrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getAllRxBytes(Traffic Management)](arkts-network-statistics-getallrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getAllTxBytes(Traffic Management)](arkts-network-statistics-getalltxbytes-f.md) | Obtains the total uplink traffic of all NICs (in bytes) from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getAllTxBytes(Traffic Management)](arkts-network-statistics-getalltxbytes-f.md) | Obtains the total uplink traffic (in bytes) of all NICs from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getCellularRxBytes(Traffic Management)](arkts-network-statistics-getcellularrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getCellularRxBytes(Traffic Management)](arkts-network-statistics-getcellularrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getCellularTxBytes(Traffic Management)](arkts-network-statistics-getcellulartxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getCellularTxBytes(Traffic Management)](arkts-network-statistics-getcellulartxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getIfaceRxBytes(Traffic Management)](arkts-network-statistics-getifacerxbytes-f.md) | Obtains the total downlink traffic of the specified NIC from the last startup to the time when this API is called (in bytes). This API uses an asynchronous callback to return the result. |
| [getIfaceRxBytes(Traffic Management)](arkts-network-statistics-getifacerxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getIfaceTxBytes(Traffic Management)](arkts-network-statistics-getifacetxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getIfaceTxBytes(Traffic Management)](arkts-network-statistics-getifacetxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getSelfTrafficStats(Traffic Management)](arkts-network-statistics-getselftrafficstats-f.md) | Obtains the traffic statistics of the specified application on the specified network within the specified period. This API uses a promise to return the result. |
| [getSockfdRxBytes(Traffic Management)](arkts-network-statistics-getsockfdrxbytes-f.md) | Obtains the downlink traffic (in bytes) of the specified socket. This API uses an asynchronous callback to return the result. |
| [getSockfdRxBytes(Traffic Management)](arkts-network-statistics-getsockfdrxbytes-f.md) | Obtains the downlink traffic (in bytes) of the specified socket. This API uses a promise to return the result. |
| [getSockfdTxBytes(Traffic Management)](arkts-network-statistics-getsockfdtxbytes-f.md) | Obtains the uplink traffic of the specified socket (in bytes). This API uses an asynchronous callback to return the result. |
| [getSockfdTxBytes(Traffic Management)](arkts-network-statistics-getsockfdtxbytes-f.md) | Obtains the uplink traffic (in bytes) of the specified socket. This API uses a promise to return the result. |
| [getUidRxBytes(Traffic Management)](arkts-network-statistics-getuidrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getUidRxBytes(Traffic Management)](arkts-network-statistics-getuidrxbytes-f.md) | Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses a promise to return the result. |
| [getUidTxBytes(Traffic Management)](arkts-network-statistics-getuidtxbytes-f.md) | Obtains the total uplink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. |
| [getUidTxBytes(Traffic Management)](arkts-network-statistics-getuidtxbytes-f.md) | Obtains the total uplink traffic of the specified application from the last startup to the time when this API is called (in bytes). This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getMonthTrafficStats(Traffic Management)](arkts-network-statistics-getmonthtrafficstats-f-sys.md) | Get this month traffic data of the cellular network. |
| [getTrafficPlanInfo(Traffic Management)](arkts-network-statistics-gettrafficplaninfo-f-sys.md) | Get traffic plan info. |
| [getTrafficStatsByIface(Traffic Management)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | Obtains the historical data traffic of the specified NIC. This API uses an asynchronous callback to return the result. |
| [getTrafficStatsByIface(Traffic Management)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | Obtains the historical data traffic of the specified NIC. This API uses a promise to return the result.  \| Name \| Type \| Mandatory\| Description \| \| --------- \| ------------------------- \| ---- \| --------------------------------------------------- \| \| ifaceInfo \| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) \| Yes \| NIC information. For details, see [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md).\| |
| [getTrafficStatsByNetwork(Traffic Management)](arkts-network-statistics-gettrafficstatsbynetwork-f-sys.md) | Obtains the traffic statistics of all applications on the specified network within the specified period. This API uses a promise to return the result. |
| [getTrafficStatsByUid(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) | Obtains the historical data traffic of the specified application. This API uses an asynchronous callback to return the result. |
| [getTrafficStatsByUid(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) | Obtains the historical data traffic of the specified application. This API uses a promise to return the result. |
| [getTrafficStatsByUidNetwork(Traffic Management)](arkts-network-statistics-gettrafficstatsbyuidnetwork-f-sys.md) | Obtains the traffic statistics of the specified application on the specified network within the specified period. This method uses a promise to return the result. |
| off(Traffic Management) | Unsubscribes from traffic change events. This API uses an asynchronous callback to return the result. |
| on(Traffic Management) | Subscribes to traffic change events. This API uses an asynchronous callback to return the result. |
| [setCalibrationTraffic(Traffic Management)](arkts-network-statistics-setcalibrationtraffic-f-sys.md) | Sets traffic calibration data. You can use this API to set traffic data during traffic calibration. This API uses a promise to return the result. |
| [setTrafficPlanInfo(Traffic Management)](arkts-network-statistics-settrafficplaninfo-f-sys.md) | Set traffic plan info. |
| [updateIfacesStats(Traffic Management)](arkts-network-statistics-updateifacesstats-f-sys.md) | Updates network interface statistics data. |
| [updateStatsData(Traffic Management)](arkts-network-statistics-updatestatsdata-f-sys.md) | Updates network statistics data. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [NetStatsInfo(Traffic Management)](arkts-network-statistics-netstatsinfo-i.md) | Defines the historical traffic information. |
| [NetworkInfo(Traffic Management)](arkts-network-statistics-networkinfo-i.md) | Defines the network information. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [IfaceInfo(Traffic Management)](arkts-network-statistics-ifaceinfo-i-sys.md) | Defines the parameters for querying historical traffic of an NIC. |
| [NetStatsChangeInfo(Traffic Management)](arkts-network-statistics-netstatschangeinfo-i-sys.md) | Defines the NIC status and usage of an application. |
| [UidInfo(Traffic Management)](arkts-network-statistics-uidinfo-i-sys.md) | Defines the parameters for querying historical traffic of an application. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [TrafficPlanParam(Traffic Management)](arkts-network-statistics-trafficplanparam-e-sys.md) | Defines the fields related to the traffic plan. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [NetBearType(Traffic Management)](arkts-network-statistics-netbeartype-t.md) | Defines the network type. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [UidNetStatsInfo(Traffic Management)](arkts-network-statistics-uidnetstatsinfo-t-sys.md) |  |
<!--DelEnd-->
