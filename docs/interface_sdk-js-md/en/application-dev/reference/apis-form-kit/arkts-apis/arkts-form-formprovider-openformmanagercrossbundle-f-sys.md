# openFormManagerCrossBundle (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## openFormManagerCrossBundle

```TypeScript
function openFormManagerCrossBundle(want: Want): void
```

Open the view of forms belonging to the specified bundle.Client to communication with FormManagerService.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PUBLISH_FORM_CROSS_BUNDLE

<!--Device-formProvider-function openFormManagerCrossBundle(want: Want): void--><!--Device-formProvider-function openFormManagerCrossBundle(want: Want): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | The want of the form to open. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

