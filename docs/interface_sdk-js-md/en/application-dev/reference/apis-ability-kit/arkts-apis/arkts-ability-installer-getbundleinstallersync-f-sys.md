# getBundleInstallerSync (System API)

## Modules to Import

```TypeScript
import { installer } from 'kits/@kit.AbilityKit';
```

## getBundleInstallerSync

```TypeScript
function getBundleInstallerSync(): BundleInstaller
```

获取并返回BundleInstaller对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-installer-function getBundleInstallerSync(): BundleInstaller--><!--Device-installer-function getBundleInstallerSync(): BundleInstaller-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [BundleInstaller](arkts-ability-installer-bundleinstaller-i-sys.md) | BundleInstaller object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

