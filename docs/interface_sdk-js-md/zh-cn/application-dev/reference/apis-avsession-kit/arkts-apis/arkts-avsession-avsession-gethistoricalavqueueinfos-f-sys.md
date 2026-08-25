# getHistoricalAVQueueInfos（系统接口）

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## getHistoricalAVQueueInfos

```TypeScript
function getHistoricalAVQueueInfos(maxSize: number, maxAppSize: number, callback: AsyncCallback<Array<Readonly<AVQueueInfo>>>): void
```

获取全部的历史播放歌单。结果通过callback异步回调方式返回。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxSize | number | 是 |
| maxAppSize | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Readonly&lt;[AVQueueInfo](arkts-avsession-avsession-avqueueinfo-i-sys.md)&gt;&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |


## getHistoricalAVQueueInfos

```TypeScript
function getHistoricalAVQueueInfos(maxSize: number, maxAppSize: number): Promise<Array<Readonly<AVQueueInfo>>>
```

获取全部的历史播放歌单。结果通过Promise异步回调方式返回。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxSize | number | 是 |
| maxAppSize | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Readonly&lt;[AVQueueInfo](arkts-avsession-avsession-avqueueinfo-i-sys.md)&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
