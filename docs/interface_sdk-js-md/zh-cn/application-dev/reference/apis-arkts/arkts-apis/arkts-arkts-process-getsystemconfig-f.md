# getSystemConfig

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## getSystemConfig

```TypeScript
function getSystemConfig(name: number): number
```

获取系统配置信息。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getSystemConfig](arkts-arkts-process-processmanager-c.md#getsystemconfig)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 定义系统配置参数
let _SC_ARG_MAX = 0;
// 获取系统配置信息
let pres = processManager.getSystemConfig(_SC_ARG_MAX);
```
