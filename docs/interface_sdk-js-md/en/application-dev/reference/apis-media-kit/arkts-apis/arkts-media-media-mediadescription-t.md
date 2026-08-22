# MediaDescription

```TypeScript
type MediaDescription = Record<string, Object>
```

Provides the container definition for media description key-value pairs.

The media description consists of key-value pairs where keys reference @MediaDescriptionKey.

**Since:** 23

<!--Device-media-type MediaDescription = Record<string, Object>--><!--Device-media-type MediaDescription = Record<string, Object>-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Property type:** Record&lt;string, Object&gt;

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

function printfItemDescription(obj: media.MediaDescription, key: string) {
  let property: Object = obj[key];
  console.info('audio key is ' + key); // Obtain the value of the key. For details about the keys, see MediaDescriptionKey.
  console.info('audio value is ' + property); // Obtain the value of the key. The value can be any type. For details about the types, see MediaDescriptionKey.
}

let avPlayer: media.AVPlayer | undefined = undefined;
media.createAVPlayer((err: BusinessError, player: media.AVPlayer) => {
  if(player != null) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
      if (arrList != null) {
        for (let i = 0; i < arrList.length; i++) {
          printfItemDescription(arrList[i], media.MediaDescriptionKey.MD_KEY_TRACK_TYPE); // Print the MD_KEY_TRACK_TYPE value of each track.
        }
      } else {
        console.error(`Failed to get TrackDescription, error:${error}`);
      }
    });
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

