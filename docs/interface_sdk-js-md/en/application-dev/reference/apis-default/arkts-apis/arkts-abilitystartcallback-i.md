# AbilityStartCallback

The module describes the callback invoked to return the UIExtensionAbility startup result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface AbilityStartCallback--><!--Device-unnamed-declare interface AbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onError

```TypeScript
onError(code: int, name: string, message: string): void
```

Called when the UIExtensionAbility fails to start.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void--><!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Result code returned when the UIExtensionAbility fails to start <br>The value range is all integers. |
| name | string | Yes | Name returned when the UIExtensionAbility fails to start. |
| message | string | Yes | Error information returned when the UIExtensionAbility fails to start. |

## completionHandler

```TypeScript
completionHandler?: CompletionHandlerForAbilityStartCallback
```

Callback invoked when the ability of a specified type is started.

**Type:** [CompletionHandlerForAbilityStartCallback](../../apis-ability-kit/arkts-apis/arkts-ability-appabilitycompletionhandlerforabilitystartcallback-completionhandlerforabilitystartcallback-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback--><!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onResult

```TypeScript
onResult?: OnResultFn
```

Called when the UIExtensionAbility is terminated.

**Type:** [OnResultFn](arkts-onresultfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStartCallback-onResult?: OnResultFn--><!--Device-AbilityStartCallback-onResult?: OnResultFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

