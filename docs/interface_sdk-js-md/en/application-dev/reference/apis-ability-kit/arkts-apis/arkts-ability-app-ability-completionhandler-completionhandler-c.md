# CompletionHandler

CompletionHandler提供了  
[onRequestSuccess](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestsuccess)和  
[onRequestFailure](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestfailure)两个回调函数，分别用来处理拉起应用成功和失败时的结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class CompletionHandler--><!--Device-unnamed-declare class CompletionHandler-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { CompletionHandler } from 'kits/@kit.AbilityKit';
```

## onRequestFailure

```TypeScript
onRequestFailure(elementName: ElementName, message: string): void
```

拉起应用失败时的回调函数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | ElementName信息用于标识被拉起应用。  - 通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信息是否存在取决于调用方是否传入。shortName和uri为空。  - 隐式启动失败时，无法获取ElementName信息。 |
| message | string | Yes | 拉起应用失败时的信息。该信息采用JSON格式，样式如下：  {  ?"errMsg": "xxx"  }  其中，"xxx"的取值说明如下：  Failed to call &lt;api-name&gt;：表示调用接口出错。其中，&lt;api-name&gt;为具体的接口名，比如startAbility。  User refused redirection：表示用户关闭了应用跳转弹框。  User closed the implicit startup picker：表示用户关闭了隐式启动时的应用选择弹框。  User closed the app clone picker：表示用户关闭了分身应用选择弹框。  Free installation failed：表示免安装失败。 |

## Examples

See [Usage of CompletionHandler](#usage-of-completionhandler).

## onRequestFailure

```TypeScript
onRequestFailure: OnRequestFailureFn
```

拉端失败时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletionHandler-onRequestFailure: OnRequestFailureFn--><!--Device-CompletionHandler-onRequestFailure: OnRequestFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onRequestSuccess

```TypeScript
onRequestSuccess(elementName: ElementName, message: string): void
```

拉起应用成功时的回调函数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | ElementName信息用于标识被拉起应用。通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信 息是否存在取决于调用方是否传入。shortName和uri为空。 |
| message | string | Yes | 成功拉起应用时的信息。该信息采用JSON格式，样式如下：  {  ?"errMsg": "Succeeded."  } |

## Examples

See [Usage of CompletionHandler](#usage-of-completionhandler).

## onRequestSuccess

```TypeScript
onRequestSuccess: OnRequestSuccessFn
```

拉端成功时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletionHandler-onRequestSuccess: OnRequestSuccessFn--><!--Device-CompletionHandler-onRequestSuccess: OnRequestSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

