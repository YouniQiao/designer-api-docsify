# removeCheckRule

## 导入模块

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## removeCheckRule

```TypeScript
function removeCheckRule(rule: bigint) : void
```

删除一条或多条规则，删除的规则后续将不再生效。

**起始版本：** 9

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | bigint | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
