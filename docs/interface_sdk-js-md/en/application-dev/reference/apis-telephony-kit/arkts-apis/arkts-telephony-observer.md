# @ohos.telephony.observer

Monitors telephony state updates of a device, including updates of the network state,signal strength, call state, the data link connection state and others.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace observer--><!--Device-unnamed-declare namespace observer-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off](arkts-telephony-observer-off-f.md#off) | Cancel callback when the network state is updated. |
| [off](arkts-telephony-observer-off-f.md#off-1) | Cancel callback when the signal strength is updated. |
| [off](arkts-telephony-observer-off-f.md#off-3) | Cancel callback when the cellular data link connection state is updated. |
| [off](arkts-telephony-observer-off-f.md#off-4) | Cancel callback when the uplink and downlink data flow state of cellular data services is updated. |
| [off](arkts-telephony-observer-off-f.md#off-5) | Cancel callback when the call state is updated. |
| [off](arkts-telephony-observer-off-f.md#off-6) | Cancel callback when the telCall state is updated. |
| [off](arkts-telephony-observer-off-f.md#off-7) | Cancel callback when the sim state is updated. |
| [off](arkts-telephony-observer-off-f.md#off-8) | Cancel to receive an ICC account change. |
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md#offccallstatechange) | Unsubscribes from the callback for listening to the carrier call state. |
| [offCallStateChange](arkts-telephony-observer-offcallstatechange-f.md#offcallstatechange) | Cancel callback when the call state is updated. |
| [offCallStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offcallstatechangeex) | Cancel callback when the telCall state is updated. |
| [offCellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offcellulardataconnectionstatechange) | Cancel callback when the cellular data link connection state is updated. |
| [offCellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offcellulardataflowchange) | Cancel callback when the uplink and downlink data flow state of cellular data services is updated. |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md#offcommunicationstatechange) | Unsubscribes from the callback for listening to the 5A state. |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md#offgetsimactivestate) | Cancel callback when the sim active state is updated. |
| [offIccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#officcaccountinfochange) | Cancel to receive an ICC account change. |
| [offNetworkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offnetworkstatechange) | Cancel callback when the network state is updated. |
| [offSignalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offsignalinfochange) | Cancel callback when the signal strength is updated. |
| [offSimStateChange](arkts-telephony-observer-offsimstatechange-f.md#offsimstatechange) | Cancel callback when the sim state is updated. |
| [on](arkts-telephony-observer-on-f.md#on) | Callback when the network state corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-1) | Callback when the network state corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-2) | Callback when the signal strength corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-3) | Callback when the signal strength corresponding to a monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-6) | Callback when the cellular data link connection state corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-7) | Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-8) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-9) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-10) | Callback when the call state corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-11) | Callback when the call state corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-12) | Callback when the telCall state corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-13) | Callback when the sim state corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f.md#on-14) | Callback when the sim state corresponding to the monitored {@code slotId} is updated. |
| [on](arkts-telephony-observer-on-f.md#on-15) | Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates. |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md#onccallstatechange) | Called when the carrier call state changes. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) | Callback when the call state corresponding to the default sim card is updated. |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange-1) | Callback when the call state corresponding to the monitored {@code slotId} is updated. |
| [onCallStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#oncallstatechangeex) | Callback when the telCall state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) | Callback when the cellular data link connection state corresponding to the default sim card is updated. |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange-1) | Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the default sim card is updated. |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange-1) | Callback when the uplink and downlink data flow state of cellular data services corresponding to the monitored {@code slotId} is updated. |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md#oncommunicationstatechange) | This API uses an asynchronous callback to return the result. |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md#ongetsimactivestate) | Subscribe to sim active state change events using a callback-based approach as an asynchronous method. |
| [onIccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#oniccaccountinfochange) | Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) | Callback when the network state corresponding to the default sim card is updated. |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange-1) | Callback when the network state corresponding to the monitored {@code slotId} is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) | Callback when the signal strength corresponding to the default sim card is updated. |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange-1) | Callback when the signal strength corresponding to a monitored {@code slotId} is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) | Callback when the sim state corresponding to the default sim card is updated. |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange-1) | Callback when the sim state corresponding to the monitored {@code slotId} is updated. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [off](arkts-telephony-observer-off-f-sys.md#off-2) | Cancel callback when the cell information is updated. |
| [offCellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offcellinfochange) | Cancel callback when the cell information is updated. |
| [on](arkts-telephony-observer-on-f-sys.md#on-4) | Callback when the cell information corresponding to the default sim card is updated. |
| [on](arkts-telephony-observer-on-f-sys.md#on-5) | Callback when the cell information corresponding to a monitored {@code slotId} is updated. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange) | Callback when the cell information corresponding to the default sim card is updated. |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange-1) | Callback when the cell information corresponding to a monitored {@code slotId} is updated. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md) | Indicates carrier call state and number. |
| [CallStateInfo](arkts-telephony-observer-callstateinfo-i.md) | Indicates call state and number. |
| [DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md) | Indicates cellular data connect state and technology type. |
| [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Indicates observer options. |
| [SimStateData](arkts-telephony-observer-simstatedata-i.md) | Indicates SIM card type and status. |

### Enums

| Name | Description |
| --- | --- |
| [LockReason](arkts-telephony-observer-lockreason-e.md) | Enum for SIM card lock type. |

### Types

| Name | Description |
| --- | --- |
| [CCallState](arkts-telephony-observer-ccallstate-t.md) | Indicates the states of carrier call. |
| [CallState](arkts-telephony-observer-callstate-t.md) | Indicates the states of call. |
| [CardType](arkts-telephony-observer-cardtype-t.md) | Indicates the SIM card types. |
| [DataConnectState](arkts-telephony-observer-dataconnectstate-t.md) | Describes the cellular data link connection state. |
| [DataFlowType](arkts-telephony-observer-dataflowtype-t.md) | Describes the cellular data flow type. |
| [NetworkState](arkts-telephony-observer-networkstate-t.md) | Describes the network registration state. |
| [RatType](arkts-telephony-observer-rattype-t.md) | Describes the radio access technology. |
| [SignalInformation](arkts-telephony-observer-signalinformation-t.md) | Describes the signal strength information. |
| [SimState](arkts-telephony-observer-simstate-t.md) | Indicates the SIM card states. |
| [TelCallState](arkts-telephony-observer-telcallstate-t.md) | Indicates the states of tel call. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md) | Describes current cell information. |
| [NetworkSearchRealTimeResult](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) | Indicates the result of network search. |
<!--DelEnd-->

