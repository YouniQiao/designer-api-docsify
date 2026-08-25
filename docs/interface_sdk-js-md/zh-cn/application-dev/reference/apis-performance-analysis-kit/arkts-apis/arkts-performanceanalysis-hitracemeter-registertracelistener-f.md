# registerTraceListener

## 导入模块

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## registerTraceListener

```TypeScript
function registerTraceListener(callback: TraceEventListener): number
```

注册应用trace捕获开关通知回调，使用callback异步回调。注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。回调函数保存在应用进程内，一个进程最多可以注册10个回调函数。若注册的回调包含耗时操作，当回调被执行时，注册或注销行为会被阻塞 （等待回调执行完成）。因此，建议不要在应用主线程中注册或注销包含耗时操作的回调，避免发生应用冻屏。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TraceEventListener](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
