# PolicyErrorResult

授予或激活权限失败的URI策略结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-fileShare-export interface PolicyErrorResult--><!--Device-fileShare-export interface PolicyErrorResult-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## code

```TypeScript
code: PolicyErrorCode
```

授权策略失败的URI对应的错误码。

**Type:** [PolicyErrorCode](arkts-corefile-fileshare-policyerrorcode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyErrorResult-code: PolicyErrorCode--><!--Device-PolicyErrorResult-code: PolicyErrorCode-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## message

```TypeScript
message: string
```

授权策略失败的URI对应的原因。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyErrorResult-message: string--><!--Device-PolicyErrorResult-message: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

## uri

```TypeScript
uri: string
```

授予或激活权限失败的URI。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PolicyErrorResult-uri: string--><!--Device-PolicyErrorResult-uri: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

