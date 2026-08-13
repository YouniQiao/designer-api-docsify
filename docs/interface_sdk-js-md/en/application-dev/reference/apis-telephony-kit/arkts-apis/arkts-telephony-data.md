# @ohos.telephony.data

Provides methods related to cellular data services.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace data--><!--Device-unnamed-declare namespace data-End-->

**System capability:** SystemCapability.Telephony.CellularData

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getActiveApnName](arkts-telephony-data-getactiveapnname-f.md#getActiveApnName) | Get Active APN's Name. |
| [getCellularDataFlowType](arkts-telephony-data-getcellulardataflowtype-f.md#getCellularDataFlowType) | Indicates that there is no uplink or downlink data. &lt;p&gt;It is a return value of service state query of cellular data services. |
| [getCellularDataFlowType](arkts-telephony-data-getcellulardataflowtype-f.md#getCellularDataFlowType) | Indicates that there is no uplink or downlink data. &lt;p&gt;It is a return value of service state query of cellular data services. |
| [getCellularDataState](arkts-telephony-data-getcellulardatastate-f.md#getCellularDataState) | Obtain the connection state of the PS domain. |
| [getCellularDataState](arkts-telephony-data-getcellulardatastate-f.md#getCellularDataState) | Obtain the connection state of the PS domain. |
| [getDefaultCellularDataSimId](arkts-telephony-data-getdefaultcellulardatasimid-f.md#getDefaultCellularDataSimId) | Obtains the default cellular data SIM ID. |
| [getDefaultCellularDataSlotId](arkts-telephony-data-getdefaultcellulardataslotid-f.md#getDefaultCellularDataSlotId) | Get the default cellular data card. |
| [getDefaultCellularDataSlotId](arkts-telephony-data-getdefaultcellulardataslotid-f.md#getDefaultCellularDataSlotId) | Get the default cellular data card. |
| [getDefaultCellularDataSlotIdSync](arkts-telephony-data-getdefaultcellulardataslotidsync-f.md#getDefaultCellularDataSlotIdSync) | Get the default cellular data card. |
| [isCellularDataEnabled](arkts-telephony-data-iscellulardataenabled-f.md#isCellularDataEnabled) | Check whether cellular data services are enabled. |
| [isCellularDataEnabled](arkts-telephony-data-iscellulardataenabled-f.md#isCellularDataEnabled) | Check whether cellular data services are enabled. |
| [isCellularDataEnabledSync](arkts-telephony-data-iscellulardataenabledsync-f.md#isCellularDataEnabledSync) | Check whether cellular data services are enabled. |
| [isCellularDataRoamingEnabled](arkts-telephony-data-iscellulardataroamingenabled-f.md#isCellularDataRoamingEnabled) | Check whether roaming is enabled for cellular data services. |
| [isCellularDataRoamingEnabled](arkts-telephony-data-iscellulardataroamingenabled-f.md#isCellularDataRoamingEnabled) | Check whether roaming is enabled for cellular data services. |
| [isCellularDataRoamingEnabledSync](arkts-telephony-data-iscellulardataroamingenabledsync-f.md#isCellularDataRoamingEnabledSync) | Check whether roaming is enabled for cellular data services. |
| [queryAllApns](arkts-telephony-data-queryallapns-f.md#queryAllApns) | Query all APN info. |
| [queryApnIds](arkts-telephony-data-queryapnids-f.md#queryApnIds) | Query APN IDs. |
| [setPreferredApn](arkts-telephony-data-setpreferredapn-f.md#setPreferredApn) | Set preferred APN. |
| [showSystemApnSettings](arkts-telephony-data-showsystemapnsettings-f.md#showSystemApnSettings) | Open the system APN selection menu, which is presented in a semi-modal form and can be used to select a specific APN. This API uses a promise to return the result. If there is no SIM card or the device does not support the APN menu, the menu cannot be displayed. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableCellularData](arkts-telephony-data-disablecellulardata-f-sys.md#disableCellularData) | Disable cellular data services. |
| [disableCellularData](arkts-telephony-data-disablecellulardata-f-sys.md#disableCellularData-(System-API)) | Disable cellular data services. |
| [disableCellularDataRoaming](arkts-telephony-data-disablecellulardataroaming-f-sys.md#disableCellularDataRoaming) | Disable cellular data roaming. |
| [disableCellularDataRoaming](arkts-telephony-data-disablecellulardataroaming-f-sys.md#disableCellularDataRoaming-(System-API)) | Disable cellular data roaming. |
| [enableCellularData](arkts-telephony-data-enablecellulardata-f-sys.md#enableCellularData) | Enable cellular data services. |
| [enableCellularData](arkts-telephony-data-enablecellulardata-f-sys.md#enableCellularData-(System-API)) | Enable cellular data services. |
| [enableCellularDataRoaming](arkts-telephony-data-enablecellulardataroaming-f-sys.md#enableCellularDataRoaming) | Enable cellular data roaming. |
| [enableCellularDataRoaming](arkts-telephony-data-enablecellulardataroaming-f-sys.md#enableCellularDataRoaming-(System-API)) | Enable cellular data roaming. |
| [setDefaultCellularDataSlotId](arkts-telephony-data-setdefaultcellulardataslotid-f-sys.md#setDefaultCellularDataSlotId) | Switch cellular data services to another card, without changing the default settings. |
| [setDefaultCellularDataSlotId](arkts-telephony-data-setdefaultcellulardataslotid-f-sys.md#setDefaultCellularDataSlotId-(System-API)) | Switch cellular data services to another card, without changing the default settings. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ApnInfo](arkts-telephony-data-apninfo-i.md) | Defines the APN info. |

### Enums

| Name | Description |
| --- | --- |
| [DataConnectState](arkts-telephony-data-dataconnectstate-e.md) | Describes the cellular data link connection state. |
| [DataFlowType](arkts-telephony-data-dataflowtype-e.md) | Describes the cellular data flow type. |

