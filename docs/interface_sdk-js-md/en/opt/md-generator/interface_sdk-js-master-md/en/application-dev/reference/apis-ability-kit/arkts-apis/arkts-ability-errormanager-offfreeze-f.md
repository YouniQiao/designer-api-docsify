# offFreeze

## Modules to Import

```TypeScript
```

## offFreeze

```TypeScript
function offFreeze(observer?: FreezeObserver): void
```

Unregister the observer for freeze event. This function can only be called from main thread.

**Since:** 24

<!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void--><!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |
