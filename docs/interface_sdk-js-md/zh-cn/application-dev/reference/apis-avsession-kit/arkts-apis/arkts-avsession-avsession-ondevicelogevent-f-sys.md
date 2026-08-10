# onDeviceLogEvent（系统接口）

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## onDeviceLogEvent

```TypeScript
function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void
```

Register log event callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-avSession-function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceLogEventCode&gt; | 是 | Used to handle ('deviceLogEvent') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 202 | Not System App. |

