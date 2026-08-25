# openNetworkManagerSettings

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## openNetworkManagerSettings

```TypeScript
function openNetworkManagerSettings(context: Context): Promise<boolean>
```

Open the network manager settings page.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-settings.md#14800000-parameter-check-failed) |
| [14800010](../errorcode-settings.md#14800010-uiability-required) |
