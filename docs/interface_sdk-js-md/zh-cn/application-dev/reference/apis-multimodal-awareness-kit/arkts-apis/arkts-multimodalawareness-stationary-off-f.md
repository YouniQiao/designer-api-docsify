# off

## 导入模块

```TypeScript
import { stationary } from 'kits/@kit.MultimodalAwarenessKit';
```

## off

```TypeScript
function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void
```

Unsubscribes from the device status.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void--><!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | 是 | Device status type. |
| event | [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | 是 | Event type. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActivityResponse&gt; | 否 | Callback used to receive reported data. If no value or **undefined** is passed, all callbacks associated with the specified event in the process will be unregistered. |

## 示例

```TypeScript
stationary.off('still', stationary.ActivityEvent.ENTER);
```

