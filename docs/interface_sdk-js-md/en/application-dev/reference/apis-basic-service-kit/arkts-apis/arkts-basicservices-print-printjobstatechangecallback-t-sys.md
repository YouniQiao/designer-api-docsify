# PrintJobStateChangeCallback (System API)

```TypeScript
type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void
```

Defines the callback type used in registering to listen for PrintJobState.The value of state indicates the state of print job.The value of job indicates the latest print job info.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-print-type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void--><!--Device-print-type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the state of print job  |
| job | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the information of the print job  |

