# UIServiceExtensionAbility (System API)

UIServiceExtensionAbility provides extended capabilities related to the floating window component. It inherits from [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md). It is mainly used to provide services with UIs for third-party applications.

> **NOTE：**&gt;
> The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Inheritance/Implementation:** UIServiceExtensionAbility extends ExtensionAbility

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { UIServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

Called when the connection to a [UIServiceExtensionAbility](#uiserviceextensionability-system-api) is established. If the UIServiceExtensionAbility is started by calling [connectUIServiceExtensionAbility()](arkts-ability-uiextensioncontext-c.md#connectuiserviceextensionability), this callback will be invoked after [onCreate()](#oncreate). This callback receives a [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) object for communication between the client and server.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes |

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called to initialize the service logic.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onData

```TypeScript
onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void
```

Callback invoked when data is received.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes |
| data | Record & lt;string, Object & gt; | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called to clear resources when this [UIServiceExtensionAbility](#uiserviceextensionability-system-api) is destroyed.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onDisconnect

```TypeScript
onDisconnect(want: Want, proxy: UIServiceHostProxy): void
```

Called when the connection to a [UIServiceExtensionAbility](#uiserviceextensionability-system-api) is interrupted.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes |

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

Called to request to start a [UIServiceExtensionAbility](#uiserviceextensionability-system-api). If the UIServiceExtensionAbility is started by calling [startAbility](arkts-ability-uiabilitycontext-c.md#startability) or [startUIServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#startuiserviceextensionability), this callback will be invoked after [onCreate](#oncreate). The value of **startId** is incremented for each UIServiceExtensionAbility that is started.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| startId | number | Yes |

## onWindowDidCreate

```TypeScript
onWindowDidCreate(window: window.Window): void
```

Called when a window is created for the [UIServiceExtensionAbility](#uiserviceextensionability-system-api). Through this callback, the [UIServiceExtensionAbility](#uiserviceextensionability-system-api) passes the created window object to the foreground application.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [window](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) | window.Window | Yes |

## onWindowWillCreate

```TypeScript
onWindowWillCreate(config: window.ExtensionWindowConfig): void
```

Called when a window will be created for the [UIServiceExtensionAbility](#uiserviceextensionability-system-api). Through **window.ExtensionWindowConfig** in the callback, the foreground application sends the parameters for creating the window to the [UIServiceExtensionAbility](#uiserviceextensionability-system-api).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | window.ExtensionWindowConfig | Yes |

## context

```TypeScript
context: UIServiceExtensionContext
```

Context environment for a [UIServiceExtensionAbility](#uiserviceextensionability-system-api). This context inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md).

**Type:** [UIServiceExtensionContext](arkts-ability-uiserviceextensioncontext-c-sys.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.
