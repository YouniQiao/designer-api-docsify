# SharedDirectoryInfo (System API)

应用程序向系统捐献的目录信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-fileShare-export interface SharedDirectoryInfo--><!--Device-fileShare-export interface SharedDirectoryInfo-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## bundleName

```TypeScript
bundleName: string
```

应用程序的包名。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SharedDirectoryInfo-bundleName: string--><!--Device-SharedDirectoryInfo-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

## path

```TypeScript
path: string
```

应用程序捐献的目录。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SharedDirectoryInfo-path: string--><!--Device-SharedDirectoryInfo-path: string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

## permissionMode

```TypeScript
permissionMode: int
```

应用程序捐献目录的权限，例如 { OperationMode.READ_MODE } 或{ OperationMode.READ_MODE | OperationMode.WRITE_MODE }。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SharedDirectoryInfo-permissionMode: int--><!--Device-SharedDirectoryInfo-permissionMode: int-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

