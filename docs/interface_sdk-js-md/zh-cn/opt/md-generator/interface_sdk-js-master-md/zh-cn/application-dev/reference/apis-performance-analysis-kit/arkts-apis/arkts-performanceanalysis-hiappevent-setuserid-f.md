# setUserId

## 导入模块

```TypeScript
```

## setUserId

```TypeScript
function setUserId(name: string, value: string): void
```

设置用户ID值。用于在配置[Processor](arkts-performanceanalysis-hiappevent-processor-i.md#processor)数据处理者时进行关联。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-hiAppEvent-function setUserId(name: string, value: string): void--><!--Device-hiAppEvent-function setUserId(name: string, value: string): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  hiAppEvent.setUserId('key', 'value');
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to setUserId event, code=${error.code}`);
}
```
