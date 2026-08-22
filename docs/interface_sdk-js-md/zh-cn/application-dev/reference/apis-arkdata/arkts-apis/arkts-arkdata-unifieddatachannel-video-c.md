# Video

视频类型数据，是[File](arkts-arkdata-unifieddatachannel-file-c.md)的子类，用于描述视频文件。

**继承/实现关系：** Video extends [File](arkts-arkdata-unifieddatachannel-file-c.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unifiedDataChannel-class Video--><!--Device-unifiedDataChannel-class Video-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**示例**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
import { fileUri } from '@kit.CoreFileKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
    let video = new unifiedDataChannel.Video();
    let filePath = pathDir + '/test.mp4';
    video.videoUri = fileUri.getUriFromPath(filePath);
  }
}
```

