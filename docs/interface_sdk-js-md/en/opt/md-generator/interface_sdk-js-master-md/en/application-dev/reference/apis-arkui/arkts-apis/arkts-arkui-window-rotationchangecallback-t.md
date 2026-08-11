# RotationChangeCallback

```TypeScript
type RotationChangeCallback<T, U> = (info: T) => U
```

Describes a generic callback function for rotation event notifications.

In this callback function, the parameter type is [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), and the return value type is [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U--><!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| U |
