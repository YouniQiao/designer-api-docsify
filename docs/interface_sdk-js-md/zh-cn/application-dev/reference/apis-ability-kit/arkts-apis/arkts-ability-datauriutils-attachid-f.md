# attachId

## 导入模块

```TypeScript
import { dataUriUtils } from 'kits/@kit.AbilityKit';
```

## attachId

```TypeScript
function attachId(uri: string, id: number): string
```

将ID附加到uri的路径末尾。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
