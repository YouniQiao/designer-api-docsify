# ShareOption

Enumerates the pasteable ranges of PasteData.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Pasteboard

## INAPP

```TypeScript
INAPP = 0
```

Only intra-application pasting is allowed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## LOCALDEVICE

```TypeScript
LOCALDEVICE = 1
```

Paste is allowed in any application.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## CROSSDEVICE

```TypeScript
CROSSDEVICE = 2
```

Paste is allowed in any application across devices.This API is deprecated since API version 12 without any alternative API or method.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard
