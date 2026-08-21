# @ohos.inputMethodSystemPanelManager

@brief This module provides the input method system panel management functions, which are used for communication and state synchronization between the input method system panel and the system-default input method application.

> **NOTE：**
> 
> The APIs provided by this module are system APIs.
> 
> This module supports only the stage model.

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
| [connectSystemChannel](arkts-ime-inputmethodsystempanelmanager-connectsystemchannel-f-sys.md) | @brief Connects to the system channel for communication between the input method system panel and the system-default input method application. This API can be called only by the input method system panel. |
| [offSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-offsystempanelstatuschange-f-sys.md) | @brief Unsubscribes from system panel state change events. |
| [offSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-offsystemprivatecommand-f-sys.md) | @brief Unsubscribes from events that the system-default input method application sends a private data command. |
| [onSystemPanelStatusChange](arkts-ime-inputmethodsystempanelmanager-onsystempanelstatuschange-f-sys.md) | @brief Subscribes to system panel state change events. |
| [onSystemPrivateCommand](arkts-ime-inputmethodsystempanelmanager-onsystemprivatecommand-f-sys.md) | @brief Subscribe to the event when the input method application sends private data commands. |
| [sendPrivateCommand](arkts-ime-inputmethodsystempanelmanager-sendprivatecommand-f-sys.md) | @brief Sends a private command to the system-default input method application. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [SystemPanelStatus](arkts-ime-inputmethodsystempanelmanager-systempanelstatus-i-sys.md) | @brief System panel status. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [InputMethodInputType](arkts-ime-inputmethodsystempanelmanager-inputmethodinputtype-e-sys.md) | @brief Enumerates input types, which are used to identify the input modes supported by the system panel. Different input types correspond to different input scenarios and panel layouts. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [CommandDataType](arkts-ime-inputmethodsystempanelmanager-commanddatatype-t-sys.md) | @brief Describes the private data type, which varies depending on its function. |
<!--DelEnd-->

