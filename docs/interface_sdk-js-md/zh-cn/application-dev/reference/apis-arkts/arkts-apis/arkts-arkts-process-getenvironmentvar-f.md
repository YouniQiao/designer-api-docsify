# getEnvironmentVar

## 导入模块

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getEnvironmentVar

```TypeScript
function getEnvironmentVar(name: string): string
```

获取环境变量名对应的值。如果环境变量不存在，返回undefined。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getEnvironmentVar](arkts-arkts-process-processmanager-c.md#getenvironmentvar)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |
