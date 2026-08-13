# offUpdate (System API)

## Modules to Import

```TypeScript
import { bundleMonitor } from '@kit.AbilityKit';
```

## offUpdate

```TypeScript
function offUpdate(callback?: Callback<BundleChangedInfo>): void
```

Unregister update listener.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function offUpdate(callback?: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function offUpdate(callback?: Callback<BundleChangedInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BundleChangedInfo](arkts-ability-bundlemonitor-bundlechangedinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
