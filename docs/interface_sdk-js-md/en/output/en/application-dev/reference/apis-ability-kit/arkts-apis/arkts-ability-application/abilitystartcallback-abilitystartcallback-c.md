# AbilityStartCallback

The module describes the callback invoked to return the UIExtensionAbility startup result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-export default class AbilityStartCallback--><!--Device-unnamed-export default class AbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onError

```TypeScript
onError(code: int, name: string, message: string): void
```

Called when the UIExtensionAbility fails to start.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void--><!--Device-AbilityStartCallback-onError(code: int, name: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Result code returned when the UIExtensionAbility fails to start. |
| name | string | Yes | Name returned when the UIExtensionAbility fails to start. |
| message | string | Yes | Error information returned when the UIExtensionAbility fails to start. |

## onResult

```TypeScript
onResult?(parameter: AbilityResult): void
```

Called when the UIExtensionAbility is terminated.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityStartCallback-onResult?(parameter: AbilityResult): void--><!--Device-AbilityStartCallback-onResult?(parameter: AbilityResult): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Result returned when [terminateSelfWithResult]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_is called to terminate the UIExtensionAbility. |

## completionHandler

```TypeScript
completionHandler?: CompletionHandlerForAbilityStartCallback
```

Callback invoked when the ability of a specified type is started.

**Type:** CompletionHandlerForAbilityStartCallback

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback--><!--Device-AbilityStartCallback-completionHandler?: CompletionHandlerForAbilityStartCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

