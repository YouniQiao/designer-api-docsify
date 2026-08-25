# generateKeyItem

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## generateKeyItem

```TypeScript
function generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void
```

Generates a key. This API uses an asynchronous callback to return the result.Based on the principle that the key cannot be transferred out of [Trusted Execution Environment (TEE)](../../../security/UniversalKeystoreKit/huks-concepts.md#tee), the key material content is not returned through this API and is only used to indicate whether the call is successful.

> **NOTE：**&gt;
> Generating SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)
> requires the ohos.permission.ACCESS_SE_KEY permission.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000013](../errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000015](../errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |


## generateKeyItem

```TypeScript
function generateKeyItem(keyAlias: string, options: HuksOptions): Promise<void>
```

Generates a key. This API uses a promise to return the result.

> **NOTE：**&gt;
> Generating SE security level keys defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)
> requires the ohos.permission.ACCESS_SE_KEY permission.
Based on the principle that the key cannot be transferred out of [Trusted Execution Environment (TEE)](../../../security/UniversalKeystoreKit/huks-concepts.md#tee), the key material content is not returned through this API and is only used to indicate whether the call is successful.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000013](../errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000015](../errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
