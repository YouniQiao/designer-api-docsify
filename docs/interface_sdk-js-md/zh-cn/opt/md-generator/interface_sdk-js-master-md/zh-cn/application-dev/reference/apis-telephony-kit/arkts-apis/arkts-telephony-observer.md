# @ohos.telephony.observer

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

**起始版本：** 23

<!--Device-unnamed-declare namespace observer--><!--Device-unnamed-declare namespace observer-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [offCCallStateChange](arkts-telephony-observer-offccallstatechange-f.md#offccallstatechange) |
| [offCallStateChange](arkts-telephony-observer-offcallstatechange-f.md#offcallstatechange) |
| [offCallStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offcallstatechangeex) |
| [offCellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offcellulardataconnectionstatechange) |
| [offCellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offcellulardataflowchange) |
| [offCommunicationStateChange](arkts-telephony-observer-offcommunicationstatechange-f.md#offcommunicationstatechange) |
| [offGetSimActiveState](arkts-telephony-observer-offgetsimactivestate-f.md#offgetsimactivestate) |
| [offIccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#officcaccountinfochange) |
| [offNetworkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offnetworkstatechange) |
| [offSignalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offsignalinfochange) |
| [offSimStateChange](arkts-telephony-observer-offsimstatechange-f.md#offsimstatechange) |
| [off_callStateChange](arkts-telephony-observer-offcallstatechange-f.md#offcallstatechange) |
| [off_callStateChangeEx](arkts-telephony-observer-offcallstatechangeex-f.md#offcallstatechangeex) |
| [off_cellularDataConnectionStateChange](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md#offcellulardataconnectionstatechange) |
| [off_cellularDataFlowChange](arkts-telephony-observer-offcellulardataflowchange-f.md#offcellulardataflowchange) |
| [off_iccAccountInfoChange](arkts-telephony-observer-officcaccountinfochange-f.md#officcaccountinfochange) |
| [off_networkStateChange](arkts-telephony-observer-offnetworkstatechange-f.md#offnetworkstatechange) |
| [off_signalInfoChange](arkts-telephony-observer-offsignalinfochange-f.md#offsignalinfochange) |
| [off_simStateChange](arkts-telephony-observer-offsimstatechange-f.md#offsimstatechange) |
| [onCCallStateChange](arkts-telephony-observer-onccallstatechange-f.md#onccallstatechange) |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) |
| [onCallStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) |
| [onCallStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#oncallstatechangeex) |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) |
| [onCellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) |
| [onCellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) |
| [onCommunicationStateChange](arkts-telephony-observer-oncommunicationstatechange-f.md#oncommunicationstatechange) |
| [onGetSimActiveState](arkts-telephony-observer-ongetsimactivestate-f.md#ongetsimactivestate) |
| [onIccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#oniccaccountinfochange) |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) |
| [onNetworkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) |
| [onSignalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) |
| [onSimStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) |
| [on_callStateChange](arkts-telephony-observer-oncallstatechange-f.md#oncallstatechange) |
| [on_callStateChangeEx](arkts-telephony-observer-oncallstatechangeex-f.md#oncallstatechangeex) |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) |
| [on_cellularDataConnectionStateChange](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md#oncellulardataconnectionstatechange) |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) |
| [on_cellularDataFlowChange](arkts-telephony-observer-oncellulardataflowchange-f.md#oncellulardataflowchange) |
| [on_iccAccountInfoChange](arkts-telephony-observer-oniccaccountinfochange-f.md#oniccaccountinfochange) |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) |
| [on_networkStateChange](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) |
| [on_signalInfoChange](arkts-telephony-observer-onsignalinfochange-f.md#onsignalinfochange) |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) |
| [on_simStateChange](arkts-telephony-observer-onsimstatechange-f.md#onsimstatechange) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [offCellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offcellinfochange) |
| [off_cellInfoChange](arkts-telephony-observer-offcellinfochange-f-sys.md#offcellinfochange) |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange) |
| [onCellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange系统接口) |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange) |
| [on_cellInfoChange](arkts-telephony-observer-oncellinfochange-f-sys.md#oncellinfochange系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md) |
| [CallStateInfo](arkts-telephony-observer-callstateinfo-i.md) |
| [DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md) |
| [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) |
| [SimStateData](arkts-telephony-observer-simstatedata-i.md) |

### 枚举

| 名称 |
| --- |
| [LockReason](arkts-telephony-observer-lockreason-e.md) |

### 类型

| 名称 |
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
### 类型（系统接口）

| 名称 |
| --- |
| [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md) |
| [NetworkSearchRealTimeResult](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) |
<!--DelEnd-->
