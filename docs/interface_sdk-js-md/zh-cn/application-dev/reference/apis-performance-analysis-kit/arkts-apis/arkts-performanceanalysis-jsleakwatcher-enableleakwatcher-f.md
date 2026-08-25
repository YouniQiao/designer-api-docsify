# enableLeakWatcher

## 导入模块

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void
```

使能ArkTS对象泄漏检测。此接口通过一次调用即可检测ArkTS对象的内存泄漏，比之前需要调用四个函数（enable、watch、check、dump）的方法更加简洁。使用场景：  
- 对内存使用有严格要求的应用，需要持续监控内存泄漏情况。  
- 监控使用XComponent、NodeContainer、Window、CustomComponent、Ability等组件的应用是否发生泄漏。  
- 应用开发调试和测试阶段，快速发现内存泄漏问题。  
- 长时间运行的应用，需要定期检测内存泄漏。

**起始版本：** 20

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |
| configs | Array & lt;string & gt; | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001-参数isenabled无效) |
| [10801002](../errorcode-jsleakwatcher.md#10801002-参数config无效) |
| [10801003](../errorcode-jsleakwatcher.md#10801003-参数callback无效) |


## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void
```

使能ArkTS对象泄漏检测。此接口通过一次调用即可检测ArkTS对象的内存泄漏，比之前需要调用四个函数（enable、watch、check、dump）的方法更加简洁；通过configs可配置项参数，自定义设置监测项各属性，相比较之前极大提升了泄漏检测性能。

> **注意：**&gt;
> 当前jsLeakWatcher泄漏检测性能开销较大，会导致应用卡顿，建议增大检测间隔时间，减少卡顿频率。
> 使用场景：
- 对性能要求较高的应用，需要通过配置检测间隔、阈值等参数来平衡检测精度和性能开销。  
- 大型应用或复杂应用，需要精细控制泄漏检测的参数，如检测间隔、泄漏阈值、最大dump数量等。  
- 使用特定组件（如CustomComponent、Window、Ability等）的应用，需要针对性监控这些组件的泄漏。  
- 对内存管理有严格要求的应用，需要设置过滤规则排除某些不需要监控的对象。  
- 长时间运行或需要持续监控的应用，需要合理设置检测间隔和最大保存数量。

**起始版本：** 24

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |
| configs | [LeakWatcherConfig](arkts-performanceanalysis-jsleakwatcher-leakwatcherconfig-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001-参数isenabled无效) |
| [10801002](../errorcode-jsleakwatcher.md#10801002-参数config无效) |
| [10801003](../errorcode-jsleakwatcher.md#10801003-参数callback无效) |
