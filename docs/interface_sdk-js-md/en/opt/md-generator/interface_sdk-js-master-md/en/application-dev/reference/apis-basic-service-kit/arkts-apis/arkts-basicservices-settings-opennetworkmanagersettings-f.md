# openNetworkManagerSettings

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openNetworkManagerSettings

```TypeScript
function openNetworkManagerSettings(context: Context): Promise<boolean>
```

Open the network manager settings page.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-settings-function openNetworkManagerSettings(context: Context): Promise<boolean>--><!--Device-settings-function openNetworkManagerSettings(context: Context): Promise<boolean>-End-->

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
| [14800000](../../apis-arkdata/errorcode-data-rdb.md#14800000-internal-error) |
| [14800010](../../apis-arkdata/errorcode-data-rdb.md#14800010-invalid-database-path) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Redirect to the network manager settings page.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.openNetworkManagerSettings(context).then((status) => {
  console.info(`callback:return whether settings is open.`);
});
```
