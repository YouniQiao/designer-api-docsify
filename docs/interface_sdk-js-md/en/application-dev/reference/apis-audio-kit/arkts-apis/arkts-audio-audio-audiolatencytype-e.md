# AudioLatencyType

表示音频时延类型的枚举。

| 名称 | 值 | 说明 |  
| ---- | -- | ---- |  
| LATENCY_TYPE_ALL | 0 | 计算包含软件和硬件在内的整体音频处理链路时延。 |  
| LATENCY_TYPE_SOFTWARE | 1 | 计算软件侧时延，包含软件音效。 |  
| LATENCY_TYPE_HARDWARE | 2 | 计算硬件侧时延，包含HAL、驱动和硬件。 |

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-audio-enum AudioLatencyType--><!--Device-audio-enum AudioLatencyType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## LATENCY_TYPE_ALL

```TypeScript
LATENCY_TYPE_ALL = 0
```

Type to get latency of all audio processing units, including software and hardware.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLatencyType-LATENCY_TYPE_ALL = 0--><!--Device-AudioLatencyType-LATENCY_TYPE_ALL = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## LATENCY_TYPE_SOFTWARE

```TypeScript
LATENCY_TYPE_SOFTWARE = 1
```

Type to get latency of software part, including audio effects in software.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLatencyType-LATENCY_TYPE_SOFTWARE = 1--><!--Device-AudioLatencyType-LATENCY_TYPE_SOFTWARE = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## LATENCY_TYPE_HARDWARE

```TypeScript
LATENCY_TYPE_HARDWARE = 2
```

Type to get latency of hardware part, including audio effects in hal, driver and hardware.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLatencyType-LATENCY_TYPE_HARDWARE = 2--><!--Device-AudioLatencyType-LATENCY_TYPE_HARDWARE = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

