# share（系统接口）

## share

```TypeScript
function share(
      sharingResource: string,
      participants: Array<Participant>,
      callback: AsyncCallback<Result<Array<Result<Participant>>>>
    ): void
```

根据指定的共享资源标识和共享参与者发起共享邀请，使用callback异步回调。

**起始版本：** 11

<!--Device-sharing-function share(      sharingResource: string,      participants: Array<Participant>,      callback: AsyncCallback<Result<Array<Result<Participant>>>>    ): void--><!--Device-sharing-function share(      sharingResource: string,      participants: Array<Participant>,      callback: AsyncCallback<Result<Array<Result<Participant>>>>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sharingResource | string | 是 |
| participants | Array&lt;Participant&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Result&lt;Array&lt;Result&lt;Participant&gt;&gt;&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
});
cloudData.sharing.share('sharing_resource_test', participants, (err: BusinessError, result) => {
  if (err) {
    console.error(`share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info(`share succeeded, result: ${result}`);
});
```


## share

```TypeScript
function share(
      sharingResource: string,
      participants: Array<Participant>
    ): Promise<Result<Array<Result<Participant>>>>
```

根据指定的共享资源标识和共享参与者发起共享邀请，使用Promise异步回调。

**起始版本：** 11

<!--Device-sharing-function share(      sharingResource: string,      participants: Array<Participant>    ): Promise<Result<Array<Result<Participant>>>>--><!--Device-sharing-function share(      sharingResource: string,      participants: Array<Participant>    ): Promise<Result<Array<Result<Participant>>>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sharingResource | string | 是 |
| participants | Array&lt;Participant&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Result&lt;Array&lt;Result&lt;Participant&gt;&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
});
cloudData.sharing.share('sharing_resource_test', participants).then((result) => {
  console.info(`share success, result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`share failed, code is ${err.code},message is ${err.message}`);
});
```
