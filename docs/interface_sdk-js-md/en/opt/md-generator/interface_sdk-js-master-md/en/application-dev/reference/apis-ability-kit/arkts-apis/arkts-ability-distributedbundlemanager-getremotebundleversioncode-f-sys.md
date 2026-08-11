# getRemoteBundleVersionCode (System API)

## Modules to Import

```TypeScript
import { distributedBundleManager } from 'kits/@kit.AbilityKit';
```

## getRemoteBundleVersionCode

```TypeScript
function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<number>
```

Obtains the version information of an app with a specified bundle name on a specified remote device.This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedBundleManager-function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<long>--><!--Device-distributedBundleManager-function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17700027](../errorcode-bundle.md#17700027-distributed-service-is-not-started) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700007](../errorcode-bundle.md#17700007-incorrect-device-id) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { distributedBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  distributedBundleManager.getRemoteBundleVersionCode('1111', 'com.hap.myapplication').then((data: number) => {
    console.info(`getRemoteBundleVersionCode succeed:` + data);
  }).catch((err: BusinessError) => {
    console.error(`getRemoteBundleVersionCode failed: error code is ${err.code}  and error msg is ${err.message}`);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`getRemoteBundleVersionCode failed: error code is ${code}  and error msg is ${message}`);
}
```
