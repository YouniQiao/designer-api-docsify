# AbilityStartCallback

定义拉起UIExtensionAbility执行结果的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare interface AbilityStartCallback--><!--Device-unnamed-declare interface AbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onError

```TypeScript
onError(code: int, name: string, message: string): void
```

拉起UIExtensionAbility执行失败的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void--><!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | 拉起UIExtensionAbility执行失败时返回的结果码。 |
| name | string | Yes | 拉起UIExtensionAbility执行失败时返回的名称。 |
| message | string | Yes | 拉起UIExtensionAbility执行失败时返回的错误信息。 |

## onResult

```TypeScript
onResult?: OnResultFn
```

拉起UIExtensionAbility终止时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStartCallback-onResult?: OnResultFn--><!--Device-AbilityStartCallback-onResult?: OnResultFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## completionHandler

```TypeScript
completionHandler?: CompletionHandlerForAbilityStartCallback
```

用于返回拉起指定类型的Ability组件的回调结果。

**Type:** [CompletionHandlerForAbilityStartCallback](arkts-ability-app-ability-completionhandlerforabilitystartcallback-completionhandlerforabilitystartcallback-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback--><!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

