# OnAtomicServiceRequestFailureFn

```TypeScript
type OnAtomicServiceRequestFailureFn = (appId: string, failureCode: FailureCode, failureMessage: string) => void
```

Notify the failure result of openAtomicService.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAtomicServiceRequestFailureFn = (appId: string, failureCode: FailureCode, failureMessage: string) => void--><!--Device-unnamed-type OnAtomicServiceRequestFailureFn = (appId: string, failureCode: FailureCode, failureMessage: string) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Globally unique identifier of an atomicservice, which is allocated by the cloud. |
| failureCode | [FailureCode](arkts-ability-app-ability-completionhandlerforatomicservice-failurecode-e.md) | Yes | Indicates the failure code for open atomic service. |
| failureMessage | string | Yes | Indicates the detail failure message for open atomic service. |

