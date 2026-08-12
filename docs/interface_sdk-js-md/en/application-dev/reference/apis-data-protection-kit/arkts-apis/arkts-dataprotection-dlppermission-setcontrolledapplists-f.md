# setControlledAppLists

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## setControlledAppLists

```TypeScript
function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>
```

Sets the list of applications controlled by enterprise DLP. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.DLP_POLICY_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpPermission-function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>--><!--Device-dlpPermission-function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appLists | Array&lt;string&gt; | Yes | List of application identifiers of the controlled applications. &lt;br&gt;The maximum length of the array is 100. If the length exceeds 100, error code 19100001 is returned. &lt;br&gt;Each element in the array is the appIdentifier of the application. The maximum length of a single application identifier is 4096 bytes. If the length exceeds 4096 bytes, error code 19100001 is returned. |
| userId | number | No | ID of the user for whom the controlled application is configured. If this parameter is not specified, the current user is used by default. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [19100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100023](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100023-specified-user-id-inconsistent-with-the-current-user-id) | The specified userId is inconsistent with the current userId. |
| [19100011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [19100024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100024-personal-space-users-cannot-set-controlled-apps) | The specified userId belongs to a personal space user and cannot be managed. |

