# Caller

A Caller UIAbility can use the [startAbilityByCall](arkts-ability-uiabilitycontext-c.md#startabilitybycall) API to start the target Callee UIAbility. After the target UIAbility is started successfully, a Caller object is returned to the caller for communication.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## call

```TypeScript
call(method: string, data: rpc.Parcelable): Promise<void>
```

Used by a Caller UIAbility to send serialized data, as agreed upon by both parties, to the Callee UIAbility. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |
| data | rpc.Parcelable | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16200002](../errorcode-ability.md#16200002-invalid-callee) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## callWithResult

```TypeScript
callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>
```

Used by a Caller UIAbility to send serialized data to a Callee UIAbility and return the result after the Callee UIAbility processes the message. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |
| data | rpc.Parcelable | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;rpc.MessageSequence & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16200002](../errorcode-ability.md#16200002-invalid-callee) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## off('release')

```TypeScript
off(type: 'release', callback: OnReleaseCallback): void
```

Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation of [on('release')](#onrelease). It is currently not supported.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'release' | Yes |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('release')

```TypeScript
off(type: 'release'): void
```

Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation of [Caller.on('release')](#onrelease). It is currently not supported.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'release' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('release')

```TypeScript
on(type: 'release', callback: OnReleaseCallback): void
```

Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'release' | Yes |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## onRelease

```TypeScript
onRelease(callback: OnReleaseCallback): void
```

Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## onRemoteStateChange

```TypeScript
onRemoteStateChange(callback: OnRemoteStateChangeCallback): void
```

Called when the remote UIAbility state changes in the collaboration scenario. This API uses an asynchronous callback to return the result.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnRemoteStateChangeCallback](arkts-ability-app-ability-uiability-onremotestatechangecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## release

```TypeScript
release(): void
```

Used by a Caller UIAbility to proactively release the connection with the Callee UIAbility. After this API is called, the Caller UIAbility can no longer use **call** or **callWithResult** to send messages to the Callee UIAbility.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Error codes:**

| Error Code ID |
| --- |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16200002](../errorcode-ability.md#16200002-invalid-callee) |
