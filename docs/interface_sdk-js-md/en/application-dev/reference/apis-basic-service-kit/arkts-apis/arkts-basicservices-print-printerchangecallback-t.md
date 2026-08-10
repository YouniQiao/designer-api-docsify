# PrinterChangeCallback

```TypeScript
type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void
```

将打印机事件和打印机信息作为参数的回调方法。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-print-type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void--><!--Device-print-type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PrinterEvent](arkts-basicservices-print-printerevent-e.md) | Yes | 表示打印机事件。 |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Yes | 表示打印机信息。 |

