# PrintJobStateChangeCallback (System API)

```TypeScript
type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void
```

Defines the callback type used in registering to listen for PrintJobState. The value of state indicates the state of print job. The value of job indicates the latest print job info.

**Since:** 23

**Deprecated since:** -1

<!--Device-print-type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void--><!--Device-print-type PrintJobStateChangeCallback = (state: PrintJobState, job: PrintJob) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [PrintJobState](arkts-basicservices-print-printjobstate-e.md) | Yes |
| job | [PrintJob](arkts-basicservices-print-printjob-i.md) | Yes |
