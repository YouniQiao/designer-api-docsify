# @ohos.multimodalInput.inputConsumer(Global Shortcut Keys)

The **inputConsumer** module implements listening for combination key events as well as listening and interception for volume key events.

> **NOTE：**
> 
> - Global shortcut keys are combination keys defined by the system or application. System shortcut keys are defined
> by the system, and application shortcut keys are defined by applications.

**Since:** 14

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllSystemHotkeys(Global Shortcut Keys)](arkts-input-inputconsumer-getallsystemhotkeys-f.md) | Obtains all system shortcut keys. This API uses a promise to return the result. |
| [off(Global Shortcut Keys)](arkts-input-inputconsumer-off-f.md#offhotkeychange) | Unsubscribes from application shortcut key change events. This API uses an asynchronous callback to return the result. |
| [off(Global Shortcut Keys)](arkts-input-inputconsumer-off-f.md#offkeypressed) | Unsubscribes from key press events. This API uses an asynchronous callback to return the result. If the API call is successful, the system's default response to the key event will be resumed; that is, system-level actions, such as volume adjustment, will be triggered normally. |
| [on(Global Shortcut Keys)](arkts-input-inputconsumer-on-f.md#onhotkeychange) | Subscribes to application shortcut key change events. This API obtains combination key input events that meet the specified conditions, and uses an asynchronous callback to return the result. |
| [on(Global Shortcut Keys)](arkts-input-inputconsumer-on-f.md#onkeypressed) | Subscribes to key press events. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed. This API uses an asynchronous callback to return the result.If the API call is successful, the system's default response to the key event will be intercepted; that is, system- level actions, such as volume adjustment, will no longer be triggered. To restore the system response, call off to disable listening for the key event. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getShieldStatus(Global Shortcut Keys)](arkts-input-inputconsumer-getshieldstatus-f-sys.md) | Obtains the system hotkey shield status. |
| off(Global Shortcut Keys) | Disables listening for system hotkey change events. This API uses an asynchronous callback to return the result. |
| [offKey(Global Shortcut Keys)](arkts-input-inputconsumer-offkey-f-sys.md) | Unsubscribe system keys. |
| on(Global Shortcut Keys) | Enables listening for system hotkey change events. This API uses an asynchronous callback to return the system hotkey data when a system hotkey event that meets the specified condition occurs. |
| [onKey(Global Shortcut Keys)](arkts-input-inputconsumer-onkey-f-sys.md) | Subscribe system keys. |
| [setShieldStatus(Global Shortcut Keys)](arkts-input-inputconsumer-setshieldstatus-f-sys.md) | Sets the system hotkey shield status. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [HotkeyOptions(Global Shortcut Keys)](arkts-input-inputconsumer-hotkeyoptions-i.md) | Defines shortcut key options. |
| [KeyPressedConfig(Global Shortcut Keys)](arkts-input-inputconsumer-keypressedconfig-i.md) | Sets the key event consumption configuration. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [KeyOptions(Global Shortcut Keys)](arkts-input-inputconsumer-keyoptions-i-sys.md) | Represents combination key options. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [KeyCommandTriggerType(Global Shortcut Keys)](arkts-input-inputconsumer-keycommandtriggertype-e-sys.md) | [KeyCommandTriggerType](arkts-input-inputconsumer-keycommandtriggertype-e-sys.md) |
| [ShieldMode(Global Shortcut Keys)](arkts-input-inputconsumer-shieldmode-e-sys.md) | Enumerates shortcut key shield modes. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [KeyCommandCallback(Global Shortcut Keys)](arkts-input-inputconsumer-keycommandcallback-t-sys.md) | Callback function when the shortcut key registered by the system application meets the conditions. |
<!--DelEnd-->
