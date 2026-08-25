# TestRunner

Base class for the test framework. If you want to implement your own unit test framework, you must inherit this class and overrides all its methods.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { TestRunner } from '@kit.TestKit';
```

## onPrepare

```TypeScript
onPrepare(): void
```

Prepare the unit testing environment for running test cases.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
  }
}
```

## onPrepare

```TypeScript
onPrepare: OnPrepareFn
```

Prepare the unit testing environment for running test cases.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

See [onPrepare](#onprepare)

## onRun

```TypeScript
onRun(): void
```

Run all test cases.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  onRun() {
    console.info('Trigger onRun');
  }
}
```

## onRun

```TypeScript
onRun: OnRunFn
```

Run all test cases.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

See [onRun](#onrun)

## onStop

```TypeScript
onStop?: OnStopFn
```

Stop all test cases.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
    console.info('Trigger onRun');
  }

  onStop() {
    console.info('Trigger onStop');
  }
}
```
