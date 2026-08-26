# @ohos.telephony.data(Cellular Data)

The **data** module provides basic mobile data management functions. With the APIs provided by this module, you can obtain the default slot of the SIM card used for mobile data, obtain the cellular data flow type and connection status, and check whether cellular data and roaming are enabled.

**Since:** 7

**System capability:** SystemCapability.Telephony.CellularData

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getActiveApnName(Cellular Data)](arkts-telephony-data-getactiveapnname-f.md) | Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result asynchronously.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getCellularDataFlowType(Cellular Data)](arkts-telephony-data-getcellulardataflowtype-f.md) | Obtains the data flow type of the cellular network (corresponding to the uplink and downlink arrows next to the signal bar). This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getCellularDataFlowType(Cellular Data)](arkts-telephony-data-getcellulardataflowtype-f.md) | Obtains the data flow type of the cellular network (corresponding to the uplink and downlink arrows next to the signal bar). This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getCellularDataState(Cellular Data)](arkts-telephony-data-getcellulardatastate-f.md) | Obtains the cellular data connection status. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getCellularDataState(Cellular Data)](arkts-telephony-data-getcellulardatastate-f.md) | Obtains the cellular data connection status. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getDefaultCellularDataSimId(Cellular Data)](arkts-telephony-data-getdefaultcellulardatasimid-f.md) | Obtains the default ID of the SIM card used for mobile data. |
| [getDefaultCellularDataSlotId(Cellular Data)](arkts-telephony-data-getdefaultcellulardataslotid-f.md) | Obtains the default slot of the SIM card used for mobile data. This API uses an asynchronous callback to return the result. |
| [getDefaultCellularDataSlotId(Cellular Data)](arkts-telephony-data-getdefaultcellulardataslotid-f.md) | Obtains the default slot of the SIM card used for mobile data. This API uses a promise to return the result. |
| [getDefaultCellularDataSlotIdSync(Cellular Data)](arkts-telephony-data-getdefaultcellulardataslotidsync-f.md) | Obtains the default SIM card used for mobile data synchronously. |
| [isCellularDataEnabled(Cellular Data)](arkts-telephony-data-iscellulardataenabled-f.md) | Checks whether the cellular data service is enabled. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isCellularDataEnabled(Cellular Data)](arkts-telephony-data-iscellulardataenabled-f.md) | Checks whether the cellular data service is enabled. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isCellularDataEnabledSync(Cellular Data)](arkts-telephony-data-iscellulardataenabledsync-f.md) | Checks whether the cellular data service is enabled. This API returns the result synchronously.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isCellularDataRoamingEnabled(Cellular Data)](arkts-telephony-data-iscellulardataroamingenabled-f.md) | Checks whether roaming is enabled for the cellular data service. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isCellularDataRoamingEnabled(Cellular Data)](arkts-telephony-data-iscellulardataroamingenabled-f.md) | Checks whether roaming is enabled for the cellular data service. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isCellularDataRoamingEnabledSync(Cellular Data)](arkts-telephony-data-iscellulardataroamingenabledsync-f.md) | Checks whether roaming is enabled for the cellular data service. This API returns the result synchronously.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [queryAllApns(Cellular Data)](arkts-telephony-data-queryallapns-f.md) | Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result asynchronously. |
| [queryApnIds(Cellular Data)](arkts-telephony-data-queryapnids-f.md) | Obtains the APN ID corresponding to the specified **ApnInfo**. This API returns the result asynchronously. |
| [setPreferredApn(Cellular Data)](arkts-telephony-data-setpreferredapn-f.md) | Sets the APN corresponding to the specified **apnId** as the preferred APN. This API returns the result asynchronously. |
| [showSystemApnSettings(Cellular Data)](arkts-telephony-data-showsystemapnsettings-f.md) | Open the system APN selection menu, which is presented in a semi-modal form and can be used to select a specific APN. This API uses a promise to return the result. If there is no SIM card or the device does not support the APN menu, the menu cannot be displayed. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [disableCellularData(Cellular Data)](arkts-telephony-data-disablecellulardata-f-sys.md) | Disables the cellular data service. This API uses an asynchronous callback to return the result. |
| [disableCellularData(Cellular Data)](arkts-telephony-data-disablecellulardata-f-sys.md) | Disables the cellular data service. This API uses a promise to return the result. |
| [disableCellularDataRoaming(Cellular Data)](arkts-telephony-data-disablecellulardataroaming-f-sys.md) | Disables the cellular data roaming service. This API uses an asynchronous callback to return the result. |
| [disableCellularDataRoaming(Cellular Data)](arkts-telephony-data-disablecellulardataroaming-f-sys.md) | Disables the cellular data roaming service. This API uses a promise to return the result. |
| [enableCellularData(Cellular Data)](arkts-telephony-data-enablecellulardata-f-sys.md) | Enables the cellular data service. This API uses an asynchronous callback to return the result. |
| [enableCellularData(Cellular Data)](arkts-telephony-data-enablecellulardata-f-sys.md) | Enables the cellular data service. This API uses a promise to return the result. |
| [enableCellularDataRoaming(Cellular Data)](arkts-telephony-data-enablecellulardataroaming-f-sys.md) | Enables the cellular data roaming service. This API uses an asynchronous callback to return the result. |
| [enableCellularDataRoaming(Cellular Data)](arkts-telephony-data-enablecellulardataroaming-f-sys.md) | Enables the cellular data roaming service. This API uses a promise to return the result. |
| [setDefaultCellularDataSlotId(Cellular Data)](arkts-telephony-data-setdefaultcellulardataslotid-f-sys.md) | Sets the default slot of the SIM card used for mobile data. This API uses an asynchronous callback to return the result. |
| [setDefaultCellularDataSlotId(Cellular Data)](arkts-telephony-data-setdefaultcellulardataslotid-f-sys.md) | Sets the default slot of the SIM card used for mobile data. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ApnInfo(Cellular Data)](arkts-telephony-data-apninfo-i.md) | Defines the APN information. |

### Enums

| Name | Description |
| --- | --- |
| [DataConnectState(Cellular Data)](arkts-telephony-data-dataconnectstate-e.md) | Describes the connection status of a cellular data link. |
| [DataFlowType(Cellular Data)](arkts-telephony-data-dataflowtype-e.md) | Defines the cellular data flow type. |
