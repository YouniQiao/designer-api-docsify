# anonAttestKeyItemOffline

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## anonAttestKeyItemOffline

```TypeScript
function anonAttestKeyItemOffline(keyAlias: string, params: HuksParam[]): Promise<HuksReturnResult>
```

Obtains an anonymous key certificate in offline mode. This API uses a promise to return the result. > **NOTE：**> > > - Offline key attestation depends on the network. You need to periodically connect to the network to use this API > to update the offline certificate. Offline anonymous key attestation is recommended. > > > - Offline anonymous key attestation requires that the local time be accurate. Otherwise, the peer end may fail to > verify the certificate expiration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function anonAttestKeyItemOffline(keyAlias: string, params: HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function anonAttestKeyItemOffline(keyAlias: string, params: HuksParam[]): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | Alias of the key. The certificate to be obtained stores the key. |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | Yes | Parameters and data required for obtaining the certificate. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Promise that returns the operation result. When the call is successful, the **certChains** member of **HuksReturnResult** is the obtained certificate chain. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | The API is not supported. |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) | The encryption engine is faulty. |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | The IPC communication failed. |
| [12000004](../errorcode-huks.md#12000004-file-error) | The file operation failed. |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | The parameter is incorrect. Possible causes: 1. A mandatory parameter is left empty. 2. The parameter type is incorrect. 3. The parameter verification failed. 4. The group ID specified by the access group tag is invalid. |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) | The algorithm mode is not supported. |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | The memory is insufficient. |
| [12000012](../errorcode-huks.md#12000012-external-error) | The device environment or input parameter is abnormal. |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | The queried entity does not exist. |
| 12000027 | The network is unavailable. Check network connections. |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) | The operation times out. This may be caused by network jitter. You can try again later. |

