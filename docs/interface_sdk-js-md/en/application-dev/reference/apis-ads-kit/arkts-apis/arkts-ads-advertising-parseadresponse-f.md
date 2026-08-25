# parseAdResponse

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## parseAdResponse

```TypeScript
function parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, 
    context: common.UIAbilityContext): void
```

Parses and processes the body of an ad response (this API is only open to some pre-installed system applications).

**Since:** 12

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adResponse | string | Yes |
| listener | [MultiSlotsAdLoadListener](arkts-ads-advertising-multislotsadloadlistener-i.md) | Yes |
| context | common.UIAbilityContext | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../errorcode-ads.md#801-ad-request-failure) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |
| [21800005](../errorcode-ads.md#21800005-ad-data-parsing-failure) |
