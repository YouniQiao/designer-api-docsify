# AudioCapturerMicInData (System API)

描述音频录音数据，其中包含已处理的音频数据和进行音频处理前的纯净麦克风输入（mic-in）音频数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-audio-interface AudioCapturerMicInData--><!--Device-audio-interface AudioCapturerMicInData-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## data

```TypeScript
data: ArrayBuffer
```

处理后的音频数据缓冲。

**Type:** ArrayBuffer

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInData-data: ArrayBuffer--><!--Device-AudioCapturerMicInData-data: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## ecData

```TypeScript
ecData?: ArrayBuffer
```

回声参考音频数据缓冲。如果录音配置没有设置ecStreamInfo，则此缓冲将为空。有关详细信息，请参见{@link #AudioCapturerMicInConfig}。

**Type:** ArrayBuffer

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInData-ecData?: ArrayBuffer--><!--Device-AudioCapturerMicInData-ecData?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## micInData

```TypeScript
micInData: ArrayBuffer
```

麦克风输入音频数据缓冲。

**Type:** ArrayBuffer

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInData-micInData: ArrayBuffer--><!--Device-AudioCapturerMicInData-micInData: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

