# UIServiceExtensionContext (System API)

The UIServiceExtensionContext module provides the context environment for a  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md). It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md).

UIServiceExtensionContext provides access to a  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md) and APIs for operating the ability, for example, starting, terminating, connecting, and disconnecting ability.

> **NOTE：**
> 
> - The APIs of this module must be used on the main thread, but not on child threads such as Worker and TaskPool.

**Inheritance/Implementation:** UIServiceExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 14

<!--Device-unnamed-declare class UIServiceExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIServiceExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

Connects to a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) and returns the connection ID.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIServiceExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connectionId: number): Promise<void>
```

Disconnects from a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md). This API is opposite to [connectServiceExtensionAbility](arkts-ability-uiserviceextensioncontext-c-sys.md#connectserviceextensionability). This API uses a promise to return the result.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-disconnectServiceExtensionAbility(connectionId: long): Promise<void>--><!--Device-UIServiceExtensionContext-disconnectServiceExtensionAbility(connectionId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connectionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts an ability. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbilityByType

```TypeScript
startAbilityByType(type: string, wantParam: Record<string, Object>,
    abilityStartCallback: AbilityStartCallback): Promise<void>
```

Starts a [UIAbility](arkts-app-ability-uiability.md) or  
[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) based on the type of the target ability. This API can be called only by applications running in the foreground. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>--><!--Device-UIServiceExtensionContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| wantParam | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |
| abilityStartCallback | [AbilityStartCallback](arkts-ability-abilitystartcallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Terminates this  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md). This API uses a promise to return the result.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-terminateSelf(): Promise<void>--><!--Device-UIServiceExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
