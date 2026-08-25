# closeFormEditAbility

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## closeFormEditAbility

```TypeScript
function closeFormEditAbility(isMainPage?: boolean): void
```

Closes the widget editing page.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMainPage | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16501015](../errorcode-form.md#16501015-failed-to-close-semi-modal-widget-editing-page-of-another-application) |
