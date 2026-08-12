# @ohos.app.ability.CompletionHandlerForAtomicService

## Modules to Import

```TypeScript
import { FailureCode } from '@kit.AbilityKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CompletionHandlerForAtomicService](arkts-ability-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md) | CompletionHandlerForAtomicService provides two callback functions,  [onAtomicServiceRequestSuccess](arkts-ability-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md#onAtomicServiceRequestSuccess) and [onAtomicServiceRequestFailure](arkts-ability-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md#onAtomicServiceRequestFailure),to handle the results of successful and failed atomic service launch requests, respectively. |

### Enums

| Name | Description |
| --- | --- |
| [FailureCode](arkts-ability-app-ability-completionhandlerforatomicservice-failurecode-e.md) | Enumerates the errors codes available for failures in launching an atomic service. |

### Types

| Name | Description |
| --- | --- |
| [OnAtomicServiceRequestFailureFn](arkts-ability-onatomicservicerequestfailurefn-t.md) | Notify the failure result of openAtomicService. |
| [OnAtomicServiceRequestSuccessFn](arkts-ability-onatomicservicerequestsuccessfn-t.md) | Notify the success result of openAtomicService. |

