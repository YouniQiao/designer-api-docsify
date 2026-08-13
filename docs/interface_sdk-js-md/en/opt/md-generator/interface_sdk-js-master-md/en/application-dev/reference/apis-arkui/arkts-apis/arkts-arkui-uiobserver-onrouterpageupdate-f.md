# on_routerPageUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on_routerPageUpdate

```TypeScript
export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void
```

Subscribes to state changes of the page during routing.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void--><!--Device-uiObserver-export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'routerPageUpdate' | Yes |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RouterPageInfo&gt; | Yes |

## Examples

```TypeScript
// used in UIAbility
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { UIContext, window, uiObserver } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  private uiContext: UIContext | null = null;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Subscribe to the target events within the scope of the page under the ability context.
    uiObserver.on('routerPageUpdate', this.context, (info: uiObserver.RouterPageInfo) => {
      console.info(`[uiObserver][abilityContext] got info: ${JSON.stringify(info)}`)
    })
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      windowStage.getMainWindow((err: BusinessError, data) => {
        let windowInfo: window.Window = data;
        // Obtain a UIContext instance.
        this.uiContext = windowInfo.getUIContext();
        // Subscribe to the target events within the scope of the page under the UI context.
        uiObserver.on('routerPageUpdate', this.uiContext, (info: uiObserver.RouterPageInfo)=>{
          console.info(`[uiObserver][uiContext] got info: ${JSON.stringify(info)}`)
        })
      })
    });
  }

  // ... other function in EntryAbility
}
```
