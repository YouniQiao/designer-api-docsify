# spring

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## spring

```TypeScript
function spring(velocity: number, mass: number, stiffness: number, damping: number): string
```

Constructs a spring curve object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [springCurve](arkts-arkui-curves-springcurve-f.md)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |
| mass | number | Yes |
| [stiffness](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |
| [damping](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
