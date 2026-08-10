# @ohos.inputMethodSystemPanelManager

输入法系统面板管理器。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace inputMethodSystemPanelManager--><!--Device-unnamed-declare namespace inputMethodSystemPanelManager-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'kits/@kit.IMEKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [connectSystemChannel](arkts-ime-inputmethodsystempanelmanager-connectsystemchannel-f-sys.md#connectsystemchannel) | 连接面板和输入法之间的系统通道。 |
| [offSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-offsystempanelstatuschange-f-sys.md#offsystempanelstatuschange) | 取消订阅系统面板状态改变事件。 |
| [offSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-offsystemprivatecommand-f-sys.md#offsystemprivatecommand) | 取消订阅输入法应用发送私有数据命令的事件。 |
| [onSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-onsystempanelstatuschange-f-sys.md#onsystempanelstatuschange) | 订阅系统面板状态改变事件。 |
| [onSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-onsystemprivatecommand-f-sys.md#onsystemprivatecommand) | 订阅输入法应用发送私有数据命令的事件。 |
| [sendPrivateCommand](arkts-ime-inputmethodsystempanelmanager-sendprivatecommand-f-sys.md#sendprivatecommand) | 发送私有命令。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [SystemPanelStatus](arkts-ime-inputmethodsystempanelmanager-systempanelstatus-i-sys.md) | 系统面板状态。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [InputMethodInputType](arkts-ime-inputmethodsystempanelmanager-inputmethodinputtype-e-sys.md) | 定义输入类型。 |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [CommandDataType](arkts-ime-inputmethodsystempanelmanager-commanddatatype-t-sys.md) | 表示命令的数据类型。 |
<!--DelEnd-->

