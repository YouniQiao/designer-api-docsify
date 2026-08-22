# LiveFormExtensionContext

```TypeScript
export type LiveFormExtensionContext = _LiveFormExtensionContext
```

The context of live form extension. It allows access to liveFormExtension-specific resources.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-common-export type LiveFormExtensionContext = _LiveFormExtensionContext--><!--Device-common-export type LiveFormExtensionContext = _LiveFormExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

**Property type:** _LiveFormExtensionContext

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';

let uiAbilityContext: common.UIAbilityContext;
let abilityStageContext: common.AbilityStageContext;
let applicationContext: common.ApplicationContext;
let baseContext: common.BaseContext;
let context: common.Context;
let uiExtensionContext: common.UIExtensionContext;
let extensionContext: common.ExtensionContext;
let formExtensionContext: common.FormExtensionContext;
let vpnExtensionContext: common.VpnExtensionContext;
let eventHub: common.EventHub;
let pacMap: common.PacMap;
let abilityResult: common.AbilityResult;
let abilityStartCallback: common.AbilityStartCallback;
let connectOptions: common.ConnectOptions;
let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
let uiServiceProxy : common.UIServiceProxy;
let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
let appServiceExtensionContext : common.AppServiceExtensionContext;
let formEditExtensionContext : common.FormEditExtensionContext;
let liveFormExtensionContext : common.LiveFormExtensionContext;
```

