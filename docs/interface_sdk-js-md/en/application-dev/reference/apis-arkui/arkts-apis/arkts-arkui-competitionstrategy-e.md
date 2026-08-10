# CompetitionStrategy

定义分发的事件是否为竞争手势，竞争场景手势原始节点和目标节点只有一个节点会响应手势，非竞争场景可以同时响应。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

<!--Device-unnamed-declare enum CompetitionStrategy--><!--Device-unnamed-declare enum CompetitionStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

表示分发的事件为非竞争手势。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CompetitionStrategy-DEFAULT = 0--><!--Device-CompetitionStrategy-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COMPETITION

```TypeScript
COMPETITION = 1
```

表示分发的事件为竞争手势。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CompetitionStrategy-COMPETITION = 1--><!--Device-CompetitionStrategy-COMPETITION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

