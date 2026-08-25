# ShareCenter（系统接口）

提供对接共享云服务的类。开发者需要继承此类并实现类的接口，系统内部通过该类的接口连接并使用共享云服务，实现端云共享的发起、取消或退出等能力。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## changeConfirmation

```TypeScript
changeConfirmation(
      userId: number,
      bundleName: string,
      sharingResource: string,
      state: cloudData.sharing.State
    ): Promise<Result<void>>
```

更改端云共享邀请。更改共享邀请时，需指定当前更改共享邀请的应用、共享数据的共享资源标识以及更改的状态，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |
| state | cloudData.sharing.State | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;void & gt; & gt; |

## changePrivilege

```TypeScript
changePrivilege(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

更改已共享数据的操作权限。更改权限时，需指定当前更改权限的应用、更改权限数据的资源标识和更改权限的参与者，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |
| participants | Array & lt;cloudData.sharing.Participant & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |

## confirmInvitation

```TypeScript
confirmInvitation(
      userId: number,
      bundleName: string,
      invitationCode: string,
      state: cloudData.sharing.State
    ): Promise<Result<string>>
```

被邀请者确认端云共享邀请。确认时，需指定当前确认邀请的应用、共享数据的邀请码以及确认状态，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| invitationCode | string | 是 |
| state | cloudData.sharing.State | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;string & gt; & gt; |

## exit

```TypeScript
exit(userId: number, bundleName: string, sharingResource: string): Promise<Result<void>>
```

退出端云共享。退出共享时，需指定当前退出共享的应用以及退出共享数据的资源标识，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;void & gt; & gt; |

## queryParticipants

```TypeScript
queryParticipants(
      userId: number,
      bundleName: string,
      sharingResource: string
    ): Promise<Result<Array<cloudData.sharing.Participant>>>
```

查询当前端云共享的参与者。查询时，需指定当前查询参与者的应用、查询参与者数据的资源标识，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;cloudData.sharing.Participant & gt; & gt; & gt; |

## queryParticipantsByInvitation

```TypeScript
queryParticipantsByInvitation(
      userId: number,
      bundleName: string,
      invitationCode: string
    ): Promise<Result<Array<cloudData.sharing.Participant>>>
```

根据邀请码查询端云共享参与者。查询时，需指定当前查询参与者的应用、共享数据的邀请码，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| invitationCode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;cloudData.sharing.Participant & gt; & gt; & gt; |

## share

```TypeScript
share(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

发起端云共享邀请。共享邀请时，需指定当前发起共享的应用、共享数据的资源标识和共享参与者，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |
| participants | Array & lt;cloudData.sharing.Participant & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |

## unshare

```TypeScript
unshare(
      userId: number,
      bundleName: string,
      sharingResource: string,
      participants: Array<cloudData.sharing.Participant>
    ): Promise<Result<Array<Result<cloudData.sharing.Participant>>>>
```

取消端云共享。取消共享时，需指定当前取消共享的应用、取消共享数据的资源标识和取消共享的参与者，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |
| sharingResource | string | 是 |
| participants | Array & lt;cloudData.sharing.Participant & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;Result & lt;cloudData.sharing.Participant & gt; & gt; & gt; & gt; |
