# once

## 导入模块

```TypeScript
import { stationary } from 'kits/@kit.MultimodalAwarenessKit';
```

## once

```TypeScript
function once(activity: ActivityType, callback: Callback<ActivityResponse>): void
```

查询设备状态。通过callback回调返回查询结果，仅执行一次。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActivityResponse](arkts-multimodalawareness-stationary-activityresponse-i.md)&gt; | 是 |
