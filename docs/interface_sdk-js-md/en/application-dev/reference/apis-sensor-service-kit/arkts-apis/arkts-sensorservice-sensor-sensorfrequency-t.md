# SensorFrequency

```TypeScript
type SensorFrequency = 'game' | 'ui' | 'normal'
```

传感器上报频率模式，提供预定义的频率档位，方便开发者快速设置常用的上报频率。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sensor-type SensorFrequency = 'game' | 'ui' | 'normal'--><!--Device-sensor-type SensorFrequency = 'game' | 'ui' | 'normal'-End-->

**System capability:** SystemCapability.Sensors.Sensor

| Type | Description |
| --- | --- |
| 'game' | 游戏模式，用于指定传感器上报频率。频率值：20000000ns（即20ms），适用于对数据延迟敏感的游戏类应用。该频率被设置在硬件支持的频率范围内时会生效，值固定为'game'字符串。 |
| 'ui' | UI模式，用于指定传感器上报频率。频率值：60000000ns（即60ms），适用于对数据更新有中等要求的UI交互类应用。该频率被设置在硬件支持的频率范围内时会生效，值固定为'ui'字符串。 |
| 'normal' | 普通模式，用于指定传感器上报频率。频率值：200000000ns（即200ms），适用于对数据更新频率要求不高的常规应用。该频率被设置在硬件支持的频率范围内时会生效，值固定为'normal '字符串。 |

