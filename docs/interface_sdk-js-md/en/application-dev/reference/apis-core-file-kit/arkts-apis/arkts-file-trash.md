# @ohos.file.trash

The **file.trash** module provides APIs for querying, recovering, or permanently deleting the files or directories in Recently deleted (trash). Currently, only local files and directories are supported. You can use **delete()** of [@ohos.file.fileAccess](arkts-file-fileaccess.md) to move a file or directory to the trash.

> **NOTE：**&gt;
> - Currently, the APIs of this module can be called only by **FileManager**.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { trash } from '@kit.CoreFileKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [completelyDelete](arkts-corefile-trash-completelydelete-f-sys.md) |
| [listFile](arkts-corefile-trash-listfile-f-sys.md) |
| [recover](arkts-corefile-trash-recover-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FileInfo](arkts-corefile-trash-fileinfo-i-sys.md) |
<!--DelEnd-->
