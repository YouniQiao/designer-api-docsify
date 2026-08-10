# TestRunner

TestRunner模块提供了框架测试的能力。包括准备单元测试环境、运行测试用例。如果您想实现自己的单元测试框架，您必须继承这个类并覆盖它的所有方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-interface TestRunner--><!--Device-unnamed-interface TestRunner-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { TestRunner } from 'kits/@kit.TestKit';
```

## onPrepare

```TypeScript
onPrepare(): void
```

为运行测试用例准备单元测试环境。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TestRunner-onPrepare(): void--><!--Device-TestRunner-onPrepare(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

```TypeScript
import { TestRunner } from '@kit.TestKit';

// Implement a custom test runner.
export default class UserTestRunner implements TestRunner {
  // Prepare the unit test environment.
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

为运行测试用例准备单元测试环境。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TestRunner-onPrepare: OnPrepareFn--><!--Device-TestRunner-onPrepare: OnPrepareFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onRun

```TypeScript
onRun(): void
```

运行测试用例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TestRunner-onRun(): void--><!--Device-TestRunner-onRun(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

```TypeScript
import { TestRunner } from '@kit.TestKit';

// Implement a custom test runner.
export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  // Run test cases.
  onRun() {
    console.info('Trigger onRun');
  }
}
```

## onRun

```TypeScript
onRun: OnRunFn
```

运行测试用例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TestRunner-onRun: OnRunFn--><!--Device-TestRunner-onRun: OnRunFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onStop

```TypeScript
onStop?: OnStopFn
```

当测试完成时，系统会在测试环境退出前触发该回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TestRunner-onStop?: OnStopFn--><!--Device-TestRunner-onStop?: OnStopFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

