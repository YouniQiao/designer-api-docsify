# AVQueueInfo (System API)

歌单（歌曲列表）的相关属性。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVQueueInfo--><!--Device-avSession-interface AVQueueInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## avQueueId

```TypeScript
avQueueId: string
```

歌单（歌曲列表）唯一标识Id。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVQueueInfo-avQueueId: string--><!--Device-AVQueueInfo-avQueueId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

## avQueueImage

```TypeScript
avQueueImage: image.PixelMap | string
```

歌单（歌曲列表）封面图，图片的像素数据或者图片路径地址（本地路径或网络路径）。

**Type:** image.PixelMap \| string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVQueueInfo-avQueueImage: image.PixelMap | string--><!--Device-AVQueueInfo-avQueueImage: image.PixelMap | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

## avQueueName

```TypeScript
avQueueName: string
```

歌单（歌曲列表）名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVQueueInfo-avQueueName: string--><!--Device-AVQueueInfo-avQueueName: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

歌单所属应用包名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVQueueInfo-bundleName: string--><!--Device-AVQueueInfo-bundleName: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

## lastPlayedTime

```TypeScript
lastPlayedTime?: long
```

歌单最后播放时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVQueueInfo-lastPlayedTime?: long--><!--Device-AVQueueInfo-lastPlayedTime?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

