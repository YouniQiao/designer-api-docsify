# getKeyItemProperties

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## getKeyItemProperties

```TypeScript
function getKeyItemProperties(
    keyAlias: string,
    options: HuksOptions,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Obtains key properties. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Getting properties of SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)
> requires the ohos.permission.ACCESS_SE_KEY permission.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.Huks.Core
- API version 9 to 11: SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12000026](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-secure-element-fault) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) |
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

huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: getKeyItemProperties failed`);
  } else {
    console.info(`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  }
});
```


## getKeyItemProperties

```TypeScript
function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>
```

Obtains key properties. This API uses a promise to return the result.

> **NOTE：**
> 
> Getting properties of SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)
> requires the ohos.permission.ACCESS_SE_KEY permission.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12000026](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-secure-element-fault) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) |
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

huks.getKeyItemProperties(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  });
```
