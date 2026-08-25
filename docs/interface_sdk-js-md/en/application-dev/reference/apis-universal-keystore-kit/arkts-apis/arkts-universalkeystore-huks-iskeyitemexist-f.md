# isKeyItemExist

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## isKeyItemExist

```TypeScript
function isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>): void
```

Checks whether a key exists. This API uses an asynchronous callback to return the result.If the key does not exist, the error code 12000011 is returned.

**Since:** 9

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |


## isKeyItemExist

```TypeScript
function isKeyItemExist(keyAlias: string, options: HuksOptions): Promise<boolean>
```

Checks whether a key exists. This API uses a promise to return the result.If the key does not exist, the error code 12000011 is returned.

**Since:** 9

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
