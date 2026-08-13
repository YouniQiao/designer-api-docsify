# UnhandledRejectionObserver

```TypeScript
export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void
```

The observer will be called by system when an unhandled rejection occurs.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void--><!--Device-errorManager-export type UnhandledRejectionObserver = (reason: Error | Any, promise: Promise<Any>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | Error \| Any | Yes |
| promise | Promise & lt;Any & gt; | Yes |
