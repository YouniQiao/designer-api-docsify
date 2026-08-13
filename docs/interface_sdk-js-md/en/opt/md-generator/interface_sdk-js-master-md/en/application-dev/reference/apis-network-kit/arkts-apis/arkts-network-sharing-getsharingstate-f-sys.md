# getSharingState (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## getSharingState

```TypeScript
function getSharingState(type: SharingIfaceType, callback: AsyncCallback<SharingIfaceState>): void
```

Obtains the network sharing state for given type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingState(type: SharingIfaceType, callback: AsyncCallback<SharingIfaceState>): void--><!--Device-sharing-function getSharingState(type: SharingIfaceType, callback: AsyncCallback<SharingIfaceState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing.getSharingState(SHARING_WIFI, (error: BusinessError, data: sharing.SharingIfaceState) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## getSharingState

```TypeScript
function getSharingState(type: SharingIfaceType): Promise<SharingIfaceState>
```

Obtains the network sharing state for given type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingState(type: SharingIfaceType): Promise<SharingIfaceState>--><!--Device-sharing-function getSharingState(type: SharingIfaceType): Promise<SharingIfaceState>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing
  .getSharingState(SHARING_WIFI)
  .then((data: sharing.SharingIfaceState) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```
