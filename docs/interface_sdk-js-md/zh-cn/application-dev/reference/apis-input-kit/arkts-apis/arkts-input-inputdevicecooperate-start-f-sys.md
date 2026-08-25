# start（系统接口）

## 导入模块

```TypeScript
import { inputDeviceCooperate } from 'kits/@kit.InputKit';
```

## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void
```

启动键鼠穿越，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinkDeviceDescriptor | string | 是 |
| srcInputDeviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4400001](../errorcode-cooperator.md#4400001-目标设备描述符错误) |
| [4400002](../errorcode-cooperator.md#4400002-操作输入设备失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>
```

启动键鼠穿越，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinkDeviceDescriptor | string | 是 |
| srcInputDeviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4400001](../errorcode-cooperator.md#4400001-目标设备描述符错误) |
| [4400002](../errorcode-cooperator.md#4400002-操作输入设备失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
