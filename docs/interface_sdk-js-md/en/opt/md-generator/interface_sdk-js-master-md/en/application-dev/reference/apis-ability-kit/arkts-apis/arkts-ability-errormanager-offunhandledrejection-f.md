# offUnhandledRejection

## Modules to Import

```TypeScript
```

## offUnhandledRejection

```TypeScript
function offUnhandledRejection(observer?: UnhandledRejectionObserver): void
```

Unregister unhandled rejection observer.

**Since:** 24

<!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void--><!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |
