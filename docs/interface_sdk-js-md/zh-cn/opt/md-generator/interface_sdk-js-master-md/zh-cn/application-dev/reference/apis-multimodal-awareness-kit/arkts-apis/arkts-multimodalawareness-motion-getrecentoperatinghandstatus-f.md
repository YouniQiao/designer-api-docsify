# getRecentOperatingHandStatus

## getRecentOperatingHandStatus

```TypeScript
function getRecentOperatingHandStatus(): OperatingHandStatus
```

获取最新触控操作手状态。

**起始版本：** 15

**需要权限：** 
- API版本20+：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE
- API版本15 - 19：ohos.permission.ACTIVITY_MOTION

<!--Device-motion-function getRecentOperatingHandStatus(): OperatingHandStatus--><!--Device-motion-function getRecentOperatingHandStatus(): OperatingHandStatus-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**返回值：**

| 类型 |
| --- |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let data:motion.OperatingHandStatus = motion.getRecentOperatingHandStatus();
    console.info('get succeeded: ' + data);
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get recent operating hand status. Code: ${error.code}, message: ${error.message}`);
}
```
