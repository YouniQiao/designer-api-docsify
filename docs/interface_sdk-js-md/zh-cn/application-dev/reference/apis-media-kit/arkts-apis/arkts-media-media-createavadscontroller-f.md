# createAVAdsController

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVAdsController

```TypeScript
function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>
```

创建一个与播放器实例关联的广告播放控制器。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| player | [AVPlayer](arkts-media-media-avplayer-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVAdsController](arkts-media-media-avadscontroller-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  media.createAVAdsController(player).then((adsController: media.AVAdsController | undefined) => {
    if (adsController) {
      console.info('Succeeded in creating AVAdsController');
    } else {
      console.error('Failed to create AVAdsController');
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to create AVAdsController, error: ${error}`);
  });
}
```
