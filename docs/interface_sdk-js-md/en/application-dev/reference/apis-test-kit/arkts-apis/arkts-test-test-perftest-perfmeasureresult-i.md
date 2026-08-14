# PerfMeasureResult

Represents the measurement result data corresponding to the performance metric.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare interface PerfMeasureResult--><!--Device-unnamed-declare interface PerfMeasureResult-End-->

**System capability:** SystemCapability.Test.PerfTest

## Modules to Import

```TypeScript
import { PerfMetric } from 'PerfMetric';
import { PerfTestStrategy } from 'PerfTestStrategy';
import { PerfMeasureResult } from 'PerfMeasureResult';
import { PerfTest } from 'PerfTest';
```

## average

```TypeScript
readonly average: double
```

Average value of the measurement data of each round (the value **-1** is excluded).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PerfMeasureResult-readonly average: double--><!--Device-PerfMeasureResult-readonly average: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## maximum

```TypeScript
readonly maximum: double
```

Maximum value of the measurement data of each round (the value **-1** is excluded).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PerfMeasureResult-readonly maximum: double--><!--Device-PerfMeasureResult-readonly maximum: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## metric

```TypeScript
readonly metric: PerfMetric
```

Performance metric to test.

**Type:** [PerfMetric](arkts-test-test-perftest-perfmetric-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PerfMeasureResult-readonly metric: PerfMetric--><!--Device-PerfMeasureResult-readonly metric: PerfMetric-End-->

**System capability:** SystemCapability.Test.PerfTest

## minimum

```TypeScript
readonly minimum: double
```

Minimum value of the measurement data of each round (the value **-1** is excluded).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PerfMeasureResult-readonly minimum: double--><!--Device-PerfMeasureResult-readonly minimum: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## roundValues

```TypeScript
readonly roundValues: Array<double>
```

Measurement data value of each round of the tested performance metric. The unit is the same as that of the corresponding [PerfMetric](arkts-test-test-perftest-perfmetric-e.md#PerfMetric). If data collection fails, the value **-1** is returned.

**Type:** Array&lt;double&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PerfMeasureResult-readonly roundValues: Array<double>--><!--Device-PerfMeasureResult-readonly roundValues: Array<double>-End-->

**System capability:** SystemCapability.Test.PerfTest

