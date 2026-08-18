# on_ActivityType

## 导入模块

```TypeScript
```

## on_ActivityType

```TypeScript
function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void
```

订阅设备状态变化事件。当设备满足指定状态条件时，系统会触发回调函数上报状态变化事件。调用on()后，必须在不使用时调用off()取消订阅，避免多余的性能功耗开销。

**起始版本：** 9

<!--Device-stationary-function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void--><!--Device-stationary-function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | 是 |
| event | [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | 是 |
| reportLatencyNs | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActivityResponse](arkts-multimodalawareness-stationary-activityresponse-i.md)&gt; | 是 |

**示例**

```TypeScript
let reportLatencyNs = 1000000000; // 单位：纳秒
stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
    console.info('data=' + JSON.stringify(data));
});
```
