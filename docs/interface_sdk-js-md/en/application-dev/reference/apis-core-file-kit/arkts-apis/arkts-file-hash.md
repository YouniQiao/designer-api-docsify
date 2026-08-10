# @ohos.file.hash

该模块提供文件哈希处理能力，对文件内容进行哈希处理。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace hash--><!--Device-unnamed-declare namespace hash-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createHash](arkts-corefile-hash-createhash-f.md#createhash) | 创建并返回 HashStream 对象，该对象可用于使用给定的 algorithm 生成哈希摘要。 |
| [hash](arkts-corefile-hash-f.md#hash) | 计算文件的哈希值，使用Promise异步回调。 |
| [hash](arkts-corefile-hash-f.md#hash-1) | 计算文件的哈希值，使用callback异步回调。 |

### Classes

| Name | Description |
| --- | --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) | HashStream 类是用于创建数据的哈希摘要的实用工具。由 [createHash](arkts-corefile-hash-createhash-f.md#createhash) 接口获得。 |

