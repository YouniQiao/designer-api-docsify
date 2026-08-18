# offDeviceAvailable（系统接口）

## 导入模块

```TypeScript
```

## offDeviceAvailable

```TypeScript
function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void
```

Unregister device discovery callback

**起始版本：** 23

<!--Device-avSession-function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
