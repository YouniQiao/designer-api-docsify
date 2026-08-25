# @ohos.file.hash(@ohos.file.hash (文件哈希处理))

该模块提供文件哈希处理能力，对文件内容进行哈希处理，适用于数据完整性校验、版本比对与内容去重等场景，可确保计算结果的不可变性与一致性，并支持流式处理大文件。

> **使用说明：**
使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取沙箱路径的方式及其接口用法可参考： [应用上下文Context-获取应用文件路径](../../../application-models/application-context-stage.md#获取应用文件路径)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { hash } from '@kit.CoreFileKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createHash(@ohos.file.hash (文件哈希处理))](arkts-corefile-hash-createhash-f.md) |
| [hash(@ohos.file.hash (文件哈希处理))](arkts-corefile-hash-f.md) |
| [hash(@ohos.file.hash (文件哈希处理))](arkts-corefile-hash-f.md) |

### 类

| 名称 |
| --- |
| [HashStream(@ohos.file.hash (文件哈希处理))](arkts-corefile-hash-hashstream-c.md) |
