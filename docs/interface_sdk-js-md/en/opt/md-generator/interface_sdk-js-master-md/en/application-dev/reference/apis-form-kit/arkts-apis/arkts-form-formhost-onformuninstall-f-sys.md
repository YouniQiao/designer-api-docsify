# onFormUninstall (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## onFormUninstall

```TypeScript
function onFormUninstall(callback: Callback<string>): void
```

Listens to the event of uninstall form. You can use this method to listen to the event of uninstall form.

**Since:** 23

**Deprecated since:** -1

<!--Device-formHost-function onFormUninstall(callback: Callback<string>): void--><!--Device-formHost-function onFormUninstall(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
