# global

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [canIUse](arkts-arkui-global-caniuse-f.md#caniuse-1) | Defining syscap function. |
| [clearInterval](arkts-arkui-global-clearinterval-f.md#clearinterval-1) | Cancels the repeated timer set via **setInterval()**. The timer object is stored in the thread where the timer is created and must be deleted in that thread. |
| [clearTimeout](arkts-arkui-global-cleartimeout-f.md#cleartimeout-1) | Cancels a timer set via **setTimeout()**. The timer object is stored in the thread where the timer is created and must be deleted in that thread. |
| [getInspectorByKey](arkts-arkui-global-getinspectorbykey-f.md#getinspectorbykey-1) | Obtains all attributes of the component with the specified ID, excluding the information about child components.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [getInspectorTree](arkts-arkui-global-getinspectortree-f.md#getinspectortree-1) | Obtains the component tree and component attributes.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [loadNativeModule](arkts-arkui-global-loadnativemodule-f.md#loadnativemodule-1) | The **loadNativeModule** API is used to synchronously and dynamically load a native module, that is, only load the required module at a time. Using this API increases the time for loading the .so file. You need to evaluate the impact on the functionality. |
| [sendEventByKey](arkts-arkui-global-sendeventbykey-f.md#sendeventbykey-1) | Sends an event to the component with the specified ID.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [sendKeyEvent](arkts-arkui-global-sendkeyevent-f.md#sendkeyevent-1) | Sends a key event.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [sendMouseEvent](arkts-arkui-global-sendmouseevent-f.md#sendmouseevent-1) | Sends a mouse event.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [sendTouchEvent](arkts-arkui-global-sendtouchevent-f.md#sendtouchevent-1) | Sends a touch event.<br>This API is intended for application testing purposes only. It is recommended that you call this API after application startup and layout completion. The API requires significant processing time. Avoid using it. |
| [setInterval](arkts-arkui-global-setinterval-f.md#setinterval-1) | Sets a repeating timer for the system to repeatedly call a function at a fixed interval. The timer can only be manually deleted when the **clearInterval** API is called. |
| [setTimeout](arkts-arkui-global-settimeout-f.md#settimeout-1) | Sets a timer for the system to call a function after the timer goes off. The timer is automatically deleted after callback execution, or you may manually delete it via the **clearTimeout()** API. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [markModuleCollectable](arkts-arkui-global-markmodulecollectable-f-sys.md#markmodulecollectable-1) | Mark moduleNamespace which loaded by dynamic-import is collectable. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [console](arkts-arkui-global-console-c.md) | Defines the console info. |
