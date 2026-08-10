# offAdd (System API)

## Modules to Import

```TypeScript
import { bundleMonitor } from 'kits/@kit.AbilityKit';
```

## offAdd

```TypeScript
function offAdd(callback?: Callback<BundleChangedInfo>): void
```

注销监听应用的安装。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function offAdd(callback?: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function offAdd(callback?: Callback<BundleChangedInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BundleChangedInfo&gt; | No | 注销监听的AsyncCallback，默认值：注销当前事件的所有callback。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

