# UninstallParam (System API)

Defines the parameters required for the uninstall of a shared bundle.

**Since:** 23

<!--Device-installer-export interface UninstallParam--><!--Device-installer-export interface UninstallParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from 'installer';
```

## bundleName

```TypeScript
bundleName: string
```

Name of the shared bundle.

**Type:** string

**Since:** 23

<!--Device-UninstallParam-bundleName: string--><!--Device-UninstallParam-bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## versionCode

```TypeScript
versionCode?: int
```

Version number of the shared bundle. By default, no value is passed, and all shared bundles of the specified name are uninstalled.

**Type:** int

**Since:** 23

<!--Device-UninstallParam-versionCode?: int--><!--Device-UninstallParam-versionCode?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

