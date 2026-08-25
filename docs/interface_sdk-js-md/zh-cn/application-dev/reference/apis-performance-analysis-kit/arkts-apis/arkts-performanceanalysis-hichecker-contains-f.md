# contains

## 导入模块

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## contains

```TypeScript
function contains(rule: bigint): boolean
```


> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[hichecker.containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md)替代。
当前已添加的规则集中是否包含了某一个特定的规则。如果传入的规则级别为线程级别，则仅在当前线程中进行查询。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
