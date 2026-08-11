# PerfMeasureResult

Represents the measurement result data corresponding to the performance metric.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface PerfMeasureResult--><!--Device-unnamed-declare interface PerfMeasureResult-End-->

**System capability:** SystemCapability.Test.PerfTest

## Modules to Import

```TypeScript
import { PerfTestStrategy, PerfMetric, PerfTest, PerfMeasureResult } from 'kits/@kit.TestKit';
```

## average

```TypeScript
readonly average: double
```

Average value of the measurement data of each round (the value **-1** is excluded).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfMeasureResult-readonly average: double--><!--Device-PerfMeasureResult-readonly average: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## maximum

```TypeScript
readonly maximum: double
```

Maximum value of the measurement data of each round (the value **-1** is excluded).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfMeasureResult-readonly maximum: double--><!--Device-PerfMeasureResult-readonly maximum: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## metric

```TypeScript
readonly metric: PerfMetric
```

Performance metric to test.

**Type:** [PerfMetric](arkts-test-test-perftest-perfmetric-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfMeasureResult-readonly metric: PerfMetric--><!--Device-PerfMeasureResult-readonly metric: PerfMetric-End-->

**System capability:** SystemCapability.Test.PerfTest

## minimum

```TypeScript
readonly minimum: double
```

Minimum value of the measurement data of each round (the value **-1** is excluded).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfMeasureResult-readonly minimum: double--><!--Device-PerfMeasureResult-readonly minimum: double-End-->

**System capability:** SystemCapability.Test.PerfTest

## roundValues

```TypeScript
readonly roundValues: Array<double>
```

Measurement data value of each round of the tested performance metric. The unit is the same as that of the corresponding {@link PerfMetric}. If data collection fails, the value **-1** is returned.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfMeasureResult-readonly roundValues: Array<double>--><!--Device-PerfMeasureResult-readonly roundValues: Array<double>-End-->

**System capability:** SystemCapability.Test.PerfTest

