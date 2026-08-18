# Usage

```TypeScript
type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' |
  'touch' | 'media' | 'physicalFeedback' | 'simulateReality'
```

振动使用场景。不同usage值对应不同的系统振动开关管控规则，开发者需根据实际业务场景选择合适的usage值。 &lt;!--RP1End--&gt;

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-vibrator-type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' |  'touch' | 'media' | 'physicalFeedback' | 'simulateReality'--><!--Device-vibrator-type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' |  'touch' | 'media' | 'physicalFeedback' | 'simulateReality'-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

| 类型 |
| --- |
| 'unknown' |
| 'alarm' |
| 'ring' |
| 'notification' |
| 'communication' |
| 'touch' |
| 'media' |
| 'physicalFeedback' |
| 'simulateReality' |
