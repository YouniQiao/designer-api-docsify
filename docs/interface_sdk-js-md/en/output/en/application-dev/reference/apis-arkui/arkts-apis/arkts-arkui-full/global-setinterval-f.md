# setInterval

## setInterval

```TypeScript
export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number
```

Sets the interval for repeatedly calling a function.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number--><!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | Function \| string | Yes | Indicates the function to be called after the timer goes off.For devices of "tv", "phone, tablet", and "wearable" types, this parameter can be a function or string.For devices of "lite wearable" and "smartVision" types, this parameter must be a function. |
| delay | number | Yes | Indicates the interval between each two calls, in milliseconds. The function will be called after this delay. |
| arguments | any[] | Yes | Indicates additional arguments to pass to "handler" when the timer goes off. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the timer ID. |

