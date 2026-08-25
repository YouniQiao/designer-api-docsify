# WindowExtensionAbility (System API)

class of window extension ability.

**Since:** 9

**Deprecated since:** 21

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { WindowExtensionAbility, WindowExtensionContext } from 'kits/@kit.ArkUI';
```

## onConnect

```TypeScript
onConnect(want: Want): void
```

Called back when a window extension is first connected to an ability.

**Since:** 9

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

Called back when all abilities connected to a window extension are disconnected.

**Since:** 9

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onWindowReady

```TypeScript
onWindowReady(window: window.Window): void
```

Called back when window is created.

**Since:** 9

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [window](arkts-arkui-window-n.md) | window.Window | Yes |

## context

```TypeScript
context: WindowExtensionContext
```

Indicates window extension ability context.

**Type:** [WindowExtensionContext](arkts-arkui-windowextensioncontext-t-sys.md)

**Since:** 9

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.
