# setDisposedRules (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## setDisposedRules

```TypeScript
function setDisposedRules(disposedRuleConfigurations: Array<DisposedRuleConfiguration>): void
```

Sets disposed rules in batches for an application or an application clone.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| disposedRuleConfigurations | Array&lt;[DisposedRuleConfiguration](arkts-ability-appcontrol-disposedruleconfiguration-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700005](../errorcode-bundle.md#17700005-appid-is-an-empty-string) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
