# offMessage (System API)

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## offMessage

```TypeScript
function offMessage(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void
```

Unregister form message event Listening.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function offMessage(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function offMessage(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | No |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
