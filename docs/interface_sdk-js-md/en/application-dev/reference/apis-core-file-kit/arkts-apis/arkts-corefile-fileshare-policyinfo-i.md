# PolicyInfo

Policy information to manager permissions on a URI.

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

Indicates the mode of operation for the URI, example { OperationMode.READ_MODE } or { OperationMode.READ_MODE | OperationMode.WRITE_MODE }

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyInfo-operationMode: int--><!--Device-PolicyInfo-operationMode: int-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## uri

```TypeScript
uri: string
```

Indicates the uri of the policy information.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyInfo-uri: string--><!--Device-PolicyInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

