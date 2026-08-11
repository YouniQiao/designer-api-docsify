# pick

## Modules to Import

```TypeScript
import { cameraPicker } from 'kits/@kit.CameraKit';
```

## pick

```TypeScript
function pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>
```

Starts the camera picker and enters the corresponding mode based on the media type. This API uses a promise to return the result.

> **NOTE：**
> 
> When an application is running on a widescreen foldable device and the camera picker is launched while the device
> is unfolded, switching the device from unfolded to folded will automatically move the camera picker to the
> background.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cameraPicker-function pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>--><!--Device-cameraPicker-function pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| mediaTypes | Array&lt;PickerMediaType&gt; | Yes |
| pickerProfile | [PickerProfile](arkts-camera-camerapicker-pickerprofile-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PickerResult&gt; |

## Examples

```TypeScript
import { cameraPicker } from '@kit.CameraKit';
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function demo(context: Context) {
  try {
    let pickerProfile: cameraPicker.PickerProfile = {
      cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
    };
    let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(context,
      [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
    console.info("the pick pickerResult is:" + JSON.stringify(pickerResult));
  } catch (error) {
    let err = error as BusinessError;
    console.error(`the pick call failed. error code: ${err.code}`);
  }
}
```
