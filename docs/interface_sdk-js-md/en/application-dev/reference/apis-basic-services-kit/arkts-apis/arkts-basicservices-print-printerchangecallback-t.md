# PrinterChangeCallback

```TypeScript
type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void
```

Defines a callback that takes the printer event and printer information as parameters.

**Since:** 18

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PrinterEvent](arkts-basicservices-print-printerevent-e.md) | Yes |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Yes |
