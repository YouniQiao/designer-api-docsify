# RotationChangeCallback

```TypeScript
type RotationChangeCallback<T, U> = (info: T) => U
```

Describes a generic callback function for rotation event notifications.

In this callback function, the parameter type is [RotationChangeInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, and the return value type is [RotationChangeResult]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ \| void.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U--><!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | T | Yes | Parameter of type [RotationChangeInfo]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_ passed by the system when the callback function is called.  |

**Return value:**

| Type | Description |
| --- | --- |
| U | Value of type [RotationChangeResult]{ |

