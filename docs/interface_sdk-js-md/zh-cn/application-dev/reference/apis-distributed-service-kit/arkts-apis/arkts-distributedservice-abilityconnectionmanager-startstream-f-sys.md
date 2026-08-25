# startStream（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## startStream

```TypeScript
function startStream(streamId: number): void
```

启动指定传输流，使传输流开始发送或接收视频数据。启动前需确保传输流已完成Surface绑定， 否则无法正常启动。需与stopStream()方法配对使用，使用完毕后应调用stopStream()停止传输流， 最后调用destroyStream()销毁传输流以释放资源。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [32300002](../errorcode-device-manager.md#32300002-流接收端未启动) |
