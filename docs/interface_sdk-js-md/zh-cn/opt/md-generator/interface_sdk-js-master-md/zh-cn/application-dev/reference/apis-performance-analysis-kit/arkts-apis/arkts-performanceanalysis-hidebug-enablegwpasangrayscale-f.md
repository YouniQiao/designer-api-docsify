# enableGwpAsanGrayscale

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

使能GWP-ASan，用于检测堆内存使用中的非法行为。该接口主要用于动态配置并启用GWP-ASan，以适配应用自定义的GWP-ASan检测策略。配置在应用重新启动后生效。

**起始版本：** 20

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | 否 |
| duration | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [11400114](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiviewdfx-hidebug.md#11400114-使能gwpasan失败) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function enableGwpAsanTask(): void {
  let options: hidebug.GwpAsanOptions = {
    alwaysEnabled: true,
    sampleRate: 2500,
    maxSimutaneousAllocations: 5000,
  };
  let duration: number = 4;
  hidebug.enableGwpAsanGrayscale(options, duration);
}

taskpool.execute(enableGwpAsanTask).then(() => {
  console.info(`Succeeded in enabling GWP-ASan.`);
}).catch((error: BusinessError) => {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
})
```


## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

使能GWP-ASan，用于检测堆内存使用中的非法行为。

**起始版本：** 20

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | 否 |
| duration | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [11400114](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiviewdfx-hidebug.md#11400114-使能gwpasan失败) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function enableGwpAsanTask(): void {
  let options: hidebug.GwpAsanOptions = {
    alwaysEnabled: true,
    sampleRate: 2500,
    maxSimutaneousAllocations: 5000,
  };
  let duration: number = 4;
  hidebug.enableGwpAsanGrayscale(options, duration);
}

taskpool.execute(enableGwpAsanTask).then(() => {
  console.info(`Succeeded in enabling GWP-ASan.`);
}).catch((error: BusinessError) => {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
})
```
