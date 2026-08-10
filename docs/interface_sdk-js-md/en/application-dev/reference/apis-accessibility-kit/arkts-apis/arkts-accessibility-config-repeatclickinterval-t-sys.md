# RepeatClickInterval (System API)

```TypeScript
type RepeatClickInterval = 'Shortest' | 'Short' | 'Medium' | 'Long' | 'Longest'
```

忽略重复点击功能开启时（[ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignorerepeatclick)设置为true)，忽略重复点击的配置(即设置的RepeatClickInterval的值)生效；忽略重复点击功能关闭时（[ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignorerepeatclick)设置为false)，显示为正常类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-type RepeatClickInterval = 'Shortest' | 'Short' | 'Medium' | 'Long' | 'Longest'--><!--Device-config-type RepeatClickInterval = 'Shortest' | 'Short' | 'Medium' | 'Long' | 'Longest'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| 'Shortest' | 表示最短。 |
| 'Short' | 表示短。 |
| 'Medium' | 表示中。 |
| 'Long' | 表示长。 |
| 'Longest' | 表示最长。 |

