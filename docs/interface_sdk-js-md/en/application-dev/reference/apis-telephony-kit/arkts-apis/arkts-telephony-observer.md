# @ohos.telephony.observer

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

**Since:** 23

<!--Device-unnamed-declare namespace observer--><!--Device-unnamed-declare namespace observer-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md) | Cancels the listening on the carrier call status and obtaining of the call number by a third-party application. This method uses an asynchronous callback to return the result. |
| [offCallStateChange](arkts-telephony-observer-offcallstatechange-f.md) | Cancel callback when the call state is updated. |
| [offCallStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md) | Cancel callback when the telCall state is updated. |
| [offCellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md) | Cancel callback when the cellular data link connection state is updated. |
| [offCellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md) | Cancel callback when the uplink and downlink data flow state of cellular data services is updated. |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md) | Unsubscribes from the callback for listening to the 5A state. |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md) | Unregisters an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result. |
| [offIccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md) | Cancel to receive an ICC account change. |
| [offNetworkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md) | Cancel callback when the network state is updated. |
| [offSignalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md) | Cancel callback when the signal strength is updated. |
| [offSimStateChange](arkts-telephony-observer-offsimstatechange-f.md) | Cancel callback when the sim state is updated. |
| [off_callStateChange](arkts-telephony-observer-offcallstatechange-f.md) | Unregisters the observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [off_callStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md) | Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return the execution result. |
| [off_cellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md) | Unregisters the observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. |
| [off_cellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md) | Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. |
| [off_iccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md) | Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. |
| [off_networkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md) | Unregisters the observer for network status change events. This API uses an asynchronous callback to return the execution result. |
| [off_signalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md) | Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the execution result. |
| [off_simStateChange](arkts-telephony-observer-offsimstatechange-f.md) | Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the result. |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md) | Subscribes to the carrier call state changes and obtains the call number. This method uses an asynchronous callback to return the execution result. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md) | Callback when the call state corresponding to the default sim card is updated. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md) | Callback when the call state corresponding to the monitored {@code slotId} is updated. |
| [onCallStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md) | Callback when the telCall state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) | Callback when the cellular data link connection state corresponding to the default sim card is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) | Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the default sim card is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the monitored {@code slotId} is updated. |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md) | This API uses an asynchronous callback to return the result. |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md) | Registers an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result. |
| [onIccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md) | Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) | Callback when the network state corresponding to the default sim card is updated. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) | Callback when the network state corresponding to the monitored {@code slotId} is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) | Callback when the signal strength corresponding to the default sim card is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) | Callback when the signal strength corresponding to a monitored {@code slotId} is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md) | Callback when the sim state corresponding to the default sim card is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md) | Callback when the sim state corresponding to the monitored {@code slotId} is updated. |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_callStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md) | Registers an observer for extended call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) | Registers an observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) | Registers an observer for connection status change events of the cellular data link over the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service on the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on_iccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md) | Registers an observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) | Registers an observer for network status change events. This API uses an asynchronous callback to return the execution result. |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) | Registers an observer for network status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) | Registers an observer for signal status change events. This API uses an asynchronous callback to return the execution result. |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md) | Registers an observer for SIM card status change events. This API uses an asynchronous callback to return the result. |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md) | Registers an observer for status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [offCellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md) | Cancel callback when the cell information is updated. |
| [off_cellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md) | Unregisters the observer for cell information change events. This API uses an asynchronous callback to return the result. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) | Callback when the cell information corresponding to the default sim card is updated. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) | Callback when the cell information corresponding to a monitored {@code slotId} is updated. |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) | Registers an observer for cell information change events. This API uses an asynchronous callback to return the result. |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md) | Defines information about the call status. |
| [CallStateInfo](arkts-telephony-observer-callstateinfo-i.md) | Defines information about the call status. |
| [DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md) | Defines information about the data connection status. |
| [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Defines event subscription parameters. |
| [SimStateData](arkts-telephony-observer-simstatedata-i.md) | Enumerates SIM card types and states. |

### Enums

| Name | Description |
| --- | --- |
| [LockReason](arkts-telephony-observer-lockreason-e.md) | Enumerates SIM card lock types. |

### Types

| Name | Description |
| --- | --- |
| [CCallState](arkts-telephony-observer-ccallstate-t.md) | Enumerates carrier call states. |
| [CallState](arkts-telephony-observer-callstate-t.md) | Enumerates call states. |
| [CardType](arkts-telephony-observer-cardtype-t.md) | Enumerates SIM card types. |
| [DataConnectState](arkts-telephony-observer-dataconnectstate-t.md) | Describes the connection status of a cellular data link. |
| [DataFlowType](arkts-telephony-observer-dataflowtype-t.md) | Defines the cellular data flow type. |
| [NetworkState](arkts-telephony-observer-networkstate-t.md) | Defines the network status. |
| [RatType](arkts-telephony-observer-rattype-t.md) | Enumerates the radio access technologies. |
| [SignalInformation](arkts-telephony-observer-signalinformation-t.md) | Defines the signal strength. |
| [SimState](arkts-telephony-observer-simstate-t.md) | SIM card state. |
| [TelCallState](arkts-telephony-observer-telcallstate-t.md) | Enumerates call states. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md) | Describes current cell information. |
| [NetworkSearchRealTimeResult](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) | Indicates the result of network search. |
<!--DelEnd-->

