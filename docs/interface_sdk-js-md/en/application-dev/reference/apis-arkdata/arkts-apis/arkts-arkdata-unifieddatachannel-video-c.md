# Video

Represents video data. It is a child class of [File](arkts-arkdata-unifieddatachannel-file-c.md) and is used to describe a video file.

**Inheritance/Implementation:** Video extends [File](arkts-arkdata-unifieddatachannel-file-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unifiedDataChannel-class Video--><!--Device-unifiedDataChannel-class Video-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**Examples**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let video = new unifiedDataChannel.Video();
    let filePath = pathDir + '/test.mp4';
    video.videoUri =fileUri.getUriFromPath(filePath);
  }
}
```

