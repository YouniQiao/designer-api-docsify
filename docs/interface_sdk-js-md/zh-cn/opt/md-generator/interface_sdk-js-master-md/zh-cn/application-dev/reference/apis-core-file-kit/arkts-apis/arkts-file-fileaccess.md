# @ohos.file.fileAccess

fileAccess模块是基于[extension](../../../application-models/extensionability-overview.md)机制实现的一个对公共文件访问和操作的框架。该模块一方面对接各类文 件管理服务，如存储管理服务等；另一方面为系统应用提供一套统一的文件访问管理接口。存储管理服务可以管理内置存储部分目录，以及共享盘、U盘、SD卡等设备上的资源。 > **说明：** > > - 当前只支持FilePicker、文件管理器调用。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [fileIo](arkts-corefile-fileio-n.md#fileIo)

<!--Device-unnamed-declare namespace fileAccess--><!--Device-unnamed-declare namespace fileAccess-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md#createFileAccessHelper（系统接口）) |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md#createFileAccessHelper（系统接口）) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md#getFileAccessAbilityInfo（系统接口）) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md#getFileAccessAbilityInfo（系统接口）) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md) |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |
| [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md) |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |
| [MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md) |
| [NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md) |
| [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md) |
| [RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FileKey](arkts-corefile-fileaccess-filekey-e-sys.md) |
| [NotifyType](arkts-corefile-fileaccess-notifytype-e-sys.md) |
| [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [DEVICES_URI](arkts-corefile-fileaccess-con-sys.md#DEVICES_URI) |
<!--DelEnd-->
