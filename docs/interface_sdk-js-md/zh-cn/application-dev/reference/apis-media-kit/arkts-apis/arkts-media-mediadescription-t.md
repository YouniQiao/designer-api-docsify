# MediaDescription

```TypeScript
type MediaDescription = Record<string, Object>
```

Provides the container definition for media description key-value pairs.

The media description consists of key-value pairs where keys reference @MediaDescriptionKey.

**起始版本：** 23

<!--Device-unnamed-type MediaDescription = Record<string, Object>--><!--Device-unnamed-type MediaDescription = Record<string, Object>-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**属性类型：** [Record](../../apis-arkts/arkts-apis/arkts-arkts-map-record-c.md)&lt;string, Object&gt;

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

function printfItemDescription(obj: media.MediaDescription, key: string) {
  let property: Object = obj[key];
  console.info('audio key is ' + key); // 通过key值获取对应的value。key值具体可见MediaDescriptionKey。
  console.info('audio value is ' + property); // 对应key值的value。其类型可为任意类型，具体key对应value的类型可参考MediaDescriptionKey。
}

let avPlayer: media.AVPlayer | undefined = undefined;
media.createAVPlayer((err: BusinessError, player: media.AVPlayer) => {
  if(player != null) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
      if (arrList != null) {
        for (let i = 0; i < arrList.length; i++) {
          printfItemDescription(arrList[i], media.MediaDescriptionKey.MD_KEY_TRACK_TYPE); // 打印出每条轨道MD_KEY_TRACK_TYPE的值。
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

