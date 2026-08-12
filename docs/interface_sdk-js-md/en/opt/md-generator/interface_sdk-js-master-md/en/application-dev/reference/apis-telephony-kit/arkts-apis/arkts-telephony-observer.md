# @ohos.telephony.observer

Monitors telephony state updates of a device, including updates of the network state,signal strength, call state, the data link connection state and others.

**Since:** 6

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
| [off](arkts-telephony-observer-off-f.md#off) |
| [off](arkts-telephony-observer-off-f.md#off-1) |
| [off](arkts-telephony-observer-off-f.md#off-3) |
| [off](arkts-telephony-observer-off-f.md#off-4) |
| [off](arkts-telephony-observer-off-f.md#off-5) |
| [off](arkts-telephony-observer-off-f.md#off-6) |
| [off](arkts-telephony-observer-off-f.md#off-7) |
| [off](arkts-telephony-observer-off-f.md#off-8) |
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md#offccallstatechange) |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md#offcommunicationstatechange) |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md#offgetsimactivestate) |
| [on](arkts-telephony-observer-on-f.md#on) |
| [on](arkts-telephony-observer-on-f.md#on-1) |
| [on](arkts-telephony-observer-on-f.md#on-2) |
| [on](arkts-telephony-observer-on-f.md#on-3) |
| [on](arkts-telephony-observer-on-f.md#on-6) |
| [on](arkts-telephony-observer-on-f.md#on-7) |
| [on](arkts-telephony-observer-on-f.md#on-8) |
| [on](arkts-telephony-observer-on-f.md#on-9) |
| [on](arkts-telephony-observer-on-f.md#on-10) |
| [on](arkts-telephony-observer-on-f.md#on-11) |
| [on](arkts-telephony-observer-on-f.md#on-12) |
| [on](arkts-telephony-observer-on-f.md#on-13) |
| [on](arkts-telephony-observer-on-f.md#on-14) |
| [on](arkts-telephony-observer-on-f.md#on-15) |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md#onccallstatechange) |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md#oncommunicationstatechange) |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md#ongetsimactivestate) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off](arkts-telephony-observer-off-f-sys.md#off-2) |
| [on](arkts-telephony-observer-on-f-sys.md#on-4) |
| [on](arkts-telephony-observer-on-f-sys.md#on-5) |
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
