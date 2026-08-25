# getAdRequestBody

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## getAdRequestBody

```TypeScript
function getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>
```

Obtains the body of an ad request. This API uses a promise to return the result (this API is only open to some pre-installed system applications).

**Since:** 12

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adParams | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md)[] | Yes |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../errorcode-ads.md#801-ad-request-failure) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |
