# offFormUninstall (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## offFormUninstall

```TypeScript
function offFormUninstall(callback?: Callback<string>): void
```

Cancels listening to the event of uninstall form.

You can use this method to cancel listening to the event of uninstall form.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-formHost-function offFormUninstall(callback?: Callback<string>): void--><!--Device-formHost-function offFormUninstall(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | The callback of formUninstall. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 202 | The application is not a system application. |

