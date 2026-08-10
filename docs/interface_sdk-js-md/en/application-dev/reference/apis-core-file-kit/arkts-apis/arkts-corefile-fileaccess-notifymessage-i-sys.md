# NotifyMessage (System API)

通知回调函数的值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Substitutes:** @ohos.file.fs:fileIo.WatchEvent

<!--Device-fileAccess-interface NotifyMessage--><!--Device-fileAccess-interface NotifyMessage-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## type

```TypeScript
type: NotifyType
```

变更的通知类型。

**Type:** [NotifyType](arkts-corefile-cloudsync-notifytype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyMessage-type: NotifyType--><!--Device-NotifyMessage-type: NotifyType-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## uris

```TypeScript
uris: Array<string>
```

所变更文件的uri集合，目前仅支持单条通知，后序支持多条通知。

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyMessage-uris: Array<string>--><!--Device-NotifyMessage-uris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

