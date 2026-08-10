# getSharingIfaces (System API)

## Modules to Import

```TypeScript
import { sharing } from 'kits/@kit.NetworkKit';
```

## getSharingIfaces

```TypeScript
function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void
```

Obtains the names of interfaces in each sharing state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void--><!--Device-sharing-function getSharingIfaces(state: SharingIfaceState, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | Yes | Is the network sharing state. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Returns an array of interface names that meet this status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_BLUETOOTH = 2;
sharing.getSharingIfaces(SHARING_BLUETOOTH, (error: BusinessError, data: string[]) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## getSharingIfaces

```TypeScript
function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>
```

Obtains the names of interfaces in each sharing state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>--><!--Device-sharing-function getSharingIfaces(state: SharingIfaceState): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [SharingIfaceState](arkts-network-sharing-sharingifacestate-e-sys.md) | Yes | Is the network sharing state. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let SHARING_BLUETOOTH = 2;
sharing
  .getSharingIfaces(SHARING_BLUETOOTH)
  .then((data: string[]) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

