# State

表示任务（Task）状态的枚举。

状态转换规则如下：  
- 当任务创建成功后，调用execute，任务进入taskpool等待队列，状态设置为WAITING。  
- 任务从等待队列出来进入taskpool工作线程中，任务状态更新为RUNNING。  
- 当任务执行完成，返回结果后，如果任务再次被执行，则状态重置为WAITING。  
- 当主动cancel任务时，将任务状态更新为CANCELED。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-enum State--><!--Device-taskpool-enum State-End-->

**System capability:** SystemCapability.Utils.Lang

## WAITING

```TypeScript
WAITING = 1
```

任务正在等待。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-State-WAITING = 1--><!--Device-State-WAITING = 1-End-->

**System capability:** SystemCapability.Utils.Lang

## RUNNING

```TypeScript
RUNNING = 2
```

任务正在执行。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-State-RUNNING = 2--><!--Device-State-RUNNING = 2-End-->

**System capability:** SystemCapability.Utils.Lang

## CANCELED

```TypeScript
CANCELED = 3
```

任务已被取消。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-State-CANCELED = 3--><!--Device-State-CANCELED = 3-End-->

**System capability:** SystemCapability.Utils.Lang

