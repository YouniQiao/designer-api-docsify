# BundleChangedInfo (System API)

应用变更信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-bundleMonitor-interface BundleChangedInfo--><!--Device-bundleMonitor-interface BundleChangedInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bundleMonitor } from 'kits/@kit.AbilityKit';
```

## appIndex

```TypeScript
readonly appIndex: int
```

应用状态发生变化的应用分身索引。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BundleChangedInfo-readonly appIndex: int--><!--Device-BundleChangedInfo-readonly appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## bundleName

```TypeScript
readonly bundleName: string
```

应用状态发生变化的应用Bundle名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleChangedInfo-readonly bundleName: string--><!--Device-BundleChangedInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## userId

```TypeScript
readonly userId: int
```

应用状态发生变化的用户ID，可以通过getOsAccountLocalId接口获取。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleChangedInfo-readonly userId: int--><!--Device-BundleChangedInfo-readonly userId: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

