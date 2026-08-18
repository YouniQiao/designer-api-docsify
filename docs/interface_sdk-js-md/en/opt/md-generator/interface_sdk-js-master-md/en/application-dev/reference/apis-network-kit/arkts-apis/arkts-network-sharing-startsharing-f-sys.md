# startSharing (System API)

## Modules to Import

```TypeScript
```

## startSharing

```TypeScript
function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void
```

Start network sharing for given type.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void--><!--Device-sharing-function startSharing(type: SharingIfaceType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2202005](../errorcode-net-sharing.md#2202005-wifi-sharing-failure) |
| [2202004](../errorcode-net-sharing.md#2202004-shared-iface-unavailable) |
| [2202006](../errorcode-net-sharing.md#2202006-bluetooth-sharing-failure) |
| [2202009](../errorcode-net-sharing.md#2202009-failed-to-enable-forwarding-for-network-sharing) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2202011](../errorcode-net-sharing.md#2202011-failed-to-obtain-the-network-sharing-configuration) |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing.startSharing(SHARING_WIFI, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## startSharing

```TypeScript
function startSharing(type: SharingIfaceType): Promise<void>
```

Start network sharing for given type.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function startSharing(type: SharingIfaceType): Promise<void>--><!--Device-sharing-function startSharing(type: SharingIfaceType): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SharingIfaceType](arkts-network-sharing-sharingifacetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2202005](../errorcode-net-sharing.md#2202005-wifi-sharing-failure) |
| [2202004](../errorcode-net-sharing.md#2202004-shared-iface-unavailable) |
| [2202006](../errorcode-net-sharing.md#2202006-bluetooth-sharing-failure) |
| [2202009](../errorcode-net-sharing.md#2202009-failed-to-enable-forwarding-for-network-sharing) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2202011](../errorcode-net-sharing.md#2202011-failed-to-obtain-the-network-sharing-configuration) |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_WIFI = 0;
sharing
  .startSharing(SHARING_WIFI)
  .then(() => {
    console.info('start wifi sharing successful');
  })
  .catch((error: BusinessError) => {
    console.error('start wifi sharing failed');
  });
```
