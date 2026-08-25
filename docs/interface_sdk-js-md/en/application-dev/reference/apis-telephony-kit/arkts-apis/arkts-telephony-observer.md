# @ohos.telephony.observer(Telephony Status Observer)

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

**Since:** 6

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
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
| [offCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-offccallstatechange-f.md) |
| [offCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-offcommunicationstatechange-f.md) |
| [offGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-offgetsimactivestate-f.md) |
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
| [onCCallStateChange(Telephony Status Observer)](arkts-telephony-observer-onccallstatechange-f.md) |
| [onCommunicationStateChange(Telephony Status Observer)](arkts-telephony-observer-oncommunicationstatechange-f.md) |
| [onGetSimActiveState(Telephony Status Observer)](arkts-telephony-observer-ongetsimactivestate-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| off(Telephony Status Observer) |
| on(Telephony Status Observer) |
| on(Telephony Status Observer) |
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
