# updateSession

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## updateSession

```TypeScript
function updateSession(handle: long, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

Updates the key operation. This API uses an asynchronous callback to return the result.

The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function updateSession(handle: long, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void--><!--Device-huks-function updateSession(handle: long, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | long | Yes | Handle of the **updateSession** operation, which is of the uint64 type. |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Parameter set used for the **updateSession** operation. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12000023](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000023-unauthenticated-ukey-pin) | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000021](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000021-ukey-pin-locked) | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| [12000020](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-dependent-module-error) | the provider operation failed<br>**Applicable version:** 22 and later |
| [12000018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| [12000026](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| [12000024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-device-or-resource-busy) | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| [12000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [12000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine or UKey driver |
| [12000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |


## updateSession

```TypeScript
function updateSession(
    handle: long,
    options: HuksOptions,
    token: Uint8Array,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Updates the key operation by segment. The **updateSession** operation is used for user identity authentication and access control. This API uses an asynchronous callback to return the result.

The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function updateSession(    handle: long,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function updateSession(    handle: long,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | long | Yes | Handle of the **updateSession** operation, which is of the uint64 type. |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Parameter set used for the **updateSession** operation. |
| token | Uint8Array | Yes | Authentication token for [refined key access control](../../../security/UniversalKeystoreKit/huks-identity-authentication-overview.md#refined-key-access-control) . |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| [12000026](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| [12000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [12000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine |
| [12000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |


## updateSession

```TypeScript
function updateSession(handle: long, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>
```

Updates the key operation. This API uses a promise to return the result.

The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function updateSession(handle: long, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function updateSession(handle: long, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | long | Yes | Handle of the **updateSession** operation, which is of the uint64 type. |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Parameter set used for the **updateSession** operation. |
| token | Uint8Array | No | Authentication token for [refined key access control](../../../security/UniversalKeystoreKit/huks-identity-authentication-overview.md#refined-key-access-control) . If this parameter is left blank, refined key access control is not performed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Promise that returns the operation result. If the operation is successful and the AES, DES, 3DES, or SM4 key is used for encryption or decryption, **outData** in **HuksReturnResult** returns the ciphertext or decrypted plaintext. Otherwise, **outData** is empty. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12000023](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000023-unauthenticated-ukey-pin) | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000021](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000021-ukey-pin-locked) | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| [12000020](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-dependent-module-error) | the provider operation failed<br>**Applicable version:** 22 and later |
| [12000018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| [12000026](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| [12000024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-device-or-resource-busy) | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| [12000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [12000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine or UKey driver |
| [12000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |

