# callbackWrapper

## callbackWrapper

```TypeScript
function callbackWrapper(original: Function): Function
```

Takes an async function (or a function that returns a Promise) and returns a function following the error-first callback style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-util-function callbackWrapper(original: Function): Function--><!--Device-util-function callbackWrapper(original: Function): Function-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| original | Function | Yes | Asynchronous function |

**Return value:**

| Type | Description |
| --- | --- |
| Function | Return a Asynchronous function |

