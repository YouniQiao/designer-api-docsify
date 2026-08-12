# @ohos.file.fileAccess

The **fileAccess** module provides a framework for accessing and operating user files based on   
[extension](../../../application-models/extensionability-overview.md). This module interacts with a variety of file management services, such as the storage management service, and provides a set of unified file access and management APIs for system applications. The storage management service manages both the directories of the built-in storage and resources on external devices, such as shared disks, USB flash drives, and SD cards.

> **NOTE：**
> 
> - Currently, the APIs of this module can be called only by **FilePicker** and **FileManager**.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [fileIo](arkts-corefile-fileio-n.md#fileIo)

<!--Device-unnamed-declare namespace fileAccess--><!--Device-unnamed-declare namespace fileAccess-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { fileAccess } from '@kit.CoreFileKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md#createfileaccesshelper) |
| [createFileAccessHelper](arkts-corefile-fileaccess-createfileaccesshelper-f-sys.md#createfileaccesshelper-1) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md#getfileaccessabilityinfo) |
| [getFileAccessAbilityInfo](arkts-corefile-fileaccess-getfileaccessabilityinfo-f-sys.md#getfileaccessabilityinfo-1) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FileKey](arkts-corefile-fileaccess-filekey-e-sys.md) |
| [NotifyType](arkts-corefile-fileaccess-notifytype-e-sys.md) |
| [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Constants（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DEVICES_URI](arkts-corefile-fileaccess-con-sys.md#devices_uri) |
<!--DelEnd-->
