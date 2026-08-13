# onAdd (System API)

## Modules to Import

```TypeScript
import { bundleMonitor } from '@kit.AbilityKit';
```

## onAdd

```TypeScript
function onAdd(callback: Callback<BundleChangedInfo>): void
```

Register installation listener.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function onAdd(callback: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function onAdd(callback: Callback<BundleChangedInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BundleChangedInfo](arkts-ability-bundlemonitor-bundlechangedinfo-i-sys.md)&gt; | Yes | Indicates the callback to be registered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

