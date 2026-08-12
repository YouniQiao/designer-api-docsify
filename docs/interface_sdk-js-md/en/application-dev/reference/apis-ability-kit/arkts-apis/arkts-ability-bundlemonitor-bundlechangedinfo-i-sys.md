# BundleChangedInfo (System API)

This module defines the result information of monitoring install, update and uninstall.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-bundleMonitor-interface BundleChangedInfo--><!--Device-bundleMonitor-interface BundleChangedInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bundleMonitor } from '@kit.AbilityKit';
```

## appIndex

```TypeScript
readonly appIndex: int
```

The app index of clone app

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

The bundle name

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

The user id

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleChangedInfo-readonly userId: int--><!--Device-BundleChangedInfo-readonly userId: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

