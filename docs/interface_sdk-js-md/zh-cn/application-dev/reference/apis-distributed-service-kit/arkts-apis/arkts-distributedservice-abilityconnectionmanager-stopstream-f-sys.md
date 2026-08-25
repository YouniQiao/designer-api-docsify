# stopStream（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## stopStream

```TypeScript
function stopStream(streamId: number): void
```

停止指定传输流，使传输流停止发送或接收视频数据。需与startStream()方法配对使用， 在不需要传输数据时应调用此方法停止传输流，最后调用destroyStream()销毁传输流以释放资源。 使用场景包括视频通话暂停、用户关闭摄像头、切换前后摄像头等需要临时停止视频传输时调用。

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
