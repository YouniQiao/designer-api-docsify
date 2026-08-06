# registerKeyObserver

## registerKeyObserver

```TypeScript
function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean
```

Monitor registration key(synchronous method)  
[USER\_SECURE] domain need ohos.permission.MANAGE\_SECURE\_SETTINGS permission.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean--><!--Device-settings-function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Application context. Only UIAbilityContext and ExtensionContext are supported. |
| name | string | Yes | Indicates the name of the character string. |
| domainName | string | Yes | Indicates the name of the domain name to set. |
| observer | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | callback when monitored key value is changed. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Example**

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.registerKeyObserver(context, settings.display.SCREEN_BRIGHTNESS_STATUS, settings.domainName.DEVICE_SHARED, () => {
  let value:string = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
  console.info(`Promise:value -> ${value}`);
});
```

