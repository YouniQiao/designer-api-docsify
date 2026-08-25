# unprepare（系统接口）

## 导入模块

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## unprepare

```TypeScript
function unprepare(callback: AsyncCallback<void>): void
```

取消键鼠穿越准备，使用Callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md)(callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## unprepare

```TypeScript
function unprepare(): Promise<void>
```

取消键鼠穿越准备，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md)()

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
