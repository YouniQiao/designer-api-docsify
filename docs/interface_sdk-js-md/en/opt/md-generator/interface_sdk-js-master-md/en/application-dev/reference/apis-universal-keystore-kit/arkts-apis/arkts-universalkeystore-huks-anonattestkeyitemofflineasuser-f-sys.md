# anonAttestKeyItemOfflineAsUser (System API)

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## anonAttestKeyItemOfflineAsUser

```TypeScript
function anonAttestKeyItemOfflineAsUser(userId: number, keyAlias: string,
      params: HuksParam[]): Promise<HuksReturnResult>
```

Obtains an anonymous key certificate in offline mode for a specified user. This API uses a promise to return the result.

> **NOTE：**
> 
> - Offline key attestation depends on the network. You need to periodically connect to the network to use this API
> to update the offline certificate.
> 
> - Offline anonymous key attestation requires that the local time be accurate. Otherwise, the peer end may fail to
> verify the certificate expiration.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-huks-function anonAttestKeyItemOfflineAsUser(userId: number, keyAlias: string,      params: HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function anonAttestKeyItemOfflineAsUser(userId: number, keyAlias: string,      params: HuksParam[]): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| keyAlias | string | Yes |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HuksReturnResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 12000027 |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |

## Examples

Prerequisites: see Example of [generateKeyItemAsUser](#huksgeneratekeyitemasuser).

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit"

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const userId = 100;
const userIdStorageLevel = huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_CE;
const keyAliasString = "key anon local attest as user";

const challenge = StringToUint8Array('challenge_data');

async function generateKey(alias: string) {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: userIdStorageLevel,
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };

  await huks.generateKeyItemAsUser(userId, alias, options);
}

async function anonAttestKeyItemOfflineAsUser() {
  let aliasString = keyAliasString;
  let aliasUint8 = StringToUint8Array(aliasString);
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    },
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: userIdStorageLevel,
    }
  ];

  await generateKey(aliasString);
  await huks.anonAttestKeyItemOfflineAsUser(userId, aliasString, properties).then((data) => {
    console.info('anonAttestationOffline ok!')
    console.debug(`'CERT:${JSON.stringify(data)}`)
    for (let i = 0; data?.certChains?.length && i < data?.certChains?.length; ++i) {
      console.info(`CERT${i} is ${data.certChains[i]}`)
    }
    console.info("anonAttestationOffline Success")
  }).catch((err: BusinessError) => {
    console.error("anonAttestationOffline fail, erroCode: " + err.code + " erroInfo: " + err.message)
  })
}
```
