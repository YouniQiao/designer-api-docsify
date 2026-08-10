# TaskResult

处于等待或执行过程中的任务进行取消操作后，在catch分支里捕获到BusinessError里的补充信息。其他场景下该信息为undefined。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-taskpool-interface TaskResult--><!--Device-taskpool-interface TaskResult-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## error

```TypeScript
error?: Error | Object
```

错误信息。默认和BusinessError的message字段一致。不建议修改此值。

**Type:** Error \| Object

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TaskResult-error?: Error | Object--><!--Device-TaskResult-error?: Error | Object-End-->

**System capability:** SystemCapability.Utils.Lang

## result

```TypeScript
result?: Object
```

任务执行结果。默认为undefined。不建议修改此值。

**Type:** Object

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TaskResult-result?: Object--><!--Device-TaskResult-result?: Object-End-->

**System capability:** SystemCapability.Utils.Lang

