# queryParticipants（系统接口）

## queryParticipants

```TypeScript
function queryParticipants(sharingResource: string, callback: AsyncCallback<Result<Array<Participant>>>): void
```

根据指定的共享资源标识查询当前共享的参与者，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sharing-function queryParticipants(sharingResource: string, callback: AsyncCallback<Result<Array<Participant>>>): void--><!--Device-sharing-function queryParticipants(sharingResource: string, callback: AsyncCallback<Result<Array<Participant>>>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sharingResource | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt;&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.queryParticipants('sharing_resource_test', (err: BusinessError, result) => {
  if (err) {
    console.error(`query participants failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`query participants succeeded, result: ${result}`);
});
```


## queryParticipants

```TypeScript
function queryParticipants(sharingResource: string): Promise<Result<Array<Participant>>>
```

根据指定的共享资源标识查询当前共享的参与者，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sharing-function queryParticipants(sharingResource: string): Promise<Result<Array<Participant>>>--><!--Device-sharing-function queryParticipants(sharingResource: string): Promise<Result<Array<Participant>>>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.sharing.queryParticipants('sharing_resource_test').then((result) => {
  console.info(`query participants succeeded, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`query participants failed, code is ${err.code},message is ${err.message}`);
});
```
