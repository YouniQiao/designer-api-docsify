# acquireDataAbilityHelper

## acquireDataAbilityHelper

```TypeScript
function acquireDataAbilityHelper(uri: string): DataAbilityHelper
```

Obtains a dataAbilityHelper object. > **NOTE** > > For details about the startup rules for the components in the FA model, see > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. > > To access a DataAbility of another application, the target application must be configured with associated startup > (**AssociateWakeUp** set to **true**).

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function acquireDataAbilityHelper(uri: string): DataAbilityHelper--><!--Device-featureAbility-function acquireDataAbilityHelper(uri: string): DataAbilityHelper-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the file to open. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A utility class used to help other abilities access the Data ability. |

**Example**

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

let dataAbilityHelper = featureAbility.acquireDataAbilityHelper(
  'dataability:///com.example.DataAbility'
);
```

