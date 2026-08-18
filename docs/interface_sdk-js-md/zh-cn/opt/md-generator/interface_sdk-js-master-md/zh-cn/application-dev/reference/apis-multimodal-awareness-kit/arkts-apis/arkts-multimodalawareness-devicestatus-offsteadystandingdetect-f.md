# offSteadyStandingDetect

## 导入模块

```TypeScript
```

## offSteadyStandingDetect

```TypeScript
function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void
```

取消订阅设备静止姿态感知（支架态）事件。

**起始版本：** 23

<!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [32500003](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500003-取消订阅失败) |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-服务异常) |
