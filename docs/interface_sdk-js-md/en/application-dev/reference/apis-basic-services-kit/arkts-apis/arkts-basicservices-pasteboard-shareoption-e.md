# ShareOption

```TypeScript
enum ShareOption
```

Enumerates the pasteable ranges of pasteboard data.

**Since:** 9

<!--Device-pasteboard-enum ShareOption--><!--Device-pasteboard-enum ShareOption-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## INAPP

```TypeScript
INAPP = 0
```

Only intra-application pasting is allowed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShareOption-INAPP = 0--><!--Device-ShareOption-INAPP = 0-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## LOCALDEVICE

```TypeScript
LOCALDEVICE = 1
```

Indicates that paste is allowed within any application. <!--RP1--><!--RP1End-->

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShareOption-LOCALDEVICE = 1--><!--Device-ShareOption-LOCALDEVICE = 1-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## CROSSDEVICE

```TypeScript
CROSSDEVICE = 2
```

Indicates that pasting is allowed within any application. Discarded in API version 12 and later versions. There is no substitute interface or alternative method. <!--RP2--><!--RP2End-->

**Since:** 9

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShareOption-CROSSDEVICE = 2--><!--Device-ShareOption-CROSSDEVICE = 2-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
