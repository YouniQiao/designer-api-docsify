# @ohos.test.PerfTest

PerfTest provides white-box performance testing capabilities.
 It can test performance data of specified code segments or scenarios, automatically execute test code segments,
 and collect performance data such as time consumption, CPU, memory, latency, and frame rate.
 > **NOTE**
 > - The initial APIs of this module are supported since API version 20.
 Newly added APIs will be marked with a superscript to indicate their earliest API version.
 > - The APIs of this module can be used only in <!--RP1-->[JsUnit](../../application-test/unittest-guidelines.md)<!--RP1End-->.
 > - The APIs of this module do not support concurrent calls.
 > - The APIs of this module are applicable to phones, tablets, PCs/2-in-1 devices, smart TVs, and head units.


## Summary

### Classes

| Name | Description |
| --- | --- |
| [PerfTest](arkts-test-test-perftest-perftest-c.md) | Represents the general entry of the white-box performance test framework.It provides capabilities such as test task creation, test code segment execution, data collection, and measurement result obtaining. |

### Interfaces

| Name | Description |
| --- | --- |
| [PerfMeasureResult](arkts-test-test-perftest-perfmeasureresult-i.md) | Represents the measurement result data corresponding to the performance metric. |
| [PerfTestStrategy](arkts-test-test-perftest-perfteststrategy-i.md) | Represents the performance test strategy. |

### Enums

| Name | Description |
| --- | --- |
| [PerfMetric](arkts-test-test-perftest-perfmetric-e.md) | Represents performance metrics that can be collected by the framework. |

