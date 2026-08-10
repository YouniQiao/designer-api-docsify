# UninstallParam (System API)

共享包卸载需指定的参数信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-installer-export interface UninstallParam--><!--Device-installer-export interface UninstallParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from 'kits/@kit.AbilityKit';
```

## bundleName

```TypeScript
bundleName: string
```

共享包包名。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-UninstallParam-bundleName: string--><!--Device-UninstallParam-bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## versionCode

```TypeScript
versionCode?: int
```

指示共享包的版本号。默认值：如果不填写versionCode，则卸载该包名的所有共享包。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-UninstallParam-versionCode?: int--><!--Device-UninstallParam-versionCode?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

