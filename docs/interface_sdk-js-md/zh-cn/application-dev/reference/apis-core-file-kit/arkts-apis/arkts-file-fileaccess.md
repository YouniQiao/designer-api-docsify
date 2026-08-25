# @ohos.file.fileAccess

fileAccess模块是基于[extension](../../../application-models/extensionability-overview.md)机制实现的一个对公共文件访问和操作的 框架。该模块一方面对接各类文件管理服务，如存储管理服务等；另一方面为系统应用提供一套统一的文件访问管理接口。存储管理服务可以管理内置存储部分目录， 以及共享盘、U盘、SD卡等设备上的资源。

> **说明：**
> - 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> - 本模块为系统接口。
> - 当前只支持FilePicker、文件管理器调用。
> - 本模块接口从API version 23开始废弃。不建议使用以下接口，
> - 推荐使用[@ohos.file.fs](arkts-corefile-fileio-n.md)接口进行文件访问。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 23

**替代接口：** [fileIo](arkts-corefile-fileio-n.md)

**系统能力：** SystemCapability.FileManagement.UserFileService

## 导入模块

```TypeScript
import { fileAccess } from '@kit.CoreFileKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md) |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md) |
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
| [DEVICES_URI](arkts-corefile-fileaccess-con-sys.md#devices_uri) |
<!--DelEnd-->
