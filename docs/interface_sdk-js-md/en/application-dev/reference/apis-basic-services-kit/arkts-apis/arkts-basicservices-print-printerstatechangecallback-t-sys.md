# PrinterStateChangeCallback (System API)

```TypeScript
type PrinterStateChangeCallback = (state: PrinterState, info: PrinterInfo) => void
```

Defines the callback type used in registering to listen for PrinterState. The value of state indicates the state of printer. The value of info indicates the latest printer info.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [PrinterState](arkts-basicservices-print-printerstate-e.md) | Yes |
| info | [PrinterInfo](arkts-basicservices-print-printerinfo-i.md) | Yes |
