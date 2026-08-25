# AbilityStartCallback

The module describes the callback invoked to return the UIExtensionAbility startup result.

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onError

```TypeScript
onError(code: number, name: string, message: string): void
```

Called when the UIExtensionAbility fails to start.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| name | string | Yes |
| message | string | Yes |

## onResult

```TypeScript
onResult?(parameter: AbilityResult): void
```

Called when the UIExtensionAbility is terminated.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes |

## completionHandler

```TypeScript
completionHandler?: CompletionHandlerForAbilityStartCallback
```

Callback invoked when the ability of a specified type is started.

**Type:** [CompletionHandlerForAbilityStartCallback](arkts-ability-app-ability-completionhandlerforabilitystartcallback-completionhandlerforabilitystartcallback-c.md)

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
