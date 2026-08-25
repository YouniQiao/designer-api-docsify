# setUserOperation（系统接口）

## 导入模块

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## setUserOperation

```TypeScript
function setUserOperation(operation: Operation, mac: string, params: string): void
```

设置用户操作

**起始版本：** 20

**需要权限：** ohos.permission.CONNECT_MECHANIC_HARDWARE

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operation | [Operation](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-operation-e.md) | 是 |
| mac | string | 是 |
| params | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
