# getISOCountryCodeForNetworkSync

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getISOCountryCodeForNetworkSync

```TypeScript
function getISOCountryCodeForNetworkSync(slotId: number): string
```

Obtains the ISO-defined country code of the country where the registered network is deployed.

**Since:** 10

<!--Device-radio-function getISOCountryCodeForNetworkSync(slotId: int): string--><!--Device-radio-function getISOCountryCodeForNetworkSync(slotId: int): string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let slotId: number = 0;
let countryISO: string = radio.getISOCountryCodeForNetworkSync(slotId);
console.info(`the country ISO is:` + countryISO);
```
