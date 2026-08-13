# InputKeyEventCallback

```TypeScript
export type InputKeyEventCallback = (event: InputKeyEvent) => boolean
```

The callback of 'keyEvent' event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethodEngine-export type InputKeyEventCallback = (event: InputKeyEvent) => boolean--><!--Device-inputMethodEngine-export type InputKeyEventCallback = (event: InputKeyEvent) => boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | InputKeyEvent | Yes | the key event. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether to consume this key event. |

