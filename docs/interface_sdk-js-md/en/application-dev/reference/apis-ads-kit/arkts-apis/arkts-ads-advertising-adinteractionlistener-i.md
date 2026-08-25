# AdInteractionListener

Defines the ad status change callback.

**Since:** 11

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## onStatusChanged

```TypeScript
onStatusChanged(status: string, ad: Advertisement, data: string)
```

Called when the ad display status changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | string | Yes |
| ad | [Advertisement](arkts-ads-advertisement-advertisement-i.md) | Yes |
| data | string | Yes |
