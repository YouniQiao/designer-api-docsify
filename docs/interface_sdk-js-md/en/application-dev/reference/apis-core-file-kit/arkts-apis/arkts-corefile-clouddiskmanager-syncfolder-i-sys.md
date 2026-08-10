# SyncFolder (System API)

表示同步根信息。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-cloudDiskManager-interface SyncFolder--><!--Device-cloudDiskManager-interface SyncFolder-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudDiskManager } from 'kits/@kit.CoreFileKit';
```

## bundleName

```TypeScript
bundleName: string
```

同步根对应的包名。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-SyncFolder-bundleName: string--><!--Device-SyncFolder-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## customAlias

```TypeScript
customAlias?: string
```

在文管列表显示的别名。默认值为undefined。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-SyncFolder-customAlias?: string--><!--Device-SyncFolder-customAlias?: string-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## displayNameResId

```TypeScript
displayNameResId?: int
```

资源ID，可以映射到文管列表显示的别名。默认值为undefined。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-SyncFolder-displayNameResId?: int--><!--Device-SyncFolder-displayNameResId?: int-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## path

```TypeScript
path: string
```

同步根对应的URI。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-SyncFolder-path: string--><!--Device-SyncFolder-path: string-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## state

```TypeScript
state: SyncFolderState
```

同步根对应的状态信息。

**Type:** [SyncFolderState](arkts-corefile-clouddiskmanager-syncfolderstate-e-sys.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-SyncFolder-state: SyncFolderState--><!--Device-SyncFolder-state: SyncFolderState-End-->

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

