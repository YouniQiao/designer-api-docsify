# recordInputEventTime（系统接口）

## recordInputEventTime

```TypeScript
function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void
```

记录动效场景开始前，用户输入触发事件类型与时间。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void--><!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | 是 |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | 是 |
| time | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { systemDateTime, BusinessError } from '@kit.BasicServicesKit';
import { performanceMonitor } from '@kit.ArkUI';

// 获取当前系统时间
let time = systemDateTime.getTime(false);
// 更新用户触发事件类型与时间
performanceMonitor.recordInputEventTime(performanceMonitor.ActionType.LAST_UP, performanceMonitor.SourceType.PERF_MOUSE_EVENT, time);
```
