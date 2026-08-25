# AppServiceExtensionContext

The AppServiceExtensionContext module provides the context environment for the [AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md). It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md).AppServiceExtensionContext provides APIs to connect to and disconnect from a ServiceExtensionAbility (an ExtensionAbility for system application background services), as well as to terminate an AppServiceExtensionAbility. Note that a ServiceExtensionAbility can only be developed by system applications and supports connections from third- party applications.

> **NOTE：**&gt;
> - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Inheritance/Implementation:** AppServiceExtensionContext extends ExtensionContext

**Since:** 20

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, callback: ConnectOptions): number
```

Connects this AppServiceExtensionAbility to a ServiceExtensionAbility. It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility. This API can be called only by the main thread.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

Disconnects this AppServiceExtensionAbility from a ServiceExtensionAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts the UIAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000072](../errorcode-ability.md#16000072-multi-app-mode-is-not-supported) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000076](../errorcode-ability.md#16000076-app_instance_key-does-not-exist) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multi-instance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-app_instance_key-cannot-be-specified) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Terminates this AppServiceExtensionAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
