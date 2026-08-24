# onFormUninstall (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## onFormUninstall

```TypeScript
function onFormUninstall(callback: Callback<string>): void
```

Listens to the event of uninstall form.You can use this method to listen to the event of uninstall form.

**Since:** 23

<!--Device-formHost-function onFormUninstall(callback: Callback<string>): void--><!--Device-formHost-function onFormUninstall(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | The callback of formUninstall. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

