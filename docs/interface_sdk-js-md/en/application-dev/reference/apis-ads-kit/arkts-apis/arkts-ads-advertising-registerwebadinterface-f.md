# registerWebAdInterface

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## registerWebAdInterface

```TypeScript
function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext): void
```

Injects an ad JavaScript object to the **Web** component (this API is only open to some pre-installed system applications).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controller | web_webview.WebviewController | Yes |
| context | common.UIAbilityContext | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |


## registerWebAdInterface

```TypeScript
function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext, 
    needRefresh: boolean): void
```

Injects an ad JavaScript object to the **Web** component (this API is only open to some pre-installed system applications).

**Since:** 16

**Atomic service API:** This API can be used in atomic services since API version 16.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controller | web_webview.WebviewController | Yes |
| context | common.UIAbilityContext | Yes |
| needRefresh | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |
