# createAVPlayer

## createAVPlayer

```TypeScript
function createAVPlayer(callback: AsyncCallback<AVPlayer>): void
```

Creates an AVPlayer instance. This API uses an asynchronous callback to return the result. > **NOTE** > > - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video > playback scenarios.\_\_\_MD\_COMMENT\_DESC\_USD\_0\_\_\_ > > - The actual number of instances that can be created may be different. It depends on the specifications of the > device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer > instances for an application in audio and video playback scenarios.\_\_\_MD\_COMMENT\_DESC\_USD\_1\_\_\_ > > - Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing > them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the > system might terminate applications to free up resources.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-media-function createAVPlayer(callback: AsyncCallback<AVPlayer>): void--><!--Device-media-function createAVPlayer(callback: AsyncCallback<AVPlayer>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AVPlayer&gt; | Yes | Callback used to return the result. If the operation is successful,an AVPlayer instance is returned; otherwise, **null** is returned. The instance can be used to play audio and video. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by callback. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer((error: BusinessError, video: media.AVPlayer) => {
  if (video) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error(`Failed to create AVPlayer, error message:${error.message}`);
  }
});
```


## createAVPlayer

```TypeScript
function createAVPlayer(callback: AsyncCallback<AVPlayer | undefined>): void
```

Creates an **AVPlayer** instance. This API uses an asynchronous callback to return the result. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE:**\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ You are advised to create a maximum of 16 **AVPlayer** instances for an application in both audio and video playback scenarios. The actual number of instances that can be created may be different. It depends on the specifications of the device chip in use.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVPlayer(callback: AsyncCallback<AVPlayer | undefined>): void--><!--Device-media-function createAVPlayer(callback: AsyncCallback<AVPlayer | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AVPlayer \| undefined&gt; | Yes | used to return the result. If the operation is successful, an **AVPlayer** instance is returned; otherwise, **undefined** is returned. The instance can be used to play audio and video. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by callback. |


## createAVPlayer

```TypeScript
function createAVPlayer(): Promise<AVPlayer>
```

Creates an AVPlayer instance. This API uses a promise to return the result. > **NOTE** > > - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video > playback scenarios.\_\_\_MD\_COMMENT\_DESC\_USD\_0\_\_\_ > > - The actual number of instances that can be created may be different. It depends on the specifications of the > device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer > instances for an application in audio and video playback scenarios.\_\_\_MD\_COMMENT\_DESC\_USD\_1\_\_\_ > > - Applications should reasonably use AVPlayer objects in accordance with actual service requirements, create them > on demand, and release them in a timely manner. This avoids excessive memory consumption caused by holding too > many AVPlayer instances, which may result in the system terminating the application.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-media-function createAVPlayer(): Promise<AVPlayer>--><!--Device-media-function createAVPlayer(): Promise<AVPlayer>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVPlayer&gt; | Promise used to return the result. If the operation is successful, an AVPlayer |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by promise. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer().then((video: media.AVPlayer) => {
  if (video) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error('Failed to create AVPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVPlayer, error message:${error.message}`);
});
```


## createAVPlayer

```TypeScript
function createAVPlayer(): Promise<AVPlayer | undefined>
```

Creates an **AVPlayer** instance. This API uses a promise to return the result. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE:**\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ You are advised to create a maximum of 16 **AVPlayer** instances for an application in both audio and video playback scenarios. The actual number of instances that can be created may be different. It depends on the specifications of the device chip in use.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVPlayer(): Promise<AVPlayer | undefined>--><!--Device-media-function createAVPlayer(): Promise<AVPlayer | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVPlayer \| undefined&gt; | A Promise instance used to return the result. If the operation is |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by promise. |

