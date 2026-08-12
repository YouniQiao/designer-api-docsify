# getEnterpriseManagedTips

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## getEnterpriseManagedTips

```TypeScript
function getEnterpriseManagedTips(): Promise<string>
```

Gets enterprise message tips.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function getEnterpriseManagedTips(): Promise<string>--><!--Device-adminManager-function getEnterpriseManagedTips(): Promise<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | returns the enterprise message tips. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

