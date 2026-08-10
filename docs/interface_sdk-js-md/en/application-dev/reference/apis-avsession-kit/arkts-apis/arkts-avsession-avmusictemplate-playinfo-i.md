# PlayInfo

播放信息的定义。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface PlayInfo--><!--Device-avMusicTemplate-interface PlayInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## currentPlayDuration

```TypeScript
currentPlayDuration: int
```

当前播放的时长，单位为毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-currentPlayDuration: int--><!--Device-PlayInfo-currentPlayDuration: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## currentPlayRate

```TypeScript
currentPlayRate: string
```

当前的播放速率。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-currentPlayRate: string--><!--Device-PlayInfo-currentPlayRate: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportNext

```TypeScript
isSupportNext: boolean
```

是否支持下一首。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportNext: boolean--><!--Device-PlayInfo-isSupportNext: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportPlayMode

```TypeScript
isSupportPlayMode: boolean
```

是否支持切换播放模式。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportPlayMode: boolean--><!--Device-PlayInfo-isSupportPlayMode: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportPlayRate

```TypeScript
isSupportPlayRate: boolean
```

是否支持改变播放速率。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportPlayRate: boolean--><!--Device-PlayInfo-isSupportPlayRate: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportPrev

```TypeScript
isSupportPrev: boolean
```

是否支持上一首。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportPrev: boolean--><!--Device-PlayInfo-isSupportPrev: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportProgress

```TypeScript
isSupportProgress: boolean
```

是否支持进度。true表示支持，false表示不支持。默认值为true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportProgress: boolean--><!--Device-PlayInfo-isSupportProgress: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportQuickBackward

```TypeScript
isSupportQuickBackward: boolean
```

是否支持快退。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportQuickBackward: boolean--><!--Device-PlayInfo-isSupportQuickBackward: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportQuickForward

```TypeScript
isSupportQuickForward: boolean
```

是否支持快进。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportQuickForward: boolean--><!--Device-PlayInfo-isSupportQuickForward: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportSkipHead

```TypeScript
isSupportSkipHead: boolean
```

是否支持跳过开头。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportSkipHead: boolean--><!--Device-PlayInfo-isSupportSkipHead: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportSkipTail

```TypeScript
isSupportSkipTail: boolean
```

是否支持跳过结尾。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportSkipTail: boolean--><!--Device-PlayInfo-isSupportSkipTail: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportSoundEffect

```TypeScript
isSupportSoundEffect: boolean
```

是否支持音效。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportSoundEffect: boolean--><!--Device-PlayInfo-isSupportSoundEffect: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isSupportSoundQuality

```TypeScript
isSupportSoundQuality: boolean
```

是否支持声音质量。true表示支持，false表示不支持。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-isSupportSoundQuality: boolean--><!--Device-PlayInfo-isSupportSoundQuality: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## playCounts

```TypeScript
playCounts: string
```

播放量。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-playCounts: string--><!--Device-PlayInfo-playCounts: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## quickBackwardStep

```TypeScript
quickBackwardStep: int
```

快退的步长，单位为毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-quickBackwardStep: int--><!--Device-PlayInfo-quickBackwardStep: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## quickForwardStep

```TypeScript
quickForwardStep: int
```

快进的步长，单位为毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-quickForwardStep: int--><!--Device-PlayInfo-quickForwardStep: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## supportedPlayRate

```TypeScript
supportedPlayRate: string[]
```

支持的播放速率的数组。

**Type:** string[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-supportedPlayRate: string[]--><!--Device-PlayInfo-supportedPlayRate: string[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## totalDuration

```TypeScript
totalDuration: int
```

播放总时长，单位为毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayInfo-totalDuration: int--><!--Device-PlayInfo-totalDuration: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

