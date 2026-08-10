# @ohos.file.recent

该模块提供最近访问列表插入、移除、查询等常用能力。

> **说明：**
> 
> - 当前只支持文件管理器调用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace recent--><!--Device-unnamed-declare namespace recent-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { recent } from 'kits/@kit.CoreFileKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [add](arkts-corefile-recent-add-f-sys.md#add) | 将uri对应的文件加入最近访问列表。 |
| [listFile](arkts-corefile-recent-listfile-f-sys.md#listfile) | 查询最近访问列表中文件信息。 |
| [remove](arkts-corefile-recent-remove-f-sys.md#remove) | 将uri对应的文件从最近访问列表中移除。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [FileInfo](arkts-corefile-recent-fileinfo-i-sys.md) | 最近访问列表文件信息。 |
<!--DelEnd-->

