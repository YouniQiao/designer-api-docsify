# openFormEditAbility

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormEditAbility

```TypeScript
function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void
```

Opens the widget editing page.

**Since:** 18

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abilityName | string | Yes |
| formId | string | Yes |
| isMainPage | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [16501007](../errorcode-form.md#16501007-untrusted-widget) |
