# PerfTest

PerfTest类为白盒性能测试框架的总入口。 提供测试任务创建、测试代码段执行和数据采集、测量结果获取等能力。 通过[create](#create)创建实例。

**起始版本：** 20

**系统能力：** SystemCapability.Test.PerfTest

## 导入模块

```TypeScript
import {PerfMetric, PerfTestStrategy, PerfMeasureResult, PerfTest} from 'kits/@kit.TestKit';
```

## create

```TypeScript
static create(strategy: PerfTestStrategy): PerfTest
```

静态方法，构造一个PerfTest对象，并返回该对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.PerfTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [PerfTestStrategy](arkts-test-test-perftest-perfteststrategy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PerfTest](arkts-test-test-perftest-perftest-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [32400001](../errorcode-perftest.md#32400001-初始化失败) |
| [32400002](../errorcode-perftest.md#32400002-内部错误) |
| [32400003](../errorcode-perftest.md#32400003-参数校验失败) |
| [32400007](../errorcode-perftest.md#32400007-接口不支持并行调用) |

## destroy

```TypeScript
destroy(): void
```

销毁PerfTest对象，释放该对象占用的相关资源。与[create](#create)方法配对使用，在PerfTest对象使用完毕后调用， 未调用此方法可能导致资源无法释放。调用后不应再使用该PerfTest对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.PerfTest

**错误码：**

| 错误码ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-内部错误) |
| [32400007](../errorcode-perftest.md#32400007-接口不支持并行调用) |

## getMeasureResult

```TypeScript
getMeasureResult(metric: PerfMetric): PerfMeasureResult
```

获取指定性能指标的测量数据。需要在run()执行完成后调用，否则无法获取到有效的测量数据。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.PerfTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [metric](arkts-test-test-perftest-perfmeasureresult-i.md) | [PerfMetric](arkts-test-test-perftest-perfmetric-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PerfMeasureResult](arkts-test-test-perftest-perfmeasureresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-内部错误) |
| [32400003](../errorcode-perftest.md#32400003-参数校验失败) |
| [32400006](../errorcode-perftest.md#32400006-无法获取性能数据) |
| [32400007](../errorcode-perftest.md#32400007-接口不支持并行调用) |

## run

```TypeScript
run(): Promise<void>
```

运行性能测试，按配置次数迭代执行测试代码段并采集性能数据，使用Promise回调。每次迭代中，框架依次执行 actionCode和resetCode（若已配置），并在actionCode执行期间采集性能数据。执行完成后，可通过 [getMeasureResult](#getmeasureresult)获取采集到的测量结果数据。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.PerfTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-内部错误) |
| [32400004](../errorcode-perftest.md#32400004-执行回调函数失败) |
| [32400005](../errorcode-perftest.md#32400005-采集性能数据失败) |
| [32400007](../errorcode-perftest.md#32400007-接口不支持并行调用) |
