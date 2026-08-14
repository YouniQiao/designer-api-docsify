# CompletionHandlerForAbilityStartCallback

CompletionHandlerForAbilityStartCallback provides two callback functions, **onRequestSuccess** and **onRequestFailure**, which are invoked when launching the specified ability succeeds or fails, respectively.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export class CompletionHandlerForAbilityStartCallback--><!--Device-unnamed-export class CompletionHandlerForAbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { CompletionHandlerForAbilityStartCallback } from 'CompletionHandlerForAbilityStartCallback';
import { AbilityStartFailureCode } from 'AbilityStartFailureCode';
```

## onRequestFailure

```TypeScript
onRequestFailure?: OnRequestFailureFn
```

Callback invoked when launching the specified ability fails. This API can be used in atomic services since API version 21.

**Type:** [OnRequestFailureFn](arkts-ability-onrequestfailurefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CompletionHandlerForAbilityStartCallback-onRequestFailure?: OnRequestFailureFn--><!--Device-CompletionHandlerForAbilityStartCallback-onRequestFailure?: OnRequestFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onRequestSuccess

```TypeScript
onRequestSuccess?: OnRequestSuccessFn
```

Callback invoked when the specified ability is successfully launched. This API can be used in atomic services since API version 21.

**Type:** [OnRequestSuccessFn](arkts-ability-onrequestsuccessfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CompletionHandlerForAbilityStartCallback-onRequestSuccess?: OnRequestSuccessFn--><!--Device-CompletionHandlerForAbilityStartCallback-onRequestSuccess?: OnRequestSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

