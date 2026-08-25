# getRecentOperatingHandStatus

## 导入模块

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## getRecentOperatingHandStatus

```TypeScript
function getRecentOperatingHandStatus(): OperatingHandStatus
```

获取最新触控操作手状态。该方法直接返回最新的操作手状态，无需订阅事件即可调用。

**起始版本：** 15

**需要权限：** 
- API版本20+：ohos.permission.ACTIVITY_MOTION 或 ohos.permission.DETECT_GESTURE
- API版本15 - 19：ohos.permission.ACTIVITY_MOTION

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**返回值：**

| 类型 |
| --- |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../errorcode-motion.md#31500001-服务异常) |
