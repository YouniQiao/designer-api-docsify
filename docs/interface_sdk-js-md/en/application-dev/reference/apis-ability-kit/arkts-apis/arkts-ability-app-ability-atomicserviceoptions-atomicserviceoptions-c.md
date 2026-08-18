# AtomicServiceOptions

**AtomicServiceOptions** is used as an input parameter of [openAtomicService()](arkts-ability-uiabilitycontext-c.md#openatomicservice) to carry arguments. It inherits from [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md).

**Inheritance/Implementation:** AtomicServiceOptions extends [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md)

**Since:** 23

<!--Device-unnamed-export default class AtomicServiceOptions--><!--Device-unnamed-export default class AtomicServiceOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AtomicServiceOptions } from '@kit.AbilityKit';
```

## completionHandlerForAtomicService

```TypeScript
completionHandlerForAtomicService?: CompletionHandlerForAtomicService
```

Operation class for receiving the result of opening an atomic service.

**Type:** [CompletionHandlerForAtomicService](../../apis-na/arkts-apis/arkts-na-app-ability-completionhandlerforatomicservice-completionhandlerforatomicservice-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceOptions-completionHandlerForAtomicService?: CompletionHandlerForAtomicService--><!--Device-AtomicServiceOptions-completionHandlerForAtomicService?: CompletionHandlerForAtomicService-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## flags

```TypeScript
flags?: int
```

Mode in which the system processes the startup. For example, **wantConstant.Flags.FLAG_INSTALL_ON_DEMAND** indicates that the installation-free capability is used.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceOptions-flags?: int--><!--Device-AtomicServiceOptions-flags?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters?: Record<string, RecordData>
```

Additional parameters. For details, see the **parameters** field in [Want](arkts-ability-app-ability-want-want-c.md).

**Type:** Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceOptions-parameters?: Record<string, RecordData>--><!--Device-AtomicServiceOptions-parameters?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

