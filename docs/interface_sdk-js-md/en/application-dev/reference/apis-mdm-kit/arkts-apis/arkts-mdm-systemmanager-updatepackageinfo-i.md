# UpdatePackageInfo

系统更新包信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemManager-export interface UpdatePackageInfo--><!--Device-systemManager-export interface UpdatePackageInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## authInfo

```TypeScript
authInfo?: string
```

系统更新包的鉴权信息。

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdatePackageInfo-authInfo?: string--><!--Device-UpdatePackageInfo-authInfo?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## description

```TypeScript
description?: PackageDescription
```

系统更新包描述信息。

**Type:** [PackageDescription](arkts-mdm-systemmanager-packagedescription-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdatePackageInfo-description?: PackageDescription--><!--Device-UpdatePackageInfo-description?: PackageDescription-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## packages

```TypeScript
packages: Array<Package>
```

系统更新包详情。

**Type:** Array&lt;Package&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdatePackageInfo-packages: Array<Package>--><!--Device-UpdatePackageInfo-packages: Array<Package>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## version

```TypeScript
version: string
```

系统更新包版本号。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdatePackageInfo-version: string--><!--Device-UpdatePackageInfo-version: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

