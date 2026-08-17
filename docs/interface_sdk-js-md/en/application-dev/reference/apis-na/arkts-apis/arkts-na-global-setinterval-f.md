# setInterval

## setInterval

```TypeScript
function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

Repeatedly call the function with delayMs interval between calls. The first call will be after delayMs.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int--><!--Device-unnamed-function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | The function to be executed. |
| delayMs | int \| null \| undefined | Yes | Timeout in milliseconds (ms), if pass null or undefined will be treated as 0 milliseconds. |
| args | FixedArray&lt;Any&gt; | Yes | Parameters passed to func. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the timer ID. |

