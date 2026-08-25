# runCmd（系统接口）

## 导入模块

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## runCmd

```TypeScript
function runCmd(
    command: string,
    options?: ConditionType
  ): ChildProcess
```

返回一个子进程对象，并 spawn 一个新的 ChildProcess 来运行命令。

**起始版本：** 7

**系统能力：** SystemCapability.Utils.Lang

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | string | 是 |
| options | [ConditionType](arkts-arkts-process-conditiontype-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ChildProcess](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-childprocess-childprocess-c.md) |
