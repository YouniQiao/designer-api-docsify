# offApplicationStateChange

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void
```

注销应用状态监听器。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void--><!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observerId | int | 是 | 注册的应用状态监听器ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback of off. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |


## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int): Promise<void>
```

注销应用状态监听器。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>--><!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observerId | int | 是 | 注册的应用状态监听器ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |

