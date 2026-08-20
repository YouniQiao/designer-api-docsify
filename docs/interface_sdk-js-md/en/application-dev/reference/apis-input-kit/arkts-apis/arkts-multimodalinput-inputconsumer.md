# @ohos.multimodalInput.inputConsumer

The **inputConsumer** module implements listening for combination key events as well as listening and interception for volume key events.

> **NOTE：**
> 
> - Global shortcut keys are combination keys defined by the system or application. System shortcut keys are defined &gt; by the system, and application shortcut keys are defined by applications.

**Since:** 23

<!--Device-unnamed-declare namespace inputConsumer--><!--Device-unnamed-declare namespace inputConsumer-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllSystemHotkeys](arkts-input-inputconsumer-getallsystemhotkeys-f.md) | Obtains all system shortcut keys. This API uses a promise to return the result. |
| [offHotkeyChange](arkts-input-inputconsumer-offhotkeychange-f.md) | Unsubscribe from hotkey event. |
| [offKeyPressed](arkts-input-inputconsumer-offkeypressed-f.md) | Cancels consumption of key events. |
| [off_hotkeyChange](arkts-input-inputconsumer-offhotkeychange-f.md) | Unsubscribes from application shortcut key change events. This API uses an asynchronous callback to return the result. |
| [off_keyPressed](arkts-input-inputconsumer-offkeypressed-f.md) | Unsubscribes from key press events. This API uses an asynchronous callback to return the result. If the API call is successful, the system's default response to the key event will be resumed; that is, system-level actions, such as volume adjustment, will be triggered normally. |
| [onHotkeyChange](arkts-input-inputconsumer-onhotkeychange-f.md) | Listening for hotkey event. |
| [onKeyPressed](arkts-input-inputconsumer-onkeypressed-f.md) | Subscribes to key press events. This API uses an asynchronous callback to return the result. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. |
| [on_hotkeyChange](arkts-input-inputconsumer-onhotkeychange-f.md) | Subscribes to application shortcut key change events. This API obtains combination key input events that meet the specified conditions, and uses an asynchronous callback to return the result. |
| [on_keyPressed](arkts-input-inputconsumer-onkeypressed-f.md) | Subscribes to key press events. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. This API uses an asynchronous callback to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getShieldStatus](arkts-input-inputconsumer-getshieldstatus-f-sys.md) | Obtains the system hotkey shield status. |
| [offKey](arkts-input-inputconsumer-offkey-f-sys.md) | Subscribe system keys. |
| [offKey](arkts-input-inputconsumer-offkey-f-sys.md) | Unsubscribe system keys. |
| [off_key](arkts-input-inputconsumer-offkey-f-sys.md) | Disables listening for system hotkey change events. This API uses an asynchronous callback to return the result. |
| [onKey](arkts-input-inputconsumer-onkey-f-sys.md) | Subscribe system keys. |
| [onKey](arkts-input-inputconsumer-onkey-f-sys.md) | Subscribe system keys. |
| [on_key](arkts-input-inputconsumer-onkey-f-sys.md) | Enables listening for system hotkey change events. This API uses an asynchronous callback to return the system hotkey data when a system hotkey event that meets the specified condition occurs. |
| [setShieldStatus](arkts-input-inputconsumer-setshieldstatus-f-sys.md) | Sets the system hotkey shield status. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | Defines shortcut key options. |
| [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Sets the key event consumption configuration. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [KeyOptions](arkts-input-inputconsumer-keyoptions-i-sys.md) | Represents combination key options. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [KeyCommandTriggerType](arkts-input-inputconsumer-keycommandtriggertype-e-sys.md) | KeyCommandTriggerType |
| [ShieldMode](arkts-input-inputconsumer-shieldmode-e-sys.md) | Enumerates shortcut key shield modes. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [KeyCommandCallback](arkts-input-inputconsumer-keycommandcallback-t-sys.md) | Callback function when the shortcut key registered by the system application meets the conditions. |
<!--DelEnd-->

