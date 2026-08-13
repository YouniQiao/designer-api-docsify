# @ohos.telephony.observer

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace observer--><!--Device-unnamed-declare namespace observer-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md#offCCallStateChange) |
| [offCallStateChange](arkts-telephony-observer-offcallstatechange-f.md#offCallStateChange) |
| [offCallStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offCallStateChangeEx) |
| [offCellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offCellularDataConnectionStateChange) |
| [offCellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offCellularDataFlowChange) |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md#offCommunicationStateChange) |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md#offGetSimActiveState) |
| [offIccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#offIccAccountInfoChange) |
| [offNetworkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offNetworkStateChange) |
| [offSignalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offSignalInfoChange) |
| [offSimStateChange](arkts-telephony-observer-offsimstatechange-f.md#offSimStateChange) |
| off_callStateChange |
| [off_callStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md) |
| [off_cellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md) |
| [off_cellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md) |
| [off_iccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md) |
| [off_networkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md) |
| [off_signalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md) |
| [off_simStateChange](arkts-telephony-observer-offsimstatechange-f.md) |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md#onCCallStateChange) |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#onCallStateChange) |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#onCallStateChange) |
| [onCallStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#onCallStateChangeEx) |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#onCellularDataConnectionStateChange) |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#onCellularDataConnectionStateChange) |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#onCellularDataFlowChange) |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#onCellularDataFlowChange) |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md#onCommunicationStateChange) |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md#onGetSimActiveState) |
| [onIccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#onIccAccountInfoChange) |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onNetworkStateChange) |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onNetworkStateChange) |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onSignalInfoChange) |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onSignalInfoChange) |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onSimStateChange) |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onSimStateChange) |
| on_callStateChange |
| on_callStateChange |
| [on_callStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md) |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [on_iccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md) |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md) |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md) |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offCellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offCellInfoChange-(System-API)) |
| [off_cellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md) |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#onCellInfoChange-(System-API)) |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#onCellInfoChange-(System-API)) |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md) |
| [CallStateInfo](arkts-telephony-observer-callstateinfo-i.md) |
| [DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md) |
| [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) |
| [SimStateData](arkts-telephony-observer-simstatedata-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LockReason](arkts-telephony-observer-lockreason-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CCallState](arkts-telephony-observer-ccallstate-t.md) |
| [CallState](arkts-telephony-observer-callstate-t.md) |
| [CardType](arkts-telephony-observer-cardtype-t.md) |
| [DataConnectState](arkts-telephony-observer-dataconnectstate-t.md) |
| [DataFlowType](arkts-telephony-observer-dataflowtype-t.md) |
| [NetworkState](arkts-telephony-observer-networkstate-t.md) |
| [RatType](arkts-telephony-observer-rattype-t.md) |
| [SignalInformation](arkts-telephony-observer-signalinformation-t.md) |
| [SimState](arkts-telephony-observer-simstate-t.md) |
| [TelCallState](arkts-telephony-observer-telcallstate-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md) |
| [NetworkSearchRealTimeResult](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) |
<!--DelEnd-->
