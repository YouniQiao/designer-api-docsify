# TestRunner

Base class for the test framework.If you want to implement your own unit test framework, you must inherit this class and overrides all its methods.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-interface TestRunner--><!--Device-unnamed-interface TestRunner-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onPrepare

```TypeScript
onPrepare(): void
```

Prepare the unit testing environment for running test cases.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TestRunner-onPrepare(): void--><!--Device-TestRunner-onPrepare(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Example**

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TestRunner-onPrepare: OnPrepareFn--><!--Device-TestRunner-onPrepare: OnPrepareFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onRun

```TypeScript
onRun(): void
```

Run all test cases.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TestRunner-onRun(): void--><!--Device-TestRunner-onRun(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Example**

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TestRunner-onRun: OnRunFn--><!--Device-TestRunner-onRun: OnRunFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onStop

```TypeScript
onStop?: OnStopFn
```

Stop all test cases.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TestRunner-onStop?: OnStopFn--><!--Device-TestRunner-onStop?: OnStopFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

