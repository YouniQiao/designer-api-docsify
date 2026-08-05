# KeyCommandCallback (System API)

```TypeScript
type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void
```

Callback function when the shortcut key registered by the system application meets the conditions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputConsumer-type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void--><!--Device-inputConsumer-type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOptions | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options for registering shortcut keys when the system applies.  |
| keyEvent | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Key event when a shortcut key is triggered.  |

