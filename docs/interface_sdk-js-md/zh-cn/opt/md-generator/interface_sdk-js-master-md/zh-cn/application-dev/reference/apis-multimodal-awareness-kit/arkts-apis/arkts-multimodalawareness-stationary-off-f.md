# off

## off

```TypeScript
function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void
```

设备状态管理，取消订阅设备状态服务。取消订阅后，将停止接收该状态相关的回调函数调用。调用off()时需要使用与on()相同的activity和event参数，才能正确取消对应的订阅。

**起始版本：** 9

<!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void--><!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | 是 |
| event | [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActivityResponse&gt; | 否 |

## 示例

```TypeScript
stationary.off('still', stationary.ActivityEvent.ENTER);
```
