# generateKeyItem

## Modules to Import

```TypeScript
```

## generateKeyItem

```TypeScript
function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void
```

Generates a key. This API uses an asynchronous callback to return the result. Based on the principle that the key cannot be transferred out of [Trusted Execution Environment (TEE)](../../../security/UniversalKeystoreKit/huks-concepts.md#tee), the key material content is not returned through this API and is only used to indicate whether the call is successful. > **NOTE：**> > Generating SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#hukskeysecuritylevel) > requires the ohos.permission.ACCESS_SE_KEY permission.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void--><!--Device-huks-function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000015](../errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000013](../errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |

**Examples**

ArkTS sample code:

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Generate a 256-bit ECC key. */
let keyAlias: string = 'keyAlias';
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
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options, (error) => {
  if (error) {
    console.error(`callback: generateKeyItem failed`);
  } else {
    console.info(`callback: generateKeyItem key success`);
  }
});
```

The JS sample code is used only for the lightweight devices.

```TypeScript
<stack class="container">
    <input type="button" class="generateBtn" @click="generateKey">Generate Key</input>
    <text class="result">{{result}}</text>
</stack>
```

```TypeScript
.container {
  width: 454px;
  height: 800px;
  background-color: #ffffffff;
}

.generateBtn {
  left: 77px;
  top: 100px;
  width: 300px;
  height: 80px;
  text-align: center;
  color: white;
  background-color: orange;
  font-size: 25px;
}

.result {
  left: 30px;
  top: 190px;
  width: 390px;
  height: 80px;
  text-align: center;
  color: #ff000000;
  background-color: #ffffffff;
  font-size: 25px;
}
```

```TypeScript
import huks from '@ohos.security.huks';

function testGenerateKey() {
    let huksInfo;
    let keyAlias = 'keyAlias';
    let properties = [{
        tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
        value: huks.HuksKeyAlg.HUKS_ALG_DES
    }, {
        tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
        value: huks.HuksKeySize.HUKS_DES_KEY_SIZE_64
    }, {
        tag: huks.HuksTag.HUKS_TAG_PURPOSE,
        value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
        huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    }];
    let options = {
        properties: properties
    };

    huks.generateKeyItem(keyAlias, options, (err) => {
        if (err) {
            huksInfo = 'generateKeyItem failed, code: ' + err.code + ', message: ' + err.message;
            console.error(huksInfo);
        } else {
            huksInfo = 'generateKeyItem succeeded';
            console.info(huksInfo);
        }
    });
    return huksInfo;
}

export default {
    data: {
        result: ''
    },

    generateKey() {
        this.result = testGenerateKey();
    }
};
```


## generateKeyItem

```TypeScript
function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>
```

Generates a key. This API uses a promise to return the result. > **NOTE：**> > Generating SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#hukskeysecuritylevel) > requires the ohos.permission.ACCESS_SE_KEY permission. Based on the principle that the key cannot be transferred out of [Trusted Execution Environment (TEE)](../../../security/UniversalKeystoreKit/huks-concepts.md#tee), the key material content is not returned through this API and is only used to indicate whether the call is successful.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>--><!--Device-huks-function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000015](../errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000013](../errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |

**Examples**

```TypeScript
/* Generate a 256-bit ECC key. */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'keyAlias';
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
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options)
  .then((data) => {
    console.info(`promise: generateKeyItem success`);
  });
```
