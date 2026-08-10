# CallbackFunctionWithError

```TypeScript
type CallbackFunctionWithError = (e: Error) => void
```

注册带有错误码的回调函数类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-type CallbackFunctionWithError = (e: Error) => void--><!--Device-taskpool-type CallbackFunctionWithError = (e: Error) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | Error | Yes | 错误信息。 |

