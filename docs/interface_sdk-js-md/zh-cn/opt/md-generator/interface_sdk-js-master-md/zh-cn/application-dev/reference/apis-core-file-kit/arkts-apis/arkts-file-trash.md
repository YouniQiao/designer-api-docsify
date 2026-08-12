# @ohos.file.trash

The **file.trash** module provides APIs for querying, recovering, or permanently deleting the files or directories in Recently deleted (trash). Currently, only local files and directories are supported.You can use **delete()** of [@ohos.file.fileAccess](arkts-file-fileaccess.md#fileAccess) to move a file or directory to the trash.

> **NOTE：**
> 
> - Currently, the APIs of this module can be called only by **FileManager**.

**起始版本：** 10

**废弃版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace trash--><!--Device-unnamed-declare namespace trash-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [completelyDelete](arkts-corefile-trash-completelydelete-f-sys.md#completelydelete) |
| [listFile](arkts-corefile-trash-listfile-f-sys.md#listfile) |
| [recover](arkts-corefile-trash-recover-f-sys.md#recover) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [FileInfo](arkts-corefile-trash-fileinfo-i-sys.md) |
<!--DelEnd-->
