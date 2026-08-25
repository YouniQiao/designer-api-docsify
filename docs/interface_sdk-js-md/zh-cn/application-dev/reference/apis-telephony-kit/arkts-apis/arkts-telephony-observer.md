# @ohos.telephony.observer(电话服务状态监听)

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offnetworkstatechange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offsignalinfochange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offcellulardataconnectionstatechange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offcellulardataflowchange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offcallstatechange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offcallstatechangeex) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#offsimstatechange) |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f.md#officcaccountinfochange) |
| [offCallStateChange(电话服务状态监听)](arkts-telephony-observer-offcallstatechange-f.md) |
| [offCallStateChangeEx(电话服务状态监听)](arkts-telephony-observer-offcallstatechangeex-f.md) |
| [offCCallStateChange(电话服务状态监听)](arkts-telephony-observer-offccallstatechange-f.md) |
| [offCellularDataConnectionStateChange(电话服务状态监听)](arkts-telephony-observer-offcellulardataconnectionstatechange-f.md) |
| [offCellularDataFlowChange(电话服务状态监听)](arkts-telephony-observer-offcellulardataflowchange-f.md) |
| [offCommunicationStateChange(电话服务状态监听)](arkts-telephony-observer-offcommunicationstatechange-f.md) |
| [offGetSimActiveState(电话服务状态监听)](arkts-telephony-observer-offgetsimactivestate-f.md) |
| [offIccAccountInfoChange(电话服务状态监听)](arkts-telephony-observer-officcaccountinfochange-f.md) |
| [offNetworkStateChange(电话服务状态监听)](arkts-telephony-observer-offnetworkstatechange-f.md) |
| [offSignalInfoChange(电话服务状态监听)](arkts-telephony-observer-offsignalinfochange-f.md) |
| [offSimStateChange(电话服务状态监听)](arkts-telephony-observer-offsimstatechange-f.md) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onnetworkstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onnetworkstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onsignalinfochange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onsignalinfochange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncellulardataconnectionstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncellulardataflowchange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncallstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncallstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oncallstatechangeex) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onsimstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#onsimstatechange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f.md#oniccaccountinfochange) |
| [onCallStateChange(电话服务状态监听)](arkts-telephony-observer-oncallstatechange-f.md) |
| [onCallStateChange(电话服务状态监听)](arkts-telephony-observer-oncallstatechange-f.md) |
| [onCallStateChangeEx(电话服务状态监听)](arkts-telephony-observer-oncallstatechangeex-f.md) |
| [onCCallStateChange(电话服务状态监听)](arkts-telephony-observer-onccallstatechange-f.md) |
| [onCellularDataConnectionStateChange(电话服务状态监听)](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [onCellularDataConnectionStateChange(电话服务状态监听)](arkts-telephony-observer-oncellulardataconnectionstatechange-f.md) |
| [onCellularDataFlowChange(电话服务状态监听)](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [onCellularDataFlowChange(电话服务状态监听)](arkts-telephony-observer-oncellulardataflowchange-f.md) |
| [onCommunicationStateChange(电话服务状态监听)](arkts-telephony-observer-oncommunicationstatechange-f.md) |
| [onGetSimActiveState(电话服务状态监听)](arkts-telephony-observer-ongetsimactivestate-f.md) |
| [onIccAccountInfoChange(电话服务状态监听)](arkts-telephony-observer-oniccaccountinfochange-f.md) |
| [onNetworkStateChange(电话服务状态监听)](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [onNetworkStateChange(电话服务状态监听)](arkts-telephony-observer-onnetworkstatechange-f.md) |
| [onSignalInfoChange(电话服务状态监听)](arkts-telephony-observer-onsignalinfochange-f.md) |
| [onSignalInfoChange(电话服务状态监听)](arkts-telephony-observer-onsignalinfochange-f.md) |
| [onSimStateChange(电话服务状态监听)](arkts-telephony-observer-onsimstatechange-f.md) |
| [onSimStateChange(电话服务状态监听)](arkts-telephony-observer-onsimstatechange-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [off(电话服务状态监听)](arkts-telephony-observer-off-f-sys.md#offcellinfochange) |
| [offCellInfoChange(电话服务状态监听)](arkts-telephony-observer-offcellinfochange-f-sys.md) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f-sys.md#oncellinfochange) |
| [on(电话服务状态监听)](arkts-telephony-observer-on-f-sys.md#oncellinfochange) |
| [onCellInfoChange(电话服务状态监听)](arkts-telephony-observer-oncellinfochange-f-sys.md) |
| [onCellInfoChange(电话服务状态监听)](arkts-telephony-observer-oncellinfochange-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CallStateInfo(电话服务状态监听)](arkts-telephony-observer-callstateinfo-i.md) |
| [CCallStateInfo(电话服务状态监听)](arkts-telephony-observer-ccallstateinfo-i.md) |
| [DataConnectionStateInfo(电话服务状态监听)](arkts-telephony-observer-dataconnectionstateinfo-i.md) |
| [ObserverOptions(电话服务状态监听)](arkts-telephony-observer-observeroptions-i.md) |
| [SimStateData(电话服务状态监听)](arkts-telephony-observer-simstatedata-i.md) |

### 枚举

| 名称 |
| --- |
| [LockReason(电话服务状态监听)](arkts-telephony-observer-lockreason-e.md) |

### 类型

| 名称 |
| --- |
| [CallState(电话服务状态监听)](arkts-telephony-observer-callstate-t.md) |
| [CardType(电话服务状态监听)](arkts-telephony-observer-cardtype-t.md) |
| [CCallState(电话服务状态监听)](arkts-telephony-observer-ccallstate-t.md) |
| [DataConnectState(电话服务状态监听)](arkts-telephony-observer-dataconnectstate-t.md) |
| [DataFlowType(电话服务状态监听)](arkts-telephony-observer-dataflowtype-t.md) |
| [NetworkState(电话服务状态监听)](arkts-telephony-observer-networkstate-t.md) |
| [RatType(电话服务状态监听)](arkts-telephony-observer-rattype-t.md) |
| [SignalInformation(电话服务状态监听)](arkts-telephony-observer-signalinformation-t.md) |
| [SimState(电话服务状态监听)](arkts-telephony-observer-simstate-t.md) |
| [TelCallState(电话服务状态监听)](arkts-telephony-observer-telcallstate-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [CellInformation(电话服务状态监听)](arkts-telephony-observer-cellinformation-t-sys.md) |
| [NetworkSearchRealTimeResult(电话服务状态监听)](arkts-telephony-observer-networksearchrealtimeresult-t-sys.md) |
<!--DelEnd-->
