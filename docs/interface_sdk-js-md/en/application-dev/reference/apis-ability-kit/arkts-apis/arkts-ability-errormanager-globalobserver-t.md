# GlobalObserver

```TypeScript
export type GlobalObserver = (reason: GlobalError) => void
```

Defines an exception observer that can be used as an input parameter for  
[errorManager.on('globalErrorOccurred')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_and  
[errorManager.on('globalUnhandledRejectionDetected')]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_to monitor event processing on the main thread of the current application.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void--><!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Object related to the exception event name, message, error stack information, exception thread name, and exception thread type.  |

