# onDeviceAvailable（系统接口）

## onDeviceAvailable

```TypeScript
function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void
```

Register device discovery callback

**起始版本：** 23

**废弃版本：** -1

<!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
