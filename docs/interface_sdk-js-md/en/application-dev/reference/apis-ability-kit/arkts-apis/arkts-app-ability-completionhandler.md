# @ohos.app.ability.CompletionHandler

**CompletionHandler** is an optional parameter of [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md)
 and [OpenLinkOptions](arkts-ability-app-ability-openlinkoptions-openlinkoptions-i.md). It is used to process the result of
 an application launch request.


## Modules to Import

```TypeScript
import { CompletionHandler } from 'kits/@kit.AbilityKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CompletionHandler](arkts-ability-app-ability-completionhandler-completionhandler-c.md) | CompletionHandler provides two callback functions,  [onRequestSuccess](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestsuccess) and  [onRequestFailure](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestfailure), to handle the results of successful and failed application launch requests, respectively. |

### Types

| Name | Description |
| --- | --- |
| [OnRequestFailureFn](arkts-ability-onrequestfailurefn-t.md) | Notify the failure result of startAbility. |
| [OnRequestSuccessFn](arkts-ability-onrequestsuccessfn-t.md) | Notify the success result of startAbility. |

