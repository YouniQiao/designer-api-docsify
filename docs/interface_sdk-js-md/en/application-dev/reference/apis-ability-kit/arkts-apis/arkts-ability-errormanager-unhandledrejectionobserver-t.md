# UnhandledRejectionObserver

```TypeScript
export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void
```

The observer will be called by system when an unhandled rejection occurs.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void--><!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | Error \| Any | Yes | the reason of the rejection, typically of Error type |
| promise | Promise&lt;Any&gt; | Yes | the promise that is rejected |

