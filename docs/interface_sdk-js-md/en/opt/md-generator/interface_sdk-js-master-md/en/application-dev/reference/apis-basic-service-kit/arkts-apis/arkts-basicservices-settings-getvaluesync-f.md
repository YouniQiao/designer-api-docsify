# getValueSync

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## getValueSync

```TypeScript
function getValueSync(dataAbilityHelper: DataAbilityHelper, name: string, defValue: string): string
```

Get value from settingsdata(synchronous method)

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.settings#getValueSync

**Model restriction:** This API can be used only in the FA model.

<!--Device-settings-function getValueSync(dataAbilityHelper: DataAbilityHelper, name: string, defValue: string): string--><!--Device-settings-function getValueSync(dataAbilityHelper: DataAbilityHelper, name: string, defValue: string): string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | Yes |
| name | string | Yes |
| defValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

// Obtain the value of SCREEN_BRIGHTNESS_STATUS (this data item already exists in the database).
let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let value:string = settings.getValueSync(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
```


## getValueSync

```TypeScript
function getValueSync(context: Context, name: string, defValue: string): string
```

Get value from settingsdata(synchronous method)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function getValueSync(context: Context, name: string, defValue: string): string--><!--Device-settings-function getValueSync(context: Context, name: string, defValue: string): string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| defValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the value of SCREEN_BRIGHTNESS_STATUS (this data item already exists in the database).
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
```


## getValueSync

```TypeScript
function getValueSync(context: Context, name: string, defValue: string, domainName: string): string
```

Get value from settingsdata(synchronous method).  
[USER_SECURE] domain need ohos.permission.MANAGE_SECURE_SETTINGS permission.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function getValueSync(context: Context, name: string, defValue: string, domainName: string): string--><!--Device-settings-function getValueSync(context: Context, name: string, defValue: string, domainName: string): string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| defValue | string | Yes |
| domainName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN_BRIGHTNESS_STATUS (this data item already exists in the database).
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100',  settings.domainName.DEVICE_SHARED);
```
