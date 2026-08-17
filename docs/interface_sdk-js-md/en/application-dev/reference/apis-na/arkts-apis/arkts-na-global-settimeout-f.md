# setTimeout

## setTimeout

```TypeScript
function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

Execute function with parameters after the timer expires.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int--><!--Device-unnamed-function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | The function to be executed after the timer expires. |
| delayMs | int \| null \| undefined | Yes | Timeout in milliseconds (ms), if pass null or undefined will be treated as 0 milliseconds. |
| args | FixedArray&lt;Any&gt; | Yes | Parameters passed to func. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Timer id. |

