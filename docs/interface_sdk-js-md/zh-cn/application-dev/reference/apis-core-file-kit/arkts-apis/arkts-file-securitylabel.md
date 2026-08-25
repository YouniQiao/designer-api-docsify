# @ohos.file.securityLabel(@ohos.file.securityLabel (数据标签))

该模块提供文件数据安全等级的相关功能：向应用程序提供查询、设置文件数据安全等级的ArkTS接口。该功能可以帮助应用实现对不同安全等级文件的分级管理和访问控制，解决数据安全管控的需求，提升应用的数据安全合规性。

> **使用说明：**
使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取沙箱路径的方式及其接口用法可参考： [应用上下文Context-获取应用文件路径](../../../application-models/application-context-stage.md#获取应用文件路径)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { securityLabel } from '@kit.CoreFileKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getSecurityLabel(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-getsecuritylabel-f.md) |
| [getSecurityLabel(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-getsecuritylabel-f.md) |
| [getSecurityLabelSync(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-getsecuritylabelsync-f.md) |
| [setSecurityLabel(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-setsecuritylabel-f.md) |
| [setSecurityLabel(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-setsecuritylabel-f.md) |
| [setSecurityLabelSync(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-setsecuritylabelsync-f.md) |

### 类型

| 名称 |
| --- |
| [DataLevel(@ohos.file.securityLabel (数据标签))](arkts-corefile-securitylabel-datalevel-t.md) |
