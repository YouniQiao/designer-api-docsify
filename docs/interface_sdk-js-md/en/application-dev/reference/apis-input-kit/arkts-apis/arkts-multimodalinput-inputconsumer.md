# @ohos.multimodalInput.inputConsumer

The **inputConsumer** module implements listening for combination key events as well as listening and interception for volume key events. > **NOTE：**> > - Global shortcut keys are combination keys defined by the system or application. System shortcut keys are defined > by the system, and application shortcut keys are defined by applications.

**Since:** 23

<!--Device-unnamed-declare namespace inputConsumer--><!--Device-unnamed-declare namespace inputConsumer-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
import { inputConsumer } from 'inputConsumer';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllSystemHotkeys](arkts-input-inputconsumer-getallsystemhotkeys-f.md#getallsystemhotkeys) | Obtains all system shortcut keys. This API uses a promise to return the result. |
| [offHotkeyChange](arkts-input-inputconsumer-offhotkeychange-f.md#offhotkeychange) | Unsubscribe from hotkey event. |
| [offKeyPressed](arkts-input-inputconsumer-offkeypressed-f.md#offkeypressed) | Cancels consumption of key events. |
| [off_hotkeyChange](arkts-input-inputconsumer-offhotkeychange-f.md#offhotkeychange) | Unsubscribes from application shortcut key change events. This API uses an asynchronous callback to return the result. |
| [off_keyPressed](arkts-input-inputconsumer-offkeypressed-f.md#offkeypressed) | Unsubscribes from key press events. This API uses an asynchronous callback to return the result. If the API call is successful, the system's default response to the key event will be resumed; that is, system-level actions, such as volume adjustment, will be triggered normally. |
| [onHotkeyChange](arkts-input-inputconsumer-onhotkeychange-f.md#onhotkeychange) | Listening for hotkey event. |
| [onKeyPressed](arkts-input-inputconsumer-onkeypressed-f.md#onkeypressed) | Subscribes to key press events. This API uses an asynchronous callback to return the result. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. |
| [on_hotkeyChange](arkts-input-inputconsumer-onhotkeychange-f.md#onhotkeychange) | Subscribes to application shortcut key change events. This API obtains combination key input events that meet the specified conditions, and uses an asynchronous callback to return the result. |
| [on_keyPressed](arkts-input-inputconsumer-onkeypressed-f.md#onkeypressed) | Subscribes to key press events. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. This API uses an asynchronous callback to return the result. If the API call is successful, the system's default response to the key event will be intercepted; that is, system- level actions, such as volume adjustment, will no longer be triggered. To restore the system response, call [off](arkts-input-inputconsumer-offkey-f-sys.md#offkey) to disable listening for the key event. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getShieldStatus](arkts-input-inputconsumer-getshieldstatus-f-sys.md#getshieldstatus) | Obtains the system hotkey shield status. |
| [offKey](arkts-input-inputconsumer-offkey-f-sys.md#offkey) | Subscribe system keys. |
| [offKey](arkts-input-inputconsumer-offkey-f-sys.md#offkey-system-api) | Unsubscribe system keys. |
| [off_key](arkts-input-inputconsumer-offkey-f-sys.md#offkey) | Disables listening for system hotkey change events. This API uses an asynchronous callback to return the result. |
| [onKey](arkts-input-inputconsumer-onkey-f-sys.md#onkey) | Subscribe system keys. |
| [onKey](arkts-input-inputconsumer-onkey-f-sys.md#onkey-system-api) | Subscribe system keys. |
| [on_key](arkts-input-inputconsumer-onkey-f-sys.md#onkey) | Enables listening for system hotkey change events. This API uses an asynchronous callback to return the system hotkey data when a system hotkey event that meets the specified condition occurs. > **NOTE：**> > - You can subscribe to only the Down event of a key, or subscribe to both the Down and Up events of a key. > > - If you subscribe to only the Up event of a key, the Down event may be consumed by the focus window, and the Up > event may not be closed. In this case, check whether the design and implementation are proper. |
| [setShieldStatus](arkts-input-inputconsumer-setshieldstatus-f-sys.md#setshieldstatus) | Sets the system hotkey shield status. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | Defines shortcut key options. |
| [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Sets the key event consumption configuration. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [KeyOptions](arkts-input-inputconsumer-keyoptions-i-sys.md) | Represents combination key options. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [KeyCommandTriggerType](arkts-input-inputconsumer-keycommandtriggertype-e-sys.md) | KeyCommandTriggerType |
| [ShieldMode](arkts-input-inputconsumer-shieldmode-e-sys.md) | Enumerates shortcut key shield modes. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [KeyCommandCallback](arkts-input-inputconsumer-keycommandcallback-t-sys.md) | Callback function when the shortcut key registered by the system application meets the conditions. |
<!--DelEnd-->

