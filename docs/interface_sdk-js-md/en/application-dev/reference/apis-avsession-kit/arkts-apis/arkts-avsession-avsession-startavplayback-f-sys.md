# startAVPlayback (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## startAVPlayback

```TypeScript
function startAVPlayback(bundleName: string, assetId: string): Promise<void>
```

Start an application for media playback.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string): Promise<void>--><!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Specifies the bundleName which to be started. |
| assetId | string | Yes | Specifies the assetId to be started. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

avSession.startAVPlayback("com.example.myapplication", "121278").then(() => {
  console.info('startAVPlayback : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`startAVPlayback BusinessError: code: ${err.code}, message: ${err.message}`);
});
```


## startAVPlayback

```TypeScript
function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>
```

Start an application for media playback with command info.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>--><!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Specifies the bundleName which to be started. |
| assetId | string | Yes | Specifies the assetId to be started. |
| info | [CommandInfo](arkts-avsession-avsession-commandinfo-i.md) | Yes | Specifies the specified command information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

avSession.startAVPlayback("com.example.myapplication", "121278", "entry").then(() => {
  console.info('startAVPlayback : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`startAVPlayback BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

