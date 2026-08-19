# @ohos.test.PerfTest

## Modules to Import

```TypeScript
import {PerfMetric, PerfTestStrategy, PerfMeasureResult, PerfTest} from '@kit.TestKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [PerfTest](arkts-test-test-perftest-perftest-c.md) | Represents the general entry of the white-box performance test framework. It provides capabilities such as test task creation, test code segment execution, data collection, and measurement result obtaining. |

### Interfaces

| Name | Description |
| --- | --- |
| [PerfMeasureResult](arkts-test-test-perftest-perfmeasureresult-i.md) | Represents the measurement result data corresponding to the performance metric. |
| [PerfTestStrategy](arkts-test-test-perftest-perfteststrategy-i.md) | Represents the performance test strategy. &gt; **NOTE：**&gt; &gt; The input parameter type of the **actionCode** and **resetCode** attributes is **Callback\&lt;boolean&gt;**. You need to call &gt; this callback in the code segment to notify the framework that the code segment execution is complete. Otherwise, the &gt; code segment execution times out. The callback parameter is of the **Boolean** type. The value **true** indicates that &gt; the code segment execution meets the expectation, and **false** indicates the opposite. |

### Enums

| Name | Description |
| --- | --- |
| [PerfMetric](arkts-test-test-perftest-perfmetric-e.md) | APP_START_COMPLETE_TIME**): &gt; - Application startup latency data is subject to the system logging and reporting and may be different from &gt; what end users perceive. The start time is when the tap event is reported, the end time of the response &gt; latency is when the first frame is displayed on the screen after the tap, and the end time of the &gt; completion latency is when the first frame is displayed on the screen after the application is started. &gt; - Application startup latency data can be collected in the following scenarios: tapping an application icon &gt; on the home screen, tapping an application icon on the dock bar, and tapping an application icon in the &gt; application center. &gt; - During a test, only the first startup latency of the specified application is collected. &gt; 4. Description of collecting the page switching latency data (**PAGE_SWITCH_COMPLETE_TIME**): &gt; - Page switching latency calculation is subject to the system logging and reporting and may be different &gt; from what end users perceive. The start time is when the tap event is reported, and the end time is &gt; when the first frame is displayed on the screen after the page switching. &gt; - Page switching latency data can be collected in the **Router** and **Navigation** components. &gt; - During a test, only the first page switching latency in the specified application is collected. &gt; 5. Description of collecting the list scrolling frame rate (**LIST_SWIPE_FPS**): &gt; - **LIST_SWIPE_FPS**: The number of frames rendered and updated on the screen per second when the list is scrolled. &gt; - Supported scenarios: list scrolling of the **List**, **Grid**, **Scroll**, and **WaterFlow** components in the ArkUI subsystem. &gt; - During a test, only the first list scrolling frame rate in the specified application is collected. |

