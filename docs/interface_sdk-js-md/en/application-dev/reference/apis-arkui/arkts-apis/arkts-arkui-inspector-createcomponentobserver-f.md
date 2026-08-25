# createComponentObserver

## Modules to Import

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## createComponentObserver

```TypeScript
function createComponentObserver(id: string): ComponentObserver
```

Sets the component after layout or draw criteria and returns the corresponding listening handle

**Since:** 10

**Deprecated since:** 18

**Substitutes:** createComponentObserver

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ComponentObserver](arkts-arkui-inspector-componentobserver-i.md) |
