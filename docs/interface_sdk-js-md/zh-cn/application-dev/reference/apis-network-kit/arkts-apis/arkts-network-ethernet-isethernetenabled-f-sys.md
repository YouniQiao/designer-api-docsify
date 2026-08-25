# isEthernetEnabled（系统接口）

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## isEthernetEnabled

```TypeScript
function isEthernetEnabled(): boolean
```

检查全局以太网开关是否启用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_NETWORK_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |
