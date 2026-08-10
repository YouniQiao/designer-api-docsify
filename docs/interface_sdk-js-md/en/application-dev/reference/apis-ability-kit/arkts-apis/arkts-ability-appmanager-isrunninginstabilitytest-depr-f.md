# isRunningInStabilityTest

## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void
```

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

> **说明：**
> 
> 稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#isRunningInStabilityTest

<!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void--><!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 以回调方式返回接口运行结果及当前系统是否处于稳定性测试场景，可进行错误处理或其他自定义处理。返回true表示系统处于稳定性测试场景，返回false表示 系统不处于稳定性测试场景。 |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';

appManager.isRunningInStabilityTest((error, flag) => {
  if (error && error.code !== 0) {
    console.error(`isRunningInStabilityTest fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`isRunningInStabilityTest success, the result is: ${JSON.stringify(flag)}`);
  }
});
```


## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(): Promise<boolean>
```

查询当前系统是否处于稳定性测试场景。使用Promise异步回调。

> **说明：**
> 
> 稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#isRunningInStabilityTest

<!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>--><!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | 以Promise方式返回接口运行结果及当前是否处于稳定性测试场景，可进行错误处理或其他自定义处理。返回true表示系统处于稳定性测试场景，返回false表示系统不处于稳定性测试场景 。 |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.isRunningInStabilityTest().then((flag) => {
  console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```

