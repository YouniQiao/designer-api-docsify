# removeCandidateConfig

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## removeCandidateConfig

```TypeScript
function removeCandidateConfig(networkId: int): Promise<void>
```

Remove a specified candidate hotspot configuration, only the configuration which is added by ourself is allowed to be removed.The app must be in the foreground.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-wifiManager-function removeCandidateConfig(networkId: int): Promise<void>--><!--Device-wifiManager-function removeCandidateConfig(networkId: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Network ID which will be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Return results. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```


## removeCandidateConfig

```TypeScript
function removeCandidateConfig(networkId: int, callback: AsyncCallback<void>): void
```

Remove a specified candidate hotspot configuration, only the configuration which is added by ourself is allowed to be removed.The app must be in the foreground.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-wifiManager-function removeCandidateConfig(networkId: int, callback: AsyncCallback<void>): void--><!--Device-wifiManager-function removeCandidateConfig(networkId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Network ID which will be removed. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates call back of removeCandidateConfig. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

