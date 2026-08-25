# UnhandledRejectionObserver

```TypeScript
export type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void
```

Defines an observer to capture the cause of a rejected promise.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | Error \| any | Yes |
| promise | Promise & lt;any & gt; | Yes |
