# getDisposedRulesByBundle (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## getDisposedRulesByBundle

```TypeScript
function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>
```

Query all disposed rules under the current user for the specified bundle name.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

**Model restriction:** This API can be used only in the stage model.

<!--Device-appControl-function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>--><!--Device-appControl-function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;DisposedRuleConfiguration&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
