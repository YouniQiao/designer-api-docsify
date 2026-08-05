# WatermarkCallback

```TypeScript
type WatermarkCallback = (jobId: string, fd: int) => void
```

Defines the callback type used in registering to listen for watermark handling. The value of jobId indicates the print job ID. The value of fd indicates the fd.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-type WatermarkCallback = (jobId: string, fd: int) => void--><!--Device-print-type WatermarkCallback = (jobId: string, fd: int) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | the print job ID \_\_\_HTML\_TAG\_USD\_0\_\_\_Print job ID in preview.  |
| fd | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | File Descriptor \_\_\_HTML\_TAG\_USD\_0\_\_\_File descriptor in preview.  |

