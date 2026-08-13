# DistributedExtensionContext

Class inherited for the distributed extension function.

**Inheritance/Implementation:** DistributedExtensionContext extends ExtensionContext

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class DistributedExtensionContext--><!--Device-unnamed-declare class DistributedExtensionContext-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { DistributedExtensionContext } from '@kit.DistributedServiceKit';
```

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

Connects to a remote Service extension ability. This method connects to a Service extension ability on a remote device. You must implement the ConnectOptions interface to obtain the proxy of the target service extension when connected.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

Disconnects from a remote Service extension ability.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

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
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000003](../../apis-ability-kit/errorcode-ability.md#16000003-id-does-not-exist) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |
