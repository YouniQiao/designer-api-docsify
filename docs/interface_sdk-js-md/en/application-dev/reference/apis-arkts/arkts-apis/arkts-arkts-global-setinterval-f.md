# setInterval

## setInterval

```TypeScript
function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int
```

按照delayMs间隔重复调用回调函数。首次调用将在delayMs之后执行。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int--><!--Device-unnamed-function setInterval(func: Function, delayMs: int | null | undefined, ...args: FixedArray<Any>): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | 要执行的回调函数。 |
| delayMs | int \| null \| undefined | Yes | 超时时间，单位为毫秒（ms）， 如果传入null或undefined，将视为0毫秒。 |
| args | FixedArray&lt;Any&gt; | Yes | 传递给func的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回定时器ID。 |

