# CopyResult (System API)

表示复制操作失败时的返回信息，复制成功时则没有返回信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

<!--Device-fileAccess-interface CopyResult--><!--Device-fileAccess-interface CopyResult-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## destUri

```TypeScript
destUri: string
```

产生冲突的目标文件的 uri。如果非冲突导致的错误，则为空。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-CopyResult-destUri: string--><!--Device-CopyResult-destUri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## errCode

```TypeScript
errCode: number
```

错误码。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-CopyResult-errCode: number--><!--Device-CopyResult-errCode: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## errMsg

```TypeScript
errMsg: string
```

错误信息。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-CopyResult-errMsg: string--><!--Device-CopyResult-errMsg: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## sourceUri

```TypeScript
sourceUri: string
```

源文件(夹) uri。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-CopyResult-sourceUri: string--><!--Device-CopyResult-sourceUri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

