# UnhandledRejectionObserver

```TypeScript
export type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void
```

定义异常监听，用于捕获Promise异步操作失败的原因。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void--><!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | Error \| any | Yes | 通常是`Error`类型，表示被拒绝的理由。 |
| promise | Promise&lt;any&gt; | Yes | 被拒绝的promise。 |

