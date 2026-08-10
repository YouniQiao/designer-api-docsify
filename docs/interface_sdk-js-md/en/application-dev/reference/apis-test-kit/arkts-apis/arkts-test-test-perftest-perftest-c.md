# PerfTest

PerfTest类为白盒性能测试框架的总入口，提供测试任务创建、测试代码段执行和数据采集、测量结果获取等能力。通过{@link create}创建实例。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class PerfTest--><!--Device-unnamed-declare class PerfTest-End-->

**System capability:** SystemCapability.Test.PerfTest

## Modules to Import

```TypeScript
import { PerfTestStrategy, PerfMetric, PerfTest, PerfMeasureResult } from 'kits/@kit.TestKit';
```

## create

```TypeScript
static create(strategy: PerfTestStrategy): PerfTest
```

静态方法，构造一个PerfTest对象，并返回该对象。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTest-static create(strategy: PerfTestStrategy): PerfTest--><!--Device-PerfTest-static create(strategy: PerfTestStrategy): PerfTest-End-->

**System capability:** SystemCapability.Test.PerfTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | [PerfTestStrategy](arkts-test-test-perftest-perfteststrategy-i.md) | Yes | 性能测试执行策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PerfTest](arkts-test-test-perftest-perftest-c.md) | 返回构造的PerfTest对象，可用于执行测试任务、采集性能数据和获取测量结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32400007 | The API does not support concurrent calls. @static |
| 32400002 | Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist. |
| 32400003 | Parameter verification failed. |
| 32400001 | Initialization failed. |

## Examples

```TypeScript
import { PerfMetric, PerfTest, PerfTestStrategy } from '@kit.TestKit';

async function demo() {
  let metrics: Array<PerfMetric> = [PerfMetric.DURATION];
  let num = 0;
  let actionCode = async (finish: Callback<boolean>) => { // Define the test code segment. The input parameter type is Callback<boolean> and the name is finish.
    for (let index = 0; index < 10000; index++) {
      num++;
    }
    finish(true); // Call the finish callback to notify that the code segment is executed successfully and as expected.
  };
  let resetCode = async (finish: Callback<boolean>) => { // Define the code segment for resetting the environment after the test ends.
    num = 0;
    finish(true);
  };
  let perfTestStrategy: PerfTestStrategy = {
    metrics: metrics,
    actionCode: actionCode,
    resetCode: resetCode,
    timeout: 30000,
    iterations: 10
  };
  let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // Construct a PerfTest object and create a test task.
}
```

## destroy

```TypeScript
destroy(): void
```

销毁PerfTest对象。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTest-destroy(): void--><!--Device-PerfTest-destroy(): void-End-->

**System capability:** SystemCapability.Test.PerfTest

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32400007 | The API does not support concurrent calls. |
| 32400002 | Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist. |

## Examples

```TypeScript
import { PerfMetric, PerfTest, PerfTestStrategy } from '@kit.TestKit';

async function demo() {
  let metrics: Array<PerfMetric> = [PerfMetric.DURATION];
  let num = 0;
  let actionCode = async (finish: Callback<boolean>) => {
    for (let index = 0; index < 10000; index++) {
      num++;
    }
    finish(true); // Call the finish callback to notify that the code segment is executed successfully and as expected.
  };
  let perfTestStrategy: PerfTestStrategy = {
    metrics: metrics,
    actionCode: actionCode
  };
  let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // Construct a PerfTest object and create a test task.
  await perfTest.run();
  perfTest.destroy(); // Destroy the PerfTest object.
}
```

## getMeasureResult

```TypeScript
getMeasureResult(metric: PerfMetric): PerfMeasureResult
```

获取指定性能指标的测量数据。需要在run()执行完成后调用，否则无法获取到有效的测量数据。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTest-getMeasureResult(metric: PerfMetric): PerfMeasureResult--><!--Device-PerfTest-getMeasureResult(metric: PerfMetric): PerfMeasureResult-End-->

**System capability:** SystemCapability.Test.PerfTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metric | [PerfMetric](arkts-test-test-perftest-perfmetric-e.md) | Yes | 性能指标。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PerfMeasureResult](arkts-test-test-perftest-perfmeasureresult-i.md) | 性能指标对应测量结果数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32400006 | Failed to obtain the measurement result. |
| 32400007 | The API does not support concurrent calls. |
| 32400002 | Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist. |
| 32400003 | Parameter verification failed. |

## Examples

```TypeScript
import { PerfMetric, PerfTest, PerfTestStrategy } from '@kit.TestKit';

async function demo() {
  let metrics: Array<PerfMetric> = [PerfMetric.DURATION];
  let num = 0;
  let actionCode = async (finish: Callback<boolean>) => {
    for (let index = 0; index < 10000; index++) {
      num++;
    }
    finish(true); // Call the finish callback to notify that the code segment is executed successfully and as expected.
  };
  let perfTestStrategy: PerfTestStrategy = {
    metrics: metrics,
    actionCode: actionCode
  };
  let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // Construct a PerfTest object and create a test task.
  await perfTest.run();
  let res = perfTest.getMeasureResult(PerfMetric.DURATION); // Obtain the measurement data of a specified performance metric.
}
```

## run

```TypeScript
run(): Promise<void>
```

运行性能测试，迭代执行测试代码段并采集性能数据，使用Promise回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTest-run(): Promise<void>--><!--Device-PerfTest-run(): Promise<void>-End-->

**System capability:** SystemCapability.Test.PerfTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32400007 | The API does not support concurrent calls. |
| 32400004 | Failed to execute the callback. Possible causes: 1. An exception is thrown in the callback. 2. Callback execution timed out. |
| 32400005 | Failed to collect metric data. |
| 32400002 | Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist. |

## Examples

```TypeScript
import { PerfMetric, PerfTest, PerfTestStrategy } from '@kit.TestKit';

async function demo() {
  let metrics: Array<PerfMetric> = [PerfMetric.DURATION];
  let num = 0;
  let actionCode = async (finish: Callback<boolean>) => {
    for (let index = 0; index < 10000; index++) {
      num++;
    }
    finish(true); // Call the finish callback to notify that the code segment is executed successfully and as expected.
  };
  let perfTestStrategy: PerfTestStrategy = {
    metrics: metrics,
    actionCode: actionCode
  };
  let perfTest: PerfTest = PerfTest.create(perfTestStrategy); // Construct a PerfTest object and create a test task.
  await perfTest.run(); // Run the performance test.
}
```

