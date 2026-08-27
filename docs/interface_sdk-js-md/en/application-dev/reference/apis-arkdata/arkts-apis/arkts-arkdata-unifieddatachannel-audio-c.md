# Audio

Represents audio data. It is a child class of [File](arkts-arkdata-unifieddatachannel-file-c.md) and is used to describe an audio file.

**Inheritance/Implementation:** Audio extends [File](arkts-arkdata-unifieddatachannel-file-c.md)

**Since:** 10

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## audioUri

```TypeScript
set audioUri(value: string)
```

Indicates the uri of audio

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

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
    let audio = new unifiedDataChannel.Audio();
    let filePath = pathDir + '/test.mp3';
    audio.audioUri = fileUri.getUriFromPath(filePath);
  }
}
```
