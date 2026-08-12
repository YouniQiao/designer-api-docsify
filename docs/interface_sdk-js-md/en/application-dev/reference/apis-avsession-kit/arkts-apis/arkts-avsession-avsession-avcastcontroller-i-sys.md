# AVCastController

AVCastController definition used to implement a remote control when a cast is connected

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCastController--><!--Device-avSession-interface AVCastController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void
```

Set a surface instance to display playing view, used at sink side.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void--><!--Device-AVCastController-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | surface id, video player will use this id get a surface instance. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | A callback instance used to return when set surface completed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600109](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600109-remote-session-does-not-exist) | The remote connection is not established |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
let surfaceID: string = '';
media.createAVRecorder().then((avRecorder) => {
  avRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
    if (err == null) {
      console.info('getInputSurface success');
      surfaceID = surfaceId;
      if (surfaceID) {
        aVCastController.setDisplaySurface(surfaceID, (err: BusinessError) => {
          if (err) {
            console.error(`setDisplaySurface BusinessError: code: ${err.code}, message: ${err.message}`);
          } else {
            console.info('setDisplaySurface : SUCCESS');
          }
        });
      }
    } else {
      console.error('getInputSurface failed and error is ' + err.message);
    }
  });
})
```

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string): Promise<void>
```

Set a surface instance to display playing view, used at sink side.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-setDisplaySurface(surfaceId: string): Promise<void>--><!--Device-AVCastController-setDisplaySurface(surfaceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | surface id, video player will use this id get a surface instance. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600109](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600109-remote-session-does-not-exist) | The remote connection is not established |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
import { media } from '@kit.MediaKit';
let surfaceID: string = '';
media.createAVRecorder().then((avRecorder) => {
  avRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
    if (err == null) {
      console.info('getInputSurface success');
      surfaceID = surfaceId;
      if (surfaceID) {
        aVCastController.setDisplaySurface(surfaceID).then(() => {
          console.info('setDisplaySurface : SUCCESS');
        });
      }
    } else {
      console.error('getInputSurface failed and error is ' + err.message);
    }
  });
})
```

