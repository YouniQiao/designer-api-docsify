# PrinterStateChangeCallback (System API)

```TypeScript
type PrinterStateChangeCallback = (state: PrinterState, info: PrinterInfo) => void
```

Defines the callback type used in registering to listen for PrinterState. The value of state indicates the state of printer. The value of info indicates the latest printer info.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-print-type PrinterStateChangeCallback = (state: PrinterState, info: PrinterInfo) => void--><!--Device-print-type PrinterStateChangeCallback = (state: PrinterState, info: PrinterInfo) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the state of printer  |
| info | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the information of the latest printer  |

