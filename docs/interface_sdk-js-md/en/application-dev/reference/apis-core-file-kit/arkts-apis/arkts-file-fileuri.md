# @ohos.file.fileuri(文件URI)

提供文件URI相关接口，可用于URI与应用沙箱路径之间的转换。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace fileUri--><!--Device-unnamed-declare namespace fileUri-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

## Modules to Import

```TypeScript
import { fileUri } from 'kits/@kit.CoreFileKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getUriFromPath](arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath) | 通过应用沙箱内的文件路径生成URI。路径中的中文及非数字字母的特殊字符会进行百分号编码。 |

### Classes

| Name | Description |
| --- | --- |
| [FileUri](arkts-corefile-fileuri-fileuri-c.md) | FileUri表示文件的URI，继承自uri.URI。 |

