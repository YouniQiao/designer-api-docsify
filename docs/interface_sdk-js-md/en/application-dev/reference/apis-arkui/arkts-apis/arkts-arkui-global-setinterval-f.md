# setInterval

## Modules to Import

```TypeScript
```

## setInterval

```TypeScript
export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number
```

Sets a repeating timer for the system to repeatedly call a function at a fixed interval. The timer can only be manually deleted when the **clearInterval** API is called.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number--><!--Device-unnamed-export declare function setInterval(handler: Function | string, delay: number, ...arguments: any[]): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | Function &#124; string | Yes | When the type is function, this parameter specifies the callback function to be invoked upon the timer's expiration. <br>When the type is string, error information is printed with no additional processing. |
| delay | number | Yes | Number of milliseconds delayed before the execution. It is recommended that an integer be passed in; a decimal will be rounded down.<br>If this parameter is omitted, the default value of **0** is used.<br>**NOTE:** <br>1. This timer is not a precise timer, and there may be a discrepancy between the actual delay and the expected delay.<br>2. If the value is less than 1, it will be defaulted to **0**.<br>3. The value is subject to system limitations. If it exceeds 2^31 �C 1, the value will be **0**. |
| arguments | any[] | Yes | Additional parameters that are passed to **handler** only when **handler** is of the function type.<br>If the number of arguments is less than that of the **handler** function parameters, the parameters that are not overwritten by arguments are set to **undefined**.<br>If the number of arguments exceeds that of the **handler** function parameters, the excess arguments will be ignored. However, they can still be accessed via the built-in arguments object within the **handler** function. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the timer. The timer ID is shared by processes and is an integer starting from 0 in ascending order. |
