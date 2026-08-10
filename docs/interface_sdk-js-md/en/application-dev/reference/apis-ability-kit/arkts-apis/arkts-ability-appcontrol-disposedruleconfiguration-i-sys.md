# DisposedRuleConfiguration (System API)

标识批量设置拦截规则的配置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-appControl-export interface DisposedRuleConfiguration--><!--Device-appControl-export interface DisposedRuleConfiguration-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## appId

```TypeScript
appId: string
```

要被设置拦截规则应用的appId或appIdentifier。appId和appIdentifier可以标识同一个应用，因此针对同一应用如果用appIdentifier设置拦截规则，可以覆盖之前采用appId设置的，反之同理。

**说明：**

appId是应用的唯一标识，由应用Bundle名称和签名信息决定，获取方法参见  
[获取应用的appId](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appid)。

[appIdentifier](arkts-ability-bundleinfo-signatureinfo-i.md)也是应用的唯一标识，详情信息可参考  
[什么是appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)，获取方法参见  
[获取应用的appIdentifier](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appidentifier)。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-appId: string--><!--Device-DisposedRuleConfiguration-appId: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex: int
```

表示分身应用的索引，默认值为0。

appIndex为0时，表示设置主应用的拦截规则。appIndex大于0时，表示设置指定分身应用的拦截规则。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-appIndex: int--><!--Device-DisposedRuleConfiguration-appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## disposedRule

```TypeScript
disposedRule: DisposedRule
```

表示对应用的拦截规则，包括拦截时将拉起能力的类型等。

**Type:** [DisposedRule](arkts-ability-appcontrol-disposedrule-i-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-disposedRule: DisposedRule--><!--Device-DisposedRuleConfiguration-disposedRule: DisposedRule-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

