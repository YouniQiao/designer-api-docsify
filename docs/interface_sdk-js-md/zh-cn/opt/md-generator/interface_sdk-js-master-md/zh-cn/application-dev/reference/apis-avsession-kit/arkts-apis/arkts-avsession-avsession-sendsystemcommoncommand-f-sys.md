# sendSystemCommonCommand（系统接口）

## sendSystemCommonCommand

```TypeScript
function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>
```

发送通用事件命令

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>--><!--Device-avSession-function sendSystemCommonCommand(command: string, args: ExtraInfo): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [ExtraInfo](arkts-avsession-avsession-extrainfo-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [6600105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600107-命令消息过载) |
