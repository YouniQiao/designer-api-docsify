# ErrorHandler

```TypeScript
export type ErrorHandler = (errObject: Error) => void
```

The ErrorHandler will be called when the ArkTS runtime throws an exception that is not caught by the user.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-errorManager-export type ErrorHandler = (errObject: Error) => void--><!--Device-errorManager-export type ErrorHandler = (errObject: Error) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errObject | Error | Yes | Event name, message, and error stack of the exception. |

