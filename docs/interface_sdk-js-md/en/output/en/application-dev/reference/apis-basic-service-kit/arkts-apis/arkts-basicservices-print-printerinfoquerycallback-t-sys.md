# PrinterInfoQueryCallback (System API)

```TypeScript
type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void
```

Defines the callback type used in registering to listen for printerInfoQuery event. The value of printerInfo indicates the printer info. The value of ppdInfo indicates all the printer ppd info.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void--><!--Device-print-type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the printer info \_\_\_HTML\_TAG\_USD\_0\_\_\_Printer Information.  |
| ppdInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | all the printer ppd info \_\_\_HTML\_TAG\_USD\_0\_\_\_All the printer ppd info.  |

