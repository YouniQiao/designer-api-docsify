# CompletionHandlerForAtomicService

CompletionHandlerForAtomicService provides two callback functions, [onAtomicServiceRequestSuccess](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md#onatomicservicerequestsuccess) and [onAtomicServiceRequestFailure] [onAtomicServiceRequestFailure](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md#onatomicservicerequestfailure), to handle the results of successful and failed atomic service launch requests, respectively.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare class CompletionHandlerForAtomicService--><!--Device-unnamed-declare class CompletionHandlerForAtomicService-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAtomicServiceRequestFailure

```TypeScript
onAtomicServiceRequestFailure: OnAtomicServiceRequestFailureFn
```

Notify the failure result of openAtomicService.

**Type:** [OnAtomicServiceRequestFailureFn](arkts-na-onatomicservicerequestfailurefn-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletionHandlerForAtomicService-onAtomicServiceRequestFailure: OnAtomicServiceRequestFailureFn--><!--Device-CompletionHandlerForAtomicService-onAtomicServiceRequestFailure: OnAtomicServiceRequestFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAtomicServiceRequestSuccess

```TypeScript
onAtomicServiceRequestSuccess: OnAtomicServiceRequestSuccessFn
```

Notify the success result of openAtomicService.

**Type:** [OnAtomicServiceRequestSuccessFn](arkts-na-onatomicservicerequestsuccessfn-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletionHandlerForAtomicService-onAtomicServiceRequestSuccess: OnAtomicServiceRequestSuccessFn--><!--Device-CompletionHandlerForAtomicService-onAtomicServiceRequestSuccess: OnAtomicServiceRequestSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

