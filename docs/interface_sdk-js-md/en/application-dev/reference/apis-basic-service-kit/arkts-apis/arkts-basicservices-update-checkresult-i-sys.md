# CheckResult (System API)

版本检查结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface CheckResult--><!--Device-update-export interface CheckResult-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## isExistNewVersion

```TypeScript
isExistNewVersion: boolean
```

是否有新版本。true表示有新版本，false表示没有新版本。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-CheckResult-isExistNewVersion: boolean--><!--Device-CheckResult-isExistNewVersion: boolean-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## newVersionInfo

```TypeScript
newVersionInfo: NewVersionInfo
```

新版本数据。

**Type:** [NewVersionInfo](arkts-basicservices-update-newversioninfo-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-CheckResult-newVersionInfo: NewVersionInfo--><!--Device-CheckResult-newVersionInfo: NewVersionInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

