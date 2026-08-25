# isSupported

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## isSupported

```TypeScript
function isSupported(feature: number): boolean
```

Checks whether a certain type of card emulation is supported.

> **NOTE：**&gt;
> This API is supported since API version 6 and deprecated since API version 9. Use
> [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md) instead.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md)

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
