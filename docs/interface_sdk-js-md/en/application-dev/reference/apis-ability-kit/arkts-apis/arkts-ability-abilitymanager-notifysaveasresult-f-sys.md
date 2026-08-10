# notifySaveAsResult (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void
```

该接口仅供[DLP](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md/arkts-dlppermission.md)（Data Loss Prevention, 数据丢失防护）管理应用使用，其他应用禁止使用，DLP管理应用通过该接口通知沙箱应用另存为结果。使用callback异步回调。

> **说明：**
> 
> 从API version 10开始支持，从API version 24开始废弃。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Deprecated since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | 返回给调用startAbilityForResult?接口调用方的相关信息。 |
| requestCode | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | DLP管理应用传入的请求代码。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当另存为结果通知成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |


## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>
```

该接口仅供[DLP](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md/arkts-dlppermission.md)（Data Loss Prevention, 数据丢失防护）管理应用使用，其他应用禁止使用，DLP管理应用通过该接口通知沙箱应用另存为结果。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Deprecated since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | 返回给调用startAbilityForResult?接口调用方的相关信息。 |
| requestCode | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | DLP管理应用传入的请求代码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

