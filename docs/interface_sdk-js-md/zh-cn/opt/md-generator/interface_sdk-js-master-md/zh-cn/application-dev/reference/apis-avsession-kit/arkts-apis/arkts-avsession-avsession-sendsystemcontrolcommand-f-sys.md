# sendSystemControlCommand（系统接口）

## sendSystemControlCommand

```TypeScript
function sendSystemControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void
```

发送控制命令给置顶会话。结果通过callback异步回调方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function sendSystemControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void--><!--Device-avSession-function sendSystemControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [6600105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600107-命令消息过载) |

## 示例

```TypeScript
let cmd : avSession.AVControlCommandType = 'play';
// let cmd : avSession.AVControlCommandType = 'pause';
// let cmd : avSession.AVControlCommandType = 'stop';
// let cmd : avSession.AVControlCommandType = 'playNext';
// let cmd : avSession.AVControlCommandType = 'playPrevious';
// let cmd : avSession.AVControlCommandType = 'fastForward';
// let cmd : avSession.AVControlCommandType = 'rewind';
let avcommand: avSession.AVControlCommand = {command:cmd};
// let cmd: avSession.AVControlCommandType = 'seek';
// let avcommand = {command:cmd, parameter:10};
// let cmd : avSession.AVControlCommandType = 'setSpeed';
// let avcommand = {command:cmd, parameter:2.6};
// let cmd : avSession.AVControlCommandType = 'setLoopMode';
// let avcommand = {command:cmd, parameter:avSession.LoopMode.LOOP_MODE_SINGLE};
// let cmd : avSession.AVControlCommandType = 'toggleFavorite';
// let avcommand = {command:cmd, parameter:"false"};
avSession.sendSystemControlCommand(avcommand, () => {
    console.info('Succeeded in sending system control command.');
});
```


## sendSystemControlCommand

```TypeScript
function sendSystemControlCommand(command: AVControlCommand): Promise<void>
```

发送控制命令给置顶会话。结果通过Promise异步回调方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function sendSystemControlCommand(command: AVControlCommand): Promise<void>--><!--Device-avSession-function sendSystemControlCommand(command: AVControlCommand): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [6600105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600107-命令消息过载) |

## 示例

```TypeScript
let cmd : avSession.AVControlCommandType = 'play';
// let cmd : avSession.AVControlCommandType = 'pause';
// let cmd : avSession.AVControlCommandType = 'stop';
// let cmd : avSession.AVControlCommandType = 'playNext';
// let cmd : avSession.AVControlCommandType = 'playPrevious';
// let cmd : avSession.AVControlCommandType = 'fastForward';
// let cmd : avSession.AVControlCommandType = 'rewind';
let avcommand: avSession.AVControlCommand = {command:cmd};
// let cmd : avSession.AVControlCommandType = 'seek';
// let avcommand = {command:cmd, parameter:10};
// let cmd : avSession.AVControlCommandType = 'setSpeed';
// let avcommand = {command:cmd, parameter:2.6};
// let cmd : avSession.AVControlCommandType = 'setLoopMode';
// let avcommand = {command:cmd, parameter:avSession.LoopMode.LOOP_MODE_SINGLE};
// let cmd : avSession.AVControlCommandType = 'toggleFavorite';
// let avcommand = {command:cmd, parameter:"false"};
avSession.sendSystemControlCommand(avcommand).then(() => {
  console.info('Succeeded in sending system control command.');
});
```
