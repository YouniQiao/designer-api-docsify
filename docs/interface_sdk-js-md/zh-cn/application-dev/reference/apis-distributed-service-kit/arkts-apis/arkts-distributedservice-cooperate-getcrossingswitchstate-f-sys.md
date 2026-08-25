# getCrossingSwitchState（系统接口）

## 导入模块

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## getCrossingSwitchState

```TypeScript
function getCrossingSwitchState(networkId: string, callback: AsyncCallback<boolean>): void
```

获取目标设备键鼠穿越开关的状态，使用Callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md)(networkId: string, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getCrossingSwitchState

```TypeScript
function getCrossingSwitchState(networkId: string): Promise<boolean>
```

获取目标设备键鼠穿越开关的状态，使用Promise异步方式返回结果。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md)(networkId: string)

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
