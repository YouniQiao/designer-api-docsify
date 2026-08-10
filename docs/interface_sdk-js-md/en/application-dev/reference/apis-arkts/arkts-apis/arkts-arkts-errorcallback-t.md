# ErrorCallback

```TypeScript
type ErrorCallback = (err: ErrorEvent) => void
```

表示异常回调类型。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type ErrorCallback = (err: ErrorEvent) => void--><!--Device-unnamed-type ErrorCallback = (err: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes | 错误事件类， 表示Worker执行过程中出现的异常信息。 |

