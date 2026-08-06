# KeyEventCallback

```TypeScript
export type KeyEventCallback = (event: KeyEvent) => boolean
```

The callback of 'keyDown' or 'keyUp' event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean--><!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the key event.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether to consume this key event.  |

