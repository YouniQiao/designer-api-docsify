# createMediaSourceWithDirectory

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## createMediaSourceWithDirectory

```TypeScript
function createMediaSourceWithDirectory(path: string): Promise< MediaSource | undefined>
```

根据指定目录路径创建一个媒体源对象。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaSource](arkts-media-multimedia-media-mediasource-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5411007](../errorcode-media.md#5411007-无可用资源) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test() {
  media.createMediaSourceWithDirectory("/data/storage/el2/base/media/cache/").then((mediaSource: media.MediaSource | undefined) => {
    if (mediaSource) {
      console.info('Succeeded in creating MediaSource with directory');
    } else {
      console.error('Failed to create MediaSource with directory');
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to create MediaSource with directory, error: ${error}`);
  });
}
```
