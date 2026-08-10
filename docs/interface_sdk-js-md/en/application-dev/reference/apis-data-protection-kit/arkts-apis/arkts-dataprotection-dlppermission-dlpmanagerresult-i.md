# DLPManagerResult

表示打开DLP权限管理应用的结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-dlpPermission-export interface DLPManagerResult--><!--Device-dlpPermission-export interface DLPManagerResult-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## resultCode

```TypeScript
resultCode: number
```

表示打开DLP权限管理应用并退出后返回的结果码。取值范围为0到3。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPManagerResult-resultCode: number--><!--Device-DLPManagerResult-resultCode: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## want

```TypeScript
want: Want
```

表示打开DLP权限管理应用并退出后返回的数据。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPManagerResult-want: Want--><!--Device-DLPManagerResult-want: Want-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

