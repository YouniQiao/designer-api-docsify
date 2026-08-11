# getAllDisposedRules (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## getAllDisposedRules

```TypeScript
function getAllDisposedRules(): Array<DisposedRuleConfiguration>
```

Obtains all the disposed rules set for the current user.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

<!--Device-appControl-function getAllDisposedRules(): Array<DisposedRuleConfiguration>--><!--Device-appControl-function getAllDisposedRules(): Array<DisposedRuleConfiguration>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;DisposedRuleConfiguration&gt; | Array of disposed rules. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. A non-system application is not allowed to call a system API. |

## Examples

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = appControl.getAllDisposedRules();
  console.info('getAllDisposedRules successfully. Data: ' + JSON.stringify(data));
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getAllDisposedRules failed ' + message);
}
```

