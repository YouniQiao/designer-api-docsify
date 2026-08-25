# @ohos.telephony.observer(Telephony Status Observer)

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offnetworkstatechange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offsignalinfochange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcellulardataconnectionstatechange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcellulardataflowchange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcallstatechange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offcallstatechangeex) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#offsimstatechange) |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f.md#officcaccountinfochange) |
| [offCallStateChange(Telephony Status Observer)](arkts-telephony-observer-offcallstatechange-f.md) |
| [offCallStateChangeEx(Telephony Status Observer)](arkts-telephony-observer-offcallstatechangeex-f.md) |
| [offCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-offccallstatechange-f.md) |
| [offCellularDataConnectionStateChange(Telephony Status Observer)](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md) |
| [offCellularDataFlowChange(Telephony Status Observer)](arkts-telephony-observer-offcellulardataflowchange-f.md) |
| [offCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-offcommunicationstatechange-f.md) |
| [offGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-offgetsimactivestate-f.md) |
| [offIccAccountInfoChange(Telephony Status Observer)](arkts-telephony-observer-officcaccountinfochange-f.md) |
| [offNetworkStateChange(Telephony Status Observer)](arkts-telephony-observer-offnetworkstatechange-f.md) |
| [offSignalInfoChange(Telephony Status Observer)](arkts-telephony-observer-offsignalinfochange-f.md) |
| [offSimStateChange(Telephony Status Observer)](arkts-telephony-observer-offsimstatechange-f.md) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onnetworkstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onnetworkstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsignalinfochange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsignalinfochange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oncallstatechangeex) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsimstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#onsimstatechange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f.md#oniccaccountinfochange) |
| [onCallStateChange(Telephony Status Observer)](arkts-telephony-observer-oncallstatechange-f.md) |
| [onCallStateChange(Telephony Status Observer)](arkts-telephony-observer-oncallstatechange-f.md) |
| [onCallStateChangeEx(Telephony Status Observer)](arkts-telephony-observer-oncallstatechangeex-f.md) |
| [onCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-onccallstatechange-f.md) |
| [onCellularDataConnectionStateChange(Telephony Status Observer)](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [onCellularDataConnectionStateChange(Telephony Status Observer)](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [onCellularDataFlowChange(Telephony Status Observer)](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [onCellularDataFlowChange(Telephony Status Observer)](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [onCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-oncommunicationstatechange-f.md) |
| [onGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-ongetsimactivestate-f.md) |
| [onIccAccountInfoChange(Telephony Status Observer)](arkts-telephony-observer-oniccaccountinfochange-f.md) |
| [onNetworkStateChange(Telephony Status Observer)](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [onNetworkStateChange(Telephony Status Observer)](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [onSignalInfoChange(Telephony Status Observer)](arkts-telephony-observer-onsignalinfochange-f.md) |
| [onSignalInfoChange(Telephony Status Observer)](arkts-telephony-observer-onsignalinfochange-f.md) |
| [onSimStateChange(Telephony Status Observer)](arkts-telephony-observer-onsimstatechange-f.md) |
| [onSimStateChange(Telephony Status Observer)](arkts-telephony-observer-onsimstatechange-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off(Telephony Status Observer)](arkts-telephony-observer-off-f-sys.md#offcellinfochange) |
| [offCellInfoChange(Telephony Status Observer)](arkts-telephony-observer-offcellinfochange-f-sys.md) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f-sys.md#oncellinfochange) |
| [on(Telephony Status Observer)](arkts-telephony-observer-on-f-sys.md#oncellinfochange) |
| [onCellInfoChange(Telephony Status Observer)](arkts-telephony-observer-oncellinfochange-f-sys.md) |
| [onCellInfoChange(Telephony Status Observer)](arkts-telephony-observer-oncellinfochange-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallStateInfo(Telephony Status Observer)](arkts-telephony-observer-callstateinfo-i.md) |
| [CCallStateInfo(Telephony Status Observer)](arkts-telephony-observer-ccallstateinfo-i.md) |
| [DataConnectionStateInfo(Telephony Status Observer)](arkts-telephony-observer-dataconnectionstateinfo-i.md) |
| [ObserverOptions(Telephony Status Observer)](arkts-telephony-observer-observeroptions-i.md) |
| [SimStateData(Telephony Status Observer)](arkts-telephony-observer-simstatedata-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LockReason(Telephony Status Observer)](arkts-telephony-observer-lockreason-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallState(Telephony Status Observer)](arkts-telephony-observer-callstate-t.md) |
| [CardType(Telephony Status Observer)](arkts-telephony-observer-cardtype-t.md) |
| [CCallState(Telephony Status Observer)](arkts-telephony-observer-ccallstate-t.md) |
| [DataConnectState(Telephony Status Observer)](arkts-telephony-observer-dataconnectstate-t.md) |
| [DataFlowType(Telephony Status Observer)](arkts-telephony-observer-dataflowtype-t.md) |
| [NetworkState(Telephony Status Observer)](arkts-telephony-observer-networkstate-t.md) |
| [RatType(Telephony Status Observer)](arkts-telephony-observer-rattype-t.md) |
| [SignalInformation(Telephony Status Observer)](arkts-telephony-observer-signalinformation-t.md) |
| [SimState(Telephony Status Observer)](arkts-telephony-observer-simstate-t.md) |
| [TelCallState(Telephony Status Observer)](arkts-telephony-observer-telcallstate-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CellInformation(Telephony Status Observer)](arkts-telephony-observer-cellinformation-t-sys.md) |
| [NetworkSearchRealTimeResult(Telephony Status Observer)](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) |
<!--DelEnd-->
