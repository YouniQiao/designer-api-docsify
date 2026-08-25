# getRule

## 导入模块

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## getRule

```TypeScript
function getRule() : bigint
```

获取当前线程规则、进程规则、告警规则的合集。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 |
| --- |
| bigint |

**示例**

```TypeScript
// 添加一条规则
hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);

// 获取已添加的规则
hichecker.getRule();
```
