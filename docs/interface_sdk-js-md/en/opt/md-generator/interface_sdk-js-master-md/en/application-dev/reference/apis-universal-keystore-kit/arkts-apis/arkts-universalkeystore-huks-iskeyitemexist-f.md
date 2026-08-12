# isKeyItemExist

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## isKeyItemExist

```TypeScript
function isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>): void
```

Checks whether a key exists. This API uses an asynchronous callback to return the result.

If the key does not exist, the error code 12000011 is returned.

**Since:** 9

<!--Device-huks-function isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>): void--><!--Device-huks-function isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) |

## Examples

ArkTS sample code:

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: isKeyItemExist failed`);
  } else {
    if (data) {
      console.info(`keyAlias:${keyAlias} is existed!`);
    } else {
      console.error(`find key failed`);
    }
  }
});
```

The JS sample code is used only for the lightweight devices.

```TypeScript
<stack class="container">
    <input type="button" class="existBtn" @click="existKey">Query Key</input>
    <text class="result">{{result}}</text>
</stack>
```

```TypeScript
.container {
  width: 454px;
  height: 800px;
  background-color: #ffffffff;
}

.existBtn {
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

function testKeyExist() {
    let huksInfo;
    let keyAlias = 'keyAlias';
    let emptyOptions = {
        properties: []
    };

    huks.isKeyItemExist(keyAlias, emptyOptions, (err, data) => {
        if (err) {
            huksInfo = 'isKeyItemExist failed, code: ' + err.code + ', message: ' + err.message;
            console.error(huksInfo);
        } else {
            if (data) {
                huksInfo = `key: ${keyAlias} exists`;
                console.info(huksInfo);
            } else {
                huksInfo = 'key does not exist';
                console.error(huksInfo);
            }
        }
    });
    return huksInfo;
}

export default {
    data: {
        result: ''
    },

    existKey() {
        this.result = testKeyExist();
    },
};
```


## isKeyItemExist

```TypeScript
function isKeyItemExist(keyAlias: string, options: HuksOptions): Promise<boolean>
```

Checks whether a key exists. This API uses a promise to return the result.

If the key does not exist, the error code 12000011 is returned.

**Since:** 9

<!--Device-huks-function isKeyItemExist(keyAlias: string, options: HuksOptions): Promise<boolean>--><!--Device-huks-function isKeyItemExist(keyAlias: string, options: HuksOptions): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions).then(() => {
  console.info(`keyAlias:${keyAlias} is existed!`);
});
```
