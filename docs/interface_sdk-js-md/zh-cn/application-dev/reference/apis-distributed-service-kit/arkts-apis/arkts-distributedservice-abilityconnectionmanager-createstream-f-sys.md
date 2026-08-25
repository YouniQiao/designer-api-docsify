# createStream（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## createStream

```TypeScript
function createStream(sessionId: number, param: StreamParam): Promise<number>
```

应用连接成功后，设备A或设备B可创建传输流，发送图片和视频流，使用Promise异步回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| param | [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [32300001](../errorcode-device-manager.md#32300001-重复创建传输流) |
| [32300003](../errorcode-device-manager.md#32300003-比特率不支持) |
| [32300004](../errorcode-device-manager.md#32300004-色彩空间不支持) |
