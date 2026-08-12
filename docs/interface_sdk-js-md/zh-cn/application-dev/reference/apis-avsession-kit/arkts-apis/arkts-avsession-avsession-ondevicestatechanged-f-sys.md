# onDeviceStateChanged（系统接口）

## onDeviceStateChanged

```TypeScript
function onDeviceStateChanged(callback: Callback<DeviceState>): void
```

Registers a system callback for the device connection phase.The callback includes information such as error codes, connection status, radar errors, and user behavior codes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void--><!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceState](arkts-avsession-avsession-devicestate-i-sys.md)&gt; | 是 | Callback used to return the device information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System App. |

