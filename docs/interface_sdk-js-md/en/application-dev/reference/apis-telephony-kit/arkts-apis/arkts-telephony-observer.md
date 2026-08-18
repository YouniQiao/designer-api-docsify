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
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md#offccallstatechange) | Cancels the listening on the carrier call status and obtaining of the call number by a third-party application. This method uses an asynchronous callback to return the result. |
| [offCallStateChange](arkts-telephony-observer-offcallstatechange-f.md#offcallstatechange) | Cancel callback when the call state is updated. |
| [offCallStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offcallstatechangeex) | Cancel callback when the telCall state is updated. |
| [offCellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offcellulardataconnectionstatechange) | Cancel callback when the cellular data link connection state is updated. |
| [offCellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offcellulardataflowchange) | Cancel callback when the uplink and downlink data flow state of cellular data services is updated. |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md#offcommunicationstatechange) | Unsubscribes from the callback for listening to the 5A state. |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md#offgetsimactivestate) | Unregisters an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result. **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [offIccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#officcaccountinfochange) | Cancel to receive an ICC account change. |
| [offNetworkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offnetworkstatechange) | Cancel callback when the network state is updated. |
| [offSignalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offsignalinfochange) | Cancel callback when the signal strength is updated. |
| [offSimStateChange](arkts-telephony-observer-offsimstatechange-f.md#offsimstatechange) | Cancel callback when the sim state is updated. |
| [off_callStateChange](arkts-telephony-observer-offcallstatechange-f.md#offcallstatechange) | Unregisters the observer for call status change events. This API uses an asynchronous callback to return the execution result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_callStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offcallstatechangeex) | Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return the execution result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_cellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offcellulardataconnectionstatechange) | Unregisters the observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_cellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offcellulardataflowchange) | Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_iccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#officcaccountinfochange) | Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_networkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offnetworkstatechange) | Unregisters the observer for network status change events. This API uses an asynchronous callback to return the execution result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_signalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offsignalinfochange) | Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the execution result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [off_simStateChange](arkts-telephony-observer-offsimstatechange-f.md#offsimstatechange) | Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md#onccallstatechange) | Subscribes to the carrier call state changes and obtains the call number. This method uses an asynchronous callback to return the execution result. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) | Callback when the call state corresponding to the default sim card is updated. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) | Callback when the call state corresponding to the monitored {@code slotId} is updated. |
| [onCallStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#oncallstatechangeex) | Callback when the telCall state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) | Callback when the cellular data link connection state corresponding to the default sim card is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) | Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the default sim card is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the monitored {@code slotId} is updated. |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md#oncommunicationstatechange) | This API uses an asynchronous callback to return the result. |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md#ongetsimactivestate) | Registers an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result. **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [onIccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#oniccaccountinfochange) | Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) | Callback when the network state corresponding to the default sim card is updated. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) | Callback when the network state corresponding to the monitored {@code slotId} is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) | Callback when the signal strength corresponding to the default sim card is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) | Callback when the signal strength corresponding to a monitored {@code slotId} is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) | Callback when the sim state corresponding to the default sim card is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) | Callback when the sim state corresponding to the monitored {@code slotId} is updated. |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_callStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#oncallstatechangeex) | Registers an observer for extended call status change events. This API uses an asynchronous callback to return the execution result. |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) | Registers an observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) | Registers an observer for connection status change events of the cellular data link over the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service on the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on_iccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#oniccaccountinfochange) | Registers an observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) | Registers an observer for network status change events. This API uses an asynchronous callback to return the execution result. **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) | Registers an observer for network status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) | Registers an observer for signal status change events. This API uses an asynchronous callback to return the execution result. |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) | Registers an observer for SIM card status change events. This API uses an asynchronous callback to return the result. > **NOTE：**> > The return result of this API does not contain the activation status of the SIM card. For details, see > [sim.isSimActive](arkts-telephony-sim-issimactive-f.md#issimactive). |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) | Registers an observer for status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [offCellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offcellinfochange) | Cancel callback when the cell information is updated. |
| [off_cellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offcellinfochange) | Unregisters the observer for cell information change events. This API uses an asynchronous callback to return the result. > **NOTE：**> > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If > you do not pass the callback, you will cancel listening for all events. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange) | Callback when the cell information corresponding to the default sim card is updated. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange-system-api) | Callback when the cell information corresponding to a monitored {@code slotId} is updated. |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange) | Registers an observer for cell information change events. This API uses an asynchronous callback to return the result. |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange-system-api) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
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
### Types（系统接口）

| Name | Description |
| --- | --- |
| [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md) | Describes current cell information. |
| [NetworkSearchRealTimeResult](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) | Indicates the result of network search. |
<!--DelEnd-->

