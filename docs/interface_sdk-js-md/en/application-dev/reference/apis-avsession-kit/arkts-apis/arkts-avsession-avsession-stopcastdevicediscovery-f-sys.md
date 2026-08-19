# stopCastDeviceDiscovery (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## stopCastDeviceDiscovery

```TypeScript
function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void
```

Stop device discovery.

**Since:** 23

<!--Device-avSession-function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void--><!--Device-avSession-function stopCastDeviceDiscovery(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | a callback function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.stopCastDeviceDiscovery((err: BusinessError) => {
  if (err) {
    console.error(`stopCastDeviceDiscovery BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('stopCastDeviceDiscovery successfully');
  }
});
```


## stopCastDeviceDiscovery

```TypeScript
function stopCastDeviceDiscovery(): Promise<void>
```

Stop device discovery.

**Since:** 23

<!--Device-avSession-function stopCastDeviceDiscovery(): Promise<void>--><!--Device-avSession-function stopCastDeviceDiscovery(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.stopCastDeviceDiscovery().then(() => {
  console.info('stopCastDeviceDiscovery successfully');
}).catch((err: BusinessError) => {
  console.error(`stopCastDeviceDiscovery BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

