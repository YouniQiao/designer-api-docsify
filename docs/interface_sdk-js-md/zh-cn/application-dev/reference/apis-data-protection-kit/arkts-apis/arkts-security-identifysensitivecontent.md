# @ohos.security.identifySensitiveContent(Identify sensitive file)

识别敏感内容通过输入的[Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md)来检测指定文件中的敏感信息。 系统根据提供的[Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md)策略（包括敏感标签、关键字集合和正则表达式）， 对文件内容进行关键字匹配和正则表达式匹配，返回匹配到的敏感内容结果。

**起始版本：** 21

**系统能力：** SystemCapability.Security.DataLossPrevention

## 导入模块

```TypeScript
import { identifySensitiveContent } from 'kits/@kit.DataProtectionKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [scanFile(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-scanfile-f.md) |

### 接口

| 名称 |
| --- |
| [MatchResult(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-matchresult-i.md) |
| [Policy(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-policy-i.md) |
