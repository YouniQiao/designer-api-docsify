# enableSilentProxy (System API)

## Modules to Import

```TypeScript
import { dataShare } from '@kit.ArkData';
```

## enableSilentProxy

```TypeScript
function enableSilentProxy(context: Context, uri?: string): Promise<void>
```

Enables silent access. This API uses a promise to return the result. Observe the following when using this API: - The data provider calls this API to enable silent access. - Whether silent access is enabled is determined based on the return value of this API and the **isSilentProxyEnable** field in the [data_share_config.json](../../../database/share-data-by-datashareextensionability-sys.md) file together. - If silent access is enabled for a URI using this API, the setting takes effect when the related **datashareHelper** API is called. Otherwise, the setting of **isSilentProxyEnable** in the **data_share_config.json** file is used to determine whether to enable silent access.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function enableSilentProxy(context: Context, uri?: string): Promise<void>--><!--Device-dataShare-function enableSilentProxy(context: Context, uri?: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let uri = "datashare:///com.acts.datasharetest/entry/DB00/TBL00?Proxy=true";
    let context = this.context;
    dataShare.enableSilentProxy(context, uri).then(() => {
      console.info("enableSilentProxy succeed");
    }).catch((err: BusinessError) => {
      console.error(`Failed to enable silent proxy. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
