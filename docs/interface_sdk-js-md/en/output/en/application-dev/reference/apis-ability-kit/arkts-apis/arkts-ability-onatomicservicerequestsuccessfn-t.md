# OnAtomicServiceRequestSuccessFn

```TypeScript
type OnAtomicServiceRequestSuccessFn = (appId: string) => void
```

Notify the success result of openAtomicService.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAtomicServiceRequestSuccessFn = (appId: string) => void--><!--Device-unnamed-type OnAtomicServiceRequestSuccessFn = (appId: string) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Globally unique identifier of an atomicservice, which is allocated by the cloud.  |

