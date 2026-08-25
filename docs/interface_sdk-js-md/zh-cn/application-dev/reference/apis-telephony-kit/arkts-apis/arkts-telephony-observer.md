# @ohos.telephony.observer(电话服务状态监听)

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
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
| [offCCallStateChange(电话服务状态监听)](arkts-telephony-observer-offccallstatechange-f.md) |
| [offCommunicationStateChange(电话服务状态监听)](arkts-telephony-observer-offcommunicationstatechange-f.md) |
| [offGetSimActiveState(电话服务状态监听)](arkts-telephony-observer-offgetsimactivestate-f.md) |
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
| [onCCallStateChange(电话服务状态监听)](arkts-telephony-observer-onccallstatechange-f.md) |
| [onCommunicationStateChange(电话服务状态监听)](arkts-telephony-observer-oncommunicationstatechange-f.md) |
| [onGetSimActiveState(电话服务状态监听)](arkts-telephony-observer-ongetsimactivestate-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| off(电话服务状态监听) |
| on(电话服务状态监听) |
| on(电话服务状态监听) |
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
