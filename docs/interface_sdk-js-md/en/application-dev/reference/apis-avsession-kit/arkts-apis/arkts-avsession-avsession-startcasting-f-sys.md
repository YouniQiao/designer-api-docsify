# startCasting (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
import { avSession } from '@kit.AVSessionKit';
```

## startCasting

```TypeScript
function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void
```

Cast resource to remote device.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void--><!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes | Specifies the sessionId which is to be casted. |
| device | [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | Yes | Specifies the device to cast. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | A callback instance used to return when start casting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600108](../errorcode-avsession.md#6600108-device-connection-failure) | Device connecting failed |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

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

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo): Promise<void>--><!--Device-avSession-function startCasting(session: SessionToken, device: OutputDeviceInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes | Specifies the sessionId which is to be casted. |
| device | [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | Yes | Specifies the device to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600108](../errorcode-avsession.md#6600108-device-connection-failure) | Device connecting failed |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

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

