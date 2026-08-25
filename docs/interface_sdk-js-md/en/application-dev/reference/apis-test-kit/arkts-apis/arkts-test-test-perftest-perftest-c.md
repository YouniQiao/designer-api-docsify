# PerfTest

Represents the general entry of the white-box performance test framework. It provides capabilities such as test task creation, test code segment execution, data collection, and measurement result obtaining.

**Since:** 20

**System capability:** SystemCapability.Test.PerfTest

## Modules to Import

```TypeScript
import {PerfMetric, PerfTestStrategy, PerfMeasureResult, PerfTest} from 'kits/@kit.TestKit';
```

## create

```TypeScript
static create(strategy: PerfTestStrategy): PerfTest
```

Creates a [PerfTest](#perftest) object and returns the object created. This API is a static API.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.PerfTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [PerfTestStrategy](arkts-test-test-perftest-perfteststrategy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PerfTest](arkts-test-test-perftest-perftest-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [32400001](../errorcode-perftest.md#32400001-initialization-failed) |
| [32400002](../errorcode-perftest.md#32400002-internal-error) |
| [32400003](../errorcode-perftest.md#32400003-parameter-verification-failed) |
| [32400007](../errorcode-perftest.md#32400007-api-does-not-support-concurrent-calls) |

## destroy

```TypeScript
destroy(): void
```

Destroys the **PerfTest** object to release the resources occupied by the object. This method is used together with [create](#create) and is called after the **PerfTest** object is used. If this method is not called, resources may fail to be released. The **PerfTest** object should not be used after this API is called.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.PerfTest

**Error codes:**

| Error Code ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-internal-error) |
| [32400007](../errorcode-perftest.md#32400007-api-does-not-support-concurrent-calls) |

## getMeasureResult

```TypeScript
getMeasureResult(metric: PerfMetric): PerfMeasureResult
```

Obtains the measurement data of a specified performance metric. This method must be called after [run](#run) is executed. Otherwise, valid measurement data cannot be obtained.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.PerfTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [metric](arkts-test-test-perftest-perfmeasureresult-i.md) | [PerfMetric](arkts-test-test-perftest-perfmetric-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PerfMeasureResult](arkts-test-test-perftest-perfmeasureresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-internal-error) |
| [32400003](../errorcode-perftest.md#32400003-parameter-verification-failed) |
| [32400006](../errorcode-perftest.md#32400006-failed-to-obtain-performance-data) |
| [32400007](../errorcode-perftest.md#32400007-api-does-not-support-concurrent-calls) |

## run

```TypeScript
run(): Promise<void>
```

Runs a performance test, iteratively executes test code segments based on the configured times, and collects performance data. This API uses a promise to return the result. In each iteration, the framework executes **actionCode** and **resetCode** (if configured) in sequence and collects performance data during the execution of **actionCode**. After the execution is complete, you can call [getMeasureResult](#getmeasureresult) to obtain the collected measurement result data.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.PerfTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [32400002](../errorcode-perftest.md#32400002-internal-error) |
| [32400004](../errorcode-perftest.md#32400004-failed-to-execute-the-callback) |
| [32400005](../errorcode-perftest.md#32400005-failed-to-collect-performance-data) |
| [32400007](../errorcode-perftest.md#32400007-api-does-not-support-concurrent-calls) |
