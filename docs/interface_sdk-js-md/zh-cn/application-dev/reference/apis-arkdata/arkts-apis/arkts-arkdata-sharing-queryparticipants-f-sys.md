# queryParticipants（系统接口）

## 导入模块

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## queryParticipants

```TypeScript
function queryParticipants(sharingResource: string, callback: AsyncCallback<Result<Array<Participant>>>): void
```

根据指定的共享资源标识查询当前共享的参与者，使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sharingResource | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## queryParticipants

```TypeScript
function queryParticipants(sharingResource: string): Promise<Result<Array<Participant>>>
```

根据指定的共享资源标识查询当前共享的参与者，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sharingResource | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Result&lt;Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
