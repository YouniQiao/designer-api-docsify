# PolicyInfo

需要授予或激活URI访问权限的策略信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-fileShare-export interface PolicyInfo--><!--Device-fileShare-export interface PolicyInfo-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## operationMode

```TypeScript
operationMode: int
```

授予或激活权限的URI访问模式，例如 { OperationMode.READ_MODE } 或{ OperationMode.READ_MODE | OperationMode.WRITE_MODE }。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyInfo-operationMode: int--><!--Device-PolicyInfo-operationMode: int-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## uri

```TypeScript
uri: string
```

需要授予或激活访问权限的URI，需符合URI格式规范。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyInfo-uri: string--><!--Device-PolicyInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

