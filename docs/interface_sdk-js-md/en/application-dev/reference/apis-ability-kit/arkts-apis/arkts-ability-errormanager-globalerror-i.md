# GlobalError

有关异常事件名字、消息、错误堆栈信息、异常线程名称和类型的对象。

**Inheritance/Implementation:** GlobalError extends [Error](../../apis-arkts/arkts-apis/arkts-arkts-error-c.md/arkts-arkts-error-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-errorManager-export interface GlobalError extends Error--><!--Device-errorManager-export interface GlobalError extends Error-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## instanceName

```TypeScript
instanceName: string
```

表示虚拟机实例名称。

**说明：**

TaskPool线程中异常的instanceName标识规则：

- globalErrorOccurred：标识为“TaskPool Thread + 方法名”；  
- globalUnhandledRejectionDetected：标识为“TaskPool Thread + 任务名”；  
- 若仅标识为“TaskPool Thread”，则表明异常源于异步回调内部。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GlobalError-instanceName: string--><!--Device-GlobalError-instanceName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## instanceType

```TypeScript
instanceType: InstanceType
```

表示虚拟机的实例类型。

**Type:** [InstanceType](arkts-ability-errormanager-instancetype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GlobalError-instanceType: InstanceType--><!--Device-GlobalError-instanceType: InstanceType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

