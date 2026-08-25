# @ohos.dlpSetDlpFeature(设置数据防泄漏入口)

本模块提供数据防泄漏（Data Loss Prevention，简称为DLP）特性开关的控制能力，包括开启和关闭DLP特性开关、返回特性开关设置结果等，帮助企业满足数据安全合规要求，实现机密文件的访问控制和加密保护。  
**使用场景**：  
- 需要满足数据安全合规要求的场景。 - 对机密文件进行访问控制和加密保护。

> **说明：**&gt;
> - 本模块首批接口从API version 26.0.0开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> - 本模块接口为系统接口。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { dlpSetDlpFeature } from '@kit.DataProtectionKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [setDlpFeature(设置数据防泄漏入口)](arkts-dataprotection-dlpsetdlpfeature-setdlpfeature-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DLPFeatureInfo(设置数据防泄漏入口)](arkts-dataprotection-dlpsetdlpfeature-dlpfeatureinfo-i-sys.md) |
| [StatusInfoResult(设置数据防泄漏入口)](arkts-dataprotection-dlpsetdlpfeature-statusinforesult-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DlpFeatureStatus(设置数据防泄漏入口)](arkts-dataprotection-dlpsetdlpfeature-dlpfeaturestatus-e-sys.md) |
<!--DelEnd-->
