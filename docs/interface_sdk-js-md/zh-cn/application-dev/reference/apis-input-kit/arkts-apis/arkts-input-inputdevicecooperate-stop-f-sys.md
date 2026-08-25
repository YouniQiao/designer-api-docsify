# stop（系统接口）

## 导入模块

```TypeScript
import { inputDeviceCooperate } from 'kits/@kit.InputKit';
```

## stop

```TypeScript
function stop(callback: AsyncCallback<void>): void
```

停止键鼠穿越，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [deactivateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## stop

```TypeScript
function stop(): Promise<void>
```

停止键鼠穿越，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [deactivateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
