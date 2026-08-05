# onSeniorModeStateChange

## onSeniorModeStateChange

```TypeScript
function onSeniorModeStateChange(callback: Callback<boolean>): void
```

Listens for enabling status changes of the senior mode. This API uses an asynchronous callback to return the result. > **NOTE** > > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > [accessibility.offSeniorModeStateChange]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function onSeniorModeStateChange(callback: Callback<boolean>): void--><!--Device-accessibility-function onSeniorModeStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | Yes | Callback function. The value **true** indicates that the senior mode is enabled, and the value **false** indicates that the senior mode is disabled. |

