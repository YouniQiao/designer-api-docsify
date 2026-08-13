# PrinterInfoQueryCallback (System API)

```TypeScript
type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void
```

Defines the callback type used in registering to listen for printerInfoQuery event. The value of printerInfo indicates the printer info. The value of ppdInfo indicates all the printer ppd info.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void--><!--Device-print-type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerInfo | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Yes |
| ppdInfo | [PpdInfo](arkts-basicservices-print-ppdinfo-i.md)[] | Yes |
