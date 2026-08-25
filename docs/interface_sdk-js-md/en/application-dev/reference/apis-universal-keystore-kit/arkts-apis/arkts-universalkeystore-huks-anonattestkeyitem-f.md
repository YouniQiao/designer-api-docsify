# anonAttestKeyItem

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## anonAttestKeyItem

```TypeScript
function anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

Attests an anonymous key. This API uses an asynchronous callback to return the result.This operation requires Internet access and takes time. If error code 12000012 is returned, the network is abnormal. If the device is not connected to the network, display a message, indicating that the network is not connected. If the network is connected, the failure may be caused by network jitter. Try again later.

> **NOTE：**&gt;
> Attesting SE security level keys that defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)
> requires the ohos.permission.ACCESS_SE_KEY permission.
<!--RP1--><!--RP1End-->

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |


## anonAttestKeyItem

```TypeScript
function anonAttestKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>
```

Attests an anonymous key. This API uses a promise to return the result.This operation requires Internet access and takes time. If error code 12000012 is returned, the network is abnormal. If the device is not connected to the network, display a message, indicating that the network is not connected. If the network is connected, the failure may be caused by network jitter. Try again later.

> **NOTE：**&gt;
> Attesting SE security level keys that defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)
> requires the ohos.permission.ACCESS_SE_KEY permission.
<!--RP1--><!--RP1End-->

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |
