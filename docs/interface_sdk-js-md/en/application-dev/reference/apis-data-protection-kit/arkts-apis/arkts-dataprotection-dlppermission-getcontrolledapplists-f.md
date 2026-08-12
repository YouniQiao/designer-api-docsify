# getControlledAppLists

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getControlledAppLists

```TypeScript
function getControlledAppLists(): Promise<Array<string>>
```

Obtains the list of applications controlled by enterprise DLP for the current user. This API uses a promise to return the result.

> **NOTE：**
> This API can only be used to query the list of applications controlled by enterprise DLP, which is set using
> [setControlledAppLists](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md#setControlledAppLists).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.DLP_POLICY_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpPermission-function getControlledAppLists(): Promise<Array<string>>--><!--Device-dlpPermission-function getControlledAppLists(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the list of applications controlled by enterprise DLP for the current user. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [19100011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

