# startCasting (System API)

## startCasting

```TypeScript
function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void
```

Cast resource to remote device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void--><!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Specifies the sessionId which is to be casted. |
| device | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Specifies the device to cast. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | A callback instance used to return when start casting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception |
| [6600108](../errorcode-avsession.md#6600108-device-connection-failure) | Device connecting failed |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
let castDevice: avSession.OutputDeviceInfo | undefined = undefined;
avSession.on('deviceAvailable', (device: avSession.OutputDeviceInfo) => {
  castDevice = device;
  console.info(`on deviceAvailable  : ${device} `);
  if (castDevice !== undefined) {
    avSession.startCasting(myToken, castDevice, (err: BusinessError) => {
      if (err) {
        console.error(`startCasting BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('startCasting successfully');
      }
    });
  }
});
```


## startCasting

```TypeScript
function startCasting(session: SessionToken, device: OutputDeviceInfo): Promise<void>
```

Cast resource to remote device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo): Promise<void>--><!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Specifies the sessionId which is to be casted. |
| device | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Specifies the device to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception |
| [6600108](../errorcode-avsession.md#6600108-device-connection-failure) | Device connecting failed |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
let castDevice: avSession.OutputDeviceInfo | undefined = undefined;
avSession.on('deviceAvailable', (device: avSession.OutputDeviceInfo) => {
  castDevice = device;
  console.info(`on deviceAvailable  : ${device} `);
  if (castDevice !== undefined) {
    avSession.startCasting(myToken, castDevice).then(() => {
      console.info('startCasting successfully');
    }).catch((err: BusinessError) => {
      console.error(`startCasting BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

