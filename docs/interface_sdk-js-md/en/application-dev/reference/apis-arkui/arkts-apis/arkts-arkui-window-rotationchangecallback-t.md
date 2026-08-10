# RotationChangeCallback

```TypeScript
type RotationChangeCallback<T, U> = (info: T) => U
```

旋转事件通知通用回调函数。

开发者在使用时，回调函数参数类型为[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md)，返回值类型为  
[RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U--><!--Device-window-type RotationChangeCallback<T, U> = (info: T) => U-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | T | Yes | 回调函数调用时系统传入[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md)类型的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| U | 回调函数需要返回[RotationChangeResult]{ |

