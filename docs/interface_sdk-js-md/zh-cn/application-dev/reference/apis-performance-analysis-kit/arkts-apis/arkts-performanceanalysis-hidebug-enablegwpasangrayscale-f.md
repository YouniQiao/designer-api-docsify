# enableGwpAsanGrayscale

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

使能GWP-ASan，用于检测堆内存使用中的非法行为。该接口主要用于动态配置并启用GWP-ASan，以适配应用自定义的GWP-ASan检测策略。配置在应用重新启动后生效。更多关于GWP-ASan的说明，请参见 [使用GWP-ASan检测内存错误](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-gwpasan-detection)。

> **说明：**&gt;
> 1. 若设备运行期间通过本接口设置的GWP-ASan应用数量超过配额限制，调用该接口将会失败并抛出错误码。请使用try-catch捕获异常，以避免应用异常退出。&gt;
> 2. 设备重启后，本接口设置的GWP-ASan参数将会失效。&gt;
> 3. 由于该接口涉及跨进程通信，耗时较长，为了避免引入性能问题，建议不要在主线程中直接调用该接口。可以通过[@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md)或
> [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md)开启异步线程，以避免应用卡顿。

**起始版本：** 20

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | 否 |
| duration | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [11400114](../errorcode-hiviewdfx-hidebug.md#11400114-使能gwp-asan失败) |
