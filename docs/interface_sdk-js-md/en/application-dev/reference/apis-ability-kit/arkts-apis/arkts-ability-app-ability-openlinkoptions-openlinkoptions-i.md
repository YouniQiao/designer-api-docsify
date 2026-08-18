# OpenLinkOptions

**OpenLinkOptions** can be used as an input parameter of [openLink()](arkts-ability-uiabilitycontext-c.md#openlink) to indicate whether to enable only App Linking and pass in optional parameters in the form of key-value pairs.

**Since:** 23

<!--Device-unnamed-export default interface OpenLinkOptions--><!--Device-unnamed-export default interface OpenLinkOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { OpenLinkOptions } from '@kit.AbilityKit';
import { OpenLinkOptions } from '@kit.AbilityKit';
```

## appLinkingOnly

```TypeScript
appLinkingOnly?: boolean
```

Whether the UIAbility must be started using &lt;!--RP1--&gt; [App Linking](../../../application-models/app-linking-startup.md)&lt;!--RP1End--&gt;. - If this parameter is set to **true** and no UIAbility matches the URL in App Linking, the result is returned directly. - If this parameter is set to **false** and no UIAbility matches the URL in App Linking, App Linking falls back to [Deep Linking](../../../application-models/deep-linking-startup.md). The default value is **false**. When the aa command is used to implicitly start an ability, you can set **--pb appLinkingOnly true** or **--pb appLinkingOnly false** to start the ability in App Linking mode.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OpenLinkOptions-appLinkingOnly?: boolean--><!--Device-OpenLinkOptions-appLinkingOnly?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## completionHandler

```TypeScript
completionHandler?: CompletionHandler
```

Operation class used to handle the result of an application launch request.

**Type:** [CompletionHandler](arkts-ability-app-ability-completionhandler-completionhandler-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OpenLinkOptions-completionHandler?: CompletionHandler--><!--Device-OpenLinkOptions-completionHandler?: CompletionHandler-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## hideFailureTipDialog

```TypeScript
hideFailureTipDialog?: boolean
```

Whether to display a "No app available" dialog box when a suitable application is not found using [Deep Linking](../../../application-models/deep-linking-startup.md). - **true**: The "No app available" dialog box is not displayed. - **false**: The "No app available" dialog box is displayed. The default value is **false**. Note: If **appLinkingOnly** is set to **true**, the Deep Linking process is not triggered, and this field does not take effect.

**Type:** boolean

**Default:** { false }

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OpenLinkOptions-hideFailureTipDialog?: boolean--><!--Device-OpenLinkOptions-hideFailureTipDialog?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters?: Record<string, RecordData>
```

OpenLinkOptions parameters in the form of custom key-value pairs.

**Type:** Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenLinkOptions-parameters?: Record<string, RecordData>--><!--Device-OpenLinkOptions-parameters?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

