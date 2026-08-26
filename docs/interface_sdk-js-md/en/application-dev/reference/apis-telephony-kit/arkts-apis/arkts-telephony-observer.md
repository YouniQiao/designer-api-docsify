# @ohos.telephony.observer(Telephony Status Observer)

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

**Since:** 6

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offnetworkstatechange) | Unregisters the observer for network status change events. This API uses an asynchronous callback to return the execution result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offsignalinfochange) | Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the execution result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcellulardataconnectionstatechange) | Unregisters the observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcellulardataflowchange) | Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcallstatechange) | Unregisters the observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcallstatechangeex) | Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return the execution result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offsimstatechange) | Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the result. |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#officcaccountinfochange) | Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. |
| [offCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-offccallstatechange-f.md) | Cancels the listening on the carrier call status and obtaining of the call number by a third-party application. This method uses an asynchronous callback to return the result. |
| [offCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-offcommunicationstatechange-f.md) | Unsubscribes from the callback for listening to the 5A state. |
| [offGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-offgetsimactivestate-f.md) | Unregisters an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onnetworkstatechange) | Registers an observer for network status change events. This API uses an asynchronous callback to return the execution result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onnetworkstatechange) | Registers an observer for network status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsignalinfochange) | Registers an observer for signal status change events. This API uses an asynchronous callback to return the execution result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsignalinfochange) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) | Registers an observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) | Registers an observer for connection status change events of the cellular data link over the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) | Registers an observer for the uplink and downlink data flow status change events of the cellular data service on the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechange) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechange) | Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechangeex) | Registers an observer for extended call status change events. This API uses an asynchronous callback to return the execution result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsimstatechange) | Registers an observer for SIM card status change events. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsimstatechange) | Registers an observer for status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oniccaccountinfochange) | Registers an observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result. |
| [onCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-onccallstatechange-f.md) | Subscribes to the carrier call state changes and obtains the call number. This method uses an asynchronous callback to return the execution result. |
| [onCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-oncommunicationstatechange-f.md) | This API uses an asynchronous callback to return the result. |
| [onGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-ongetsimactivestate-f.md) | Registers an observer for SIM card activation state changes. This API uses an asynchronous callback to return the execution result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| off(Telephony Status Observer) | Unregisters the observer for cell information change events. This API uses an asynchronous callback to return the result. |
| on(Telephony Status Observer) | Registers an observer for cell information change events. This API uses an asynchronous callback to return the result. |
| on(Telephony Status Observer) | Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CallStateInfo(Telephony Status Observer)](arkts-telephony-observer-callstateinfo-i.md) | Defines information about the call status. |
| [CCallStateInfo(Telephony Status Observer)](arkts-telephony-observer-ccallstateinfo-i.md) | Defines information about the call status. |
| [DataConnectionStateInfo(Telephony Status Observer)](arkts-telephony-observer-dataconnectionstateinfo-i.md) | Defines information about the data connection status. |
| [ObserverOptions(Telephony Status Observer)](arkts-telephony-observer-observeroptions-i.md) | Defines event subscription parameters. |
| [SimStateData(Telephony Status Observer)](arkts-telephony-observer-simstatedata-i.md) | Enumerates SIM card types and states. |

### Enums

| Name | Description |
| --- | --- |
| [LockReason(Telephony Status Observer)](arkts-telephony-observer-lockreason-e.md) | Enumerates SIM card lock types. |

### Types

| Name | Description |
| --- | --- |
| [CallState(Telephony Status Observer)](arkts-telephony-observer-callstate-t.md) | Enumerates call states. |
| [CardType(Telephony Status Observer)](arkts-telephony-observer-cardtype-t.md) | Enumerates SIM card types. |
| [CCallState(Telephony Status Observer)](arkts-telephony-observer-ccallstate-t.md) | Enumerates carrier call states. |
| [DataConnectState(Telephony Status Observer)](arkts-telephony-observer-dataconnectstate-t.md) | Describes the connection status of a cellular data link. |
| [DataFlowType(Telephony Status Observer)](arkts-telephony-observer-dataflowtype-t.md) | Defines the cellular data flow type. |
| [NetworkState(Telephony Status Observer)](arkts-telephony-observer-networkstate-t.md) | Defines the network status. |
| [RatType(Telephony Status Observer)](arkts-telephony-observer-rattype-t.md) | Enumerates the radio access technologies. |
| [SignalInformation(Telephony Status Observer)](arkts-telephony-observer-signalinformation-t.md) | Defines the signal strength. |
| [SimState(Telephony Status Observer)](arkts-telephony-observer-simstate-t.md) | SIM card state. |
| [TelCallState(Telephony Status Observer)](arkts-telephony-observer-telcallstate-t.md) | Enumerates call states. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [CellInformation(Telephony Status Observer)](arkts-telephony-observer-cellinformation-t-sys.md) | Describes current cell information. |
| [NetworkSearchRealTimeResult(Telephony Status Observer)](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) | Indicates the result of network search. |
<!--DelEnd-->
