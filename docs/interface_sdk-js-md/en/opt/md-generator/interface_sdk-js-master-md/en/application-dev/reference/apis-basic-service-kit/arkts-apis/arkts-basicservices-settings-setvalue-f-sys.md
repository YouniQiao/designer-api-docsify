# setValue (System API)

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## setValue

```TypeScript
function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void
```

Saves a character string name and its value to the database.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** setValue

**Model restriction:** This API can be used only in the FA model.

<!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void--><!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | Yes |
| name | string | Yes |
| value | object | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## setValue

```TypeScript
function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>
```

Saves a character string name and its value to the database.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** setValue

**Model restriction:** This API can be used only in the FA model.

<!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>--><!--Device-settings-function setValue(dataAbilityHelper: DataAbilityHelper, name: string, value: object): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataAbilityHelper | [DataAbilityHelper](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-dataabilityhelper-i.md) | Yes |
| name | string | Yes |
| value | object | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
