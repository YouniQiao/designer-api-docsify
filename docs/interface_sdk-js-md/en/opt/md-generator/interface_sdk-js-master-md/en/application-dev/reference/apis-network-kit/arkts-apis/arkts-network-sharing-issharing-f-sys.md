# isSharing (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## isSharing

```TypeScript
function isSharing(callback: AsyncCallback<boolean>): void
```

Return the global network sharing state.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function isSharing(callback: AsyncCallback<boolean>): void--><!--Device-sharing-function isSharing(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2200003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2202011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-sharing.md#2202011-failed-to-obtain-the-network-sharing-configuration) |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing.isSharing((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## isSharing

```TypeScript
function isSharing(): Promise<boolean>
```

Return the global network sharing state.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function isSharing(): Promise<boolean>--><!--Device-sharing-function isSharing(): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2202011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-sharing.md#2202011-failed-to-obtain-the-network-sharing-configuration) |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing
  .isSharing()
  .then((data: boolean) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```
