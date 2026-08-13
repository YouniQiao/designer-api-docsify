# listAliases

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## listAliases

```TypeScript
function listAliases(options: HuksOptions): Promise<HuksListAliasesReturnResult>
```

Lists key aliases. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function listAliases(options: HuksOptions): Promise<HuksListAliasesReturnResult>--><!--Device-huks-function listAliases(options: HuksOptions): Promise<HuksListAliasesReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksListAliasesReturnResult](arkts-universalkeystore-huks-hukslistaliasesreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit'

async function testListAliases() {
  let queryProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
    }
  ];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  try{
    await huks.listAliases(queryOptions)
      .then((data) => {
      console.info(`promise: listAliases success, data: ` + JSON.stringify(data));
    });
  } catch (error) {
    console.error(`promise: listAliases failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
}
```
