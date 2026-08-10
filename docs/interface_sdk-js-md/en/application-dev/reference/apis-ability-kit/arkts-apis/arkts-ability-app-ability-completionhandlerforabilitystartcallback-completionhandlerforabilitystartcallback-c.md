# CompletionHandlerForAbilityStartCallback

CompletionHandlerForAbilityStartCallback提供了onRequestSuccess和onRequestFailure两个回调函数属性，分别在拉起指定类型的Ability组件成功和失败时回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-unnamed-export class CompletionHandlerForAbilityStartCallback--><!--Device-unnamed-export class CompletionHandlerForAbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { CompletionHandlerForAbilityStartCallback, AbilityStartFailureCode } from 'kits/@kit.AbilityKit';
```

## onRequestFailure

```TypeScript
onRequestFailure?: OnRequestFailureFn
```

拉起指定类型的Ability组件失败时的回调函数。 

从API version 21开始，该接口支持在原子化服务中使用。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CompletionHandlerForAbilityStartCallback-onRequestFailure?: OnRequestFailureFn--><!--Device-CompletionHandlerForAbilityStartCallback-onRequestFailure?: OnRequestFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onRequestSuccess

```TypeScript
onRequestSuccess?: OnRequestSuccessFn
```

拉起指定类型的Ability组件成功时的回调函数。

从API version 21开始，该接口支持在原子化服务中使用。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CompletionHandlerForAbilityStartCallback-onRequestSuccess?: OnRequestSuccessFn--><!--Device-CompletionHandlerForAbilityStartCallback-onRequestSuccess?: OnRequestSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

