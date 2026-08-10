# AbilityDelegatorArgs

AbilityDelegatorArgs模块提供在应用程序执行测试用例期间，获取测试用例参数AbilityDelegatorArgs对象的能力。

> **说明：**
> 
> 本模块接口仅可在[单元测试框架](../../../application-test/unittest-guidelines.md)中使用。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityDelegatorArgs--><!--Device-unnamed-export interface AbilityDelegatorArgs-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

当前被测试应用的包名。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegatorArgs-bundleName: string--><!--Device-AbilityDelegatorArgs-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters: Record<string, string>
```

当前启动单元测试的参数。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegatorArgs-parameters: Record<string, string>--><!--Device-AbilityDelegatorArgs-parameters: Record<string, string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## testCaseNames

```TypeScript
testCaseNames: string
```

测试用例名称。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegatorArgs-testCaseNames: string--><!--Device-AbilityDelegatorArgs-testCaseNames: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## testRunnerClassName

```TypeScript
testRunnerClassName: string
```

执行测试用例的测试执行器名称。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegatorArgs-testRunnerClassName: string--><!--Device-AbilityDelegatorArgs-testRunnerClassName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

