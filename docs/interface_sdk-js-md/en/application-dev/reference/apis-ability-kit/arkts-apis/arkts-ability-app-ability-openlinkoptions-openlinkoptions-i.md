# OpenLinkOptions

OpenLinkOptions可以作为[openLink()](arkts-ability-uiabilitycontext-c.md#openlink)的入参，用于标识是否仅打开AppLinking和传递键值对可选参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface OpenLinkOptions--><!--Device-unnamed-export default interface OpenLinkOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { OpenLinkOptions } from 'kits/@kit.AbilityKit';
```

## appLinkingOnly

```TypeScript
appLinkingOnly?: boolean
```

表示是否必须以&lt;!--RP1--&gt;[AppLinking](../../../application-models/app-linking-startup.md)&lt;!--RP1End--&gt;的方式启动UIAbility。

- 取值为true时，如果不存在与AppLinking相匹配的UIAbility，直接返回。  
- 取值为false时，如果不存在与AppLinking相匹配的UIAbility，AppLinking会退化为  
[DeepLinking](../../../application-models/deep-linking-startup.md)。默认值为false。

aa命令隐式拉起Ability时可以通过设置"--pb appLinkingOnly true/false"以AppLinking的方式进行启动。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OpenLinkOptions-appLinkingOnly?: boolean--><!--Device-OpenLinkOptions-appLinkingOnly?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## completionHandler

```TypeScript
completionHandler?: CompletionHandler
```

拉起应用结果的操作类，用于处理拉起应用的结果。

**Type:** [CompletionHandler](arkts-ability-app-ability-completionhandler-completionhandler-c.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-OpenLinkOptions-completionHandler?: CompletionHandler--><!--Device-OpenLinkOptions-completionHandler?: CompletionHandler-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## hideFailureTipDialog

```TypeScript
hideFailureTipDialog?: boolean
```

表示[Deep Linking](../../../application-models/deep-linking-startup.md)找不到应用时是否显示“暂无可用打开方式”的弹窗。

- 取值为true时，不显示“暂无可用打开方式”的弹窗。  
- 取值为false时，显示“暂无可用打开方式”的弹窗。默认值为false。

**说明：**appLinkingOnly字段为true时不会触发Deep Linking流程，该字段不会生效。

**Type:** boolean

**Default:** { false }

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-OpenLinkOptions-hideFailureTipDialog?: boolean--><!--Device-OpenLinkOptions-hideFailureTipDialog?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters?: Record<string, Object>
```

表示WantParams参数。

**说明：**具体使用规则请参考[want](arkts-ability-app-ability-want-want-c.md)中的parameters属性。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OpenLinkOptions-parameters?: Record<string, Object>--><!--Device-OpenLinkOptions-parameters?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

