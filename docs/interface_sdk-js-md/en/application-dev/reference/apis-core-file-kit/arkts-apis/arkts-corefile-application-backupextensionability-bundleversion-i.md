# BundleVersion

恢复时所需要的版本信息，开发者可根据配置的版本号来判断本次恢复时的应用版本数据。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface BundleVersion--><!--Device-unnamed-export interface BundleVersion-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BundleVersion } from 'kits/@kit.CoreFileKit';
```

## code

```TypeScript
code: long
```

应用的版本号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleVersion-code: long--><!--Device-BundleVersion-code: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## name

```TypeScript
name: string
```

应用的版本名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleVersion-name: string--><!--Device-BundleVersion-name: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

