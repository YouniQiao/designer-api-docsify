# updateSession

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## updateSession

```TypeScript
function updateSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

Updates the key operation. This API uses an asynchronous callback to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function updateSession(handle: long, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void--><!--Device-huks-function updateSession(handle: long, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | number | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) |


## updateSession

```TypeScript
function updateSession(
    handle: number,
    options: HuksOptions,
    token: Uint8Array,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Updates the key operation by segment. The **updateSession** operation is used for user identity authentication and access control. This API uses an asynchronous callback to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function updateSession(    handle: long,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function updateSession(    handle: long,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | number | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| token | Uint8Array | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) |


## updateSession

```TypeScript
function updateSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>
```

Updates the key operation. This API uses a promise to return the result. The **huks.initSession**, **huks.updateSession**, and **huks.finishSession** must be used together.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function updateSession(handle: long, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function updateSession(handle: long, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | number | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| token | Uint8Array | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [12000007](../errorcode-huks.md#12000007-failed-to-access-the-key-due-to-invalidated-credential) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000009](../errorcode-huks.md#12000009-key-access-timed-out) |
| [12000008](../errorcode-huks.md#12000008-failed-to-access-the-key-due-to-a-failure-in-authentication-token-verification) |
