# finishSession

## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

Finishes the key operation. This API uses an asynchronous callback to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle of the **finishSession** operation, which is of the uint64 type. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameter set used for the **finishSession** operation. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;HuksReturnResult&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000004](../errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) | The key with the same alias already exists\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 20 and later |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) | the provider operation failed\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) | the UKey PIN is locked\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) | the UKey PIN not authenticated\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) | the provider or UKey is busy\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 26.0.0 and later |


## finishSession

```TypeScript
function finishSession(
    handle: number,
    options: HuksOptions,
    token: Uint8Array,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Finishes the key operation by segment. The **finishSession** operation is used for user identity authentication and access control. This API uses an asynchronous callback to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle of the **finishSession** operation, which is of the uint64 type. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameter set used for the **finishSession** operation. |
| token | Uint8Array | Yes | Authentication token for \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;HuksReturnResult&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000004](../errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) | The key with the same alias already exists\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 20 and later |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 26.0.0 and later |


## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>
```

Finishes the key operation. This API uses a promise to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle of the **finishSession** operation, which is of the uint64 type. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameter set used for the **finishSession** operation. |
| token | Uint8Array | No | Authentication token for \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. If this parameter is left blank, refined key access control is not performed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | Promise that returns the operation result. If the operation is successful, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) | algorithm mode is not supported |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) | algorithm param is missing |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) | algorithm param is invalid |
| [12000004](../errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) | error occurred in crypto engine |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) | this credential is already invalidated permanently |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) | verify auth token failed |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) | auth token is already timeout |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) | The key with the same alias already exists\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 20 and later |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) | the provider operation failed\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) | the UKey PIN is locked\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) | the UKey PIN not authenticated\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) | the provider or UKey is busy\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 22 and later |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the group id specified by the access group tag is invalid\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 26.0.0 and later |

