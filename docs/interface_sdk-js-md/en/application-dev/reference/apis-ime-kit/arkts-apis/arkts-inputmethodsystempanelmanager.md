# @ohos.inputMethodSystemPanelManager

Input method system panel manager.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace inputMethodSystemPanelManager--><!--Device-unnamed-declare namespace inputMethodSystemPanelManager-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [connectSystemChannel](arkts-ime-inputmethodsystempanelmanager-connectsystemchannel-f-sys.md) | Connect system channel for the panel and input method. |
| [offSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-offsystempanelstatuschange-f-sys.md) | Unsubscribe from the system panel status change event. |
| [offSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-offsystemprivatecommand-f-sys.md) | Unsubscribe from the event when the input method application sends private data commands. |
| [onSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-onsystempanelstatuschange-f-sys.md) | Subscribe to the system panel status change event. |
| [onSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-onsystemprivatecommand-f-sys.md) | Subscribe to the event when the input method application sends private data commands. |
| [sendPrivateCommand](arkts-ime-inputmethodsystempanelmanager-sendprivatecommand-f-sys.md) | Send private command. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [SystemPanelStatus](arkts-ime-inputmethodsystempanelmanager-systempanelstatus-i-sys.md) | System panel status. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [InputMethodInputType](arkts-ime-inputmethodsystempanelmanager-inputmethodinputtype-e-sys.md) | Defines the input type. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [CommandDataType](arkts-ime-inputmethodsystempanelmanager-commanddatatype-t-sys.md) | Indicates the possible data types of the command. |
<!--DelEnd-->

