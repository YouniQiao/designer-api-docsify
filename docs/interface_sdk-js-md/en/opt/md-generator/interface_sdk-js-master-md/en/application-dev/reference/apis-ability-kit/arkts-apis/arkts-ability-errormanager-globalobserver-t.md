# GlobalObserver

```TypeScript
export type GlobalObserver = (reason: GlobalError) => void
```

Defines an exception observer that can be used as an input parameter for [errorManager.on('globalErrorOccurred')](arkts-ability-errormanager-onerror-f.md#on_error) and [errorManager.on('globalUnhandledRejectionDetected')](arkts-ability-errormanager-onerror-f.md#on_error) to monitor event processing on the main thread of the current application.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void--><!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | [GlobalError](arkts-ability-errormanager-globalerror-i.md) | Yes |
