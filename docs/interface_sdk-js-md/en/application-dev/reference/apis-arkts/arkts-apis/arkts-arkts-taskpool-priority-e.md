# Priority

表示所创建任务（Task）执行时的优先级。工作线程优先级跟随任务优先级更新，对应关系参考[QoS等级定义](../../../napi/qos-guidelines.md#qos等级定义)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-taskpool-enum Priority--><!--Device-taskpool-enum Priority-End-->

**System capability:** SystemCapability.Utils.Lang

## HIGH

```TypeScript
HIGH = 0
```

任务为高优先级。

从API version 11开始，该接口支持在原子化服务中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-HIGH = 0--><!--Device-Priority-HIGH = 0-End-->

**System capability:** SystemCapability.Utils.Lang

## MEDIUM

```TypeScript
MEDIUM = 1
```

任务为中优先级。

从API version 11开始，该接口支持在原子化服务中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-MEDIUM = 1--><!--Device-Priority-MEDIUM = 1-End-->

**System capability:** SystemCapability.Utils.Lang

## LOW

```TypeScript
LOW = 2
```

任务为低优先级。

从API version 11开始，该接口支持在原子化服务中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-LOW = 2--><!--Device-Priority-LOW = 2-End-->

**System capability:** SystemCapability.Utils.Lang

## IDLE

```TypeScript
IDLE = 3
```

任务为后台任务。

从API version 12开始，该接口支持在原子化服务中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Priority-IDLE = 3--><!--Device-Priority-IDLE = 3-End-->

**System capability:** SystemCapability.Utils.Lang

