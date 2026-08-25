# addCheckRule

## 导入模块

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## addCheckRule

```TypeScript
function addCheckRule(rule: bigint) : void
```

添加一条或多条规则到系统，系统根据添加的规则进行检测或反馈，当有相应规则触发时可在hilog中grep HiChecker查看运行信息。

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
