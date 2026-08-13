# setValueSync

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## setValueSync

```TypeScript
function setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean
```

Set settingsdata value(synchronous method)

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setValueSync](#setValueSync)

**Required permissions:** ohos.permission.MANAGE_SETTINGS

**Model restriction:** This API can be used only in the FA model.

<!--Device-settings-function setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean--><!--Device-settings-function setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | Yes |
| name | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

// Update the value of SCREEN_BRIGHTNESS_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
let uri:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let ret:string = settings.setValueSync(helper, settings.display.SCREEN_BRIGHTNESS_STATUS, '100');
```


## setValueSync

```TypeScript
function setValueSync(context: Context, name: string, value: string): boolean
```

Set settingsdata value(synchronous method)

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function setValueSync(context: Context, name: string, value: string): boolean--><!--Device-settings-function setValueSync(context: Context, name: string, value: string): boolean-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN_BRIGHTNESS_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100');
```


## setValueSync

```TypeScript
function setValueSync(context: Context, name: string, value: string, domainName: string): boolean
```

Set settingsdata value(synchronous method). [DEVICE_SHARED, USER_PROPERTY] domain need ohos.permission.MANAGE_SETTINGS permission. [USER_SECURE] domain need ohos.permission.MANAGE_SECURE_SETTINGS permission.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_SECURE_SETTINGS or ohos.permission.MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function setValueSync(context: Context, name: string, value: string, domainName: string): boolean--><!--Device-settings-function setValueSync(context: Context, name: string, value: string, domainName: string): boolean-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| value | string | Yes |
| domainName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN_BRIGHTNESS_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '100', settings.domainName.DEVICE_SHARED);
```
