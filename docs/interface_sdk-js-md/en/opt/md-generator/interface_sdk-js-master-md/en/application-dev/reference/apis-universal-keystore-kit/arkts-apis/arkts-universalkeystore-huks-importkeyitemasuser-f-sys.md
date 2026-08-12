# importKeyItemAsUser (System API)

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## importKeyItemAsUser

```TypeScript
function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>
```

Imports a plaintext key for the specified user. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>--><!--Device-huks-function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| keyAlias | string | Yes |
| huksOptions | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000017-duplicate-key-alias) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) |
| [12000015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) |
| [12000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) |

## Examples

Prerequisites: see Example of [generateKeyItemAsUser](#huksgeneratekeyitemasuser).

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit"

const aesKeyAlias = 'test_aesKeyAlias';
const userId = 100;
const userIdStorageLevel = huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_CE;
const plainAesKey128 = new Uint8Array([
  0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63, 0x2a, 0x7c, 0x86, 0xba, 0xca
]);

function GetAesGenerateProperties(): Array<huks.HuksParam> {
  return [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
    value: userIdStorageLevel,
  }]
}

async function ImportPlainKey(keyAlias: string, importProperties: Array<huks.HuksParam>, plainKey: Uint8Array) {
  const options: huks.HuksOptions = {
    properties: importProperties,
    inData: plainKey
  }
  await huks.importKeyItemAsUser(userId, keyAlias, options).then((data) => {
    console.info("Imported the key with the alias of: " + keyAlias + ".")
  }).catch((err: BusinessError) => {
    console.error("Failed to import the key. Error code: " + err.code + " Error message: " + err.message)
  })
}

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  ImportPlainKey(aesKeyAlias, GetAesGenerateProperties(), plainAesKey128)
}
```
