# setTimeout

## setTimeout

```TypeScript
export declare function setTimeout(handler: Function | string, delay?: number, ...arguments: any[]): number
```

Sets a timer after which a function will be executed.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-export declare function setTimeout(handler: Function | string, delay?: number, ...arguments: any[]): number--><!--Device-unnamed-export declare function setTimeout(handler: Function | string, delay?: number, ...arguments: any[]): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | Function \| string | Yes | Indicates the function to be called after the timer goes off. For devices of "tv", "phone, tablet", and "wearable" types, this parameter can be a function or string. For devices of "lite wearable" and "smartVision" types, this parameter must be a function. |
| delay | number | No | Indicates the delay (in milliseconds) after which the function will be called. If this parameter is left empty, default value "0" will be used, which means that the function will be called immediately or as soon as possible. |
| arguments | any[] | Yes | Indicates additional arguments to pass to "handler" when the timer goes off. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the timer ID. |

