# isRunningInStabilityTest

## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void
```

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

> **说明：**
> 
> 稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isRunningInStabilityTest](ohos.app.ability.appManager/appManager#isRunningInStabilityTest)

<!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void--><!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## 示例

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isRunningInStabilityTest](ohos.app.ability.appManager/appManager#isRunningInStabilityTest)

<!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>--><!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## 示例

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.isRunningInStabilityTest().then((flag) => {
  console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```
