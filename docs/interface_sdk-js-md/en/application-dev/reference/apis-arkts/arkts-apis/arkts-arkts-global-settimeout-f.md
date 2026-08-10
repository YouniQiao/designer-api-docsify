# setTimeout

## setTimeout

```TypeScript
function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

在定时器超时后执行回调函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int--><!--Device-unnamed-function setTimeout(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | 定时器超时后要执行的回调函数。 |
| delayMs | int \| null \| undefined | Yes | 超时时间，单位为毫秒（ms）， 如果传入null或undefined，将视为0毫秒。 |
| args | FixedArray&lt;Any&gt; | Yes | 传递给func的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 定时器ID。 |

